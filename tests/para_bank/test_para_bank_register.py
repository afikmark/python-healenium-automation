from assertpy import assert_that
from settings import TEMPLATE_FILES
from forms.para_bank.register import RegistrationFactory
from framework.utils import read_file
import os
from framework.utils import retry_on_false
from api_flows.para_bank import ParaBankApi


def test_login():
    api = ParaBankApi()
    res = api.login("john", "demo")
    print(res)


def test_register(para_bank_ui, reporter):
    """The objective of this test is to verify the registration flow"""
    reporter.step(name="Step", message="Opening home page")
    para_bank_ui.home_page.open()
    registration_panel = para_bank_ui.home_page.registration_panel
    reporter.step(name="Step", message="Click on register link")
    para_bank_ui.home_page.login_panel.register_link.click_link()
    data = RegistrationFactory()
    reporter.step(name="Step", message=f"Registering with user data: {data}")
    registration_panel.register(data)
    expected_title_text = f'Welcome {data["first_name"]}'
    wait_for_title(registration_panel, expected_text=expected_title_text)
    reporter.step(name="Step", message="Asserting post registration title")
    assert_that(registration_panel.title_text, "Post registration title text").is_equal_to(expected_title_text)
    expected_sub_title_text = read_file(os.path.join(TEMPLATE_FILES, "para_bank/registration_complete.txt"))
    wait_for_sub_title(registration_panel, expected_sub_title_text)
    reporter.step(name="Step", message="Asserting post registration sub title")
    assert_that(registration_panel.sub_title_text, "Post registration sub title text").is_equal_to(
        expected_sub_title_text)


@retry_on_false()
def wait_for_title(registration_panel, expected_text) -> bool:
    """Wait until expected title text is displayed"""
    return registration_panel.title_text == expected_text


@retry_on_false()
def wait_for_sub_title(registration_panel, expected_text) -> bool:
    """Wait until expected sub title text is displayed"""
    return registration_panel.sub_title_text == expected_text
