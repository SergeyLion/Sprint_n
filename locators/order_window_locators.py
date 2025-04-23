from selenium.webdriver.common.by import By


class OrderWindowLocators:
    # Основной контейнер
    ORDER_CONTAINER = (By.CSS_SELECTOR, ".order-body")

    # Шапка заказа
    ORDER_HEADER = (By.CSS_SELECTOR, ".order-header")
    ORDER_TITLE = (By.CSS_SELECTOR, ".order-header-title")  # "6 мин. и приедет"
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")  # "п 367 уг"
    CAR_ICON = (By.CSS_SELECTOR, ".order-number img[alt='Car']")

    # Блок с кнопками
    BUTTONS_CONTAINER = (By.CSS_SELECTOR, ".order-buttons")

    # Информация о водителе
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")  # "4,9"
    DRIVER_NAME = (By.XPATH,
                   "//div[contains(@class, 'order-btn-group') and .//div[contains(@class, 'order-btn-rating')]]/following-sibling::div")  # "Жубан"
    DRIVER_AVATAR = (By.CSS_SELECTOR, "img[alt='close']")

    # Кнопки управления
    CANCEL_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]")
    CANCEL_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]/following-sibling::div")  # "Отменить"

    DETAILS_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]")
    DETAILS_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]/following-sibling::div")  # "Детали"

    # Адрес подачи
    PICKUP_ADDRESS = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Хамовнический')]")
    PICKUP_ADDRESS_LABEL = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Адрес подачи')]")

    # Адрес назначения
    DESTINATION_ADDRESS = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Зубовский')]")
    DESTINATION_ADDRESS_LABEL = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Адрес назначения')]")

    # Способ оплаты
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Наличные')]")
    PAYMENT_METHOD_LABEL = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Способ оплаты')]")
    PAYMENT_ICON = (By.CSS_SELECTOR, "img[alt='cash']")

    # Стоимость
    ORDER_PRICE = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")
