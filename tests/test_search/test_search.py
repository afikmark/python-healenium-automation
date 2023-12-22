from pytest import mark
from web_pages.search import SearchPage
from web_pages.login import LoginPage


# @mark.ui
# def test_search(driver, app_config):
#     login_page = LoginPage(driver, app_config.base_url)
#     search_page = SearchPage(driver, app_config.base_url)
#     login_page.open()
#     login_page.login('standard_user', 'secret_sauce')
#     search_page.search('חלב')
#     assert True
