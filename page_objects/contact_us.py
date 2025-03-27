import re, allure
from playwright.async_api import Page


class Contact:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def validate_contact_form(self, validation_message: str):
        return self.page.locator("div").filter(has_text=re.compile(r'{}'.format(validation_message))).get_by_role("paragraph").is_visible()