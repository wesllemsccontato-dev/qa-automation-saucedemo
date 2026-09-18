from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class LoginPage:

    URL = "https://www.saucedemo.com/"
    URL_INV = "https://www.saucedemo.com/inventory.html"
    
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        
    
        
    def wait_element(self, locator):

        return WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_inventory(self):
        WebDriverWait(self.driver, 10).until(
        EC.url_contains(self.URL)
    )
        
    def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    def wait_messege_error(self):
            WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(*self.ERROR_MESSAGE)
        )
        

    def open(self):
        self.driver.get(self.URL)

    def open_inventory(self):
        self.driver.get(self.URL_INV)
        
    def click_login(self):
        self.wait_element(self.LOGIN_BUTTON).click()
        
    def login(self, username, password):
        self.wait_element(self.USERNAME).send_keys(username)
        self.wait_element(self.PASSWORD).send_keys(password)
        self.wait_element(self.LOGIN_BUTTON).click()
        
    def login_enter(self, username, password):
        self.wait_element(self.USERNAME).send_keys(username)
        self.wait_element(self.PASSWORD).send_keys(password)
        self.wait_element(self.LOGIN_BUTTON).send_keys(Keys.ENTER)

    def apagar(self):
        self.wait_element(self.USERNAME).send_keys(Keys.CONTROL,"a")
        self.wait_element(self.USERNAME).send_keys(Keys.CONTROL,"x")
        
        self.wait_element(self.PASSWORD).send_keys(Keys.CONTROL,"a")
        self.wait_element(self.PASSWORD).send_keys(Keys.BACKSPACE)
    
    def get_element(self):
        return self.find_element("type","password")
    
    def get_error_message(self):
        return self.wait_element(self.ERROR_MESSAGE).text
    
    def get_password_type(self):
        return self.driver.find_element(*self.PASSWORD).get_attribute("type")
    
    def error_messege_exists(self):
        return len(
            self.driver.find_elements(*self.ERROR_MESSAGE)
            
        ) > 0
    def tecla_tab(self):
        self.send_keys(Keys.TAB)
            