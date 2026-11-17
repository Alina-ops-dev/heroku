# Выполнить правый клик по элементу с помощью ActionChains.
# - Проверить текст появившегося Alert с помощью assert.
# - Закрыть Alert.
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.smoke
def test_context_menu(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")
    actions = ActionChains(browser)
    element = browser.find_element(By.CSS_SELECTOR, "div#hot-spot")
    (
        actions.move_to_element(element)
        .context_click(element) #правый клик по элементу с помощью ActionChains
        .perform()
    )
    alert = browser.switch_to.alert
    assert alert.text == "You selected a context menu", f"Неверный текст алерта: {alert.text}" #текст появившегося Alert с помощью assert
    alert.accept() #Закрыть Alert





