import unittest
import json
import os
import time
from datetime import datetime
#import matplotlib.pyplot as plt
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.pc_page import PcPage
from webdriver_manager import get_chrome_driver


percorso_file = "src/json_file/dati.json"
data_odierna = datetime.now()
data = data_odierna.strftime("%Y-%m-%d")#anno - mese - giorno

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = get_chrome_driver()
        self.home_page = HomePage(self.driver)
        self.base_page = BasePage(self.driver)
        self.pc_page = PcPage(self.driver)
        self.pc_page = PcPage(self.driver)

    def test_pc_romagna(self):
        try:
            self.driver.get('https://amazon.it')
            self.home_page.wait_for_home_page(self.home_page.amazon_logo)
            #eredito dalla basepage un metodo che aspetta 5sec finché non trova il logo di amazon
            
            
            self.home_page.click_element(self.home_page.accept_cookie)
            self.home_page.set_text(self.home_page.search_field,self.base_page.item_searched)
            self.home_page.click_element(self.home_page.search_button)
            time.sleep(2)
            self.home_page.click_element(self.pc_page.marche_button)
            self.home_page.click_element(self.pc_page.marche_button)
            item = self.base_page.item_code
            descrizione = self.home_page.get_text(self.pc_page.data_asin)
            prezzo = self.home_page.get_text(self.pc_page.value)
            time.sleep(5)
            
            if os.path.exists(percorso_file) and os.path.getsize(percorso_file) > 0:
                with open(percorso_file, "r") as f:
                    contenuto = json.load(f)
            else:
                contenuto = {}

            if item in contenuto:
                contenuto[item]['descrizione'] = descrizione
                if 'storico' in contenuto[item]:
                    contenuto[item]['storico'][data] = prezzo
                else:
                    contenuto[item]['storico'] = {data: prezzo}
            else:
                contenuto[item] = {'descrizione': descrizione,'storico': {data: prezzo}}

            with open(percorso_file, "w") as f:
                json.dump(contenuto, f, indent=4)
            
            #self.home_page.set_search_field(item_searched) metodo alternativo per scrivere sulla barra di ricerca
            #self.home_page.click_search_button() idem sotto per un'altra cosa
        except Exception as e:
                print(e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
