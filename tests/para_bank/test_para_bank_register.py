from assertpy import assert_that


def test_register(para_bank_ui):
    """The objective of this test is to verify the registration flow"""
    para_bank_ui.home_page.open()
    registration_panel = para_bank_ui.home_page.registration_panel
    registration_panel.register()
