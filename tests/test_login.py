from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import USERNAME, PASSWORD, INVALID_USERNAME, INVALID_PASSWORD, PAYLOADS1, PAYLOADS2, PAYLOADS3, PAY_PASSWORD, NONEX_USER
import time
from selenium.webdriver.common.keys import Keys
from utils.ferramentas import Cronometro


# CT-001 - Login Valido.
def test_CT001_login_valido(driver): 


    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
    )

    assert "inventory.html" in driver.current_url
    
# CT-002 - Senha inválida
def test_CT002_senha_invalida(driver):
    
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
    assert driver.current_url == "https://www.saucedemo.com/"
    
# CT-003 - Usúario Invalido.
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
    assert driver.current_url == "https://www.saucedemo.com/"
    
# CT-004 - Usuario_Inexistente
def test_CT004_usuario_inexistente(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        NONEX_USER,
        PASSWORD
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Password is required"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-005 - Espaços antes do Usuário.
def test_CT005_espaco_antes_usuario(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        "   " + USERNAME,
        PASSWORD
    )
    
    assert driver.current_url == LoginPage.URL
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-006 - Espaços depois do Usuário.
def test_CT006_espaco_depois_usuario(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME + "   ",
        PASSWORD
    )
    
    assert driver.current_url == LoginPage.URL
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )

# CT-007 - Letras maiúsculas no Usuário.
def test_CT007_maiuscula_usuario(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        
        USERNAME.upper(),
        PASSWORD
    )
    
    assert driver.current_url == LoginPage.URL
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-008 - Campo senha mascarado.
def test_CT008_campo_senha_mascarado(driver):
    
    page = LoginPage(driver)

    page.open()


    
    assert page.get_password_type()== "password"
    
# CT-009 - Limite mínimo da senha.
def test_CT007_limete_minimo_senha(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        
        USERNAME,
        "123"
    )
    
    assert driver.current_url == LoginPage.URL
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    
# CT-010 - Limite máximo da senha.
def test_CT010_limete_maximo_senha(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        
        USERNAME,
        "A" * 500
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-011 - Caracteres especiais no login.
def test_CT011_caracters_especias(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        
        "@@@@",
        PASSWORD
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL

# CT-013 - Campos Obrigatorios Vazios.
def test_CT013_campos_obrigatorios_vazios(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.click_login()
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username is required"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-014 - Apenas números no Usuario.
def test_CT014_numer_usuario(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        "123456789",
        PASSWORD
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username is required"
    )
    assert driver.current_url == LoginPage.URL

# CT-015 - Apenas letras na senha.
def test_CT015_letras_senha(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        USERNAME,
        "secretsauce"
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-016 - Emojis nos campos.
def test_CT016_emojis_campos(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        "😀",
        "😀"
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL

# CT-017 - Caracteres acentuados.
def test_CT017_caracteres_acentuados(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        "stándard_user",
        "standard_usêr"
    )
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL

# CT-018 - Sensibilidade Senha.
def test_CT018_sensibilidade_senha(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        USERNAME,
        "SECRET_sauce"
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL

# CT-019 - Persistência após erro.
def test_CT019_percistencia_erro(driver):
    
    page = LoginPage(driver)
    
    page.open()
    
    page.login(
        USERNAME,
        "SECRET_sauce"
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-020 - Exibição da mensagem de erro.
def test_CT020_exibicao(driver):
    
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
    
    mensagem = driver.find_element(*page.ERROR_MESSAGE)
    
    assert mensagem.is_displayed()
    
    assert mensagem.tag_name == "h3"
    
    assert "error" in mensagem.get_attribute("data-test")
    
    assert driver.current_url == LoginPage.URL
    
# CT021 - Remoção da mensagem após nova tentativa
def test_CT021_Remoção_mensagem_após_nova_tentativa(driver):
    
    page = LoginPage(driver)
    
    
    page.open()
    
    page.login(
        USERNAME,
        INVALID_PASSWORD
    )
    assert page.error_messege_exists()
    
    
    page.apagar()
    
    

    page.login(
            USERNAME,
            PASSWORD
        )

    assert "inventory.html" in driver.current_url

# CT-023 - Senha em Branco.
def test_CT023_senha_branco(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        ""
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Password is required"
    )
    assert driver.current_url == LoginPage.URL

# CT-024 - Campo e-mail Vazio.
def test_CT024_usuario_branco(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login(
        "",
        PASSWORD
    )
    
    assert (
        page.get_error_message()
        == "Epic sadface: Username is required"
    )
    assert driver.current_url == LoginPage.URL
    
# CT-056 - Login pressionando ENTER
def  test_CT056_login_enter(driver):
    
    page = LoginPage(driver)

    page.open()

    page.login_enter(
        USERNAME,
        PASSWORD
    )

    assert "inventory.html" in driver.current_url
# CT-052 - URL após login
def test_CT052_url_apos_login(driver): 
    
    page = LoginPage(driver)

    page.open()

    page.login(
        USERNAME,
        PASSWORD
    )

    assert "inventory.html" in driver.current_url

# CT-061 - Foco automático no primeiro campo
def test_CT061_Foco_automático(driver): 

    page = LoginPage(driver)

    page.open()

    active_element = driver.switch_to.active_element

    
    username = driver.find_element(*LoginPage.USERNAME)
    

    assert(
        active_element == username
    )
    
# CT-062 - Ordem correta de navegação
def test_CT062_ordem_correta_navegacao(driver):

    page = LoginPage(driver)

    page.open()

    active_element = driver.switch_to.active_element

    active_element.send_keys(Keys.TAB)

    active_element = driver.switch_to.active_element
    
    assert active_element.get_attribute("id") == "user-name"
    

    active_element.send_keys(Keys.TAB)
    
    active_element = driver.switch_to.active_element
    
    assert active_element.get_attribute("id") == "password"
    
    
    active_element.send_keys(Keys.TAB)
    
    active_element = driver.switch_to.active_element
    
    assert active_element.get_attribute("id") == "login-button"
    
# CT-076 - Tempo de resposta do login.
def test_CT076_tempo_resposta(driver): 


    page = LoginPage(driver)

    page.open()
    
    
    page.login(
        USERNAME,
        PASSWORD
    )
    inicio = time.perf_counter()
    page.wait_for_inventory
    
    fim = time.perf_counter()
    
    tempo = inicio - fim
    
    print("Inicio: ", inicio)
    print("Fim: ",fim)
    print("Tempo: ",tempo)
    
    assert tempo <=3

# CT-077 - Múltiplas tentativas consecutivas.
def test_CT077_multiplas_tentativas(driver): 

    cronometro = Cronometro()
    page = LoginPage(driver)
    page.open()
    totaltempo = 0
    for tentativas in range(10):
        
        cronometro.iniciar()
        page.login(
            USERNAME,
            INVALID_PASSWORD
        )
        
        page.wait_messege_error()
    
        
        tempo = cronometro.parar()   
        
        print("Tempo: ",tempo)
        
        assert (
        page.get_error_message()
        == "Epic sadface: Username and password do not match any user in this service"
        )
        assert tempo <=3
        
        totaltempo = totaltempo + tempo
        
        page.apagar()
        
    totaltempo = totaltempo/10
    assert totaltempo<=3