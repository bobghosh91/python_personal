import pytest
from Pytest_Tutorial.test_logging import BaseLog


# @pytest.mark.smoke
# def test_CreditCardCheck():
#     print('credit card available')
@pytest.mark.usefixtures("dataLoad")
class TestExam2(BaseLog):
    def test_exm2(self, dataLoad):
        log = self.Log()
        log.info("hey")
        log.info(dataLoad[1])
