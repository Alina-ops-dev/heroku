# 5. Typos - проверить соответствие текста параграфа правильному написанию,
# учитывая возможные варианты текста на странице.
# Локатор: By.TAG_NAME, "p"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.advanced
@pytest.mark.regression
def test_detect_typo(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    count = 1
    count_max = 10
    correct_text = "Sometimes you'll see a typo, other times you won't."

    typo = False

    while count <= count_max:
        element = browser.find_element(By.XPATH, "//p[contains(text(), 'Sometimes you')]")
        error_text = element.text.strip()

        if error_text != correct_text:
            typo = True
            print(f"[УСПЕХ] Опечатка поймана на итерации №{count}: '{error_text}'")
            break

        browser.refresh()
        count += 1
    assert typo is True, "Ошибка: За {count_max} обновлений страницы опечатка в тексте так и не появилась!"