from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from base.base_class import Base


class CinnamonPage(Base):
    url = 'https://www.mlesna.ru/catalog/tseylonskiy/chernyiy/paketirovannyiy/aromatizirovannyiy/koritsa/'
    category_text = "Пакетированный Ароматизированный  Корица"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    section_text_css = ".catalog__mobile-title.mobile-section-title"
    product_name_xp = "//a[contains(text(),'Чай черный с ароматом корицы')]"


    link_css = "._tab-link.-current a[href='/catalog/tseylonskiy/chernyiy/']"
    section_name_css = "div[id='tab-1'] p[class='mobile-section-title']"
    parts_css = ".js-open-catalog-menu"
    cinnamon_filter_css = "a[href='/catalog/tseylonskiy/chernyiy/bayhovyiy/aromatizirovannyiy/koritsa/']"
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

    def get_cinnamon_filter(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.cinnamon_filter_css)

    def get_parts_css(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.parts_css)

    # ACTIONS
    def click_cinnamon_filter(self):
        self.get_cinnamon_filter().click()
        print("Нажат фильтр Корица")

    # METHODS
    def check_black_ceylon_section(self):
        base = Base(self.driver)
        base.assert_url(self.url)
        name = self.get_section_name().text
        self.get_current_section().is_displayed()
        self.get_link()
        parts = self.get_parts_css()
        texts = [el.text for el in parts]
        assert texts == self.categories
        print("Выбран корректный раздел: " + name)

    def check_and_go_to_cinnamon_cart(self):
        self.check_black_ceylon_section()
        self.click_cinnamon_filter()
