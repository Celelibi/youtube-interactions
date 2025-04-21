"""
Authentication module

Handles API key authentication as well as OAuth2. It is based on oauthlib and
requests and add the code around it to make it directly usable.

It currently only implements the "Device" client.
"""

import abc
import datetime
import json
import logging
import os
import subprocess
import time
import urllib

import oauthlib.oauth2
import requests



class AuthenticationTimeout(RuntimeError):
    """Raised when the OAuth2 authentication takes too long."""



class APIKeyAuth(requests.auth.AuthBase):
    """
    Subclass of AuthBase for the module requests. When __call__ed, it modifies
    the request to include the API key.
    This authentication method puts the key in the URL. That's all.
    """

    def __init__(self, key):
        self._key = key

    def __eq__(self, other):
        return self._key == other._key

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        url = urllib.parse.urlparse(r.url)

        query = urllib.parse.parse_qsl(url.query)
        query.append(("key", self._key))
        url = url._replace(query=urllib.parse.urlencode(query))

        r.url = url.geturl()

        return r



class OAuth2Auth(requests.auth.AuthBase):
    """
    Subclass of AuthBase for the module requests. When __call__ed, it modifies
    the request in whatever way necessary to include the access token. The
    exact way depend on the authentication method used.
    """

    def __init__(self, client):
        self._client = client

    def __eq__(self, other):
        return self._client.token == other._client.token

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.url, r.headers, r.body = self._client.add_token(r.url, r.method, r.body, r.headers)
        return r



