from pytest import fixture
from framework.web_browser import WebBrowser
from tests import Config


@fixture(scope='session')
def driver(browser):
    driver = WebBrowser(browser)
    yield driver
    driver.quit_driver()


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


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@fixture(scope='session')
def app_config(env, browser):
    cfg = Config(env)
    return cfg
