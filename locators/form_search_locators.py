from selenium.webdriver.common.by import By


class FormSearchLocators:
    INPUT_FROM_ADDRESS = (By.CSS_SELECTOR, "input#from")
    INPUT_TO_ADDRESS = (By.CSS_SELECTOR, "input#to")
    CLOSE_BUTTON_FROM = (By.CSS_SELECTOR, "#from + .close-button")
    CLOSE_BUTTON_TO = (By.CSS_SELECTOR, "#to + .close-button")

    # Режимы поиска
    MODE_OPTIMAL = (By.XPATH, "//div[contains(@class, 'mode') and text()='Оптимальный']")
    MODE_FAST = (By.XPATH, "//div[contains(@class, 'mode') and text()='Быстрый']")
    MODE_CUSTOM = (By.XPATH, "//div[contains(@class, 'mode') and text()='Свой']")

    # Типы транспорта
    TRANSPORT_CAR = (By.CSS_SELECTOR, ".type.active img[src*='car-active']")
    TRANSPORT_WALK = (By.CSS_SELECTOR, ".type img[src*='walk']")
    TRANSPORT_TAXI = (By.CSS_SELECTOR, ".type img[src*='taxi']")
    TRANSPORT_BIKE = (By.CSS_SELECTOR, ".type img[src*='bike']")
    TRANSPORT_SCOOTER = (By.CSS_SELECTOR, ".type img[src*='scooter']")
    TRANSPORT_DRIVE = (By.CSS_SELECTOR, ".type.drive img[src*='drive']")

    # Тарифы
    TARIFF_EVERYDAY = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Повседневный']]")
    TARIFF_CAMPING = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Походный']]")
    TARIFF_LUXURY = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Роскошный']]")

    # Кнопки
    ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, ".np-button .np-text")
    PAYMENT_METHOD_BUTTON = (By.CSS_SELECTOR, ".pp-button.filled")

    # Требования к заказу
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".reqs-header")
    LAPTOP_TABLE_SWITCH = (
    By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Столик для ноутбука']/following-sibling::div//input")
    ICE_CREAM_LINK = (By.XPATH, "//div[contains(@class, 'r-link-label') and .//div[text()='Ведёрко с мороженым']]")
    MASSAGE_CHAIR_LINK = (By.XPATH, "//div[contains(@class, 'r-link-label') and .//div[text()='Массажное кресло']]")

    # Результат маршрута
    TEXT_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='text']")
    DURATION_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='duration']")