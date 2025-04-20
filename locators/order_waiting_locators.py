from selenium.webdriver.common.by import By





#Локаторы ожидания такаси
class OrderWaitingLocators:
    # Основные элементы
    ORDER_WAITING_CONTAINER = (By.CSS_SELECTOR, ".order-body")
    ORDER_HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    ORDER_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    ORDER_PROGRESS_BAR = (By.CSS_SELECTOR, ".order-progress")

    # Кнопки
    CANCEL_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]")
    CANCEL_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]/following-sibling::div")  # "Отменить"
    DETAILS_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]")
    DETAILS_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]/following-sibling::div")  # "Детали"
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Ввести номер и заказать')]")

    # Детали заказа
    PICKUP_ADDRESS = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Хамовнический')]")
    DESTINATION_ADDRESS = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Зубовский')]")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'o-d-h') and contains(text(), 'Наличные')]")
    ORDER_PRICE = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")