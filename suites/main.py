from framework.myTestCase import AppTesting
import unittest
from selenium import webdriver

class ScraperTest(AppTesting):
    def test_scraping_data(self):
        print("test")
        #search_input = self.driver.find_element("")
        #search_input.send_keys("Scrivi qualcosa per favore")


if __name__ == "__main__":
    unittest.main()
