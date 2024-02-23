from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PcPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)#eredito il driver da basepage
        self.marche_button = (By.XPATH,"//span[contains(@data-csa-c-content-id,'ROMAGNA COMPUTER')]")
        self.data_asin = (By.XPATH,"(//div[@data-asin='B0BBWFCGFH']//h2)[1]")
        self.value = (By.XPATH,"(//div[@data-asin='B0BBWFCGFH']//span[@class='a-price']//span[@class='a-price-whole'])[1]") 

