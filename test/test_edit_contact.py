from model.contact import Contact

def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(
        firstname="John1",
        lastname="Smith1",
        company="Google1",
        home_phone="+7999999991",
        email="johnsmith@gmail.ru"
    ))