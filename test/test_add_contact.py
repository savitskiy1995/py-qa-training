# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="John",
        lastname="Smith",
        company="Google",
        home_phone="+7999999999",
        email="johnsmith@gmail.com"
    )
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
