import allure
from playwright.async_api import Page

class Leadership:
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step
    def check_founders_exist(self, founder_name: str):
        self.page.query_selector(f'css=div >> text=\"{founder_name}').click()