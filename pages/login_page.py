from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:

    URL = "https://www.saucedemo.com/"
    
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get(self.URL)

    def open_inventory(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
    def login_enter(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).send_keys(Keys.ENTER)

    def login_XSS(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
