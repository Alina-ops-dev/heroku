# Создать тестовый файл для загрузки.
# - Загрузить файл с помощью send_keys().
# - Нажать кнопку Upload.
# - Проверить с помощью assert, что имя загруженного файла на
# странице совпадает с именем исходного файла.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pathlib import Path

@pytest.mark.advanced
@pytest.mark.smoke
def test_dynamic_controls(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    file_path = Path("1.txt").resolve()
    browser.find_element(By.ID, "file-upload").send_keys(str(file_path))

    browser.find_element(By.ID, "file-submit").click()
    uploaded = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "uploaded-files"))
    )
    assert uploaded.text == file_path.name

