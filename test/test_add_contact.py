# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(
        firstname="John",
        lastname="Smith",
        company="Google",
        home_phone="+7999999999",
        email="johnsmith@gmail.com"
    ))
    app.session.logout()