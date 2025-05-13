# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create_contact(Contact(
        firstname="John",
        lastname="Smith",
        company="Google",
        home_phone="+7999999999",
        email="johnsmith@gmail.com"
    ))