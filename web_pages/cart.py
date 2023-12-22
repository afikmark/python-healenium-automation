from web_pages.page import Page
from framework.ui_elements import TextInput, Button, Locator, By
from framework.logger import get_logger

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
    ROOT_SELECTOR = Locator(By.CSS_SELECTOR, '.cart_item')

    def __init__(self, driver):
        self._driver = driver

    @property
    def items(self):
        return self._driver.find_elements(self.ROOT_SELECTOR)

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
