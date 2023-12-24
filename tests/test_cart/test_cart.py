import time

from pytest import mark
from web_pages.login import LoginPage
from web_pages.inventory import InventoryPage
from web_pages.cart import CartPage
from web_flows import login


@mark.ui
def test_remove_item_from_cart(driver, app_config):
    # login
    login_page = LoginPage(driver, app_config.base_url)
    login(login_page, 'standard_user', 'secret_sauce')
    inventory_page = InventoryPage(driver, app_config.base_url)
    inventory_page.item = inventory_page.INVENTORY_ITEMS_NAMES[0]
    inventory_page.add_to_cart_btn.click()
    cart_page = CartPage(driver, app_config.base_url)
    cart_page.open()
    cart_page.cart_items_container.item = 'Sauce Labs Backpack'
    cart_page.cart_items_container.remove_item_btn().click()
    assert cart_page.cart_items_container.is_cart_empty(), 'is cart empty'
