from selenium import webdriver

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.black_ceylon_page import BlackCeylonPage
from pages.maple_page import MaplePage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    print("Открытие главной страницы")
    url = 'https://www.mlesna.ru/'
    driver.get(url)
    driver.maximize_window()
    product = "Чай черный «Maple» (Кленовый) с ароматом сока канадского клена"
    price = "750"
    delivery = "ЖелДорЭкспедиция"
    name = "Just Test User"
    email = "test@test.ru"
    phone = "79777777777"
    comments = "tested  by python"

    main = MainPage(driver)
    black_ceylon = BlackCeylonPage(driver)
    maple = MaplePage(driver)
    basket = BasketPage(driver)

    main.go_to_black_ceylon()
    black_ceylon.check_and_go_to_maple_cart()
    maple.check_and_set_filters(-50, 10, "500", "830", "цене ↓")
    maple.buy_product_and_go_to_basket("1")
    basket.set_all_values_for_order(delivery, name, email, phone, comments)

    print("Успешное заполнение всех полей и переход к размещению заказа")
