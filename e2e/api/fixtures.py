from api.base import Base


class Fixture(object):
    def __init__(self, name):
        self.name = name

    def create_access_policy(self):
        return Base.make_request()

    @classmethod
    def create(cls, name):
        Base.make_request()
        return cls(name)
