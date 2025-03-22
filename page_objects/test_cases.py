from playwright.async_api import Page

class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def hover_over(self, menu: str):
        self.page.get_by_label("Header").get_by_role("link", name = menu).hover()

    def navigate_to(self, menu: str):
        self.page.get_by_label("Header").get_by_role("link", name = menu).click()
    
    def check_founders_exist(self, founder_name: str):
        return self.page.get_by_role("link", name=founder_name) is not None