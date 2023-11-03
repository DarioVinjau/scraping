from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.it/")

driver.quit()