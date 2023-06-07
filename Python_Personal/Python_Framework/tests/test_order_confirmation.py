import pytest
from selenium.webdriver.common.by import By
from Python_Framework.utilities.base_class import BaseClass


class TestOrderConfirm(BaseClass):

    def test_order_confirm(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//*[contains(@href, 'shop')]").click()