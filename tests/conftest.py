import pytest
from selenium import webdriver
import allure


@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome в headless-режиме."""
    with allure.step("Создаём драйвер Chrome в headless-режиме"):
        chrome_options = webdriver.ChromeOptions()  # создали объект для опций
        chrome_options.add_argument('--headless=new')  # Запускает Chrome в безголовом режиме (без графического интерфейса)
        chrome_options.add_argument('--no-sandbox')  # Отключает песочницу (sandbox) Chrome
        chrome_options.add_argument('--disable-gpu')  # Отключает GPU-рендеринг
        driver = webdriver.Chrome()  # Создали драйвер и передали в него настройки
        driver.set_window_size(1920, 1080)
        driver.set_page_load_timeout(300)    # 300 секунд на загрузку страницы
        driver.implicitly_wait(10)           # 10 секунд ожидания элемента
        yield driver
        driver.quit()


