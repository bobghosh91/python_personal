import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

url = "https://rahulshettyacademy.com/angularpractice/"
service_obj = Service(os.getcwd()+'\drivers\chromedriver.exe')
browser = webdriver.Chrome(service = service_obj, options=chrome_options)
browser.implicitly_wait(5)

browser.get(url)
browser.find_element(By.XPATH, "//*[contains(@href, 'shop')]").click()

wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//app-card-list/app-card")))

products = browser.find_elements(By.XPATH, "//app-card")
print(len(products))
for product in products:
    productName = product.find_element(By.XPATH, "div/div/h4").text
    print(productName)
    if productName == 'Blackberry':
        product.find_element(By.XPATH, "div/div/button").click()

browser.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
browser.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

browser.find_element(By.ID,"country").send_keys("ind")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@class='suggestions']")))
browser.find_element(By.LINK_TEXT,"India").click()

browser.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = browser.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText
browser.close()
