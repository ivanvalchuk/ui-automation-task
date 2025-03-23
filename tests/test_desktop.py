import allure

@allure.title("Check Founders' section => check if all 3 founders' names are displayed")
def test_desktop(desktop_app):
    founder_names = "1Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    desktop_app.hover_over('About us')
    desktop_app.navigate_to('Leadership')
    for founder_name in founder_names:
        assert desktop_app.check_founders_exist(founder_name)
