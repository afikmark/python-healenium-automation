from web_pages.login import LoginPage


def login(login_page: LoginPage, email, password):
    login_page.login(email, password)
    login_page.dialog.close_share_window()
    login_page.dialog.close_dialog()
