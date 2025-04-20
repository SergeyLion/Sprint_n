import pytest
import allure
from data import BaseData as Bd
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl



@allure.feature("Отрисовка блока маршрут")
class TestRouteOptionsDisplay:

    @allure.story("Отображение блока маршрута")
    @allure.title("Проверка отображения блока маршрута для разных адресов")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ], ids=["From Хамовнический to Зубовский", "From Зубовский to Хамовнический"])
    def test_route_block_displayed_for_different_addresses(self, driver, from_address, to_address):
        """Проверка отображения блока маршрута при вводе разных адресов"""
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адрес отправления: {from_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)

        with allure.step(f"Вводим адрес назначения: {to_address}"):
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Проверяем отображение режимов маршрута"):
            for mode in [Fsl.MODE_OPTIMAL, Fsl.MODE_FAST, Fsl.MODE_CUSTOM]:
                assert main_page.check_is_displayed(mode), f"Режим {mode} не отображается"

    @allure.story("Отображение блока маршрута")
    @allure.title("Проверка блока маршрута при вводе одинаковых адресов")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Хамовнический Вал, 34"),
        ("Зубовский бульвар, 37", "Зубовский бульвар, 37")
    ], ids=["Same address Хамовнический", "Same address Зубовский"])
    def test_route_block_for_same_address(self, driver, from_address, to_address):
        """Проверка блока маршрута при вводе одинаковых адресов"""
        text_search = "Авто Бесплатно"
        duration_search = "В пути 0 мин."

        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим одинаковый адрес: {from_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Проверяем текст результата поиска"):
            assert text_search == main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH), \
                f"Текст '{text_search}' не найден в результате"

        with allure.step("Проверяем длительность маршрута"):
            assert duration_search == main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH), \
                f"Длительность '{duration_search}' не найдена в результате"

