import allure
from playwright.async_api import Page

# from pytest import mark
@allure.title("Check Founders' section => check if all 3 founders' names are displayed")
# @mark.test_desktop(1)
def test_founders(desktop_app):
    founder_names = "Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    desktop_app.hover_over('About us')
    desktop_app.navigate_to_menu('Leadership')
    for founder_name in founder_names:
        assert desktop_app.leadership.check_founders_exist(founder_name)

@allure.title("Check that required fields trigger validation errors")
def test_validation(desktop_app):
    desktop_app.navigate_to('Contact Us')
    #Trigger errors
    desktop_app.click_button('Submit')
    validation_messages = "^First Name\*This field is required$", "^Last Name\*This field is required$", "^E-mail Address\*This field is required$",
    "^Your Message\*This field is required$"
    for validation_message in validation_messages:
        assert desktop_app.contact_us.validate_contact_form(validation_message)
