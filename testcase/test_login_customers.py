import pytest
from selenium import webdriver
from PageObjects.LoginPage import login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_LoginCustomers:
    URLADMIN = ReadConfig.getapplicationURL1()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_LoginCustomers(self,setup):
        self.logger.info("*****Test_003_login*****")
        self.logger.info("*****LoginCustomers*****")
        self.driver=setup
        self.driver.get(self.URLADMIN)

        











