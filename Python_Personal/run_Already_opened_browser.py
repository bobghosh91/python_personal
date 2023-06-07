from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detach", True)
chrome_options.debugger_address = "localhost:9867"  # Replace with the remote debugging port you enabled earlier
s = Service('C:/Users/Bob.ghosh/Desktop/Bob/Python/drivers/chromedriver.exe')
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
browser.implicitly_wait(10)
url ='https://rahulshettyacademy.com/AutomationPractice/'
#browser.get(url)
print(browser.find_element(By.XPATH, "//*[@class='blinkingText']").text)