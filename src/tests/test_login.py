import unittest
from pages.home_page import HomePage
from webdriver_manager import get_chrome_driver

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = get_chrome_driver()
        self.home_page = HomePage(self.driver)

    def test_black_friday(self):
        try:
            self.driver.get('https://amazon.it')
            self.home_page.wait_for_home_page(self.home_page.amazon_logo)
            #eredito dalla basepage un metodo che aspetta 5sec finché non trova il logo di amazon
            
            item_searched = 'pc fisso'
            self.home_page.set_click(self.home_page.accept_cookie)
            self.home_page.set_text(self.home_page.search_field,item_searched)
            self.home_page.set_click(self.home_page.search_button)
            self.home_page.set_click(self.home_page.marche_button)
            #self.home_page.set_search_field(item_searched) metodo alternativo per scrivere sulla barra di ricerca
            #self.home_page.click_search_button() idem sotto per un'altra cosa
        except Exception as e:
                print(e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
