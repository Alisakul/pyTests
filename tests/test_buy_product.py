from selenium import webdriver

from pages.main_page import MainPage
from pages.black_ceylon_page import BlackCeylonPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    print("Открытие главной страницы")
    url = 'https://www.mlesna.ru/'
    driver.get(url)
    driver.maximize_window()

    main = MainPage(driver)
    black_ceylon = BlackCeylonPage(driver)

    main.go_to_black_ceylon()
    black_ceylon.check_and_go_to_cinnamon_cart()




    print("SUCCESS........")
