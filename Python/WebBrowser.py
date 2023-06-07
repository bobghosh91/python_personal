import webbrowser, time
from selenium import webdriver
from selenium.webdriver.common.by import By
#import chromedriver_binary
#webbrowser.open("https:///www.google.com")

browser = webdriver.Chrome(executable_path=r"C:\Users\bisha\Desktop\Bob\Selenium\chromedriver.exe")
browser.get('https:google.com')
browser.maximize_window()
time.sleep(5)
element = browser.find_element(By.XPATH, '//*[@name="q"]')
time.sleep(5)

element.send_keys('bob')
element.submit()

time.sleep(5)