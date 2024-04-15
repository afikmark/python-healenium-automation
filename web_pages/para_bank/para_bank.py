from web_pages.page import Page
from .home_page import ParaBankHomePage


class ParaBank(Page):

    def __init__(self, driver):
        self.url = "https://parabank.parasoft.com/parabank/index.htm"
        super().__init__(driver, self.url)
        self.home_page = ParaBankHomePage(driver, self.url)
