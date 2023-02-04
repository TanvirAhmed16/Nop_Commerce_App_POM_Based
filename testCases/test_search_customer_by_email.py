import time
import pytest
from pageObjects.LoginPage import LoginPage
# from pageObjects.AddNewCustomerPage import AddNewCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_04_Search_Customer_By_Email:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()  # For Generating Log.

    @pytest.mark.regression
    def test_Search_Customer_By_Email(self, launchBrowser):
        self.logger.info("*********** Test_04_Search_Customer_By_Email ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)

        '''Creating an object of LoginPage to use the LoginPage class methods'''
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info("*********** Login Successful ***********")

        self.logger.info("*********** Starting Search Customer By Email Test ***********")
        self.logger.info("*********** Searching Customer By Email ***********")

        '''Creating an object of SearchCustomerPage to use the SearchCustomer class methods'''
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.clickOnCustomersMainMenu()
        self.search_customer.clickOnCustomersSubMenu()
        self.search_customer.setEmail("admin@yourStore.com")
        self.search_customer.clickOnSearch()
        time.sleep(3)

        status = self.search_customer.searchCustomerByEmail("admin@yourStore.com")
        assert True == status

        self.driver.close()
        self.logger.info("*********** Ending Search Customer By Email Test ***********")
