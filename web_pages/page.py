from framework.web_browser import WebBrowser


class Page:
    """ Page object """

    def __init__(self, browser: WebBrowser, url):
        self.driver = browser
        self.url = url

    def __getattr__(self, name: str):
        """ Delegate attribute access to the WebBrowser instance """
        if hasattr(self.driver, name):
            return getattr(self.driver, name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    @property
    def is_in_page(self) -> bool:
        """ validates browser is in current page """
        current_url = self.driver.get_current_url()
        return current_url == self.url

    def open(self) -> None:
        self.driver.get(self.url)
