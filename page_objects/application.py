from playwright.sync_api import Browser
from .test_cases import TestCases

class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)
    
    def hover_over(self, menu: str):
        self.page.get_by_label("Header").get_by_role("link", name = menu).hover()

    def navigate_to(self, menu: str):
        self.page.get_by_label("Header").get_by_role("link", name = menu).click()
    
    def check_founders_exist(self, founder_name: str):
        return self.page.get_by_role("link", name=founder_name) is not None
    
    def click_menu_button(self, menu: str):
        self.page.get_by_role("button", name = menu).click()

    # def is_menu_button_visible(self):
    #     return self.page.is_visible('.menuBtn')

    # def navigate_to_contact_form(self):

    #     self.page.get_by_role("link", name="Contact Us", exact=True).click()
    #     self.page.get_by_role("button", name="Submit").click()
    
    # def check_contact_form_validation(self):
    #     self.page.locator("div").filter(has_text=self.re.compile(r"^First Name\*This field is required$")).get_by_role("paragraph").to_be_visible()
    #     self.page.locator("div").filter(has_text=self.re.compile(r"^Last Name\*This field is required$")).get_by_role("paragraph").to_be_visible()
    #     self.page.locator("div").filter(has_text=self.re.compile(r"^E-mail Address\*This field is required$")).get_by_role("paragraph").to_be_visible()
    #     self.page.locator("div").filter(has_text=self.re.compile(r"^Your Message\*This field is required$")).get_by_role("paragraph").to_be_visible()
    #     self.page.get_by_role("textbox", name="E-mail Address*").fill("example.example.com")
    #     self.page.get_by_text("Invalid e-mail address").to_be_visible()
    #     self.page.get_by_role("textbox", name="Phone Number").fill("+abcdef")
    #     self.page.get_by_text("Invalid phone number").to_be_visible()
    
    # def navigate_to_locations_page(self):

    #     self.page.get_by_label("Header").get_by_role("link", name="About us").hover()
    #     self.page.get_by_label("Header").get_by_role("link", name="Locations").click()

    # def check_locations_page(self):

    #     self.page.get_by_role("link", name="Aalborg Aalborg Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Austin Austin Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="Boston Boston Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="Chicago Chicago Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Copenhagen Copenhagen").to_be_visible()
    #     self.page.get_by_role("link", name="Dubai Dubai Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="Greenwich Greenwich Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Hong Kong Hong Kong Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Houston Houston Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="London London Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="Miami Miami Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="New York New York Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="San Francisco San Francisco").to_be_visible()
    #     self.page.get_by_role("link", name="Singapore Singapore Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Tokyo Tokyo Balyasny Asset").to_be_visible()
    #     self.page.get_by_role("link", name="Toronto Toronto Balyasny").to_be_visible()
    #     self.page.get_by_role("link", name="Warsaw Warsaw Balyasny").to_be_visible()
    
    # def navigate_to_investment_page(self):

    #     self.page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    #     self.page.get_by_label("Header").get_by_role("link", name="Investment").click()
    
    # def check_investment_page(self):
    #     self.page.get_by_role("main").to_match_aria_snapshot("- paragraph: Investment\n- heading \"An adaptive platform, made for business builders\" [level=2]\n- paragraph: A dynamic framework where our specialist investment teams constantly research the best risk/reward opportunities.\n- img \"Investing hero image illustration\"")
        
    # def navigate_to_risk_page(self):
    #     self.page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    #     self.page.get_by_label("Header").get_by_role("link", name="Risk").click()
    
    # def check_risk_page(self):
    #     self.expect(self.page.get_by_role("main")).to_match_aria_snapshot("- paragraph: Risk\n- heading \"A customized, adaptive approach to managing risk\" [level=2]\n- paragraph: Our Risk Teams partner with investment professionals to identify opportunities and customize dynamic risk guidelines to provide uncorrelated returns.\n- img \"Investing hero image illustration\"")
    
    # def navigate_to_technology_page(self):
    #     self.page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    #     self.page.get_by_label("Header").get_by_role("link", name="Technology").click()
    
    # def check_technology_page(self):
    #     self.page.get_by_role("main").to_match_aria_snapshot("- paragraph: Technology\n- heading \"Integrating technology to drive performance and efficiency\" [level=2]\n- paragraph: Our Technology Team empowers our investment professionals with the sophisticated platform of applications, infrastructure, services, data sets, and AI tools to support returns for our investors.\n- img \"Investing hero image illustration\"")
    
    # def navigate_to_business_infrastructure_page(self):
    #     self.page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    #     self.page.get_by_label("Header").get_by_role("link", name="Business Infrastructure").click()
    
    # def check_business_infrastructure_page(self):
    #     self.page.get_by_role("main").to_match_aria_snapshot("- paragraph: Business Infrastructure\n- heading \"Collaborating across functions to magnify impact\" [level=2]\n- paragraph: Our Business Infrastructure Teams work to keep our platform world class, to support our risk takers and provide results for our investors.\n- img \"Investing hero image illustration\"")

    def close(self):
        self.page.close()
        self.context.close()