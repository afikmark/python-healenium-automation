from web_pages.page import Page
from framework.ui_elements import DropDown, Button


class InventoryPage(Page):
    URL = "inventory/"
    PRODUCT_SORT_DROPDOWN = '.product_sort_container'
    ADD_TO_CART_BTN = '#add-to-cart-sauce-labs-{}'
    ITEMS = ['backpack', '']  # TODO: add all items

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}{self.URL}'
        self.product_sort_dropdown = DropDown(self.PRODUCT_SORT_DROPDOWN, driver)
        self._current_item = ''

    @property
    def item(self):
        return self._current_item

    @item.setter
    def item(self, item_name):
        self._current_item = item_name

    @property
    def add_to_cart_btn(self):
        return Button(self.ADD_TO_CART_BTN.format(self.item), self.driver)
