from pytest import mark
from web_pages.swag_labs.web_flows.swag_web_flows import login
from assertpy import assert_that


def test_remove_item_from_cart(swag_ui, app_config, user):
    """
    This test validates the flow of removing items from the cart
    """
    login_page = swag_ui.login_page
    login(login_page, app_config.user_name, app_config.user_password)
    inventory_page = swag_ui.inventory_page
    inventory_page.item = inventory_page.inventory_items.BACKPACK
    inventory_page.add_to_cart_btn.click()
    cart_page = swag_ui.cart_page
    cart_page.open()
    cart_page.cart_items_container.item = inventory_page.inventory_items.BACKPACK
    cart_page.cart_items_container.remove_item_btn().click()
    assert_that(cart_page.cart_items_container.is_cart_empty(), 'is cart empty').is_true()
