# import secrets
from api.base import Base
from api.fixtures import Fixture
from api.groups import Group


class Org(object):
    BASE_ROUTE = "/orgs"
    FIXTURES_ROUTE = "{}/{}/fixtures"

    def __init__(self, name):
        self.name = name

    def add_member(self):
        return Base.make_request()

    def create_fixture(self, name):
        return Fixture.create(name)

    def create_group(self, name):
        Base.make_request()
        return Group(name)

    def list_fixtures(self):
        Base.make_request()
        return [Fixture("Muh Fixture 2")]

    @classmethod
    def create(cls, name):
        Base.make_request()
        return cls(name)


def list():
    Base.make_request()
    return [Org("Muh Org 2")]
