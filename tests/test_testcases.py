def test_testcases(desktop_app):
    founder_names = "Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"
    desktop_app.hover_over('About us')
    desktop_app.navigate_to('Leadership')
    for founder_name in founder_names:
        assert desktop_app.check_founders_exist(founder_name)
