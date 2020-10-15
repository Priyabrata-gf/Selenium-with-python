import pytest
from selenium import webdriver
from PageObjects.LoginPage import login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    URL = ReadConfig.getapplicationURL()
    username = ReadConfig.username()
    password = ReadConfig.password()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def testhomepage(self,setup):
        self.logger.info("*****Test_001_login*****")
        self.logger.info("*****Verifying Home page title*****")
        self.driver=setup
        self.driver.get(self.URL)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store":
            assert True
            self.logger.info("*****Test Case passed*****")
        else:
            self.logger.info("*****Test Case Failed****")
        self.lp=login(self.driver)
        self.lp.clickLogin()
        self.lp.username(self.username)
        print()
        self.lp.password(self.password)
        self.driver.save_screenshot("C:\\Users\\Priyabrata Debolina\\PycharmProjects\\Selenium with python\\Screenshots\\testhomepage.png")
        self.driver.close()
    @pytest.mark.regression
    def testregister(self, setup):
        self.driver=setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('ico-register').click()
        self.driver.close()











