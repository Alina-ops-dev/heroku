# 1. Add/Remove Elements - добавить 2 элемента, удалить элемент, проверить
# количество элементов DELETE.
# Локаторы:
# ● By.XPATH, "//button[text()='Add Element']"
# ● By.XPATH, "//button[text()='Delete']"

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.smoke

def test_add_remove_elements(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element = browser.find_element(By.XPATH, "//button[text()='Add Element']")
    add_element.click()
    add_element.click()

    delete_buttons = browser.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(delete_buttons) == 2, "Ожидалось 2 кнопки DELETE, но обнаружено: {len(delete_buttons)}"

    delete_first_element = browser.find_element(By.XPATH, "//button[text()='Delete']")
    delete_first_element.click()

    delete_buttons_all = browser.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len( delete_buttons_all) == 1, "Ожидалась 1 кнопка DELETE, но обнаружено: {len(delete_buttons_all)}"
