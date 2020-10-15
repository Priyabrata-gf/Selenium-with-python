from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
#it is required to add html reports
def pytest_configure(config):
    config._metadata['Project Name']='Selenium with Python'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Priyabrata'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)







