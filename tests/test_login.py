from selenium import webdriver
from pages.login_page import LoginPage
from data.test_data import USERNAME, PASSWORD, INVALID_USERNAME, INVALID_PASSWORD, PAYLOADS1, PAYLOADS2, PAYLOADS3, PAY_PASSWORD

from selenium.webdriver.common.keys import Keys



# CT-001 - Login Valido
def test_CT001_login_valido(driver): 


    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
    )

    assert "inventory.html" in driver.current_url
    
# CT-002 - Login Invalido
def test_CT002_login_invalido(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        INVALID_PASSWORD
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-003 - Usuario Invalido
def test_CT003_usuario_invalido(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        INVALID_USERNAME,
        PASSWORD
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-013 - Campos Obrigatorios Vazios
def test_CT013_campos_obrigatorios_vazios(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.click_login()
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username is required"
    )
    
# CT-018 - Sensibilidade Senha
def test_CT018_sensibilidade_senha(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        USERNAME,
        "SECRET_SAUCE"
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-056 - Login pressionando ENTER
def  test_CT056_login_enter(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login_enter(
        USERNAME,
        PASSWORD
    )

    assert "inventory.html" in driver.current_url


