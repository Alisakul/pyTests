import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("current url " + get_url)

    def assert_text(self, actual_text_locator, expected_test):
        """Проверка соответствия текста локатора"""
        value_text = actual_text_locator.text()
        assert value_text == expected_test
        print("Значение текста соответствует ожидаемому: " + value_text)

    def assert_url(self, expected_url):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        assert expected_url == get_url
        print("Корректный URL: " + get_url)

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screen_" + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот сохранён: " + name_screenshot)
