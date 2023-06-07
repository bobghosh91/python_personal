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
url ='https://the-internet.herokuapp.com/windows'
browser.get(url)
browser.find_element(By.LINK_TEXT, "Click Here").click()

openWindows = browser.window_handles
print(openWindows)
browser.switch_to.window(openWindows[1])
print(browser.find_element(By.TAG_NAME, "h3").text)
browser.close()
browser.switch_to.window(openWindows[0])

assert "Opening a new window" in browser.find_element(By.TAG_NAME, "h3").text

########################### Frames ############################################

browser.get('https://the-internet.herokuapp.com/iframe')

browser.switch_to.frame("mce_0_ifr")
browser.find_element(By.ID, "tinymce").clear()
browser.find_element(By.ID, "tinymce").send_keys("abe saale")

browser.switch_to.default_content()