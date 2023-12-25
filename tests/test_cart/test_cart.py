from pytest import mark
from web_pages.login import LoginPage
from web_pages.inventory import InventoryPage
from web_pages.cart import CartPage
from web_flows import login
import os


@mark.ui
def test_remove_item_from_cart(driver, app_config, user):
    # login
    login_page = LoginPage(driver, app_config.base_url)
    login(login_page, app_config.user['default'], app_config.user['password'])
    inventory_page = InventoryPage(driver, app_config.base_url)
    inventory_page.item = inventory_page.inventory_items.BACKPACK
    inventory_page.add_to_cart_btn.click()
    cart_page = CartPage(driver, app_config.base_url)
    cart_page.open()
    cart_page.cart_items_container.item = inventory_page.inventory_items.BACKPACK
    cart_page.cart_items_container.remove_item_btn().click()
    assert cart_page.cart_items_container.is_cart_empty(), 'is cart empty'


if __name__ == "__main__":
    print(os.environ)
