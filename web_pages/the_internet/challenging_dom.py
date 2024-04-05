from framework.ui_elements import TextInput, Button, Locator, By
from web_pages.page import Page


class ChallengingDom(Page):
    _QUX_BUTTON = "#e1a05c90-d57d-013c-f7aa-4aee64b33adc"
    _FOO_BUTTON = "#e1a05c90-d57d-013c-f7aa-4aee64b33adc"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}/challenging_dom'
        self.qux_btn = Button(By.CSS_SELECTOR, self._QUX_BUTTON)
        self.foo_btn = Button(By.CSS_SELECTOR, self._FOO_BUTTON)
