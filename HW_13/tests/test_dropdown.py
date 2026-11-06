# 3. Dropdown - взять все элементы дропдауна и проверить их наличие. Выбрать
# первый доступный вариант, проверить, что он выбран, выбрать второй,
# проверить, что он выбран.
# Локатор: By.ID, "dropdown"

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.advanced
@pytest.mark.regression
def test_dropdown(browser):
    browser.get("http://the-internet.herokuapp.com/dropdown")

    dropdown_element = browser.find_element(By.ID, "dropdown")

    select_object = Select(dropdown_element)
    all_options = select_object.options

    assert len(all_options) == 3, "Ожидалось, что в выпадающем списке будет 3 элемента, но найдено: {len(all_options)}"

    dropdown_element.click()

    select_object.select_by_index(1)
    assert all_options[1].is_selected() is True, "Ошибка: Первый вариант ('Option 1') должен быть выбран, но статус его выбора: {all_options[1].is_selected()}"

    dropdown_element.click()

    select_object.select_by_index(2)
    assert all_options[2].is_selected() is True, "Ошибка: Второй вариант ('Option 2') должен быть выбран, но статус его выбора: {all_options[2].is_selected()}"