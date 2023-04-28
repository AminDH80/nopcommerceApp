from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser........")
    elif browser =='firefox':
        driver =webdriver.Firefox()
        print ("Launching Firefox browser.......")
    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser (request):   #This will return the Browser value to setup method
    return request.config.getoption("--browser")

#It is a hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] ='nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amine'

#It is hook for delete / Modify Enviromnent infoto Html Report
@pytest.mark.optionalhook
def pytest_metadat(metadat):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
