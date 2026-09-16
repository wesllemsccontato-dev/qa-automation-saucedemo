from pages.inventory_page import InventoryPage
from data.test_data import USERNAME, PASSWORD
from pages.login_page import LoginPage


# CT-042 - Botão voltar após logout
def test_CT042_botao_voltar_apos_logout(driver):
        
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
        )
        
    inventory_page = InventoryPage(driver)
        
    inventory_page.open_menu()
        
    inventory_page.logout()
    
    driver.back()
    
    assert (
        page.get_error_message()
        == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
# CT-041 Logout correto
def test_CT041_logout_correto(driver):

    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
    )

    inventory_page = InventoryPage(driver)
    
    inventory_page.open_menu()
    
    inventory_page.logout()

    page.open_inventory()
    
    assert (
            page.get_error_message()
            == "Epic sadface: You can only access '/inventory.html' when you are logged in."
        )
    
# CT-046 - URL direta após logout
def test_CT046_url_direta_apos_logout(driver):
        
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
        )
        
    inventory_page = InventoryPage(driver)
        
    inventory_page.open_menu()
        
    inventory_page.logout()
    
    page.open_inventory()
    
    assert (
        page.get_error_message()
        == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
# CT-045 - Reutilização da sessão
def test_CT045_reutilização_sessao(driver):
        
    page = LoginPage(driver)

    page.open()

    print("\n=== ANTES DO LOGIN ===")
    print(driver.get_cookies())
    
    page.login(
        USERNAME,
        PASSWORD
    )
    
    cookies = driver.get_cookies()

    inventory_page = InventoryPage(driver)

    inventory_page.open_menu()

    inventory_page.logout()

    for cookie in cookies:
        driver.add_cookie(cookies[0])

    assert(
        page.get_error_message()
        == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
