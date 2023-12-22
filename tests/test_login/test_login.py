from pytest import mark
from web_pages.inventory import InventoryPage
from web_pages.login import LoginPage


@mark.ui
def test_login(driver, app_config):
    login_page = LoginPage(driver, app_config.base_url)
    login_page.open()
    assert login_page.is_in_page, 'tests if login page is opened'
    login_page.login('standard_user', 'secret_sauce')
    inventory_page = InventoryPage(driver, app_config.base_url)
    assert inventory_page.is_in_page, 'tests if successfully redirected to inventory page'
