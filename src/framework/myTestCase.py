import unittest
import time
from re import search
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

    
class defineElements():
    def element(self, xpath):
        if search("button", xpath):
            print("button")
        elif search("input",xpath):
            print("input")
        elif search("label",xpath):
            print("label")
        else: print("altro caso")
        pass
    
