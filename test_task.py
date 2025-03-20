import pytest, re
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


def test_contact_form(page: Page):

    page.get_by_role("link", name="Contact Us", exact=True).click()
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("div").filter(has_text=re.compile(r"^First Name\*This field is required$")).get_by_role("paragraph")).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(r"^Last Name\*This field is required$")).get_by_role("paragraph")).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(r"^E-mail Address\*This field is required$")).get_by_role("paragraph")).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(r"^Your Message\*This field is required$")).get_by_role("paragraph")).to_be_visible()
    page.get_by_role("textbox", name="E-mail Address*").fill("example.example.com")
    expect(page.get_by_text("Invalid e-mail address")).to_be_visible()
    page.get_by_role("textbox", name="Phone Number").fill("+abcdef")
    expect(page.get_by_text("Invalid phone number")).to_be_visible()


def test_locations_page(page: Page):

    page.get_by_label("Header").get_by_role("link", name="About us").hover()
    page.get_by_label("Header").get_by_role("link", name="Locations").click()
    expect(page.get_by_role("link", name="Aalborg Aalborg Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Austin Austin Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="Boston Boston Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="Chicago Chicago Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Copenhagen Copenhagen")).to_be_visible()
    expect(page.get_by_role("link", name="Dubai Dubai Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="Greenwich Greenwich Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Hong Kong Hong Kong Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Houston Houston Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="London London Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="Miami Miami Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="New York New York Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="San Francisco San Francisco")).to_be_visible()
    expect(page.get_by_role("link", name="Singapore Singapore Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Tokyo Tokyo Balyasny Asset")).to_be_visible()
    expect(page.get_by_role("link", name="Toronto Toronto Balyasny")).to_be_visible()
    expect(page.get_by_role("link", name="Warsaw Warsaw Balyasny")).to_be_visible()


def test_how_we_work_page(page: Page):

    page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    page.get_by_label("Header").get_by_role("link", name="Investment").click()
    expect(page.get_by_role("main")).to_match_aria_snapshot("- paragraph: Investment\n- heading \"An adaptive platform, made for business builders\" [level=2]\n- paragraph: A dynamic framework where our specialist investment teams constantly research the best risk/reward opportunities.\n- img \"Investing hero image illustration\"")
    page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    page.get_by_label("Header").get_by_role("link", name="Risk").click()
    expect(page.get_by_role("main")).to_match_aria_snapshot("- paragraph: Risk\n- heading \"A customized, adaptive approach to managing risk\" [level=2]\n- paragraph: Our Risk Teams partner with investment professionals to identify opportunities and customize dynamic risk guidelines to provide uncorrelated returns.\n- img \"Investing hero image illustration\"")
    page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    page.get_by_label("Header").get_by_role("link", name="Technology").click()
    expect(page.get_by_role("main")).to_match_aria_snapshot("- paragraph: Technology\n- heading \"Integrating technology to drive performance and efficiency\" [level=2]\n- paragraph: Our Technology Team empowers our investment professionals with the sophisticated platform of applications, infrastructure, services, data sets, and AI tools to support returns for our investors.\n- img \"Investing hero image illustration\"")
    page.get_by_label("Header").get_by_role("link", name="How we work").hover()
    page.get_by_label("Header").get_by_role("link", name="Business Infrastructure").click()
    expect(page.get_by_role("main")).to_match_aria_snapshot("- paragraph: Business Infrastructure\n- heading \"Collaborating across functions to magnify impact\" [level=2]\n- paragraph: Our Business Infrastructure Teams work to keep our platform world class, to support our risk takers and provide results for our investors.\n- img \"Investing hero image illustration\"")
