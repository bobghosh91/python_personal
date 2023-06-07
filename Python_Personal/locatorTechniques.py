import base64
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#diferent locators: Id, xpath, CSS, classname, name, linkText
#s = Service('/drivers/chromedriver.exe')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
s = Service('C:/Users/Bob.ghosh/Desktop/Bob/Python/drivers/chromedriver.exe')
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
url ='https://rahulshettyacademy.com/angularpractice/'
browser.get(url)


browser.find_element(By.NAME, "email").send_keys("helllo@gmail.com")
browser.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
browser.find_element(By.XPATH, "//input[@type='submit']").click()
message = browser.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message
#css -> tagname[atrribute='value']
print('bb')

print(base64.encode("bob"))