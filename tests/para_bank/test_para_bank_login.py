from assertpy import assert_that


def test_login_form(para_bank_ui):
    """The objective of this test is to verify the ui elements of the login form"""
    home_page = para_bank_ui.home_page
    home_page.open()
    assert_that(home_page.login_panel.forgot_login_info_link.label, "login info link text label").is_equal_to(
        "Forgot login info?")
    assert_that(home_page.login_panel.register_link.label, "register link text label").is_equal_to("Register")


def test_login(para_bank_ui):
    home_page = para_bank_ui.home_page
    home_page.open()
    home_page.login_panel.login('Ashley7', 'test_password')
    # todo: assert account overview panel


def test_login_api(para_bank_api):
    res = para_bank_api.login('Ashley7', 'test_password')
    assert_that(res.status_code, 'login attempt status code').is_equal_to(200)
