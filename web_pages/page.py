from framework.ui_elements import Dialog
from framework.web_browser import WebBrowser


class Page:
    """ Page object """

    def __init__(self, browser: WebBrowser, url):
        self.driver = browser
        self.dialog = Dialog(self.driver)
        self.url = url

    @property
    def is_in_page(self):
        """ validates browser is in current page """
        current_url = self.driver.get_current_url()
        return current_url == self.url

    def open(self):
        self.driver.get(self.url)
