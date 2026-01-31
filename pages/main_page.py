from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    main_logo_css = "#pic1"
    empty_basket_css = ".header-basket__empty"
    black_ceylon_tea_css = ".main_catalog_section-s.img-s-1"

    # GETTERS
    def get_main_logo(self):
        return WebDriverWait(self.driver, 15).until(conditions.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                              self.main_logo_css)))

    def get_empty_basket(self):
        return WebDriverWait(self.driver, 15).until(conditions.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                              self.empty_basket_css)))

    def get_black_ceylon_tea(self):
        return WebDriverWait(self.driver, 15).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.black_ceylon_tea_css)))

    # ACTIONS
    def check_main_page(self):
        self.get_main_logo()
        self.get_empty_basket()
        print("Отображается логотип, корзина пустая")

    def click_go_to_black_ceylon(self):
        self.get_black_ceylon_tea().click()
        print("Нажата кнопка раздела 'Чёрный цейлонский чай'")

    # METHODS
    def go_to_black_ceylon(self):
        """Переход в раздел 'Чёрный цейлонский чай'"""
        self.check_main_page()
        self.click_go_to_black_ceylon()
