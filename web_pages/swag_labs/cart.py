from web_pages.swag_labs.page import Page
from framework.ui_elements import Button, Locator, By
from framework.logger import get_logger
from framework.utils import Regex

logger = get_logger()


class CartPage(Page):
    URL = "cart.html"
    CONTINUE_SHOPPING_BTN = '#continue-shopping'
    CHECKOUT_BTN = '#checkout'
    CART_ITEMS = Locator(By.CSS_SELECTOR, '.cart_item')

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}{self.URL}'
        self.continue_shopping_btn = Button(self.CONTINUE_SHOPPING_BTN, driver)
        self.checkout_btn = Button(self.CHECKOUT_BTN, driver)
        self.cart_items_container = CartItemsContainer(driver)


class CartItemsContainer:
    CART_CONTENTS_CONTAINER = Locator(By.CSS_SELECTOR, '.cart_contents_container .cart_item')
    ROOT_SELECTOR = Locator(By.CSS_SELECTOR, '.cart_item')
    REMOVE_ITEM_BTN = '#remove-sauce-labs-{}'

    def __init__(self, driver):
        self._driver = driver
        self._current_item = ''

    def is_cart_empty(self) -> bool:
        return len(self._driver.find_elements(self.CART_CONTENTS_CONTAINER)) == 0

    @property
    def items(self):
        return self._driver.find_elements(self.ROOT_SELECTOR)

    @property
    def item(self) -> str:
        return self._current_item

    @item.setter
    def item(self, item_name) -> None:
        self._current_item = item_name

    def remove_item_btn(self):
        item_name = Regex.match_all_after_prefix(prefix='Sauce Labs ', text=self.item)
        formatted_item = item_name.lower().replace(" ", "-")
        return Button(self.REMOVE_ITEM_BTN.format(formatted_item), self._driver)

    @staticmethod
    def item_price(item):
        return item.find_element(*Locator(By.CSS_SELECTOR, '.inventory_item_price')).text

    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.find_element(*Locator(By.CSS_SELECTOR, '.inventory_item_name')).text \
                    == item_name:
                return item
        else:
            logger.info(f"Could not find item: {item_name}")
