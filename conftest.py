import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

@pytest.fixture
# Configuração do navegador  Chrome.
def driver():

    options = Options()
    
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()
    
    
# Configuração Prints dos erros.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome= yield
    
    report = outcome.get_result()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if report.when == "call" and report.failed:
        
        driver = item.funcargs.get("driver")
        
        if driver:
            
            os.makedirs( "screenshots", exist_ok= True)
            
            screenshot_file = ( f"screenshots/{item.name}_{timestamp}.png")
        
            driver.save_screenshot(screenshot_file)
            
            print( f"\nScreenshot salva: {screenshot_file}")
    