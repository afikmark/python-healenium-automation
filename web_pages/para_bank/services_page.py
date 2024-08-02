from web_pages.page import Page
from framework.ui_elements import Table


class ServicesTable(Table):

    def __init__(self, driver):
        super().__init__('//*[@class="heading"][1]/following-sibling::table[1]', driver)


class ParaBankServicesPage(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f'{base_url}/services.htm'
        self.services_table = ServicesTable(driver)
        self.book_store_services_table = Table('//*[@class="heading"][2]/following-sibling::table[1]', driver)
