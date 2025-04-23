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
    TRANSPORT_CAR = (By.CSS_SELECTOR, ".type img[src*='car']")
    TRANSPORT_WALK = (By.CSS_SELECTOR, ".type img[src*='walk']")
    TRANSPORT_TAXI = (By.CSS_SELECTOR, ".type img[src*='taxi']")
    TRANSPORT_BIKE = (By.CSS_SELECTOR, ".type img[src*='bike']")
    TRANSPORT_SCOOTER = (By.CSS_SELECTOR, ".type img[src*='scooter']")
    TRANSPORT_DRIVE = (By.CSS_SELECTOR, ".type img[src*='drive']")

    # Тарифы
    TARIFF_EVERYDAY = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Повседневный']]")
    TARIFF_CAMPING = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Походный']]")
    TARIFF_LUXURY = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Роскошный']]")

    # Такси
    BUTTON_CALL_TAXI = (By.XPATH, "//button[text()='Вызвать такси']")
    # Локаторы для конкретных тарифов (по названию)
    ACTIVE_TARIFF_CARD = (By.CSS_SELECTOR, ".tariff-cards .tcard.active")
    WORKER_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Рабочий']]")
    SLEEPY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Сонный']]")
    VACATION_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Отпускной']]")
    TALKATIVE_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Разговорчивый']]")
    COMFORTING_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Утешительный']]")
    GLOSSY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Глянцевый']]")
    # Стоимость поездки по тарифу
    WORKER_TARIFF_PRICE = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(@class, 'tcard-price')]")
    # Иконки информации
    WORKER_TOOLTIP_ICON = (
    By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Рабочий']]//button[contains(@class, 'tcard-i')]")
    SLEEPY_TOOLTIP_ICON = (
    By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Сонный']]//button[contains(@class, 'tcard-i')]")
    VACATION_TOOLTIP_ICON = (
    By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Отпускной']]//button[contains(@class, 'tcard-i')]")
    TALKATIVE_TOOLTIP_ICON = (By.XPATH,
                                    "//div[contains(@class, 'tcard') and .//div[text()='Разговорчивый']]//button[contains(@class, 'tcard-i')]")
    COMFORTING_TOOLTIP_ICON = (
    By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Утешительный']]//button[contains(@class, 'tcard-i')]")
    GLOSSY_TOOLTIP_ICON = (
    By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Глянцевый']]//button[contains(@class, 'tcard-i')]")
    # Локаторы для тултипов тарифов
    # Локаторы для конкретных тултипов по названию тарифа
    WORKER_TOOLTIP = (By.XPATH,
                      "//div[contains(@class, 'tcard') and .//div[text()='Рабочий']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    SLEEPY_TOOLTIP = (By.XPATH,
                      "//div[contains(@class, 'tcard') and .//div[text()='Сонный']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    VACATION_TOOLTIP = (By.XPATH,
                        "//div[contains(@class, 'tcard') and .//div[text()='Отпускной']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    TALKATIVE_TOOLTIP = (By.XPATH,
                         "//div[contains(@class, 'tcard') and .//div[text()='Разговорчивый']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    COMFORTING_TOOLTIP = (By.XPATH,
                          "//div[contains(@class, 'tcard') and .//div[text()='Утешительный']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    GLOSSY_TOOLTIP = (By.XPATH,
                      "//div[contains(@class, 'tcard') and .//div[text()='Глянцевый']]//following-sibling::div[contains(@class, '__react_component_tooltip')]")
    # Заголовки тултипов (i-title)
    WORKER_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-0')]//div[contains(@class, 'i-title')]")
    SLEEPY_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-1')]//div[contains(@class, 'i-title')]")
    VACATION_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-2')]//div[contains(@class, 'i-title')]")
    TALKATIVE_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-3')]//div[contains(@class, 'i-title')]")
    COMFORTING_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-4')]//div[contains(@class, 'i-title')]")
    GLOSSY_TOOLTIP_TITLE = (By.XPATH, "//div[contains(@id, 'tariff-card-5')]//div[contains(@class, 'i-title')]")
    # Основные описания (i-dPrefix)
    WORKER_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-0')]//div[contains(@class, 'i-dPrefix')]")
    SLEEPY_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-1')]//div[contains(@class, 'i-dPrefix')]")
    VACATION_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-2')]//div[contains(@class, 'i-dPrefix')]")
    TALKATIVE_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-3')]//div[contains(@class, 'i-dPrefix')]")
    COMFORTING_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-4')]//div[contains(@class, 'i-dPrefix')]")
    GLOSSY_TOOLTIP_PREFIX = (By.XPATH, "//div[contains(@id, 'tariff-card-5')]//div[contains(@class, 'i-dPrefix')]")
    # Форма заказа такси
    # Форма заполнения телефона
    PHONE_FIELD = (By.XPATH, "//div[contains(text(), 'Телефон')]")
    # Общие элементы модального окна
    MODAL_WINDOW = (By.CSS_SELECTOR, ".modal")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".close-button.section-close")

    # Первый экран (ввод телефона)
    PHONE_SECTION = (By.CSS_SELECTOR, ".section.active")
    PHONE_HEADER = (By.CSS_SELECTOR, ".section.active .head")
    PHONE_INPUT = (By.CSS_SELECTOR, "#phone")
    PHONE_LABEL = (By.CSS_SELECTOR, "label[for='phone']")
    PHONE_ERROR = (By.CSS_SELECTOR, ".np-input .error")
    PHONE_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Далее')]")

    # Второй экран (ввод кода из SMS)
    CODE_SECTION = (By.XPATH, "//div[contains(@class, 'section') and not(contains(@class, 'active'))]")
    CODE_HEADER = (By.CSS_SELECTOR, ".section:not(.active) .head")
    CODE_INPUT = (By.CSS_SELECTOR, "#code")
    CODE_LABEL = (By.CSS_SELECTOR, "label[for='code']")
    CODE_CLOSE_BUTTON = (By.CSS_SELECTOR, ".input-close-button")
    CODE_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Подтвердить')]")
    CODE_RESEND_BUTTON = (
    By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Отправить код еще раз')]")

    # Поле "Способ оплаты"
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'pp-button') and .//div[contains(text(), 'Способ оплаты')]]")
    COMMENT_FIELD = (By.XPATH, "//input[@id='comment']")
    REQUIREMENTS_SECTION = (By.XPATH, "//div[contains(@class, 'reqs-header')]")


    # Драйв
    BUTTON_RESERVATION_DRIVE = (By.XPATH, "//button[text()='Забронировать']")
    # Локаторы для конкретных тарифов по названию
    EVERYDAY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Повседневный']]")
    CAMPING_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Походный']]")
    LUXURY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Роскошный']]")


    # Кнопки
    ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, ".np-button .np-text")
    PAYMENT_METHOD_BUTTON = (By.CSS_SELECTOR, ".pp-button.filled")

    # Требования к заказу
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".reqs-header")
    LAPTOP_TABLE_SWITCH = (
    By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Столик для ноутбука']/following-sibling::div//span")
    ICE_CREAM_LINK = (By.XPATH, "//div[contains(@class, 'r-link-label') and .//div[text()='Ведёрко с мороженым']]")
    MASSAGE_CHAIR_LINK = (By.XPATH, "//div[contains(@class, 'r-link-label') and .//div[text()='Массажное кресло']]")

    # Результат маршрута
    TEXT_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='text']")
    DURATION_RESULT_SEARCH = (By.XPATH, "//div[@class = 'results-text']/div[@class='duration']")

    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button-main")

