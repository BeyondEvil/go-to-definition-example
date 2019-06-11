import pytest
from api.base import Base
from api.users import User
from utils.database import TestDB


@pytest.fixture
def database():
    tdb = TestDB()
    yield tdb


@pytest.fixture
def test_data(database, base_url, user, setup):
    Base.BASE_URL = base_url
    user.authenticate()
    for item in setup:
        item_class, item_data = item
        _name_to_item_replace(item_data, database)
        create_item = item_class.create(*item_data)
        database.add(create_item, "function")
    return database


@pytest.fixture
def user():
    return User.create()


@pytest.fixture
def setup(request):
    return request.node.get_closest_marker("setup").args


def _name_to_item_replace(item_data, database):
    for index, data in enumerate(item_data):
        obj = database.find(data)
        if obj:
            item_data[index] = obj
