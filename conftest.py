from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App



@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

# @fixture
# def get_browser(get_playwright, request):
#     browser = request.config.getoption('--browser')
#     headless = request.config.getini('headless')
    
#     if headless == 'True':
#         headless = True
#     else:
#         headless = False

#     if browser == 'chromium':
#         bro = get_playwright.chromium.launch(headless = headless)
#     elif browser == 'firefox':
#         bro = get_playwright.firefox.launch(headless = headless)
#     elif browser == 'webkit':
#         bro = get_playwright.webkit.launch(headless = headless)
#     else:
#         assert False, 'unsupported browser type'
    
#     yield bro
#     bro.close()

@fixture
def desktop_app(get_playwright, request):
    base_url = request.config.getini('base_url')
    app = App(get_playwright, base_url=base_url)
    app.goto('/')
    yield app
    app.close()

@fixture
def mobile_app(get_playwright, request):
    base_url = request.config.getini('base_url')
    device = request.config.getoption('--device')
    app = App(get_playwright, base_url= base_url, device= device)
    app.goto('/')
    yield app
    app.close()

def pytest_addoption(parser):
#     # parser.addoption('--device', action ='store', default= '')
#     # parser.addoption('--browser', action ='store', default= 'chromium')
#     # parser.addini('base_url', help = "base url of the site under test", default = "https://www.bamfunds.com")
    parser.addini('headless', help = "run browser in headless mode")

