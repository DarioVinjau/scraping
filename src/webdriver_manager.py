import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_driver():
    #absolute_path = os.path.dirname(__file__)
    #abs_replaced = absolute_path.replace("\\","/")
    #relative_path = "/controller/chromedriver.exe"
    #full_path = abs_replaced+relative_path
    path = "src/controller/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    #service = Service(executable_path=relative_path) #"C:/Users/dvinjau/Downloads/chromedriver.exe"
    #service = Service(executable_path="C:/Users/dvinjau/Downloads/chromedriver.exe")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
