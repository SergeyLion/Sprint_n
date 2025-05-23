# Sprint_n

## Описание
Этот проект представляет собой набор тестов для приложения Яндекс Маршруты:
- Отрисовка маршрута
- Отрисовка блока маршрут
- Функциональность маршрутов
- Заказ такси
- Заказ такси полный флоу

  

## Инструкция по настройке и запуску тестов:

1. **Клонируйте репозиторий:**
   ```bash
   git@github.com:SergeyLion/Sprint_n.git
   
2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt

3. **Запуск тестов:**
   ```bash
   pytest tests/test -n auto
   ```
   
4. **Открыть отчет allure:**

   4.1. Для Windows:
   ```bash
   allure serve .\reports\allure_results
   ```
   
   4.2. Для macOS/ubuntu/linux:
   ```bash
   allure serve reports/allure_results/
   ```
   