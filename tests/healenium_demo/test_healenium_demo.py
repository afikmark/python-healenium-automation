def test_login_healenium(healenium_ui):
    healenium_ui.open()
    login_page = healenium_ui.login_page
    login_page.login_healenium('afik', 'afik@gmail.com', '1234')
    login_page.email.enter_text("afikmark@gmail.com")
    print('')
