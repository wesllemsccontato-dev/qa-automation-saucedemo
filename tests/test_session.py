from pages.login_page import LoginPage
from data.test_data import USERNAME, PASSWORD



# CT-115 - Atualizar página logado
def test_CT115_atualizar_pagina_logado(driver): 


    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
    )
    driver.refresh()

    assert "inventory.html" in driver.current_url