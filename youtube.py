"""
Youtube module

Handles the authentication using OAuth2 as well as refreshing the token
whenever necessary. It then allows to interact with the Youtube Data V3 API.

More methods will need to be added in the future depending on the needs. See
documentation here:
https://developers.google.com/youtube/v3/docs
"""

import collections
import itertools as it
import logging
import urllib

import requests

import auth

try:
    import generated_youtube_mixin
except ImportError:
    import os
    import subprocess
    import sys
    selfpath = os.path.dirname(os.path.realpath(sys.modules[__name__].__file__))
    progpath = os.path.join(selfpath, "gen_youtube_api.py")
    subprocess.run([progpath, "generated_youtube_mixin.py"], check=True)
    import generated_youtube_mixin



class APIError(Exception):
    """Thrown when an API answered with an error."""

    def __init__(self, msg, request=None, response=None):
        super().__init__(msg)
        self.request = request
        self.response = response



class YouTubeResponse(collections.UserDict):
    def __init__(self, yt, req, data):
        super().__init__(data)
        self._yt = yt
        self._req = req

    def __getattr__(self, name):
        try:
            ret = self.data[name]
        except KeyError as e:
            raise AttributeError(f"response has no attribute {name}")

        if isinstance(ret, dict):
            return self._wrap(ret)
        if isinstance(ret, list):
            return [self._wrap(v) for v in ret]

        return ret

    def _wrap(self, data):
        return wrap_result(self._yt, self._req, data)

    def __str__(self):
        pad = "\n    "
        retval = ""
        for k in sorted(self.data):
            v = getattr(self, k)
            retval += f"{k}:"

            if isinstance(v, collections.abc.Generator):
                v = it.islice(v, len(self.data[k]))

                for e in v:
                    retval += pad + "- "
                    s = str(e)
                    if "\n" in s:
                        lines = s.splitlines()
                        retval += lines[0]
                        retval += "".join(pad + "  " + l for l in lines[1:])
                    else:
                        retval += s
                retval += pad + "..."

            elif isinstance(v, YouTubeResponse):
                retval += "".join(pad + l for l in str(v).splitlines())
            else:
                retval += f" {v}"

            retval += "\n"

        return retval.removesuffix("\n")



class YouTubeResponsePageinated(YouTubeResponse):
    def __init__(self, yt, req, data):
        super().__init__(yt, req, data)

        if "pageInfo" not in data:
            logging.warning("YouTubeResponse should only be used for paginated responses")
            if "items" in data:
                logging.error("Your code might not work properly if you try to access .items")

        if "items" not in data:
            logging.error("YouTube response is paginated for an attribute other than \"items\"")

        # We won't need to wrap the future results
        self._req["kwargs"]["wrap"] = False

    @property
    def items(self):
        yield from (self._wrap(itm) for itm in self.data["items"])

        while "nextPageToken" in self.data:
            self._req["kwargs"]["params"]["pageToken"] = self.nextPageToken
            self.data = self._yt.request(*self._req["args"], **self._req["kwargs"])
            yield from (self._wrap(itm) for itm in self.data["items"])



def wrap_result(yt, req, data):
    if "pageInfo" in data:
        return YouTubeResponsePageinated(yt, req, data)
    return YouTubeResponse(yt, req, data)



class YouTube(generated_youtube_mixin.YouTubeMixin):
    """
    Implements the authentication against the Youtube API and allows to perform
    some queries to it.
    """

    base_url = "https://www.googleapis.com/youtube/v3/"
    oauth_scope = "https://www.googleapis.com/auth/youtube.readonly"

    oauth_urls = {
        "auth": "https://oauth2.googleapis.com/device/code",
        "poll": "https://oauth2.googleapis.com/token",
        "refresh": "https://oauth2.googleapis.com/token",
    }



    def __init__(self, api_key=None, client_id=None, client_secret=None, creds=None):
        """
        Takes either an API key or a client_id + client_secret for OAuth2.

        If the token is provided, then the client_id and client_secret must be
        provided as well. If provided, it is used as long as it is not expired
        and no authorization request is made. If expired, it is refreshed.
        """

        if api_key is not None and client_id is not None:
            raise ValueError("api_key and client_id must not be given together")

        if (client_id is None) ^ (client_secret is None):
            raise ValueError("Both client_id and client_secret must be given or none of them")

        if creds is None:
            if client_id is not None:
                self._auth = auth.DeviceAuthenticator(self.oauth_urls, client_id,
                                                      client_secret, self.oauth_scope)
            elif api_key is not None:
                self._auth = auth.APIKeyAuthenticator(api_key)
            else:
                raise ValueError("No API authentication passed as argument")
        else:
            if client_id is not None and "access_token" in creds:
                self._auth = auth.DeviceAuthenticator.from_dict(creds, self.oauth_urls)
            elif api_key is not None and "key" in creds:
                self._auth = auth.APIKeyAuthenticator.from_dict(creds)
            else:
                raise ValueError(f"Malformed saved credentials: {creds!r}")

        self._sess = requests.Session()
        self._sess.auth = self._auth.auth



    @property
    def credentials(self):
        """
        A shallow dict containing the authentication information.
        Should be used to save credentials and restore them by passing the
        result back to __init__.
        """

        return self._auth.to_dict()



    def request(self, method, url, *args, raise_=True, decode_json=True, wrap=True, **kwargs):
        """
        Perform an authenticated request.

        Refresh the access token if nedded.
        Prepend the base URL of the youtube data API if needed.
        Raise an exception for an error status code by default.
        Decode the JSON response by default.
        """

        if wrap and not decode_json:
            ValueError("Cannot wrap a result whose JSON isn't decoded")

        self._auth.pre_request_hook()

        url = urllib.parse.urljoin(self.base_url, url)
        kwargs.setdefault("timeout", 60)

        res = self._sess.request(method.upper(), url, *args, **kwargs)
        if res.status_code == 401 and isinstance(self._auth, auth.OAuth2Authenticator):
            logging.warning("Error 401: %s", res.text)
            logging.info("Trying to generate a new access token")
            self._auth.refresh_access_token(force=True)
            res = self._sess.request(method.upper(), url, *args, **kwargs)

        if raise_:
            try:
                res.raise_for_status()
            except Exception as e:
                # We're on a no-fail path
                try:
                    msg = res.json()["error"]["message"]
                except:
                    msg = f"server response [{res.status_code}]: {res.text}"

                raise APIError(msg, response=e.response, request=e.request) from e

        if decode_json:
            res = res.json()
            if wrap:
                req = {
                    "args": (method, url) + args,
                    "kwargs": {
                        "raise_": raise_,
                        "decode_json": decode_json,
                        "wrap": wrap,
                        **kwargs
                    }
                }
                res = wrap_result(self, req, res)

        return res



    def get(self, *args, **kwargs):
        """Perform a GET request."""
        return self.request("GET", *args, **kwargs)



    def post(self, *args, **kwargs):
        """Perform a POST request."""
        return self.request("POST", *args, **kwargs)



    def put(self, *args, **kwargs):
        """Perform a PUT request."""
        return self.request("PUT", *args, **kwargs)



    def delete(self, *args, **kwargs):
        """Perform a DELETE request."""
        return self.request("DELETE", *args, **kwargs)
