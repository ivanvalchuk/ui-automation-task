import re, allure
from playwright.async_api import Page
# from pytest import mark

@allure.title("Accept the use of cookies")
def test_accept_cookies(desktop_app):
  desktop_app.click_button("Accept cookies")

@allure.title("Check Founders' section => check if all 3 founders' names are displayed")
# @mark.test_desktop(1)
def test_founders(desktop_app):
    founder_names = "Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    desktop_app.hover_over('About us')
    desktop_app.navigate_to_menu('Leadership')
    for founder_name in founder_names:
        assert desktop_app.leadership.check_founders_exist(founder_name)


@allure.title("Check 'Contact us' form => check required fields trigger validation errors")
def test_validation(desktop_app):
    desktop_app.navigate_to('Contact us')
    #Trigger errors on the form
    desktop_app.click_button('Submit')
    validation_messages = "^First Name\*This field is required$", "^Last Name\*This field is required$", "^E-mail Address\*This field is required$",
    "^Your Message\*This field is required$"
    for validation_message in validation_messages:
        assert desktop_app.contact_us.validate_contact_form(validation_message)


@allure.title("Check 'Contact us' form => test invalid inputs (e.g. wrong email format) and verify correct error messages")
def test_invalid_input(desktop_app):
    desktop_app.navigate_to('Contact us')
    desktop_app.contact_us.fill_text("First Name*", "Ivan")
    desktop_app.contact_us.fill_text("Last Name*", "Valchuk")
    desktop_app.contact_us.fill_text("E-mail Address*", "ivan.valchuk@gmail.com")
    desktop_app.contact_us.fill_text("Phone Number", "abcdef")
    desktop_app.contact_us.fill_text("Your Message*", "Hello there!")
    desktop_app.click_button('Submit')
    #changing to the wrong email address
    desktop_app.contact_us.fill_text("E-mail Address*", "ivan.valchukgmail.com")
    validation_messages = "Invalid e-mail address", "Invalid phone number"
    for validation_message in validation_messages:
        assert desktop_app.contact_us.verify_correct_error_message(validation_message)

@allure.title("Check 'Contact us' form submission")
def test_submit_contact_form(desktop_app):
    desktop_app.navigate_to('Contact us')
    desktop_app.contact_us.fill_text("First Name*", "John")
    desktop_app.contact_us.fill_text("Last Name*", "Smith")
    desktop_app.contact_us.fill_text("E-mail Address*", "test@test.com")
    desktop_app.contact_us.fill_text("Your Message*", "This is a test, please disregard!")
    desktop_app.click_button('Submit')
    controller_names = "First Name*", "Last Name*", "E-mail Address*", "Your Message*"
    for controller_name in controller_names:
        assert desktop_app.contact_us.verify_form_was_sent(controller_name)

@allure.title("Check locations => check if all 3 primary offices are displayed")
def test_primary_offices(desktop_app):
    desktop_app.hover_over('About us')
    desktop_app.navigate_to_menu('Locations')
    location_names = "Aalborg", "Austin", "Boston", "Chicago", "Copenhagen", "Dubai", "Greenwich", "Hong Kong",
    "Houston", "London", "Miami", "New York", "San Francisco", "Singapore", "Tokyo", "Toronto", "Warsaw"
    for location_name in location_names:
        assert desktop_app.locations.check_locations_exist(location_name)
