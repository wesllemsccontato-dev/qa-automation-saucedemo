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

# CT-046 - URL direta após logout
def test_CT046_URL_direta_apos_logout(driver):
        
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
