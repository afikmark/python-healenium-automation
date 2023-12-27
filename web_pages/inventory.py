from web_pages.page import Page
from framework.ui_elements import DropDown, Button, Locator, By
from framework.logger import get_logger
from framework.utils import Regex

logger = get_logger()


class InventoryItems:
    BACKPACK = 'Sauce Labs Backpack'
    BIKE_LIGHT = 'Sauce Labs Bike Light'
    BOLT_T_SHIRT = 'Sauce Labs Bolt T-Shirt'
    FLEECE_JACKET = 'Sauce Labs Fleece Jacket',
    ONESIE = 'Sauce Labs Onesie'


class InventoryPage(Page):
    URL = "inventory.html"
    PRODUCT_SORT_DROPDOWN = '.product_sort_container'
    ADD_TO_CART_BTN = '#add-to-cart-sauce-labs-{}'
    REMOVE_FROM_CART_BTN = '#remove-sauce-labs-{}'
    INVENTORY_LIST = Locator(By.CSS_SELECTOR, '.inventory_list >.inventory_item')

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}{self.URL}'
        self.product_sort_dropdown = DropDown(self.PRODUCT_SORT_DROPDOWN, driver)
        self.inventory_items = InventoryItems()
        self._current_item = ''

    @property
    def item(self) -> str:
        return self._current_item

    @item.setter
    def item(self, item_name) -> None:
        try:
            item_name = Regex.match_all_after_prefix(prefix='Sauce Labs ', text=item_name)
        except AttributeError as e:
            logger.warning(f"an item was not found. item text:\n{item_name} error:{e}")
        formatted_item_name = item_name.lower().replace(" ", "-")
        self._current_item = formatted_item_name

    @property
    def add_to_cart_btn(self) -> Button:
        return Button(self.ADD_TO_CART_BTN.format(self.item), self.driver)

    @property
    def remove_from_cart_btn(self) -> Button:
        return Button(self.REMOVE_FROM_CART_BTN.format(self.item), self.driver)

    def get_inventory_item_names(self) -> list[str]:
        """
        retrieves all items in the inventory container and returns
        items names list
        """
        return [item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
                for item in self.driver.find_elements(self.INVENTORY_LIST)]

    def add_item_to_cart(self, item_name):
        self.item = item_name
        self.add_to_cart_btn.click()

    def add_items_to_cart(self, items: list):
        for item in items:
            self.item = item
            self.add_to_cart_btn.click()
