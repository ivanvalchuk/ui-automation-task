import allure
<<<<<<< HEAD
from playwright.async_api import Page, expect   
=======
from playwright.async_api import Page
>>>>>>> 07ead5339047ffb4ce7f0fc017343772bb2f182c

class Leadership:
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step
    def check_founders_exist(self, founder_name: str):
<<<<<<< HEAD
        return self.page.query_selector(f'css=div >> text="{founder_name}"') is not None
=======
        self.page.query_selector(f'css=div >> text=\"{founder_name}').click()
>>>>>>> 07ead5339047ffb4ce7f0fc017343772bb2f182c
