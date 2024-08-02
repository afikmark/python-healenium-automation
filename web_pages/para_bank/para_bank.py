from web_pages.page import Page
from .home_page import ParaBankHomePage
from .services_page import ParaBankServicesPage


class ParaBank(Page):

    def __init__(self, driver):
        self.url = "https://parabank.parasoft.com/parabank"
        super().__init__(driver, self.url)
        self.home_page = ParaBankHomePage(driver, self.url)
        self.services_page = ParaBankServicesPage(driver, self.url)
