import time

import pytest
from data import BaseData as Bd
from pages.main_page import MainPage
from locators.map_locators import MapLocators as Ml
from locators.form_search_locators import FormSearchLocators as Fsl



class TestRouteFunctionality:

    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ])
    def test_route_points_displayed_on_map(self, driver, from_address, to_address):
        """Проверка отображения точек маршрута на карте при вводе разных адресов"""
        main_page = MainPage(driver)
        main_page.open(Bd.URL_YA_TRACK)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        assert main_page.check_is_displayed(Ml.END_POINT)
        assert main_page.check_is_displayed(Ml.START_POINT)

    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ])
    def test_route_block_displayed_for_different_addresses(self, driver, from_address, to_address):
        """Проверка отображения блока маршрута при вводе разных адресов"""
        main_page = MainPage(driver)
        main_page.open(Bd.URL_YA_TRACK)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        for mode in [Fsl.MODE_OPTIMAL, Fsl.MODE_FAST, Fsl.MODE_CUSTOM]:
            assert main_page.check_is_displayed(mode)

    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Хамовнический Вал, 34"),
        ("Зубовский бульвар, 37", "Зубовский бульвар, 37")
    ])
    def test_route_block_for_same_address(self, driver, from_address, to_address):
        """Проверка блока маршрута при вводе одинаковых адресов"""
        text_search = "Авто Бесплатно"
        duration_search = "В пути 0 мин."
        main_page = MainPage(driver)
        main_page.open(Bd.URL_YA_TRACK)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        assert text_search == main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
        assert duration_search == main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH)