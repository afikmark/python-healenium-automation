from web_pages.page import Page
from framework.ui_elements import TextInput, Button


class CartPage(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
