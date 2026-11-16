import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def browser_class(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()