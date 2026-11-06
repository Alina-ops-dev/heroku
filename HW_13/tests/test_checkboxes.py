# 2. Checkboxes - проверить, что первый чекбокс unchecked, отметить первый
# чекбокс, проверить, что он checked. Проверить, что второй чекбокс checked,
# сделать uncheck, проверить, что он unchecked.
# Локатор: By.CSS_SELECTOR, "[type='checkbox']"

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression

def test_checkboxes(browser):
    browser.get("http://the-internet.herokuapp.com/checkboxes")

    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    CHECKBOX_1= checkboxes[0]
    CHECKBOX_2 = checkboxes[1]

    assert CHECKBOX_1.is_selected() is False, "Ожидалось, что первый чекбокс НЕ выбран, но его статус: {checkbox_1.is_selected()}"

    CHECKBOX_1.click()

    assert CHECKBOX_1.is_selected() is True, "Ожидалось, что первый чекбокс выберется после клика, но его статус: {checkbox_1.is_selected()}"
    assert CHECKBOX_2.is_selected() is True, "Ожидалось, что второй чекбокс изначально выбран, но его статус: {checkbox_2.is_selected()}"

    CHECKBOX_2.click()

    assert CHECKBOX_2.is_selected() is False, "Ожидалось, что второй чекбокс отключится после клика, но его статус: {checkbox_2.is_selected()}"