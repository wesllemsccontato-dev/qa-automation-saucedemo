from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    
    MENU_BUTTON =(By.ID,"react-burger-menu-btn")
    
    LOGOUT_LINK = (By.ID,"logout_sidebar_link")
    
    def __init__ (self, driver):
        self.driver = driver
    
    def open_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()

        
    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()