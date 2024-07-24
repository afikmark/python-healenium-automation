from pytest import mark
from framework.logger import get_logger
from assertpy import assert_that
logger = get_logger()


@mark.swag_sanity
def test_login(swag_ui, app_config, user, reporter):
    """
    This test validates the login functionality
    of the application.
    """
    login_page = swag_ui.login_page
    reporter.step(name='Step', message='open swag labs login page')
    login_page.open()
    assert_that(login_page.is_in_page, "login page open").is_true()
    reporter.step(name='Step', message='Login to swag labs')
    login_page.login(app_config.user_name, app_config.user_password)
    inventory_page = swag_ui.inventory_page
    reporter.step(name='Step', message='assert successfully redirected to inventory page after login ')
    assert_that(inventory_page.is_in_page, 'successfully redirected to inventory page').is_true()


@mark.swag_sanity
def test_fail_login(swag_ui, app_config, user, reporter):
    """
    this test will fail if ran without healenium
    and will pass if ran with healenium
    """
    login_page = swag_ui.login_page
    reporter.step(name='Step', message='open swag labs login page')
    login_page.open()
    assert_that(login_page.is_in_page, "login page open").is_true()
    reporter.step(name='Step', message='input user name as usual')
    login_page.user_name_input.enter_text(app_config.user_name)
    login_page.user_name_input.clear_text()
    reporter.step(name='Step', message='Change the id of user name input to new-user-name')
    login_page.execute_js(f"return document.getElementById('user-name').id ='new-user-name'")
    login_page.user_name_input.enter_text(app_config.user_name)
    assert_that(login_page.user_name_input.value, 'current user name input value').is_equal_to(app_config.user_name)
    logger.info(
        f"the id of standard user has changed to:"
        f"{login_page.execute_js(f"return document.getElementById('new-user-name').id")}.\n"
        f"although the user name id selector in the POM is {login_page.USER_NAME_SELECTOR},"
        f" healenium was able to locate the element and pass the test.\n"
        f" we are able to return the value of user-name input after the id was changed")
