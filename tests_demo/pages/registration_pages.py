from selene import have, browser, by, be, command
from tests_demo import resourсe
from data.users import User
import calendar


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.sex = browser.all('.custom-radio')
        self.mobile_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.birth_day = browser.element('.react-datepicker__month')
        self.birth_month = browser.element('.react-datepicker__month-select')
        self.birth_year = browser.element('.react-datepicker__year-select')
        self.subject = browser.element('#subjectsInput')
        self.hobbies = browser.element('.custom-control')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')

    def registration(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.sex.element_by(have.text(user.sex)).click()
        self.mobile_number.type(user.mobile_number)
        self.date_of_birth.type.click()
        self.birth_month.click().element(by.text(calendar.month_name[user.birth_month])).click()
        self.birth_year.click().element(by.text(str(user.birth_year))).click()
        self.birth_day.click().element(by.text(str(user.birth_day))).click()
        self.subject.click().type(user.subject).press_enter()
        self.hobbies.element(by.text(user.hobbies)).click()
        self.picture.send_keys(resourсe.path(user.picture))
        self.address.type(user.address)
        self.state.type(user.state).press_enter()
        self.city.type(user.city).press_enter()
        self.submit_button.should(be.visible).click()

    def submit_registration(self, user: User):
        browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
        browser.element('[class="modal-body"]').should(have.text(f'Student Name {user.first_name} {user.last_name}'))
        browser.element('[class="modal-body"]').should(have.text(f'Student Email {user.email}'))
        browser.element('[class="modal-body"]').should(have.text(f'Gender {user.sex}'))
        browser.element('[class="modal-body"]').should(have.text(f'Mobile {user.mobile_number}'))
        browser.element('[class="modal-body"]').should(have.text(f'Date of Birth {user.full_date_of_birth()}'))
        browser.element('[class="modal-body"]').should(have.text(f'Subjects {user.subject}'))
        browser.element('[class="modal-body"]').should(have.text(f'Hobbies {user.hobbies}'))
        browser.element('[class="modal-body"]').should(have.text(f'Hobbies {user.picture}'))
        browser.element('[class="modal-body"]').should(have.text(f'Address {user.address}'))
        browser.element('[class="modal-body"]').should(have.text(f'State and City {user.state} {user.city}'))
