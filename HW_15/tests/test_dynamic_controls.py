# - Нажать кнопку Remove рядом с чекбоксом.
# - С помощью WebDriverWait дождаться сообщения “It’s gone!”.
# - Проверить, что чекбокс отсутствует на странице.
# - Найти поле ввода и проверить, что оно неактивно (is_enabled()).
# - Нажать кнопку Enable.
# - Дождаться сообщения “It’s enabled!”.
# - Проверить, что поле ввода стало активным.
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
@pytest.mark.smoke
def test_dynamic_controls(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")
    browser.find_element(By.XPATH, "//button[text() = 'Remove']").click()
    wait = WebDriverWait(browser, 10)
    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert message.text == "It's gone!"
    checkbox = wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))

    element_disabled = browser.find_element(By.XPATH, "//input[@type='text']")
    assert not element_disabled.is_enabled()

    browser.find_element(By.XPATH, "//button[text() = 'Enable']").click()
    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert message.text == "It's enabled!"

    assert element_disabled.is_enabled()