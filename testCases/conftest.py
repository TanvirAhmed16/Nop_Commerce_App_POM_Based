from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def launchBrowser(browser):
    serv_obj_ch = Service("F:\\Softwares\\Selenium WebDrivers\\chromedriver.exe")
    serv_obj_ff = Service("F:\\Softwares\\Selenium WebDrivers\\geckodriver.exe")
    serv_obj_edge = Service("F:\\Softwares\\Selenium WebDrivers\\msedgedriver.exe")
    if browser == "chrome":
        driver = webdriver.Chrome(service=serv_obj_ch)
        driver.maximize_window()
        print("Launching Chrome Browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=serv_obj_ff)
        driver.maximize_window()
        print("Launching Firefox Browser...")
    else:  # Default browser in case no browser name is passed through CLI
        driver = webdriver.Firefox(service=serv_obj_edge)
        driver.maximize_window()
        print("Launching Edge Browser...")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")


'''Code for Generating pyTest HTML Report...'''


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "NopCommerceApp"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Tanvir"


''' It is hook for Delete/Modify Environment info to HTML Report. This will basically remove the info from HTML report
which we don't want to see in the report.
'''


@pytest.mark.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)
