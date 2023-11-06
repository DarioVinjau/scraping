import unittest
import time
from selenium import webdriver

class AppTesting(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.it/")
        print("setup eseguito")
        
    def tearDown(self):
        while True:
            time.sleep(1)