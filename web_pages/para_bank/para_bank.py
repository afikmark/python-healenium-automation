from web_pages.page import Page
from .home_page import ParaBankHomePage


class ParaBank(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.home_page = ParaBankHomePage(driver, self.url)
