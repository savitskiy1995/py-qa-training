# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", header="logo"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header=""))
    app.session.logout()
