import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AppTesting(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.it/")
        self.driver.find_element(By.ID,"sp-cc-accept").click()
        print("setup eseguito")
        
    def tearDown(self):
        while True:
            time.sleep(1)