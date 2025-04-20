import pytest
import allure
from data import BaseData as Bd
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl




@allure.feature("Заказ такси")
class TestTaxiOrder:

    @allure.story("Проверка тарифов")
    @allure.title("Проверка формы заказа такси с разными адресами")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ])
    def test_taxi_order_with_tariffs_check(self, driver, from_address, to_address):
        """
        Проверка заказа такси:
        1. Ввод адресов
        2. Выбор быстрого маршрута
        3. Проверка тарифов
        4. Проверка формы заказа
        """
        with allure.step(f"Открываем страницу {Bd.URL_YA_TRACK}"):
            main_page = MainPage(driver)
            main_page.open(Bd.URL_YA_TRACK)

        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Выбираем быстрый маршрут"):
            main_page.click_element(Fsl.MODE_FAST)

        with allure.step("Нажимаем кнопку 'Вызвать такси'"):
            main_page.click_element(Fsl.BUTTON_CALL_TAXI)

        with allure.step("Проверяем отображение тарифов"):
            for tariff_type in [Fsl.WORKER_TARIFF, Fsl.SLEEPY_TARIFF,
                                Fsl.VACATION_TARIFF, Fsl.TALKATIVE_TARIFF,
                                Fsl.COMFORTING_TARIFF, Fsl.GLOSSY_TARIFF]:
                assert main_page.check_is_displayed(
                    tariff_type), f"Тип тарифа {tariff_type} недоступен"

        with allure.step("Проверяем что один тариф активен"):
            active_tariffs = main_page.find_elements(Fsl.ACTIVE_TARIFF_CARD)
            assert len(active_tariffs) == 1, "Должен быть активен ровно один тариф"

    @allure.story("Проверка тарифов")
    @allure.title("Проверка всплывающих подсказок тарифов")
    @pytest.mark.xfail(reason="Перепутаны тултипы тарифов Сонный и Разговорный")
    def test_tariff_tooltips(self, driver):
        """Проверка отображения и содержания тултипов тарифов"""
        main_page = MainPage(driver)
        main_page.open(Bd.URL_YA_TRACK)
        main_page.prepare_taxi_order()

        with allure.step("Проверяем тултипы для каждого тарифа"):
            tariffs_with_expected_tooltips = {
                Fsl.WORKER_TARIFF: {
                    "icon": Fsl.WORKER_TOOLTIP_ICON,
                    "tooltip": Fsl.WORKER_TOOLTIP,
                    "title": Fsl.WORKER_TOOLTIP_TITLE,
                    "description": Fsl.WORKER_TOOLTIP_PREFIX,
                    "title_ex": "Рабочий",
                    "description_ex": "Для деловых особ, которых отвлекают"
                },
                Fsl.SLEEPY_TARIFF: {
                    "icon": Fsl.SLEEPY_TOOLTIP_ICON,
                    "tooltip": Fsl.SLEEPY_TOOLTIP,
                    "title": Fsl.SLEEPY_TOOLTIP_TITLE,
                    "description": Fsl.SLEEPY_TOOLTIP_PREFIX,
                    "title_ex": "Сонный",
                    "description_ex": "Для тех, кто не выспался"
                },
                Fsl.VACATION_TARIFF: {
                    "icon": Fsl.VACATION_TOOLTIP_ICON,
                    "tooltip": Fsl.VACATION_TOOLTIP,
                    "title": Fsl.VACATION_TOOLTIP_TITLE,
                    "description": Fsl.VACATION_TOOLTIP_PREFIX,
                    "title_ex": "Отпускной",
                    "description_ex": "Если пришла пора отдохнуть"
                },
                Fsl.TALKATIVE_TARIFF: {
                    "icon": Fsl.TALKATIVE_TOOLTIP_ICON,
                    "tooltip": Fsl.TALKATIVE_TOOLTIP,
                    "title": Fsl.TALKATIVE_TOOLTIP_TITLE,
                    "description": Fsl.TALKATIVE_TOOLTIP_PREFIX,
                    "title_ex": "Разговорчивый",
                    "description_ex": "Если мысли не выходят из головы"
                },
                Fsl.COMFORTING_TARIFF: {
                    "icon": Fsl.COMFORTING_TOOLTIP_ICON,
                    "tooltip": Fsl.COMFORTING_TOOLTIP,
                    "title": Fsl.COMFORTING_TOOLTIP_TITLE,
                    "description": Fsl.COMFORTING_TOOLTIP_PREFIX,
                    "title_ex": "Утешительный",
                    "description_ex": "Если хочется свернуться калачиком"
                },
                Fsl.GLOSSY_TARIFF: {
                    "icon": Fsl.GLOSSY_TOOLTIP_ICON,
                    "tooltip": Fsl.GLOSSY_TOOLTIP,
                    "title": Fsl.GLOSSY_TOOLTIP_TITLE,
                    "description": Fsl.GLOSSY_TOOLTIP_PREFIX,
                    "title_ex": "Глянцевый",
                    "description_ex": "Если нужно блистать"
                }
            }

            for tariff, tooltip in tariffs_with_expected_tooltips.items():
                with allure.step(f"Проверяем тултип для тарифа {tooltip['title']}"):
                    main_page.click_element(tariff)
                    main_page.hover_over_element(tooltip['icon'])
                    assert main_page.check_is_displayed(tooltip['tooltip']), "Тултип не отобразился"

                    tooltip_data = main_page.get_tooltip_text(tooltip['title'], tooltip['description'])
                    assert tooltip["title_ex"] in tooltip_data["title"], "Неверный заголовок тултипа"
                    assert tooltip_data["description"] in tooltip["description_ex"], f"Неверное описание тултипа {tooltip['title']}"

    @allure.story("Проверка формы заказа")
    @allure.title("Проверка полей формы заказа такси")
    def test_order_form_fields(self, driver):
        """Проверка отображения всех необходимых полей формы заказа"""
        main_page = MainPage(driver)
        main_page.open(Bd.URL_YA_TRACK)
        main_page.prepare_taxi_order()

        with allure.step("Проверяем основные поля формы"):
            required_fields = {
                "Телефон": Fsl.PHONE_FIELD,
                "Способ оплаты": Fsl.PAYMENT_METHOD,
                "Комментарий": Fsl.COMMENT_FIELD,
                "Требования": Fsl.REQUIREMENTS_SECTION
            }

            for field_name, locator in required_fields.items():
                with allure.step(f"Проверяем поле '{field_name}'"):
                    assert main_page.check_is_displayed(locator), f"Поле {field_name} не отображается"

