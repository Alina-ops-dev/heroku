# Изучить материал по скачиванию файлов в Selenium.
# - Настроить директорию для скачивания файлов через
# ChromeOptions.
# - Скачать файл со страницы File Download.
# - Проверить наличие файла в файловой системе с помощью
# pathlib.Path.
# - При необходимости использовать ожидание завершения
# скачивания.


import time
from pathlib import Path
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.advanced
@pytest.mark.smoke
def test_file_download(browser_download):
    browser, download_dir = browser_download

    browser.get("https://the-internet.herokuapp.com/download")
    link = browser.find_element(By.XPATH, "//a[text()='some-file.txt']")
    file_name = link.text
    link.click()

    file_path = Path(download_dir) / file_name

    for test in range(10):
        if file_path.exists():
            break
        time.sleep(1)

    assert file_path.exists(), f"Файл '{file_name}' не найден по пути: {file_path}"
    assert file_path.is_file(), f"Объект '{file_path}' не является файлом"