import pytest
from fixture.application import Application

fixture = None

@pytest.fixture()
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop():
    yield fixture
    fixture.session.logout()
    fixture.destroy()