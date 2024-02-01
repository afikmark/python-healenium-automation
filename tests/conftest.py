import pytest
from framework.web_browser import WebBrowser
from framework.logger import get_logger
from settings import ROOT_DIR
from tests import Config
from web_pages.swag_labs.swag_labs import SwagLabs
import json
from typing import Dict
from framework.reporter import AllureReporter
from pytest import StashKey, CollectReport

logger = get_logger()
phase_report_key = StashKey[Dict[str, CollectReport]]()

ALLURE_RESULTS_PATH = fr'{ROOT_DIR}\allure-results'


# , 'firefox', 'edge'
@pytest.fixture(scope='function', params=['chrome'])
def driver(request):
    browser = request.param
    driver = WebBrowser(browser)
    yield driver
    driver.quit_driver()


@pytest.fixture
def reporter():
    return AllureReporter()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep


@pytest.fixture(autouse=True)
def test_details(driver) -> dict:
    """
    retrieve current driver information
    """
    return {
        'name': driver.name.capitalize(),
        'version': driver.capabilities['browserVersion'],
        'platform': driver.capabilities['platformName'].capitalize()
    }


@pytest.fixture(autouse=True)
def write_test_details(test_details: dict) -> None:
    """
    Get current driver information and writes it to environment properties file in the allure-results path
    """
    info = f'\nBrowser={test_details["name"]}\nVersion={test_details["version"]}\nPlatform={test_details["platform"]}'
    env_properties_path = fr'{ALLURE_RESULTS_PATH}\environment.properties'
    logger.info(f"path is {env_properties_path}")
    with open(env_properties_path, 'w') as f:
        f.write(info)
    logger.info(f"writing current driver details")


@pytest.fixture(autouse=True, scope="function")
def screenshot_on_failure(request, driver, reporter):
    yield  # Allow the test to run
    report = request.node.stash[phase_report_key]
    if report.get("call").failed or report.get("setup").failed:
        screenshot = driver.get_screenshot_as_png()
        reporter.attach_img(screenshot=screenshot)


@pytest.fixture(scope="function")
@pytest.mark.parametrize("driver", ['chrome'], indirect=True)
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

    parser.addoption("--allurdir",
                     action="store",
                     help="allure results directory",
                     default="allure-results")


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
