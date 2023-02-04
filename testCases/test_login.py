import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_01_Login:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Homepage_Title(self, launchBrowser):
        self.logger.info("*********** Test_01_Login ***********")
        self.logger.info("*********** Verifying Homepage Title ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)
        act_page_title = self.driver.title

        if act_page_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Homepage Title Test Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Homepage_Title.png")
            self.driver.close()
            self.logger.error("*********** Homepage Title Test Failed ***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, launchBrowser):
        self.logger.info("*********** Verifying Login Test ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)

        '''Creating an object of LoginPage to use the LoginPage class methods'''
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        act_page_title = self.driver.title

        if act_page_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** Login Test Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("*********** Login Test Failed ***********")
            assert False