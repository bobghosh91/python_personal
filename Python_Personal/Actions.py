from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
s = Service('C:/Users/Bob.ghosh/Desktop/Bob/Python/drivers/chromedriver.exe')
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
browser.implicitly_wait(10)
url ='https://rahulshettyacademy.com/AutomationPractice/'
browser.get(url)

action = ActionChains(browser)
action.move_to_element(browser.find_element(By.ID, "mousehover")).click().perform()
action.move_to_element(browser.find_element(By.ID, "mousehover")).perform()