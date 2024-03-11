from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class BasePage:
   
    item_searched = 'pc fisso'
    item_code = 'B0BBWFCGFH'
    
    def __init__(self, driver):
        self.driver = driver
    
    #metodo per scrivere all'interno di un campo
    def set_text(self, xpath, text):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(xpath)).send_keys(text)
    
    def click_element(self, xpath):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(xpath)).click()
    
    def wait_for_home_page(self,xpath):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(xpath)
        )
             
    def get_text(self,xpath):   
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((xpath)))
        return element.text