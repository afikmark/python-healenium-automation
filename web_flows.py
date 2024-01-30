from web_pages.swag_labs.login import LoginPage


def login(login_page: LoginPage, email, password):
    login_page.open()
    login_page.login(email, password)
