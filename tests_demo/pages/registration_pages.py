from selene import have, browser
from tests_demo import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_sex(self, value):
        browser.element('[name=gender][value=Female]+label').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def add_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(resource.path(file_name))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(value)).click()

    def submit_form(self):
        browser.element('#submit').click()

    def should_have_text(self, value):
        browser.element('[id="example-modal-sizes-title-lg"]').should(have.text(value))

        
    def should_have_registrated_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                               subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
