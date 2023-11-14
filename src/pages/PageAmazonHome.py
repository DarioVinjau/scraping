from selenium.webdriver.common.by import By

searchBarAmazon = (By.ID,"twotabsearchtextbox")

class AmazonPage:

    def __init__(self,driver):
        self.driver = driver
    
    def search_product(self,product_name):
        search_input = self.driver.find_element(searchBarAmazon)
        search_input.send_keys(product_name)
        search_input.submit()



#searchBarAmazon = driver.find_element(By.ID,"twotabsearchtextbox")