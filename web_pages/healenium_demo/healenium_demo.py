from web_pages.page import Page
from .login import LoginPage


class HealeniumDemo(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.login_page = LoginPage(driver, base_url)
