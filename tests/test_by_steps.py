import os
import pytest
from selene import have, be, browser, command

from demo import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[#firstName]').type(value)

    def fill_last_name(self, value):
        browser.element('["#lastName"]').type('value')

    def fill_email(self, value):
        browser.element('["#userEmail"]').type(value)

    def fill_sex(self, value):
        browser.element('[name=gender][value=Female]+label').click()

    def fill_mobile_number(self, value):
        browser.element('[#userNumber]').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('[#dateOfBirthInput]').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('[#subjectsInput]').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def add_picture(self, value):
        browser.element('["#uploadPicture"]').set_value(resource.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress"]').type(value)

    def fill_state(self, value):
        browser.element('[id="state"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('["#city"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()

    def submit_form(self):
        browser.element('["#submit"]').click()


def test_student_registration_form(browser_open):
    registration_page = RegistrationPage()
    registration_page.open()

    # First and Second Name
    registration_page.fill_first_name('Alexandra')
    registration_page.fill_last_name('Borland')

    # E-mail
    registration_page.fill_email('borland3711@gmail.com')

    # Sex
    registration_page.fill_sex('Female')

    # Number
    registration_page.fill_mobile_number('9992131512')

    # Date of birth
    registration_page.fill_date_of_birth('1998', 'June', '11')

    # Subject
    registration_page.fill_subject('Maths')

    # Hobbies
    registration_page.fill_hobbies('Music')
    
    # Picture
    registration_page.add_picture('img.png')

    # Address
    registration_page.fill_address('Kondratyevsky prospect')

    # State
    registration_page.fill_state('Haryana')

    # City
    registration_page.fill_city('Karnal')

    # Submit
    registration_page.submit_form()


    # Checking
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.element('[class="modal-body"]').should(have.text('Alexandra'))
    browser.element('[class="modal-body"]').should(have.text('Borland'))
    browser.element('[class="modal-body"]').should(have.text('borland3711@gmail.com'))
    browser.element('[class="modal-body"]').should(have.text('Female'))
    browser.element('[class="modal-body"]').should(have.text('9992131512'))
    browser.element('[class="modal-body"]').should(have.text('18 June,1998'))
    browser.element('[class="modal-body"]').should(have.text('Math'))
    browser.element('[class="modal-body"]').should(have.text('Music'))
    browser.element('[class="modal-body"]').should(have.text('img.png'))
    browser.element('[class="modal-body"]').should(have.text('Kondratyevsky prospect'))
    browser.element('[class="modal-body"]').should(have.text('Haryana Karnal'))
