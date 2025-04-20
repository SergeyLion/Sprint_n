import pytest
import allure
from selenium.common import TimeoutException
from data import BaseData as Bd
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl
from locators.order_waiting_locators import OrderWaitingLocators as Orl
from locators.order_window_locators import OrderWindowLocators as Owl



@allure.feature("Заказ такси")
class TestTaxiOrderFlow:

    @allure.story("Полный флоу заказа такси с проверкой окна ожидания")
    @allure.title("Проверка окна ожидания машины после заказа такси")
    def test_taxi_order_waiting_screen(self, driver):
        """
        1. Ввод адресов
        2. Выбор быстрого маршрута
        3. Выбор тарифа и требований
        4. Проверка окна ожидания
        """
        with allure.step("Подготовка: открытие страницы, ввод адресов и выбор тарифов"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)
            main_page.prepare_taxi_order()

        with allure.step("Выбор тарифа 'Рабочий' и включение столика"):
            main_page.click_element(Fsl.WORKER_TARIFF)
            main_page.click_element(Fsl.REQUIREMENTS_HEADER)
            main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
            main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        with allure.step("Проверка элементов окна ожидания машины"):
            # Проверка заголовка
            assert main_page.get_element_text(
                Orl.ORDER_HEADER_TITLE) == "Поиск машины", "Неверный заголовок окна ожидания"

            # Проверка наличия таймера
            assert main_page.check_is_displayed(Orl.ORDER_TIMER), "Таймер не отображается"

            # Проверка кнопок
            assert main_page.get_element_text(Orl.CANCEL_BUTTON_TEXT) == "Отменить", "Неверный текст кнопки Отменить"
            assert main_page.get_element_text(Orl.DETAILS_BUTTON_TEXT) == "Детали", "Неверный текст кнопки Детали"

    @allure.story("Полный флоу заказа такси с проверка окна завершенного заказа после поиска машины")
    @allure.title("Проверка отображения элементов окна найденной машины")
    def test_order_completion_screen(self, driver):
        """
        1. Ввод адресов
        2. Выбор быстрого маршрута
        3. Выбор тарифа и требований
        4. Дождаться окончания таймера поиска машины
        5. Проверить элементы окна найденной машины
        """
        with allure.step("Подготовка: открытие страницы, ввод адресов и выбор тарифов"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)
            main_page.prepare_taxi_order()

        with allure.step("Выбор тарифа 'Рабочий' и включение столика"):
            main_page.click_element(Fsl.WORKER_TARIFF)
            main_page.click_element(Fsl.REQUIREMENTS_HEADER)
            main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
            main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        with allure.step("Ожидание окончания таймера поиска машины"):
            try:
                main_page.wait_for_invisibility(Orl.ORDER_TIMER, 120)
            except TimeoutException:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="timer_timeout",
                    attachment_type=allure.attachment_type.PNG
                )
                pytest.fail("Таймер поиска машины не завершился в течение 2 минут")

        with allure.step("Проверка элементов окна завершенного заказа"):
            # Проверка заголовка
            assert main_page.check_is_displayed(Owl.ORDER_HEADER), "Заголовок не отображается"

            # Проверка информации о машине
            assert main_page.check_is_displayed(Owl.CAR_NUMBER), "Номер машины не отображается"
            assert main_page.check_is_displayed(Owl.CAR_ICON), "Информация о водителе не отображается"

            # Проверка информации ло водители
            assert main_page.check_is_displayed(Owl.DRIVER_RATING), "Рейтинг водителя не отображается"
            assert main_page.check_is_displayed(Owl.DRIVER_NAME), "Имя водителя не отображается"
            assert main_page.check_is_displayed(Owl.DRIVER_AVATAR), "Аватарка водителя не отображается"

            # Проверка кнопок
            assert main_page.check_is_displayed(Owl.CANCEL_BUTTON), "Кнопка отмены не отображается"
            assert main_page.check_is_displayed(Owl.DETAILS_BUTTON), "Кнопка детали не отображается"

            allure.attach(
                driver.get_screenshot_as_png(),
                name="order_complete_screen",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.story("Проверка стоимости в деталях заказа")
    @allure.title("Сравнение стоимости в деталях с выбранным тарифом")
    def test_price_in_order_details(self, driver):
        """
        1. Создать заказ такси
        2. Запомнить стоимость выбранного тарифа
        3. Создаем заказ
        4. Ждем появления окна Заказа
        5. Нажать кнопку 'Детали'
        6. Проверить, что стоимость в блоке 'Еще про поездку' совпадает с выбранным тарифом
        """
        with allure.step("Подготовка: открытие страницы, ввод адресов и выбор тарифов"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)
            main_page.prepare_taxi_order()

        with allure.step("Выбор тарифа 'Рабочий' и включение столика"):
            main_page.click_element(Fsl.WORKER_TARIFF)
            initial_price = main_page.get_element_text(Fsl.WORKER_TARIFF_PRICE)
            main_page.click_element(Fsl.REQUIREMENTS_HEADER)
            main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
            main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        with allure.step("Ожидание окончания таймера поиска машины"):
            try:
                main_page.wait_for_invisibility(Orl.ORDER_TIMER, 120)
            except TimeoutException:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="timer_timeout",
                    attachment_type=allure.attachment_type.PNG
                )
                pytest.fail("Таймер поиска машины не завершился в течение 2 минут")

        with allure.step("Нажимаем кнопку 'Детали'"):
            main_page.click_element(Owl.DETAILS_BUTTON)

        with allure.step("Проверяем стоимость в блоке 'Еще про поездку'"):
            price_in_details = main_page.get_element_text(Owl.ORDER_PRICE)

            normalized_initial_price = main_page.normalize_price(initial_price)
            normalized_price_in_details = main_page.normalize_price(price_in_details)

            allure.attach(f"Изначальная стоимость: {initial_price}", name="Изначальная стоимость",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Стоимость в деталях: {price_in_details}", name="Стоимость в деталях",
                          attachment_type=allure.attachment_type.TEXT)

            assert normalized_initial_price == normalized_price_in_details, \
                f"Стоимость не совпадает. Ожидалось: {initial_price}, Фактически: {price_in_details}"

    @allure.story("Отмена заказа через кнопку 'Отменить'")
    @allure.title("Проверка закрытия окна после отмены заказа")
    @pytest.mark.xfail(reason="Модальное окно заказа, не закрывается по нажатию на кнопку Отмены")
    def test_cancel_order_closes_window(self, driver):
        """
        1. Создать заказ такси
        2. Нажать кнопку 'Отменить'
        3. Проверить, что окно заказа закрылось
        """
        with allure.step("Подготовка: открытие страницы, ввод адресов и выбор тарифов"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)
            main_page.prepare_taxi_order()

        with allure.step("Выбор тарифа 'Рабочий' и делаем заказ"):
            main_page.click_element(Fsl.WORKER_TARIFF)
            main_page.click_element(Fsl.REQUIREMENTS_HEADER)
            main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        with allure.step("Нажимаем кнопку 'Отменить'"):
            main_page.click_element(Orl.CANCEL_BUTTON)
            allure.attach(
                driver.get_screenshot_as_png(),
                name="after_cancel_click",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Проверяем, что окно заказа закрылось"):
            try:
                main_page.wait_for_invisibility(Orl.ORDER_WAITING_CONTAINER, 10)
            except TimeoutException:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="window_not_closed",
                    attachment_type=allure.attachment_type.PNG
                )
                pytest.fail("Окно заказа не закрылось после отмены")

            assert not main_page.check_is_displayed(Orl.ORDER_WAITING_CONTAINER), \
                "Окно заказа все еще отображается после отмены"

