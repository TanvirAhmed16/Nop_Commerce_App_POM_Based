import random
import string
import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

''' Creating a random email generator function to generate unique email every time the test is executed. Otherwise
same hard coded value will resulting failure of test case.'''

def random_email_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_03_Add_Customer:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()  # For Generating Log.

    @pytest.mark.sanity
    def test_Add_Customer(self, launchBrowser):
        self.logger.info("*********** Test_03_Add_New_Customer ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)

        '''Creating an object of LoginPage to use the LoginPage class methods'''
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info("*********** Login Successful ***********")

        self.logger.info("*********** Starting Add Customer Test ***********")

        '''Creating an object of AddNewCustomerPage to use the AddNewCustomer class methods'''
        self.add_customer = AddNewCustomer(self.driver)
        self.add_customer.clickOnCustomersMainMenu()
        self.add_customer.clickOnCustomersSubMenu()
        self.add_customer.clickAddNewCustomerBtn()

        self.logger.info("*********** Providing New Customer Information ***********")
        self.email = random_email_generator() + "@gmail.com"
        self.add_customer.setEmail(self.email)
        self.add_customer.setPassword("user123")
        self.add_customer.setFirstName("Tanvir")
        self.add_customer.setLastName("Ahmed")
        self.add_customer.setGender("Male")
        self.add_customer.setDOB("01/01/1990")
        self.add_customer.setCompanyName("ABC Company")
        self.add_customer.setTax()

        '''Between Newsletter and Customer Roles we should set Customer Roles first in order to avoid errors as
        the user is by default set as Registered and We need to deselect that first. As the locators to deselect
        that option works for another element if we set the Newsletter first. We need to call the method multiple 
        time to set multiple Customer Roles.'''
        self.add_customer.setCustomerRoles("Registered")
        self.add_customer.setNewsletter("Test store 2")
        self.add_customer.setManagerOfVendor("Vendor 1")
        self.add_customer.setAdminComment("This is a user for testing...")
        self.add_customer.clickOnSave()

        self.logger.info("*********** Starting Add Customer Test ***********")

        self.logger.info("*********** Add Customer Validation Started ***********")
        self.body_msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.body_msg)

        if "customer has been added successfully" in self.body_msg:
            assert True == True
            self.logger.info("*********** Add Customer Test Passed ***********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Add_Customer_scr.png")
            self.logger.info("*********** Add Customer Test Failed ***********")
            assert True == False

        self.driver.close()
        self.logger.info("*********** Ending Add Customer Test ***********")
