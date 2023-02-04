import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddNewCustomer:
    ''' Add New Customer Page Field Locators...'''
    lnk_main_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_sub_customers_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_customer_xpath = "//a[normalize-space()='Add new']"
    #Fields
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_firstname_xpath = "//input[@id='FirstName']"
    textbox_lastname_xpath = "//input[@id='LastName']"
    rd_gender_male_xpath = "//input[@id='Gender_Male']"
    rd_gender_female_xpath = "//input[@id='Gender_Female']"
    textbox_dob_xpath = "//input[@id='DateOfBirth']"
    textbox_company_name_xpath = "//input[@id='Company']"
    checkbox_tax_xpath = "//input[@id='IsTaxExempt']"
    '''In Newsletter and Customer Roles portion all XPATH doesn't work. So we eed to use this specific XPATH's to 
    automate. And also .click() method doesn't work for this options. That's why we will use- 
    driver.execute_script("arguments[0].click();",ele) to automate the application.'''
    # Newsletter
    textbox_newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    listitem_newsletter_your_store_xpath = "//li[contains(text(),'Your store name')]"
    listitem_newsletter_test_store_xpath = "//li[contains(text(),'Test store 2')]"
    # Customer Roles
    textbox_customer_roles_xpath = "(//div[@role='listbox'])[2]"
    listitem_customer_roles_administrators_xpath = "//li[contains(text(),'Administrators')]"
    listitem_customer_roles_moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listitem_customer_roles_guests_xpath = "//li[contains(text(),'Guests')]"
    listitem_customer_roles_registered_xpath = "//li[contains(text(),'Registered')]"
    listitem_customer_roles_vendors_xpath = "//li[contains(text(),'Vendors')]"
    listitem_customer_roles_del_reg_xpath = "//span[@title='delete']"

    drop_down_vendor_xpath = "//select[@id='VendorId']"
    textbox_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMainMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_main_customers_menu_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_sub_customers_menu_xpath).click()

    def clickAddNewCustomerBtn(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_customer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def setFirstName(self, f_name):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(f_name)

    def setLastName(self, l_name):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(l_name)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rd_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.textbox_dob_xpath).send_keys(dob)

    def setCompanyName(self, com_name):
        self.driver.find_element(By.XPATH, self.textbox_company_name_xpath).send_keys(com_name)

    def setTax(self):
        self.driver.find_element(By.XPATH, self.checkbox_tax_xpath).click()

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.textbox_newsletter_xpath).click()
        time.sleep(3)
        if newsletter == "Your store name":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_newsletter_your_store_xpath)
        elif newsletter == "Test store 2":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_newsletter_test_store_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_newsletter_test_store_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRoles(self, customer_role):
        # We should remember the user can be a Registered User or can be a Guest User. Not both.
        # First we need to deselect the Registered option so that no errors occurs.
        self.driver.find_element(By.XPATH, self.listitem_customer_roles_del_reg_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_customer_roles_xpath).click()
        time.sleep(3)
        if customer_role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_administrators_xpath)
        elif customer_role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_moderators_xpath)
        elif customer_role == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_guests_xpath)
        elif customer_role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_registered_xpath)
        elif customer_role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitem_customer_roles_guests_xpath)

        # As .click() method doesn't work here, We will use .execute_script() method
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, vendor):
        vendor_dropdown = Select(self.driver.find_element(By.XPATH, self.drop_down_vendor_xpath))
        vendor_dropdown.select_by_visible_text(vendor)

    def setAdminComment(self, adm_comment):
        self.driver.find_element(By.XPATH, self.textbox_admin_comment_xpath).send_keys(adm_comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()