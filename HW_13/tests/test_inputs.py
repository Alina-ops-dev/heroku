# 4. Inputs - проверить возможность ввода различных цифровых и нецифровых
# значений, используя Keys.ARROW_UP и Keys.ARROW_DOWN.
# Локатор: By.TAG_NAME, "input"
#

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.smoke
@pytest.mark.advanced

def test_inputs(browser):
    browser.get("http://the-internet.herokuapp.com/inputs")

    input_value = browser.find_element(By.TAG_NAME, "input")
    test_letter = "a"
    input_value.send_keys(test_letter)

    current_text = input_value.get_attribute("value")
    assert test_letter not in current_text, "Ошибка! Буква '{test_letter}' ввелась в поле"
    input_value.clear()

    test_number = "5"
    input_value.send_keys(test_number)

    current_text = input_value.get_attribute("value")
    assert current_text == test_number, "Цифра '{test_number}' введена в поле"

    input_value.send_keys(Keys.ARROW_DOWN)
    current_text = input_value.get_attribute("value")
    assert current_text == "4", "Ожидаем цифру 4"

    input_value.send_keys(Keys.ARROW_UP)
    current_text = input_value.get_attribute("value")
    assert current_text == "5", "Ожидаем цифру 5"