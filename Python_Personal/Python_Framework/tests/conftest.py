import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    url = "https://rahulshettyacademy.com/angularpractice/"
    service_obj = Service(os.getcwd() + '\drivers\chromedriver.exe')
    browser = webdriver.Chrome(service=service_obj, options=chrome_options)
    browser.get(url)
    request.cls.browser = browser
    yield
    browser.close()
