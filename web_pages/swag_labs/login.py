from web_pages.swag_labs.page import Page
from framework.ui_elements import TextInput, Button


class LoginPage(Page):
    USER_NAME_SELECTOR = '#user-name'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = '[data-test="login-button"]'

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.user_name_input = TextInput(self.USER_NAME_SELECTOR, driver)
        self.password_input = TextInput(self.PASSWORD_SELECTOR, driver)
        self.login_button = Button(self.LOGIN_BUTTON_SELECTOR, driver)

    def login(self, email, password):
        """ fill username and password and submit the login button """
        self.user_name_input.enter_text(email)
        self.password_input.enter_text(password)
        self.login_button.click()
