import pytest
from api import apps, fixtures, orgs


@pytest.mark.setup(
    (orgs.Org, ["Muh Org"]),
    (apps.App, ["Muh App"]),
    (fixtures.Fixture, ["Muh Fixture"]),
)
def test_physical_access_getting_started(test_data):
    test_data.get(apps.App, "Muh App")

    org = orgs.list()[0]

    group_name = "Muh Group"
    org.create_group(group_name)
    org.add_member()

    fixture = org.list_fixtures()[0]
    actual = fixture.create_access_policy()
    assert actual == "success"
