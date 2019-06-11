from api.base import Base


class User(object):
    def __init__(self, json):
        self._json = json

    @property
    def json(self):
        return self._json

    @property
    def name(self):
        return "user name"

    @property
    def email(self):
        return "user.name@example.com"

    def authenticate(self):
        Base.make_request()
        return "success"

    @classmethod
    def create(cls):
        Base.make_request()
        return cls("User Name")
