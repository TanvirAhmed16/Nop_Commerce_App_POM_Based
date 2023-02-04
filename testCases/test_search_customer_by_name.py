import time
import pytest
from pageObjects.LoginPage import LoginPage
# from pageObjects.AddNewCustomerPage import AddNewCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_05_Search_Customer_By_Name:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()  # For Generating Log.

    @pytest.mark.regression
    def test_Search_Customer_By_Name(self, launchBrowser):
        self.logger.info("*********** Test_05_Search_Customer_By_Name ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)

        '''Creating an object of LoginPage to use the LoginPage class methods'''
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info("*********** Login Successful ***********")

        self.logger.info("*********** Starting Search Customer By Name Test ***********")
        self.logger.info("*********** Searching Customer By Name ***********")

        '''Creating an object of SearchCustomerPage to use the SearchCustomer class methods'''
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.clickOnCustomersMainMenu()
        self.search_customer.clickOnCustomersSubMenu()

        self.search_customer.setFirstName("John")
        self.search_customer.setLastName("Smith")
        self.search_customer.clickOnSearch()
        time.sleep(3)

        status = self.search_customer.searchCustomerByName("Johnn Smith")
        assert True == status

        self.driver.close()
        self.logger.info("*********** Ending Search Customer By Name Test ***********")
