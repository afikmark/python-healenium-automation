import pytest
from framework.web_browser import WebBrowser
from framework.logger import get_logger
from tests import Config
from web_pages.swag_labs import SwagLabs
import json
logger = get_logger()


@pytest.fixture(scope='function', params=['chrome', 'firefox', 'edge'])
def driver(request):
    browser = request.param
    driver = WebBrowser(browser)
    yield driver
    driver.quit_driver()


@pytest.fixture(scope="function")
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


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def user(request):
    return request.config.getoption("--user")


@pytest.fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


def pytest_collection_modifyitems(items):
    test_info = {
        item.nodeid.split("::")[1]: item.function.__doc__
        for item in items
    }
    logger.info('Test information including params:\n{}'.format(json.dumps(test_info, indent=2)))
