from web_pages.inventory import InventoryPage
from web_pages.login import LoginPage
from web_flows import login
from pytest import mark


@mark.ui
def test_inventory_add_to_cart_button(driver, app_config, user):
    login_page = LoginPage(driver, app_config.base_url)
    login(login_page, app_config.user['default'], app_config.user['password'])
    inventory_page = InventoryPage(driver, app_config.base_url)
    inventory_page.item = inventory_page.inventory_items.BACKPACK
    inventory_page.add_to_cart_btn.click()
    # assert tha button changed to "remove" after clicking add to cart
    assert inventory_page.remove_from_cart_btn.text == 'Remove', 'text of the add to cart button'
