import allure
from pages.base_page import BasePage
from locators.form_search_locators import FormSearchLocators as Fsl



class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Подготовить заказ такси (ввод адресов и открытие формы)")
    def prepare_taxi_order(self, from_address="Хамовнический Вал, 34", to_address="Зубовский бульвар, 37"):
        """Подготавливает заказ такси для тестирования"""
        with allure.step(f"Вводим адреса: {from_address} -> {to_address}"):
            self.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
            self.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        with allure.step("Выбираем быстрый маршрут"):
            self.click_element(Fsl.MODE_FAST)

        with allure.step("Нажимаем кнопку 'Вызвать такси'"):
            self.click_element(Fsl.BUTTON_CALL_TAXI)

    @allure.step('Проверяем активность таба тарифа')
    def is_tab_active_route(self, locator):
        tab = self.find_element(locator)
        return "active" in tab.get_attribute("class")

    @allure.step("Получить текст тултипа")
    def get_tooltip_text(self, title, description):
        return {
            "title": self.get_element_text(title),
            "description": self.get_element_text(description)
        }

    @allure.step('Нормализация данных')
    def normalize_price(self, price):
        # Убираем все символы, кроме цифр
        return ''.join(filter(str.isdigit, price))
