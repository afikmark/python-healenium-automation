from .login import LoginPage
from .inventory import InventoryPage
from .cart import CartPage
from web_pages.page import Page


class SwagLabs(Page):

    def __init__(self, driver):
        self.url = "https://www.saucedemo.com/"
        super().__init__(driver, self.url)
        self.login_page = LoginPage(driver, self.url)
        self.inventory_page = InventoryPage(driver, self.url)
        self.cart_page = CartPage(driver, self.url)
