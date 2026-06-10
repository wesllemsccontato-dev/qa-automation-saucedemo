from selenium import webdriver
from pages.login_page import LoginPage


def test_login_valido(driver):

    page = LoginPage(driver)

    page.open()

    page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory.html" in driver.current_url
    
def test_campos_obrigatorios_vazios(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.click_login()
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username is required"
    )