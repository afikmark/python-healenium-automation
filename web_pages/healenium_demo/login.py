from framework.ui_elements import TextInput, Button, Locator
from web_pages.page import Page


class LoginPage(Page):
    USER_NAME = "#name"
    EMAIL = "#email"
    PASSWORD = "#password"
    SUBMIT_FORM_BTN = "[type='button']"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.user_name = TextInput(self.USER_NAME, driver)
        self.email = TextInput(self.EMAIL, driver)
        self.password = TextInput(self.PASSWORD, driver)
        self.submit_btn = Button(self.SUBMIT_FORM_BTN, driver)

    def login_healenium(self, name, email, password):
        """ fill username and password and submit the login button """
        self.user_name.enter_text(name)
        self.email.enter_text(email)
        self.password.enter_text(password)
        self.submit_btn.click()
