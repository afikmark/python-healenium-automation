from selenium.webdriver.common.by import By

from forms.para_bank.register import RegistrationForm, RegisterValidationError
from forms.para_bank.login import LoginForm, LoginValidationError
from web_pages.page import Page
from framework.ui_elements import TextInput, Button, HyperLink, Component, Locator
from pydantic import ValidationError
from framework.logger import get_logger

logger = get_logger()


class LoginPanel(Component):
    USER_NAME_SELECTOR: str = '[name="username"]'
    PASSWORD_SELECTOR: str = '[name="password"]'
    REGISTER_SELECTOR: str = '//*[@id="loginPanel"]//a[text()="Register"]'
    FORGOT_LOGIN_INFO_SELECTOR: str = '//*[@id="loginPanel"]//a[text()="Forgot login info?"]'

    def __init__(self, root_selector: str, driver):
        super().__init__(root_selector, driver)
        self.user_name_input = TextInput(self.USER_NAME_SELECTOR, driver)
        self.password_input = TextInput(self.PASSWORD_SELECTOR, driver)
        self.login_button = Button(f'{root_selector} .login .button', driver)
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


class RegistrationPanel(Component):
    FIRST_NAME_SELECTOR: str = '#customerForm [name="customer.firstName"]'
    LAST_NAME_SELECTOR: str = '#customerForm [name="customer.lastName"]'
    ADDRESS_STREET_SELECTOR: str = '#customerForm [name="customer.address.street"]'
    ADDRESS_CITY_SELECTOR: str = '#customerForm [name="customer.address.city"]'
    ADDRESS_STATE_SELECTOR: str = '#customerForm [name="customer.address.state"]'
    ADDRESS_ZIPCODE_SELECTOR: str = '#customerForm [name="customer.address.zipCode"]'
    PHONE_NUMBER_SELECTOR: str = '#customerForm [name="customer.phoneNumber"]'
    SSN_SELECTOR: str = '#customerForm [name="customer.ssn"]'
    USER_NAME_SELECTOR: str = '#customerForm [name="customer.username"]'
    PASSWORD_SELECTOR: str = '#customerForm [name="customer.password"]'
    PASSWORD_CONFIRM_SELECTOR: str = '#customerForm #repeatedPassword'
    REGISTER_SELECTOR: str = '#customerForm .button[type="submit"]'


    def __init__(self, root_selector: str, driver):
        super().__init__(root_selector, driver)
        self.title_locator = Locator(By.CSS_SELECTOR, f'{root_selector} h1.title')
        self.sub_title_locator = Locator(By.CSS_SELECTOR, f'{root_selector} p')
        self.first_name_input = TextInput(f'{root_selector} {self.FIRST_NAME_SELECTOR}', driver)
        self.last_name_input = TextInput(f'{root_selector} {self.LAST_NAME_SELECTOR}', driver)
        self.address_street_input = TextInput(f'{root_selector} {self.ADDRESS_STREET_SELECTOR}', driver)
        self.address_city_input = TextInput(f'{root_selector} {self.ADDRESS_CITY_SELECTOR}', driver)
        self.address_state_input = TextInput(f'{root_selector} {self.ADDRESS_STATE_SELECTOR}', driver)
        self.address_zipcode_input = TextInput(f'{root_selector} {self.ADDRESS_ZIPCODE_SELECTOR}', driver)
        self.phone_number_input = TextInput(f'{root_selector} {self.PHONE_NUMBER_SELECTOR}', driver)
        self.ssn_input = TextInput(f'{root_selector} {self.SSN_SELECTOR}', driver)
        self.user_name_input = TextInput(f'{root_selector} {self.USER_NAME_SELECTOR}', driver)
        self.password_input = TextInput(f'{root_selector} {self.PASSWORD_SELECTOR}', driver)
        self.password_confirm_input = TextInput(f'{root_selector} {self.PASSWORD_CONFIRM_SELECTOR}', driver)
        self.register_btn = Button(f'{root_selector} {self.REGISTER_SELECTOR}', driver)

    @property
    def title_text(self) -> str:
        return self._driver.get_text(self.title_locator)

    @property
    def sub_title_text(self) -> str:
        return self._driver.get_text(self.sub_title_locator)

    def register(self, register_data: dict) -> None:
        """Takes registration data and register a new user"""
        try:
            register_data.pop("address")
            registration_data = RegistrationForm(**register_data)
        except ValidationError as e:
            raise RegisterValidationError(f"Validation error: {e}")
        self.first_name_input.enter_text(registration_data.first_name)
        self.last_name_input.enter_text(registration_data.last_name)
        self.address_street_input.enter_text(registration_data.address_street)
        self.address_city_input.enter_text(registration_data.city)
        self.address_state_input.enter_text(registration_data.state)
        self.address_zipcode_input.enter_text(registration_data.zip_code)
        self.phone_number_input.enter_text(registration_data.phone_number)
        self.ssn_input.enter_text(registration_data.ssn)
        self.user_name_input.enter_text(registration_data.user_name)
        self.password_input.enter_text(registration_data.password.get_secret_value())
        self.password_confirm_input.enter_text(registration_data.confirm_password.get_secret_value())
        self.register_btn.click()


class ParaBankHomePage(Page):
    LOGIN_PANEL_SELECTOR: str = "#loginPanel"
    REGISTRATION_PANEL_SELECTOR: str = "#rightPanel"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url
        self.login_panel = LoginPanel(self.LOGIN_PANEL_SELECTOR, driver)
        self.registration_panel = RegistrationPanel(self.REGISTRATION_PANEL_SELECTOR, driver)
