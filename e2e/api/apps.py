from api.base import Base


class App(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        Base.make_request()
        return cls(name)
