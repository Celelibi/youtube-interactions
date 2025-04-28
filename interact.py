#!/usr/bin/env python3

import argparse
import configparser
import locale
import logging
import logging.config
import os
import re
import sys

import youtube



SELFPATH = os.path.dirname(os.path.realpath(sys.modules[__name__].__file__))



# pylint: disable=invalid-name
def logging_getHandler(name):
    """Get the logging handler with the given name."""

    for h in logging.getLogger().handlers:
        if h.name == name:
            return h
    return None



def config_read(filename):
    """Read the give config file and return a dict."""

    logging.info("Reading config file %s", filename)
    config = configparser.ConfigParser()
    config.read(filename)

    if "account" not in config:
        raise ValueError("Malformed config file: requires an 'account' section.")

    retval = dict(config["account"])
    logging.debug("Read credentials: %r", retval)
    return retval



def credential_type(creds):
    """
    Heuristics to decide whether the credentials read from the config file are
    an API key or an OAuth2 token.
    Returns a string: "apikey" or "oauth2".
    Raises a ValueError if the key couldn't be recognized.
    """

    if "key" in creds:
        return "apikey"
    if "client_id" in creds:
        return "oauth2"

    raise ValueError(f"Credentials {creds!r} couldn't be identified")




def preprocess_api_key(creds):
    """
    Reshape the credentials from the config file in order to be usable by the
    class Youtube. Which is nothing to do for an API key.
    """
    return creds["key"], creds




def preprocess_oauth2_token(creds):
    """
    Reshape the credentials from the config file in order to be usable by the
    class Youtube. The following fields are expected:
    - client_id: the OAuth2 client id
    - client_secret: the OAuth2 client secret
    - token_type: the type of access token, usually "Bearer"
    - access_token: the access token itself
    - expires_at: the ISO-formated date at which the access token expires
    - refresh_token: the refresh token to use to get a new access_token when it
      expires
    - scope: the scope of access requested

    In the OAuth2 case, the fields client_id and client_secret must always be
    present.
    If one of the other fields is missing, then the token is considered
    invalid, and a new one will be requested.
    """

    try:
        client_id = creds["client_id"]
        client_secret = creds["client_secret"]
    except KeyError:
        logging.critical("Configurations client_id and client_secret are required")
        raise

    # We need all those fields to make a valid token
    fields = {"token_type", "access_token", "expires_at", "refresh_token", "scope"}
    missing_fields = fields - set(creds)
    if missing_fields:
        logging.debug("Missing token fields: %s", ", ".join(sorted(missing_fields)))
        return client_id, client_secret, None

    return client_id, client_secret, creds




def config_write(filename, creds):
    """
    Write the API key to the config file.
    """

    config = configparser.ConfigParser()
    config["account"] = creds

    with open(filename, "w") as fp:
        config.write(fp)

    logging.debug("Saved credentials %r", creds)



class ArgparseBoolAction(argparse.Action):
    """Action class for booleans.

    From a --name option it generates --no-name. It handles all the standard
    values assigmnets y, yes, true, 1 for True, and n, no, false, 0 for False.
    If no value is given, a True value is assumed.
    If the --no-* argument is used, the truth of the value is flipped."""

    pos_values = ["y", "yes", "true", "1"]
    neg_values = ["n", "no", "false", "0"]

    def __init__(self, option_strings, *args, **kwargs):
        #kwargs.setdefault("type", bool)
        kwargs.setdefault("choices", self.pos_values + self.neg_values)
        kwargs.setdefault("nargs", "?")
        kwargs.setdefault("const", True)

        if kwargs["nargs"] != "?":
            raise ValueError("nargs with ArgparseBoolAction must be \"?\"")

        neg_options = ["--no-" + o.removeprefix("--") for o in option_strings if o.startswith("--")]
        option_strings += neg_options
        self.neg_option_strings = neg_options
        super().__init__(option_strings, *args, **kwargs)



    def __call__(self, parser, namespace, values, option_string=None):
        if values in self.pos_values:
            values = True
        elif values in self.neg_values:
            values = False
        elif values is None:
            values = self.const
        elif values is self.const or values is self.default:
            pass
        else:
            raise ValueError(f"ArgparseBoolAction: unrecognized value {values!r}")

        if option_string in self.neg_option_strings:
            values = not values

        if option_string in self.option_strings:
            setattr(namespace, self.dest, values)



