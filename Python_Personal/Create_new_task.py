import base64
import os
import random
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

#url = "http://uka-bdmsuat8:34826/dm/enterprise/index.html#/home"
url = "http://uka-bdmsuat8:34826/dm/login.jsp"
service_obj = Service(os.getcwd()+'\drivers\chromedriver.exe')
browser = webdriver.Chrome(service = service_obj, options=chrome_options)
browser.implicitly_wait(5)
browser.delete_all_cookies()

#--------------------------------Login procedure----------------------------------
encryptedPass = str(base64.b64encode("Decision1".encode("utf-8")), "utf-8")
browser.get(url)

browser.find_element(By.XPATH, "//*[@name='username']").send_keys("automation1")
browser.find_element(By.XPATH, "//*[@name='password']").send_keys(str(base64.b64decode(encryptedPass),"utf-8"))
#browser.find_element(By.XPATH, "//*[@name='password']").send_keys("Decision1")
time.sleep(1)
browser.find_element(By.XPATH, "//*[@type='submit']").click()

#---------------------------------page loading wait----------------------------------
wait = WebDriverWait(browser, 30)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//dcn-create-asset-button")))
wait.until(lambda x: x.execute_script("return document.readyState === 'complete'"))

#-------------------creating task-------------------------
print('hello')
browser.find_element(By.XPATH, "//dcn-create-asset-button//*[contains(@class, 'splitbutton-menubutton')]").click()
browser.find_element(By.XPATH, "//*[text() = 'Start a New Task']/..").click()

#->community--
try:
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//dcn-autocomplete//button")))
    browser.find_element(By.XPATH, "//dcn-autocomplete//button").click()
    AllCommunity = browser.find_elements(By.XPATH,"//ul/li//dcn-autocomplete-default-template")
    for community in AllCommunity:
        CommName = community.text
        print(CommName)
        if CommName == 'Automation_Assets':
            community.click()
            break
except StaleElementReferenceException:
    AllCommunity = browser.find_elements(By.XPATH, "//ul/li//dcn-autocomplete-default-template")

#->TaskName--
number = random.randint(100000,999999)
print(number)
browser.find_element(By.XPATH, "//*[@name='taskName']").send_keys("NewTask"+str(number))
browser.find_element(By.XPATH, "//*[@name='description']").send_keys("decription of: NewTask"+str(number))

#->Modeling Project name
try:
    browser.find_element(By.XPATH, "//*[@name='project']//button").click()
    AllModelingPRj = browser.find_elements(By.XPATH,"//*[@role='option']")
    for modelingPrj in AllModelingPRj:
        MP_Name = modelingPrj.text
        print(MP_Name)
        if MP_Name == "Gil's Demo":
            modelingPrj.click()
            time.sleep(2)
            break

except StaleElementReferenceException:
    AllModelingPRj = browser.find_elements(By.XPATH,"//*[@role='option']")

#->Asset Approval name
try:
    browser.find_element(By.XPATH, "//*[@name='approvalProcess']//button").click()
    AllAsset = browser.find_elements(By.XPATH,"//*[@role='option']")
    for asset in AllAsset:
        asset_Name = asset.text
        print(asset_Name)
        if asset_Name == "TSK _ WF":
            asset.click()
            break

except StaleElementReferenceException:
    AllAsset = browser.find_elements(By.XPATH,"//*[@role='option']")

#->Facttype Approval name
try:
    browser.find_element(By.XPATH, "//*[@name='ftApprovalProcess']//button").click()
    AllFact = browser.find_elements(By.XPATH,"//*[@role='option']")
    for fact in AllFact:
        ft_Name = fact.text
        print(ft_Name)
        if ft_Name == "FT _ WF":
            fact.click()
            break

except StaleElementReferenceException:
    AllAsset = browser.find_elements(By.XPATH,"//*[@role='option']")

print('ok')

