from web_pages.page import Page
from framework.ui_elements import Locator, By


class Common(Page):
    CART_LINK = Locator(By.CSS_SELECTOR, "#shopping_cart_container a")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url

    def click_cart_link(self) -> None:
        self.driver.click(self.CART_LINK)
