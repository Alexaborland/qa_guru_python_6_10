from data import users
from tests_demo.pages.registration_pages import RegistrationPage


def test_with_high_level_registration_page():
    user = users.Alexandra
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.registration(user)
    registration_page.submit_registration(user)

