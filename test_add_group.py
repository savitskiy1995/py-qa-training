# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group


@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group", header="logo"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header=""))
    app.logout()
