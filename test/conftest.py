import json
import pytest
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop():
    yield fixture
    fixture.session.logout()
    fixture.destroy()

@pytest.fixture(scope ="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
        request.addfinalizer(fin)
    return dbfixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Поднимаемся в корень
    file_path = os.path.join(base_path, "data", f"{file}.json")  # Ищем в корне/data/file.json
    with open(file_path) as f:
        return jsonpickle.decode(f.read())