def camel_case_to_argument(camel):
    """Turn a camelCase name into a --kebab-case-option."""
    newname = re.sub(r"([a-z])([A-Z]+)", r"\1-\2", camel).lower()
    return "--" + newname



def _add_argument(parser, param, required):
    n = camel_case_to_argument(param["originalName"])
    action = ArgparseBoolAction if param["type"] == "boolean" else "store"

    if param["repeated"]:
        if action != "store":
            raise ValueError(f"Can't parse repeated argument of type {param['type']}")
        action = "append"

    parser.add_argument(n, action=action, dest=param["name"], required=required,
                          deprecated=param["deprecated"], help=param["help"])



def parse_arguments():
    """Parse sys.argv and return a Namespace object."""

    api = youtube.YouTube.api_help

    parser = argparse.ArgumentParser(description="Youtube Interactions")
    parser.add_argument("--config", "-c", metavar="configfile", required=True,
                        help="Fichier de configuration")
    parser.add_argument("--browser", "-b",
                        help="Navigateur à lancer pour l'authentification. (Environnement BROWSER)")
    parser.add_argument("--verbose", "-v", action="count", default=0,
                        help="Augmente le niveau de verbosité")
    parser.add_argument("--quiet", "-q", action="count", default=0,
                        help="Diminue le niveau de verbosité")

    subparsers = parser.add_subparsers(title="Ressources", help="Ressource sur laquelle agir")
    for resname in sorted(set(m["FQMN"][1] for m in api.values())):
        dash_resname = resname.replace("_", "-")
        resparser = subparsers.add_parser(dash_resname).add_subparsers()

        for methname in sorted(set(n for n, m in api.items() if m["FQMN"][1] == resname)):
            meth = api[methname]
            dash_methname = meth["FQMN"][2].replace("_", "-")
            methparser = resparser.add_parser(dash_methname, help=meth["help"])
            methparser.set_defaults(meth=meth)

            required = methparser.add_argument_group("Required arguments")
            optional = methparser.add_argument_group("Optional arguments")

            for p in meth["required_params"]:
                _add_argument(required, p, True)
            for p in meth["optional_params"]:
                _add_argument(optional, p, False)

    return parser.parse_args()



def main():
    # pylint: disable=missing-function-docstring
    locale.setlocale(locale.LC_ALL, '')
    logging.config.fileConfig(os.path.join(SELFPATH, "logconf.ini"),
                              disable_existing_loggers=False)

    args = parse_arguments()
    configpath = args.config
    browser = args.browser
    verbose = args.verbose - args.quiet

    loglevels = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]
    ch = logging_getHandler("consoleHandler")
    curlevel = logging.getLevelName(ch.level)
    curlevel = loglevels.index(curlevel)
    verbose = min(len(loglevels) - 1, max(0, curlevel + verbose))
    ch.setLevel(loglevels[verbose])

    if browser is not None:
        logging.info("Setting browser to %s", browser)
        os.environ["BROWSER"] = browser

    creds = config_read(configpath)
    key = None
    client_id = None
    client_secret = None

    creds_type = credential_type(creds)
    if creds_type == "apikey":
        key, creds = preprocess_api_key(creds)
    elif creds_type == "oauth2":
        client_id, client_secret, creds = preprocess_oauth2_token(creds)

    yt = youtube.YouTube(api_key=key, client_id=client_id, client_secret=client_secret, creds=creds)
    config_write(configpath, yt.credentials)



if __name__ == "__main__":
    sys.exit(main())
