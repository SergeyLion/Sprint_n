import pytest
import allure
from data import BaseData as Bd
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl




@allure.feature("Функциональность маршрутов")
class TestRouteSwitching:

    @allure.story("Переключение между видами маршрута")
    @allure.title("Проверка переключения между Быстрым и Оптимальным маршрутом")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_switch_between_optimal_and_fast_routes(self, driver, from_address, to_address):
        """Проверка смены активного таба и пересчета времени/стоимости при переключении между Оптимальным и Быстрым маршрутом"""
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Запоминаем параметры для оптимального маршрута"):
            optimal_text = main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
            optimal_duration = main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH)

        with allure.step("Переключаемся на оптимальный маршрут"):
            main_page.click_element(Fsl.MODE_OPTIMAL)

        with (allure.step("Проверяем смену активного таба и параметров маршрута")):
            assert main_page.is_tab_active_route(Fsl.MODE_OPTIMAL), "Таб оптимальный маршрута не активен"
            assert (optimal_text != main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
                    or optimal_duration != main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH)), "Стоимость и длительность не изменилась"

    @allure.story("Переключение между видами маршрута")
    @allure.title("Проверка переключения на вид маршрута 'Свой'")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_switch_to_custom_route(self, driver, from_address, to_address):
        """Проверка активации типов передвижения при переключении на маршрут 'Свой'"""
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Переключаемся на пользовательский маршрут"):
            main_page.click_element(Fsl.MODE_CUSTOM)

        with allure.step("Проверяем активность таба и доступность типов передвижения"):
            assert main_page.is_tab_active_route(Fsl.MODE_CUSTOM), "Таб пользовательского маршрута не активен"
            for transport_type in [Fsl.TRANSPORT_CAR, Fsl.TRANSPORT_WALK,
                                   Fsl.TRANSPORT_TAXI, Fsl.TRANSPORT_BIKE,
                                   Fsl.TRANSPORT_SCOOTER, Fsl.TRANSPORT_DRIVE]:
                assert main_page.check_is_displayed(
                    transport_type), f"Тип передвижения {transport_type} недоступен"

    @allure.story("Доступность кнопок заказа")
    @allure.title("Проверка активности кнопки 'Вызвать такси' для быстрого маршрута")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_taxi_button_availability_for_fast_route(self, driver, from_address, to_address):
        """Проверка активности кнопки 'Вызвать такси' при выборе быстрого маршрута"""
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Выбираем быстрый маршрут"):
            main_page.click_element(Fsl.MODE_FAST)

        with allure.step("Проверяем активность кнопки вызова такси,"
                         " кликаем на нее и проверяем отображение тарифов"):
            main_page.click_element(Fsl.BUTTON_CALL_TAXI)
            for tariff_type in [Fsl.WORKER_TARIFF, Fsl.SLEEPY_TARIFF,
                                   Fsl.VACATION_TARIFF, Fsl.TALKATIVE_TARIFF,
                                   Fsl.COMFORTING_TARIFF, Fsl.GLOSSY_TARIFF]:
                assert main_page.check_is_displayed(
                    tariff_type), f"Тип тарифа {tariff_type} недоступен"

    @allure.story("Доступность кнопок заказа")
    @allure.title("Проверка активности кнопки 'Забронировать' для типа 'Драйв'")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_book_button_availability_for_drive_type(self, driver, from_address, to_address):
        """Проверка активности кнопки 'Забронировать' при выборе типа передвижения 'Драйв'"""
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Выбираем пользовательский маршрут и тип 'Драйв'"):
            main_page.click_element(Fsl.MODE_CUSTOM)
            main_page.click_element(Fsl.TRANSPORT_DRIVE)

        with allure.step("Проверяем активность кнопки бронирования драйва, "
                         "кликаем на нее и проверяем видимость тарифов"):
            main_page.click_element(Fsl.BUTTON_RESERVATION_DRIVE)
            for tariff_type in [Fsl.EVERYDAY_TARIFF, Fsl.CAMPING_TARIFF,
                                   Fsl.LUXURY_TARIFF]:
                assert main_page.check_is_displayed(
                    tariff_type), f"Тип тарифа {tariff_type} недоступен"

