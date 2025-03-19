import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each (page: Page):
        
        # Go to the starting url before each test.
        page.goto("https://www.bamfunds.com/")

        # Accept the use of cookies
        page.get_by_role("button", name="Accept cookies").click()

def test_founders_section(page: Page):

    page.get_by_label("Header").get_by_role("link", name="About us").hover()
    page.get_by_label("Header").get_by_role("link", name="Leadership").click()
    expect(page.get_by_role("link", name="Leadership Headshot Dmitry")).to_be_visible()
    expect(page.get_by_role("link", name="Leadership Headshot Taylor O'")).to_be_visible()
    expect(page.get_by_role("link", name="Leadership Headshot Scott")).to_be_visible()