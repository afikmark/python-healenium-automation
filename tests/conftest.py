import pytest
from framework.web_browser import WebBrowser
from framework.logger import get_logger
from settings import ROOT_DIR
from tests import Config
from tests.config import RemoteMode
from web_pages.healenium_demo.healenium_demo import HealeniumDemo
from web_pages.swag_labs.swag_labs import SwagLabs
import json
from typing import Dict
from framework.reporter import AllureReporter
from pytest import StashKey, CollectReport

logger = get_logger()
phase_report_key = StashKey[Dict[str, CollectReport]]()

ALLURE_RESULTS_PATH = fr'{ROOT_DIR}\allure-results'


@pytest.fixture(scope='function')
def driver(request, browser_type, selenoid_options, remote_url):
    browser = browser_type
    driver = WebBrowser(browser, remote_url, selenoid_options)
    yield driver
    driver.quit_driver()


@pytest.fixture
def reporter():
    return AllureReporter()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    rep = yield
    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep
    return rep


# @pytest.fixture(autouse=True)
# def test_details(driver) -> dict:
#     """
#     retrieve current driver information
#     """
#     return {
#         'name': driver.name.capitalize(),
#         'version': driver.capabilities['browserVersion'],
#         'platform': driver.capabilities['platformName'].capitalize()
#     }
#
#
# @pytest.fixture(autouse=True)
# def write_test_details(test_details: dict) -> None:
#     """
#     Get current driver information and writes it to environment properties file in the allure-results path
#     """
#     info = f'\nBrowser={test_details["name"]}\nVersion={test_details["version"]}\nPlatform={test_details["platform"]}'
#     env_properties_path = fr'{ALLURE_RESULTS_PATH}\environment.properties'
#     logger.info(f"path is {env_properties_path}")
#     with open(env_properties_path, 'w') as f:
#         f.write(info)
#     logger.info(f"writing current driver details")


@pytest.fixture(autouse=True, scope="function")
def screenshot_on_failure(request, driver, reporter):
    yield  # Allow the test to run
    report = request.node.stash[phase_report_key]
    if report.get("call").failed or report.get("setup").failed:
        screenshot = driver.get_screenshot_as_png()
        logger.info("Test failed: attaching screenshot.")
        reporter.attach_img(screenshot=screenshot)


@pytest.fixture(scope="function")
def swag_ui(driver, app_config):
    return SwagLabs(driver, app_config.app_url)


@pytest.fixture(scope="function")
def healenium_ui(driver, app_config):
    return HealeniumDemo(driver, app_config.app_url)


def pytest_addoption(parser):
    parser.addoption("--browser_type", action="store", help="browser for the automation tests", default="chrome")
    parser.addoption("--user", action="store", help="user for swag labs", default="standard")
    parser.addoption("--app", action="store", help="Application under test", default="swag_labs")
    parser.addoption("--is_local", action="store", help="run locally or remotely, accept true/false", default=False)
    parser.addoption("--allurdir", action="store", help="allure results directory", default="allure-results")
    parser.addoption("--remote_mode", action="store", help="healenium OR selenoid",
                     default=RemoteMode.HEALENIUM)


@pytest.fixture(scope="session")
def user(request):
    return request.config.getoption("--user")


@pytest.fixture(scope='session')
def browser_type(request):
    return request.config.getoption("--browser_type")


@pytest.fixture(scope='session')
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope='session')
def is_local(request):
    return request.config.getoption('--is_local')


@pytest.fixture(scope='session')
def remote_mode(request):
    return request.config.getoption('--remote_mode')


@pytest.fixture(scope='session')
def selenoid_options(app_config):
    return getattr(app_config, "selenoid_options", None)


@pytest.fixture(scope="session")
def remote_url(app_config, request):
    if request.config.getoption("--is_local"):
        return None
    return getattr(app_config, "remote_url", None)


@pytest.fixture(scope='session')
def app_config(is_local, app, browser_type, remote_mode):
    cfg = Config(is_local=is_local,
                 app=app,
                 browser_type=browser_type,
                 remote_mode=remote_mode
                 )
    return cfg


def pytest_collection_modifyitems(items):
    test_info = {
        item.nodeid.split("::")[1]: item.function.__doc__
        for item in items
    }
    logger.info('Test information including params:\n{}'.format(json.dumps(test_info, indent=2)))
