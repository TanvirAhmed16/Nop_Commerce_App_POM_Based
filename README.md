# NopCommerce App (POM Based E-Commerce Testing Framework) 

### Project Overview
It’s a POM (Page Object Model) based automation testing framework designed to test the functionality of an e-commerce website. It uses the POM design pattern to create reusable objects for each web page, allowing for easy maintenance and scalability of the test suite. The app automates various backend test scenarios such as admin login, admin login using data driven testing, add customer, search customer etc. The tests are performed using a combination of Selenium WebDriver, Python, and test framework as PyTest with help of other packages like pytest-html, openpyxl etc. The results of the tests are generated and displayed in a clear and concise manner, highlighting any failures and providing detailed debugging information. This allows developers to quickly identify and fix any issues, ensuring a high-quality user experience for customers.

### Project Details
Initially in this project I have designed a complete automation testing framework using Selenium webdriver along with the help of other packages/plugins and also I have executed tests for some of the major backend functionalities for an E-Commerce platform like- 
- Admin Login 
- Admin Login with Data Driven Testing 
- Add New Customer
- Search Customer By Email
- Search Customer By Name etc.

Then I have grouped the test cases and finally generated HTML report for the executed test cases with proper logs.

### Prerequisites
- Python 3.x
- Selenium 4
- webdrivers for the browsers you want to use for testing (e.g. ChromeDriver, FirefoxDriver)
- Python Packages
    - Pytest: Python Unittest Framework
    - Pytest-html: To Generate Pytest HTML Reports
    - Pytest-xdist: To Run Tests Parallel
    - Openpyxl: MS Excel Support

### Installing

1. Install Python 3.x from the official website (https://www.python.org/downloads/)

2. Install Selenium and other packages by running the following command in your command prompt/terminal:

```bash
pip install -r requiredpackages.txt
```

3. Download the appropriate webdrivers for the browsers you want to use for testing. Here are some links to the webdrivers for popular browsers:
- Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
- Firefox: https://github.com/mozilla/geckodriver/releases
- Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/   

### Running the Tests
1. Clone or download the project to your local machine

2. Navigate to the project directory/testCases in your command prompt/terminal

3. Run the following command to run the tests :

```bash
# To Run Tests on Desired Browser
pytest -v -s testCases/test_login.py --browser chrome

# To Run Tests Parallel (If we want to run more than 1 test at a time.)
pytest -v -s -n=3 testCases/test_login.py --browser chrome

# To Generate HTML Reports
pytest -v -s -n=3 --html=Reports\report.html testCases/test_login.py --browser chrome

```
4. The tests will now run and the results will be displayed in the command prompt/terminal and also report will be generated in particular folder.

### Reference
- Selenium with Python : https://selenium-python.readthedocs.io/
- pytest : https://docs.pytest.org/en/7.2.x/
- pytest-html : https://pypi.org/project/pytest-html/
- pytest-xdist : https://pypi.org/project/pytest-xdist/
- openpyxl : https://openpyxl.readthedocs.io/en/stable/

- Website on which the project is implemented : https://admin-demo.nopcommerce.com/

### Report Screenshots

![App Screenshot-1](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/06.report_sanity_or_regression.JPG?raw=true "Report Summary-1")

![App Screenshot-2](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/07.report_passed_details.JPG?raw=true "Report Summary-2")

![App Screenshot-3](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/08.report_failed_details.JPG?raw=true "Report Summary-3")

![App Screenshot-4](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/01.report_login.JPG?raw=true "Report Summary-4")

![App Screenshot-5](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/02.report_login_ddt.JPG?raw=true "Report Summary-5")

![App Screenshot-6](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/03.report_add_customer.JPG?raw=true "Report Summary-6")

![App Screenshot-7](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/04.report_search_customer_email.JPG?raw=true "Report Summary-7")

![App Screenshot-8](https://github.com/TanvirAhmed16/Nop_Commerce_App_POM_Based/blob/main/Report%20SS/05.report_search_customer_name.JPG?raw=true "Report Summary-8")

That's all. Thank You...
