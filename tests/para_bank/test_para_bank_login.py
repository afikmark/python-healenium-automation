from assertpy import assert_that


def test_login_form(para_bank_ui):
    """The objective of this test is to verify the ui elements of the login form"""
    home_page = para_bank_ui.home_page
    home_page.open()
    assert_that(home_page.login_panel.forgot_login_info_link.label, "login info link text label").is_equal_to(
        "Forgot login info?")
    assert_that(home_page.login_panel.register_link.label, "register link text label").is_equal_to("Register")



