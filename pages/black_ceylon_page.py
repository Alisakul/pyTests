from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from base.base_class import Base


class BlackCeylonPage(Base):
    url = 'https://www.mlesna.ru/catalog/tseylonskiy/chernyiy/'
    categories = ['БАЙХОВЫЙ БЕЗ ДОБАВОК', 'ПАКЕТИРОВАНЫЙ БЕЗ ДОБАВОК', 'АРОМАТИЗИРОВАННЫЙ БАЙХОВЫЙ ЧАЙ',
                  'ПАКЕТИРОВАННЫЙ С АРОМАТАМИ', 'НАБОРЫ', 'ОСОБЫЕ ЧАИ', '', '', '', '', '', '', '', '', '']

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    current_section_css = "._tab-link.-current"
    link_css = "._tab-link.-current a[href='/catalog/tseylonskiy/chernyiy/']"
    section_name_css = "div[id='tab-1'] p[class='mobile-section-title']"
    parts_css = ".js-open-catalog-menu"
    maple_filter_css = "//a[contains(text(),'Канадский клен (6)')]"
    buy_button_xp = "//a[contains(text(),'купить')]"

    # GETTERS
    def get_current_section(self):
        return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                           self.current_section_css)))

    def get_section_name(self):
        return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                           self.section_name_css)))

    def get_link(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.link_css)

    def get_maple_filter(self):
        return self.driver.find_element(By.XPATH, self.maple_filter_css)

    def get_parts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.parts_css)

    # ACTIONS
    def click_maple_filter(self):
        self.get_maple_filter().click()
        print("Нажат фильтр Канадский клен")

    # METHODS
    def check_black_ceylon_section(self):
        base = Base(self.driver)
        base.assert_url(self.url)
        name = self.get_section_name().text
        assert self.get_current_section().is_displayed(), "не отображается текущая секция"
        self.get_link()
        parts = self.get_parts()
        texts = [el.text for el in parts]
        assert texts == self.categories, "Разделы на странице не соответствуют ожидаемому: " + ", ".join(texts)
        print("Выбран корректный раздел: " + name)

    def check_and_go_to_maple_cart(self):
        self.check_black_ceylon_section()
        self.click_maple_filter()
