import pytest
from selenium import webdriver
from PageObjects.LoginPage import login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_login_DDT:
    URL = ReadConfig.getapplicationURL()
    path=r"C:\\Users\\Priyabrata Debolina\\PycharmProjects\\Selenium with python\\TestData\practice.xlsx"
    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_ddt(self,setup):
        self.logger.info("*****Test_002_login*****")
        self.logger.info("*****Verifying Login DDT test*****")
        self.driver=setup
        self.driver.get(self.URL)

        self.lp=login(self.driver)
        self.lp.clickLogin()
        self.rows=XLUtils.getRowcount(self.path,'Sheet1')

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd=XLUtils.readData(self.path,'Sheet1',r,2)
            self.driver.save_screenshot('C:\\Users\\Priyabrata Debolina\\PycharmProjects\\Selenium with python\\Screenshots\\test_DDT.png')


        self.lp.username(self.user)
        self.lp.password(self.pwd)











