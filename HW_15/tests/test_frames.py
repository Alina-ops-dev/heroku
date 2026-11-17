# Открыть страницу с iFrame.
# - Переключиться внутрь iFrame с помощью
# driver.switch_to.frame().
# - Найти элемент с текстом внутри фрейма.
# - Проверить, что текст равен “Your content goes here.”.
# - Вернуться к основному документу с помощью
# driver.switch_to.default_content().

from selenium.webdriver.common.by import By
import pytest

@pytest.mark.advanced
@pytest.mark.smoke
def test_frames(browser):
    browser.get("https://the-internet.herokuapp.com/frames")
    browser.find_element(By.XPATH, "//a[text()='iFrame']").click()
    iframe = browser.find_element(By.ID, "mce_0_ifr")
    browser.switch_to.frame(iframe)
    text = browser.find_element(By.ID, "tinymce")
    assert text.text == "Your content goes here."

    browser.switch_to.default_content()
