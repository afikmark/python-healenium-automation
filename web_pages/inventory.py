from web_pages.page import Page
from framework.ui_elements import DropDown, Button, Locator, By
import re
from framework.logger import get_logger

logger = get_logger()


class InventoryPage(Page):
    URL = "inventory.html"
    PRODUCT_SORT_DROPDOWN = '.product_sort_container'
    ADD_TO_CART_BTN = '#add-to-cart-sauce-labs-{}'
    REMOVE_FROM_CART_BTN = '#remove-sauce-labs-{}'
    INVENTORY_ITEMS_NAMES = []
    INVENTORY_LIST = Locator(By.CSS_SELECTOR, '.inventory_list >.inventory_item')

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}{self.URL}'
        self.product_sort_dropdown = DropDown(self.PRODUCT_SORT_DROPDOWN, driver)
        self._current_item = ''
        self.get_inventory_items()

    @property
    def item(self) -> str:
        return self._current_item

    @item.setter
    def item(self, item_name) -> None:
        self._current_item = item_name

    @property
    def add_to_cart_btn(self) -> Button:
        return Button(self.ADD_TO_CART_BTN.format(self.item), self.driver)

    @property
    def remove_from_cart_btn(self) -> Button:
        return Button(self.REMOVE_FROM_CART_BTN.format(self.item), self.driver)

    def get_inventory_items(self) -> None:
        """
        retrieves all items in the inventory container and appends
        them to the Inventory items names list
        """
        inventory_list = self.driver.find_elements(self.INVENTORY_LIST)
        for item in inventory_list:
            item_text = item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
            try:
                item_name = re.match(r'Sauce Labs (.*)', item_text).group(1)
            except AttributeError as e:
                logger.warning(f"an item was not found. item text:\n{item_text} error:{e}")
                continue
            formatted_item_name = item_name.lower().replace(" ", "-")
            self.INVENTORY_ITEMS_NAMES.append(formatted_item_name)
