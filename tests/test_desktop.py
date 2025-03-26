from playwright.sync_api import expect
import allure
# from pytest import mark

@allure.title("Check Founders' section => check if all 3 founders' names are displayed")
# @mark.test_desktop(1)
def test_desktop(desktop_app):
    founder_names = "Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    desktop_app.hover_over('About us')
    desktop_app.navigate_to('Leadership')
    for founder_name in founder_names:
        assert desktop_app.leadership.check_founders_exist(founder_name)
        # assert self.page.locator(f"text={founder_name}").is_visible(), f"{founder_name} is not displayed on the page."