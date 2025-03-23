import allure

@allure.title("Check Founders' section => check if all 3 founders' names are displayed")
def test_mobile(mobile_app):
    mobile_app.click_menu_button("Open Main Navigation")
    founder_names = "Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    for founder_name in founder_names:
        assert mobile_app.check_founders_exist(founder_name)
