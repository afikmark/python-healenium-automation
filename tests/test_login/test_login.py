from pytest import mark


@mark.swag_smoke
@mark.swag_ui
def test_login(swag_ui, app_config, user):
    """
    This test validates the login functionality
    of the application.
    """
    login_page = swag_ui.login_page
    login_page.open()
    assert login_page.is_in_page, 'tests if login page is opened'
    login_page.login(app_config.user['default'], app_config.user['password'])
    inventory_page = swag_ui.inventory_page
    assert inventory_page.is_in_page, 'tests if successfully redirected to inventory page'
