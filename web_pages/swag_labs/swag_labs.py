from .login import LoginPage
from .inventory import InventoryPage
from .cart import CartPage
from web_pages.page import Page


class SwagLabs(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.login_page = LoginPage(driver, base_url)
        self.inventory_page = InventoryPage(driver, base_url)
        self.cart_page = CartPage(driver, base_url)
