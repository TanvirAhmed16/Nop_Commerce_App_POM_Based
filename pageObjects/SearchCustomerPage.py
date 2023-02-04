import time
from selenium.webdriver.common.by import By


class SearchCustomer:
    lnk_main_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_sub_customers_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    # Search Customer Fields
    textbox_email_xpath = "//input[@id='SearchEmail']"
    textbox_first_name_xpath = "//input[@id='SearchFirstName']"
    textbox_last_name_xpath = "//input[@id='SearchLastName']"
    btn_search_xpath = "//button[@id='search-customers']"

    table_search_result_xpath = "//div[@class='dataTables_scroll']"
    table_rows_xpath = "//div[@class='dataTables_scroll']//tbody//tr"
    table_columns_xpath = "//div[@class='dataTables_scroll']//tbody//tr//td"

    # table_search_result_xpath = "//table[@id='customers-grid']"
    # table_rows_xpath = "//table[@id='customers-grid']//tbody//tr"
    # table_columns_xpath = "//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMainMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_main_customers_menu_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_sub_customers_menu_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setFirstName(self, f_name):
        self.driver.find_element(By.XPATH, self.textbox_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_first_name_xpath).send_keys(f_name)

    def setLastName(self, l_name):
        self.driver.find_element(By.XPATH, self.textbox_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_last_name_xpath).send_keys(l_name)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_columns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_search_result_xpath)
            email_id = table.find_element(By.XPATH, "//div[@class='dataTables_scroll']//tbody//tr["+str(r)+"]//td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_search_result_xpath)
            u_name = table.find_element(By.XPATH, "//div[@class='dataTables_scroll']//tbody//tr["+str(r)+"]//td[3]").text
            if u_name == name:
                flag = True
                break
        return flag
