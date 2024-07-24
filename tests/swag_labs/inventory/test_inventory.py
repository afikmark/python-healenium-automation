from web_pages.swag_labs.web_flows.swag_web_flows import login
from pytest import mark
from assertpy import assert_that


def test_inventory_add_to_cart_button(swag_ui, app_config, user):
    """
    This test verifies the functionality of add to cart button
    """
    login_page = swag_ui.login_page
    login(login_page, app_config.user_name, app_config.user_password)
    inventory_page = swag_ui.inventory_page
    inventory_page.item = inventory_page.inventory_items.BACKPACK
    inventory_page.add_to_cart_btn.click()
    assert_that(inventory_page.remove_from_cart_btn.text, 'text of the add to cart button').is_equal_to('Remove')
