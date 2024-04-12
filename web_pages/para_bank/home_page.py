from selenium.webdriver.common.by import By
from web_pages.page import Page
from framework.ui_elements import TextInput, Button, HyperLink
from pydantic import BaseModel, SecretStr, Field, ValidationError
from framework.logger import get_logger

logger = get_logger()


class LoginValidationError(Exception):
    """Custom exception for login validation errors"""
    pass


class LoginForm(BaseModel):
    user_name: str = Field(examples=["test_user"],
                           description="User name")
    password: SecretStr = Field(examples=["Password123"],
                                description="Password of the user")


class ParaBankHomePage(Page):
    LOGIN_PANEL_SELECTOR: str = "#loginPanel"
    USER_NAME_SELECTOR: str = '[name="username"]'
    PASSWORD_SELECTOR: str = '[name="password"]'
    REGISTER_SELECTOR: str = '//*[@id="loginPanel"]//a[text()="Register"]'
    FORGOT_LOGIN_INFO_SELECTOR: str = '//*[@id="loginPanel"]//a[text()="Forgot login info?"]'

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.user_name_input = TextInput(self.USER_NAME_SELECTOR, driver)
        self.password_input = TextInput(self.PASSWORD_SELECTOR, driver)
        self.login_button = Button(f'{self.LOGIN_PANEL_SELECTOR} .login .button', driver)
        self.register_link = HyperLink(self.REGISTER_SELECTOR, driver, By.XPATH)
        self.forgot_login_info_link = HyperLink(self.FORGOT_LOGIN_INFO_SELECTOR, driver, By.XPATH)

    def login(self, user_name: str, password: str) -> None:
        """Logs in para bank with valid username and password"""
        try:
            login_data = LoginForm(user_name=user_name, password=password)
        except ValidationError as e:
            raise LoginValidationError(f"Validation error: {e}")
        self.user_name_input.enter_text(login_data.user_name)
        self.password_input.enter_text(login_data.password.get_secret_value())
        self.login_button.click()
