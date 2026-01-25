import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("Открытие главное страницы")
    url = 'https://www.divan.ru/'
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    # options.add_experimental_option('detach', True)
    # options.add_argument("--incognito")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()