class Authenticator(metaclass=abc.ABCMeta):
    """Base class for authenticators."""

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, saved, *args, **kwargs):
        """Instanciate the subclass from a dict as produced by to_dict."""
        raise NotImplementedError()

    @abc.abstractmethod
    def to_dict(self):
        """Saves the authentication informations as a shallow dict."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def auth(self):
        """
        A subclass of requests.AuthBase that modify a request with
        authentication informations.
        """
        raise NotImplementedError()

    def pre_request_hook(self):
        """
        This method is called before every request. It allows to refresh some
        token if needed.
        """



class APIKeyAuthenticator(Authenticator):
    """
    API key authenticator

    This authentication mechanism is only a static key added to URLs.
    Documented here:
    https://developers.google.com/youtube/registering_an_application
    """
    def __init__(self, key):
        self._key = key
        self._auth = APIKeyAuth(key)

    @classmethod
    def from_dict(cls, saved, *args, **kwargs):
        """Instanciate the subclass from a dict as produced by to_dict."""
        assert not args
        assert not kwargs
        return cls(saved["key"])

    def to_dict(self):
        """Saves the authentication informations as a shallow dict."""
        return {"key": self._key}

    @property
    def auth(self):
        """
        A subclass of requests.AuthBase that modify a request with
        authentication informations.
        """
        return self._auth



class OAuth2Authenticator(Authenticator, metaclass=abc.ABCMeta):
    """Base class for future OAuth2 authenticators."""

    @abc.abstractmethod
    def authenticate(self):
        """Performs the first authentication to get an access token."""
        raise NotImplementedError()

    @abc.abstractmethod
    def refresh_access_token(self, force=False):
        """Uses the refresh token to renew an access token."""
        raise NotImplementedError()

    def pre_request_hook(self):
        self.refresh_access_token()



class DeviceAuthenticator(OAuth2Authenticator):
    """
    Uses the "TV & Device App" OAuth2 authentication method.

    This method has the advantage of being slightly simpler than the other
    methods. (No callback URL, no encryption and signing, and so on.) It does
    not assume our application has access to a browser. However it requires the
    user to have an external access to a browser. :(

    Documentation here:
    https://developers.google.com/identity/protocols/oauth2/limited-input-device
    """

    def __init__(self, urls, client_id, client_secret, scope):
        self._urls = urls
        self._scope = scope
        self._client = oauthlib.oauth2.DeviceClient(client_id, client_secret=client_secret)
        self._access_token_expiry = None

        self.authenticate()
        self._update_expiry()
        self._auth = OAuth2Auth(self._client)



    @classmethod
    def from_dict(cls, saved, *args, **kwargs):
        """Instanciate the subclass from a dict as produced by to_dict."""
        # pylint: disable=protected-access

        assert not kwargs
        assert len(args) == 1
        urls = args[0]

        # Let's make a copy of the dict, just in case the caller needs it unmodifed
        saved = dict(saved)

        client_id = saved.pop("client_id")
        client_secret = saved.pop("client_secret")
        expires_at = datetime.datetime.fromisoformat(saved.pop("expires_at"))
        expires_in = int((expires_at - datetime.datetime.now()).total_seconds())
        if expires_in > 0:
            logging.debug("Access token expires in %d seconds", expires_in)
        else:
            logging.debug("Access token expired %d seconds ago", -expires_in)
        saved["expires_in"] = expires_in

        retval = cls.__new__(cls)
        retval._urls = urls
        retval._scope = saved["scope"]
        retval._client = oauthlib.oauth2.DeviceClient(client_id, client_secret=client_secret)
        retval._client.parse_request_body_response(json.dumps(saved))

        retval._access_token_expiry = None
        retval._update_expiry()
        retval._auth = OAuth2Auth(retval._client)

        # Update the token if needed, just in case it's already expired
        retval.refresh_access_token()
        return retval



    def to_dict(self):
        """Saves the authentication informations as a shallow dict."""

        retval = {
            "client_id": self._client.client_id,
            "client_secret": self._client.client_secret,
            **self._client.token,
        }

        # Store the absolute date `expires_at' instead of the relative `expires_in'
        retval["expires_at"] = self._access_token_expiry.isoformat()
        del retval["expires_in"]

        # Join all the scopes separated by space, as is usual
        retval["scope"] = " ".join(retval["scope"])

        return retval



    @property
    def auth(self):
        """
        A subclass of requests.AuthBase that modify a request with
        authentication informations.
        """
        return self._auth



    def _update_expiry(self):
        """
        Update self._access_token_expiry.

        This attribute contains the datetime object representing the date at
        which the access token expires.
        """

        expiry = datetime.datetime.now() + datetime.timedelta(seconds=self._client.expires_in)
        self._access_token_expiry = expiry
        logging.debug("Access token expires at: %s", self._access_token_expiry.isoformat())



    def _user_interaction(self, user_url, user_code):
        """
        This function method the user interaction for the "TV & Device App"
        authentication.
        """

        browser = os.environ.get("BROWSER", "x-www-browser")
        cmd = [browser, user_url]
        logging.debug("Running browser command: %r", cmd)
        subprocess.run(cmd, check=True)
        print("Go to:", user_url)
        print("And enter the code:", user_code)



    def authenticate(self):
        """This method actually perform the authentication."""

        # shorthands. Won't re-assign anyway.
        client = self._client
        client_id = client.client_id
        client_secret = client.client_secret

        logging.debug("Authenticating at url <%s> with client_id: %s",
                      self._urls["auth"], client_id)

        sess = requests.Session()
        data = {
            "client_id": client_id,
            "scope": self._scope,
        }

        res = sess.post(self._urls["auth"], data=data, timeout=60)
        res.raise_for_status()
        res = res.json()


        poll_data = client.prepare_request_body(device_code=res["device_code"],
                                                include_client_id=True,
                                                client_secret=client_secret)
        poll_data = dict(urllib.parse.parse_qsl(poll_data))

        self._user_interaction(res["verification_url"], res["user_code"])

        now = time.time()
        poll_until = now + res["expires_in"]
        poll_sleep = res["interval"]

        while now < poll_until:
            res = sess.post(self._urls["poll"], data=poll_data, timeout=60)
            if res.status_code != 428:
                res.raise_for_status()
                break

            time.sleep(poll_sleep)
            now = time.time()

        else:
            raise AuthenticationTimeout()

        client.parse_request_body_response(res.text)



    def refresh_access_token(self, force=False):
        """Refresh the access token if expired or if forced."""

        if not force and datetime.datetime.now() < self._access_token_expiry:
            return

        if force:
            logging.info("Requesting a new access token because we were asked to")
        else:
            date = self._access_token_expiry.isoformat()
            logging.info("Requestion a new access token because it expired at %s", date)

        client_id = self._client.client_id
        client_secret = self._client.client_secret
        url, _, data = self._client.prepare_refresh_token_request(self._urls["refresh"],
                                                                  client_id=client_id,
                                                                  client_secret=client_secret,
                                                                  include_client_id=True)

        data = dict(urllib.parse.parse_qsl(data))
        res = requests.post(url, data=data, timeout=60)
        res.raise_for_status()

        self._client.parse_request_body_response(res.text)

        # We need to set the refresh_token in self._client.token if it didn't change
        # It doesn't matter for the Client object, but we use in the property `token'
        self._client.token.setdefault("refresh_token", self._client.refresh_token)

        self._update_expiry()
