from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from typing import NamedTuple


class Locator(NamedTuple):
    """ Locator object """
    by: str
    selector: str


class Dialog:
    """ Dialog object """
    ROOT_SELECTOR = '#cfcModal'
    CLOSE_BUTTON_SELECTOR = '.btnClose'

    def __init__(self, driver):
        self.driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.ROOT_SELECTOR)
        self._close_btn_selector = f'{self.ROOT_SELECTOR} .modal-header .btnClose[aria-label="סגור"]'
        self.share_close_button_selector = '.dy-modal-contents .dy-lb-close'

    def close_dialog(self):
        Button(self._close_btn_selector, self.driver).click()
        self.driver.wait.until_invisibility_of_element(Locator(By.CSS_SELECTOR, self._close_btn_selector))

    def close_share_window(self):
        Button(self.share_close_button_selector, self.driver).click()
        self.driver.wait.until_invisibility_of_element(Locator(By.CSS_SELECTOR, self.share_close_button_selector))


class TextInput:
    """ TextInput object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'input{root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    def enter_text(self, text: str):
        """ enters text to element """
        element = self._driver.find_element(self._locator)
        element.clear()
        element.send_keys(text)


class Button:
    """ Button object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'{root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    def click(self):
        self._driver.click(self._locator)


class DropDown:
    """ DropDown Object """

    def __init__(self, root_selector, driver):
        self.root_selector = f'.select_container {root_selector}'
        self._driver = driver
        self._locator = Locator(By.CSS_SELECTOR, self.root_selector)

    @property
    def options(self) -> list:
        element = self._driver.find_element(self._locator)
        return Select(element).options

    def select_by_value(self, value: str):
        element = self._driver.find_element(self._locator)
        Select(element).select_by_value(value)

    def select_by_index(self, index: int):
        element = self._driver.find_element(self._locator)
        Select(element).select_by_index(index)