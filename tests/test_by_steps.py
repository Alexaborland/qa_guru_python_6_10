from tests_demo.pages.registration_pages import RegistrationPage


def test_for_registration_form_tests_demo(browser_open):
    registration_page = RegistrationPage()

    # Browser open
    registration_page.open()

    # First and second name
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
    registration_page.should_have_text('Thanks for submitting the form')
    registration_page.should_have_registrated_user_with(
            'Alexandra Borland',
            'borland3711@gmail.com',
            'Female',
            '9992131512',
            '14 June,1998',
            'Maths',
            'Music',
            'img.png',
            'Kondratyevsky prospect',
            'Haryana Karnal')


