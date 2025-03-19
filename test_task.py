import re
from playwright.sync_api import Page, expect


def test_founders_section(page: Page):
    page.goto("https://www.bamfunds.com/")
    page.get_by_role("button", name="Accept cookies").click()
    page.get_by_label("Header").get_by_role("link", name="About us").hover()
    page.get_by_label("Header").get_by_role("link", name="Leadership").click()
    expect(page.get_by_role("link", name="Leadership Headshot Dmitry")).to_be_visible()
    expect(page.get_by_role("link", name="Leadership Headshot Taylor O'")).to_be_visible()
    expect(page.get_by_role("link", name="Leadership Headshot Scott")).to_be_visible()