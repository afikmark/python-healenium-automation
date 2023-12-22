from web_pages.page import Page
from framework.ui_elements import TextInput, Button, DropDown, By, Locator


class SearchPage(Page):
    URL = "online/he/search"
    RESULT_CONTAINER = Locator(By.CSS_SELECTOR, '.textContainer .middleContainer')
    RESULT_PRICE = Locator(By.CSS_SELECTOR, f'.middleContainer .price')
    ADD_TO_CART_BTN = Locator(By.CSS_SELECTOR, '.addToCartWrapperOld .js-add-to-cart')
    SORT = '#sortBySection'

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}{self.URL}'
        self.sort = DropDown(self.SORT, self.driver)

    def search(self, text: str):
        self.driver.get(f'{self.url}?text={text}')

    def add_product(self, product_name: str):
        # TODO: Handle Stale Element
        # product: [WebElement] = [product for product in self.driver.find_elements(self.RESULT_CONTAINER) if
        #                          product_name in product.text]

        for product in self.driver.find_elements(self.RESULT_CONTAINER):
            if product_name in product.text:
                self.driver.click(Locator(By.CSS_SELECTOR, f'{self.RESULT_CONTAINER}  {self.ADD_TO_CART_BTN}'))
                break
