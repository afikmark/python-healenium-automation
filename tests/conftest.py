from pytest import fixture, mark
from framework.web_browser import WebBrowser
from tests import Config
from web_pages.swag_labs import SwagLabs
from pytest import fixture


@fixture(scope='function', params=['chrome', 'firefox', 'edge'])
def driver(request):
    browser = request.param
    driver = WebBrowser(browser)
    yield driver
    driver.quit_driver()


@fixture(scope="function")
def swag_ui(driver, app_config):
    return SwagLabs(driver, app_config.base_url)


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     help="Environment to run tests",
                     default="qa"
                     )
    parser.addoption("--browser",
                     action="store",
                     help="browser for the automation tests",
                     default="chrome")

    parser.addoption("--user",
                     action="store",
                     help="user for swag labs",
                     default="standard")


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def user(request):
    return request.config.getoption("--user")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
