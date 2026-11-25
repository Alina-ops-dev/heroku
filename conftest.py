import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def browser_download(tmp_path):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": str(tmp_path),  # Chrome требует строковый абсолютный путь
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    yield driver, tmp_path
    driver.quit()


@pytest.fixture(scope="class")
def browser_class(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()