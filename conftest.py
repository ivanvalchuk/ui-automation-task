from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App



@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def get_browser(get_playwright, request):
    browser = ' '.join(request.config.getoption('--browser'))
    headless = request.config.getini('headless')
    
    if headless == 'True':
        headless = True
    else:
        headless = False
    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless = headless)
    elif browser == 'firefox':
        bro = get_playwright.firefox.launch(headless = headless)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless = headless)
    else:
        assert False, 'unsupported browser type'
    
    yield bro
    bro.close()

@fixture
def desktop_app(get_browser, request):
    base_url = request.config.getini('base_url')
    app = App(get_browser, base_url=base_url)
    app.goto('/')
    yield app
    app.close()

@fixture
def mobile_app(get_playwright, get_browser, request):
    base_url = request.config.getini('base_url')
    device = request.config.getoption('--device')
    device_config = get_playwright.devices.get(device)

    if device_config is not None:
        device_config.update(**device_config)
    else:
        device_config = device

    app = App(get_browser, base_url= base_url, **device_config)
    app.goto('/')
    yield app
    app.close()

def pytest_addoption(parser):
#     # parser.addoption('--device', action ='store', default= '')
    # parser.addoption('--browser', action ='store', default= 'chromium')
#     # parser.addini('base_url', help = "base url of the site under test", default = "https://www.bamfunds.com")
    parser.addini('headless', help = "run browser in headless mode")