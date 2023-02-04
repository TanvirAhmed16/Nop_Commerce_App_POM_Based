
# import time
'''Add New Customer Functionality'''
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# serv_obj_ch = Service("F:\\Softwares\\Selenium WebDrivers\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj_ch)
# driver.maximize_window()
# driver.get("https://admin-demo.nopcommerce.com/")
#
# ex_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=Exception)
#
# driver.find_element(By.XPATH, "//input[@id='Email']").clear()
# driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH, "//input[@id='Password']").clear()
# driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
# driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
#
#
# driver.find_element(By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]").click()
# driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()
# driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/Create']").click()
# time.sleep(3)
#
# driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456")
# driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Anower")
# driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Hossain")
# driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
# driver.find_element(By.XPATH, "//input[@id='DateOfBirth']").send_keys("15/10/1995")
# driver.find_element(By.XPATH, "//input[@id='Company']").send_keys("ABC Company")
# driver.find_element(By.XPATH, "//input[@id='IsTaxExempt']").click()
#
#
# driver.find_element(By.XPATH, "//span[@title='delete']").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH, "(//div[@role='listbox'])[2]").click()
# ele3 = driver.find_element(By.XPATH, "//li[contains(text(),'Administrators')]")
# ele4 = driver.find_element(By.XPATH, "//li[contains(text(),'Forum Moderators')]")
# ele5 = driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]")
# ele6 = driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]")
# ele7 = driver.find_element(By.XPATH, "//li[contains(text(),'Vendors')]")
#
# driver.execute_script("arguments[0].click();", ele3)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", ele4)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", ele5)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", ele6)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", ele7)
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//div[@class='input-group-append']//div[@role='listbox']").click()
# ele1 = driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]")
# ele2 = driver.find_element(By.XPATH, "//li[contains(text(),'Test store 2')]")
# driver.execute_script("arguments[0].click();", ele1)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", ele2)
# time.sleep(2)
#
# ven_drp = Select(driver.find_element(By.XPATH, "//select[@id='VendorId']"))
# ven_drp.select_by_visible_text("Vendor 1")
#
# driver.find_element(By.XPATH, "//textarea[@id='AdminComment']").send_keys("This is Admin Content.")
#
# time.sleep(10)
# driver.close()

'''Search Customer By Email or Name'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj_ch = Service("F:\\Softwares\\Selenium WebDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj_ch)
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()


driver.find_element(By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()

u_mail = "admin@yourStore.com"
btn_search_xpath = "//button[@id='search-customers']"

driver.find_element(By.XPATH, "//input[@id='SearchEmail']").send_keys(u_mail)
driver.find_element(By.XPATH, btn_search_xpath).click()

time.sleep(2)

table_xpath = "//div[@class='dataTables_scroll']"
table_rows_xpath = "//div[@class='dataTables_scroll']//tbody//tr"
table_columns_xpath = "//div[@class='dataTables_scroll']//tbody//tr//td"

no_of_rows = driver.find_elements(By.XPATH, table_rows_xpath)
no_of_col = driver.find_elements(By.XPATH, table_columns_xpath)
table = driver.find_element(By.XPATH, table_xpath)
#
print(table.text)
print(len(no_of_rows))
print(len(no_of_col))
#
# if u_mail == table.find_element(By.XPATH, "//div[@class='dataTables_scrollBody']//tbody//tr[1]//td[2]").text:
#     print("Found...")

flag = False
# //div[@class='dataTables_scroll']//tbody//tr["+str(r)+"]//td[2]
for r in range(1,len(no_of_rows)+1):
    table = driver.find_element(By.XPATH, table_xpath)
    email_id = table.find_element(By.XPATH, "//div[@class='dataTables_scroll']//tbody//tr["+str(r)+"]//td[2]").text
    if email_id == u_mail:
        flag = True
    else:
        flag = False
    break
if flag == True:
    print("Found it.")

