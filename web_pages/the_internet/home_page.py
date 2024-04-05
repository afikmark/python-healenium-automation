from web_pages.page import Page


class HomePage(Page):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
