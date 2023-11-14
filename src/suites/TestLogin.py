import sys
import os
sys.path.insert(0, os.getcwd())
from src.framework.myTestCase import AppTesting
from src.pages.PageAmazonHome import AmazonPage
import unittest




class ScraperTest(AppTesting):
    def test_scraping_data(self):
        amazon_page = AmazonPage(self.driver)
        amazon_page.search_product("Benedetto")       
        #page = PageAmazonHome()
        #example = defineElements()
        #example.element(self,page)
if __name__ == "__main__":
            unittest.main()