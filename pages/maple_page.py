from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.select import Select

from base.base_class import Base


class MaplePage(Base):
    url = 'https://www.mlesna.ru/catalog/tseylonskiy/chernyiy/bayhovyiy/aromatizirovannyiy/kanadskiyklen/'
    category_text = "Байховый ароматизированный с канадским кленом"
    products = ['Чай черный с ароматом сока канадского клена',
                'Чай черный «Maple» (Кленовый) с ароматом сока канадского клена',
                'Чай черный «Maple» (Кленовый) с ароматом сока канадского клена',
                'Чай черный «Maple» (Кленовый) с ароматом сока канадского клена',
                'Чай черный «Maple» (Кленовый) с ароматом сока канадского клена',
                'Чай черный «Maple» (Кленовый) с ароматом сока канадского клена']
    articles = ['02225', '02109', '06037', '04155', '04062', '03112']

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    section_text_css = ".catalog__mobile-title.mobile-section-title"
    slider_max_xp = "//div[@class='noUi-handle noUi-handle-upper']"
    slider_min_xp = "(//div[@class='noUi-handle noUi-handle-lower'])"
    section_name_css = ".catalog__mobile-title.mobile-section-title"
    maple_products_css = "div.name > a"
    articles_css = "table.goods__props > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)"
    max_sum_css = "div[class='noUi-handle noUi-handle-upper'] div[class='noUi-tooltip']"
    min_sum_css = "div[class='noUi-handle noUi-handle-lower'] div[class='noUi-tooltip']"
    select_css = "#catalog_filter_order"
    show_button_xp = "//input[@id='search_btn']"
    buy_button_xp = "(//a[@class='goods__basket'][contains(text(),'купить')])"
    modal_buy_css = ".basket-table__row.js-basket-item"
    modal_price_css = ".basket-table__row-total.js-basket-item-total"
    basket_order_button_css = "#basketOrderButton2"

    # GETTERS
    def get_section_name(self):
        return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                           self.section_name_css)))

    def get_all_maple(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.maple_products_css)

    def get_all_articles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.articles_css)

    def get_slider_max(self):
        return self.driver.find_element(By.XPATH, self.slider_max_xp)

    def get_slider_min(self):
        return self.driver.find_element(By.XPATH, self.slider_min_xp)

    def get_summ(self, is_max):
        if is_max:
            return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                              self.max_sum_css)))
        else:
            return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                              self.min_sum_css)))

    def get_select(self):
        return Select(self.driver.find_element(By.CSS_SELECTOR, self.select_css))

    def get_buy_button(self, product_count):
        return self.driver.find_element(By.XPATH, f'{self.buy_button_xp}[{product_count}]')

    def get_modal_buy(self):
        return WebDriverWait(self.driver, 5).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                           self.modal_buy_css)))

    def get_make_order_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.basket_order_button_css)

    def get_show_button(self):
        return self.driver.find_element(By.XPATH, self.show_button_xp)

    # ACTIONS
    def move_slider(self, count, is_max):
        action = ActionChains(self.driver)
        if is_max:
            slider = self.get_slider_max()
            text = "максимум"
        else:
            slider = self.get_slider_min()
            text = "минимум"
        action.move_to_element(slider).perform()
        action.click_and_hold(slider).move_by_offset(count, 0).release().perform()

        print(f'Слайдер сдвинут на {count} от {text}')

    def select_option(self, option):
        self.get_select().select_by_visible_text(option)
        print("Выбрана опция: " + option)

    def click_show_button(self):
        self.get_show_button().click()
        print("Нажата кнопка Показать")

    def click_buy_button(self, product_count):
        self.get_buy_button(product_count).click()
        print(f'Нажата кнопка Купить {product_count} товар')

    def click_make_order_button(self):
        self.get_make_order_button().click()
        print("Нажата кнопка Оформить заказ")

    # METHODS
    def check_maple_section(self):
        base = Base(self.driver)
        base.assert_url(self.url)
        """ПРОВЕРКА ВСЕХ ТОВАРОВ НА СТРАНИЦЕ"""
        all_maple = self.get_all_maple()
        texts = [el.text for el in all_maple]
        assert texts == self.products, "Товары на странице не соответствуют ожидаемому: " + ", ".join(texts)
        all_articles = self.get_all_articles()
        arts = [el.text for el in all_articles]
        assert arts == self.articles, "Артикулы на странице не соответствуют ожидаемому: " + ", ".join(arts)
        pairs = []
        for text, art in zip(texts[:6], arts[:6]):
            pairs.append(f"{text} - {art}")
        print("Выбран корректный раздел, отображаются все товары: " + ", ".join(pairs))

    def check_slider_sums(self, min_expected, max_expected):
        min_actual = self.get_summ(False).text
        max_actual = self.get_summ(True).text
        assert min_actual == min_expected, "минимальная цена не соответствует ожидаемой: " + min_actual
        assert max_actual == max_expected, "максимальная цена не соответствует ожидаемой: " + max_actual
        print(f'Установлены корректные значения цены: {min_actual} - {max_actual}')

    def check_and_set_filters(self, count_max, count_min, min_expected, max_expected, option):
        self.check_maple_section()
        self.select_option(option)
        self.move_slider(count_max, True)
        self.move_slider(count_min, False)
        self.click_show_button()
        self.check_slider_sums(min_expected, max_expected)

    def buy_product_and_go_to_basket(self, product_count):
        self.click_buy_button(product_count)
        self.get_modal_buy()
        self.click_make_order_button()
