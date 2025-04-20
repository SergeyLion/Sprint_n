import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from data import BaseData as Bd
import logging



class BasePage: #Класс с базовыми методами

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Bd.TIMEOUT)

        # Настройка логирования
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # Открыть браузер
    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ищем элементы по {locator} и возвращением список элементов')
    def find_elements(self, locator):
        """
                Метод для поиска списка элементов на странице с явным ожиданием.
                Если элементы не найдены, возвращается пустой список.
                :param locator: кортеж с локатором (By.<METHOD>, 'value')
                :return: список найденных элементов (пустой список, если элементы не найдены)
                """
        try:
            # Пытаемся найти элементы с явным ожиданием
            elements = self.wait.until(Ec.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            # Если элементы не найдены, возвращаем пустой список
            return []

    @allure.step('Ищем элемент по {locator} и возвращением его')
    def find_element(self, locator):
        element = self.wait.until(Ec.presence_of_element_located(locator))
        return element

    # Метод ждущий загрузки элемента по локатору
    @allure.step('Ждем когда элемент {locator} загрузится')
    def wait_for_load(self, locator):
        try:
            return self.wait.until(Ec.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за отведенное время.")
            raise

    # Метод ждущий по локатору когда элемент станет кликабельным
    @allure.step('Ждем когда элемент {locator} станет кликабельным')
    def wait_for_click(self, locator):
        try:
            return self.wait.until(Ec.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным за отведенное время.")
            raise

    @allure.step('Достаем текст элемента по локатору {locator}')
    def get_element_text(self, locator):
        return self.find_element(locator).text


    # Метод проверяющий видимость элемента на странице, возвращает True если элемент отображается
    @allure.step('Проверяем видимость элемента {locator}')
    def check_is_displayed(self, locator):
        try:
            self.wait_for_load(locator)
            is_displayed = self.driver.find_element(*locator).is_displayed()
            return is_displayed
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            return False


    # Метод нажимающий на элемент
    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, locator):
        try:
            self.wait_for_click(locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

    # Метод нажимающий на элемент
    @allure.step('Нажимаем JS на элемент {locator}')
    def click_element_js(self, locator):
        try:
            button = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

    # Метод для ввода текста, set_data - текст для ввода
    @allure.step('Вводим текст {set_data} в поле ввода {locator}')
    def set_input(self, locator, set_data):
        self.wait_for_click(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(set_data)

    @allure.step('Переключаемся на вкладку {number_tab}')
    def switch_tab(self, number_tab):
        if number_tab < 1 or number_tab > len(self.driver.window_handles):
            raise ValueError(f"Вкладка с номером {number_tab} не существует.")
        self.driver.switch_to.window(self.driver.window_handles[number_tab - 1])

    @allure.step("Навести курсор на элемент")
    def hover_over_element(self, locator):
        """Наводит курсор на указанный элемент"""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            Ec.invisibility_of_element_located(locator))

