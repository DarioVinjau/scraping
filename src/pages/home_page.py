from selenium.webdriver.common.by import By
from base_page import BasePage
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)#eredito il driver da basepage
        self.amazon_logo = (By.ID,'nav-logo-sprites')
        self.accept_cookie = (By.ID,'sp-cc-accept')
        self.search_field = (By.ID,"twotabsearchtextbox")
        self.search_button = (By.ID, 'nav-search-submit-button')

"""   def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
"""