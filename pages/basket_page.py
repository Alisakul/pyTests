from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.select import Select


class BasketPage(Base):
    url = "https://www.mlesna.ru/personal/order/make/"
    card_text = "Оплатa банковской картoй на сайте"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    next_button_xp = "(//a[@class='pull-right btn btn-default btn-md'][contains(text(),'Далее')])[1]"
    delivery_checkbox_css = "#ID_DELIVERY_ID_6"
    select_delivery_css = "select[name='DELIVERY_EXTRA_SERVICES[6][2]']"
    card_payment_css = "#ID_PAY_SYSTEM_ID_24"
    name_input_css = "#soa-property-34"
    email_input_css = "#soa-property-35"
    phone_input_css = "#soa-property-36"
    comments_input_css = "#orderDescription"
    region_input_xp = "(//input[@placeholder='Введите название ...'])[2]"
    moscow_region_css = ".dropdown-item.bx-ui-sls-variant.bx-ui-sls-variant-active"

    # GETTERS
    def get_next_button(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.XPATH,
                                                                                            self.next_button_xp)))

    def get_delivery_checkbox(self):
        return (WebDriverWait(self.driver, 30).
                until(conditions.presence_of_element_located((By.CSS_SELECTOR, self.delivery_checkbox_css))))

    def get_select_delivery(self):
        return Select(WebDriverWait(self.driver, 30).
                      until(conditions.presence_of_element_located((By.CSS_SELECTOR, self.select_delivery_css))))

    def get_card_payment(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.card_payment_css)))

    def get_name_input(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.name_input_css)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.email_input_css)))

    def get_phone_input(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.phone_input_css)))

    def get_comments_input(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.comments_input_css)))

    def get_region_input(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.XPATH,
                                                                                            self.region_input_xp)))

    def get_moscow_region(self):
        return WebDriverWait(self.driver, 30).until(conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            self.moscow_region_css)))

    # ACTIONS
    def click_next_button(self):
        self.get_next_button().click()
        print("Нажата кнопка Далее")

    def set_checkbox_delivery(self):
        self.get_delivery_checkbox().click()
        print("Выбрана доставка транспортной компанией")

    def select_delivery_company(self, option):
        self.get_select_delivery().select_by_visible_text(option)
        print("Выбрана опция: " + option)

    def set_checkbox_card_pay(self):
        self.get_card_payment().click()
        print("Выбрана оплата банковской картой")

    def input_name(self, name):
        self.get_name_input().send_keys(name)
        print("Введено фио: " + name)

    def input_email(self, email):
        self.get_email_input().send_keys(email)
        print("Введен email: " + email)

    def input_phone(self, phone):
        self.get_phone_input().send_keys(phone)
        print("Введен телефон: " + phone)

    def input_comments(self, comments):
        self.get_comments_input().send_keys(comments)
        print("Введен комментарий: " + comments)

    def select_moscow_region(self):
        self.get_region_input().send_keys("Москва")
        self.get_moscow_region().click()
        print("Выбран регион: Москва")

    # METHODS
    def check_page(self):
        base = Base(self.driver)
        base.assert_url(self.url)

    def set_all_values_for_order(self, option, name, email, phone, comments):
        self.check_page()
        self.click_next_button()
        self.select_moscow_region()
        self.click_next_button()
        self.set_checkbox_delivery()
        self.select_delivery_company(option)
        self.click_next_button()
        self.set_checkbox_card_pay()
        self.click_next_button()
        self.input_name(name)
        self.input_email(email)
        self.input_phone(phone)
        self.input_comments(comments)
        base = Base(self.driver)
        base.get_screenshot()
