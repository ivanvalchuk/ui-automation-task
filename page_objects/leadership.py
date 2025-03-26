import allure
from playwright.async_api import Page, expect   

class Leadership:
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step
    def check_founders_exist(self, founder_name: str):
        self.page.locator(f'css=div >> text="{founder_name}"').wait_for(state="visible")
        return self.page.query_selector(f'css=div >> text="{founder_name}"') is not None