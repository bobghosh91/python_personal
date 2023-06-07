import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s = Service('C:/Users/Bob.ghosh/Desktop/Bob/Python/drivers/msedgedriver.exe')
browser = webdriver.Edge(service=s)
url='https://rahulshettyacademy.com/dropdownsPractise/'
browser.get(url)

browser.find_element(By.ID, "autosuggest").clear()
browser.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)

countries = browser.find_elements(By.XPATH, "//li[@role='presentation']")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        
        break

assert browser.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
browser.implicitly_wait(5)

wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//promo")))
