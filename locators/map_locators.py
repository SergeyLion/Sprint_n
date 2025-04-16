from selenium.webdriver.common.by import By


class MapLocators:
    # Основной контейнер карты
    MAP_CONTAINER = (By.CSS_SELECTOR, "div.map")
    YANDEX_MAP = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-map")

    # Элементы управления картой
    ZOOM_IN_BUTTON = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-zoom__plus")
    ZOOM_OUT_BUTTON = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-zoom__minus")
    ZOOM_SLIDER = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-zoom__scale")

    # Точки маршрута
    ROUTE_POINTS = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-route-pin")
    START_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-0')]")
    END_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-1')]")

    # Текст маршрутных точек
    POINT_TEXT = (By.XPATH, "//ymaps[@id[starts-with(., 'id_')]]") # Текс стартовой и конечной точки

    # Кнопка "Открыть маршрут"
    OPEN_ROUTE_BUTTON = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-gotoymaps")

    # Canvas элементы карты
    MAP_CANVAS = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-ground-pane")
    TILES = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-user-selection-none[style*='background-image']")