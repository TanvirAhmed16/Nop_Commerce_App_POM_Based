import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities import excel_utility
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_02_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/NPC_Login_Data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_DDT_Login(self, launchBrowser):
        self.logger.info("*********** Test_02_DDT_Login ***********")
        self.logger.info("*********** Verifying Login DDT Test ***********")
        self.driver = launchBrowser
        self.driver.get(self.base_url)

        '''Creating an object of LoginPage to use the LoginPage class methods'''
        self.lp = LoginPage(self.driver)

        '''Now we will read the email & password from the excel file.'''
        self.rows = excel_utility.get_row_count(self.path, "Sheet1")
        print("Number of Rows in an Excel: ", self.rows)

        list_status = []    # Empty list variable to store test status.
        for r in range(2, self.rows+1):
            self.email = excel_utility.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utility.read_data(self.path, "Sheet1", r, 2)
            self.exp_res = excel_utility.read_data(self.path, "Sheet1", r, 3)

            '''Now passing the data captured from excel file.'''
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLoginBtn()
            time.sleep(3)

            act_page_title = self.driver.title
            exp_page_title = "Dashboard / nopCommerce administration"

            if act_page_title == exp_page_title:
                if self.exp_res == "Pass":
                    self.logger.info("***Test Passed.")
                    self.lp.clickLogoutBtn()
                    list_status.append("Pass")
                elif self.exp_res == "Fail":
                    self.logger.info("***Test Failed.")
                    self.lp.clickLogoutBtn()
                    list_status.append("Fail")

            elif act_page_title != exp_page_title:
                if self.exp_res == "Pass":
                    self.logger.info("***Test Failed.")
                    list_status.append("Fail")
                elif self.exp_res == "Fail":
                    self.logger.info("***Test Passed.")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***** Login DDT Test is passed.*****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT Test is failed.*****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_ddt_Login.png")
            self.driver.close()
            assert False

        self.logger.info("******** End of Login DDT Test. ********")
        self.logger.info("*********** Completed Test_02_DDT_Login ***********")