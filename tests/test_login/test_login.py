from pytest import mark


@mark.swag_smoke
@mark.swag_ui
def test_login(swag_ui, app_config, user, reporter):
    """
    This test validates the login functionality
    of the application.
    """
    login_page = swag_ui.login_page
    reporter.step(name='Step', message='open swag labs login page')
    login_page.open()
    assert login_page.is_in_page, 'tests if login page is opened'
    reporter.step(name='Step', message='Login to swag labs')
    login_page.login(app_config.user['default'], app_config.user['password'])
    inventory_page = swag_ui.inventory_page
    reporter.step(name='Step', message='assert successfully redirected to inventory page after login ')
    assert inventory_page.is_in_page, 'tests if successfully redirected to inventory page'


# def test_fail_login(swag_ui, app_config, user, reporter):
#     """
#     tests example failure with screenshot
#     """
#     login_page = swag_ui.login_page
#     reporter.step(name='Step', message='open swag labs login page')
#     login_page.open()
#     assert login_page.is_in_page, 'tests if login page is opened'
#     reporter.step(name='Step', message='Login to swag labs- this will result in failure')
#     login_page.login("myLogin", "WrongPassword")
#     inventory_page = swag_ui.inventory_page
#     assert inventory_page.is_in_page, 'tests if successfully redirected to inventory page'
