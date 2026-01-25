from selenium import webdriver

from pages.main_page import MainPage
from pages.sofa_page import SofaPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)
    print("Открытие главной страницы")
    url = 'https://www.divan.ru/'
    driver.get(url)
    driver.maximize_window()

    main = MainPage(driver)
    sofa = SofaPage(driver)

    main.go_to_sofa()




    print("SUCCESS........")
