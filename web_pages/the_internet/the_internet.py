from web_pages.page import Page
from .home_page import HomePage
from .challenging_dom import ChallengingDom


class HealeniumDemo(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.home_page = HomePage(driver, base_url)
        self.challenging_dom = ChallengingDom(driver, base_url)
