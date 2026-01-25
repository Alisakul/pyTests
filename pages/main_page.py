from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # LOCATORS
    main_logo_css = ".LogotypeRedesign_logo___F_Dq.LogotypeRedesign_miniLogoOnMobile__wE_x_"
    sofa_section_xp = "//span[contains(text(), 'Products')]"

    # GETTERS
    def get_main_logo(self):
        return WebDriverWait(self.driver, 15).until(conditions.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                              self.main_logo_css)))

    def get_sofa_section(self):
        return WebDriverWait(self.driver, 15).until(conditions.presence_of_element_located((By.XPATH,
                                                                                            self.sofa_section_xp)))

    # ACTIONS
    def check_logo(self):
        self.get_main_logo()
        print("Отображается логотип")

    def click_go_to_sofa(self):
        self.get_sofa_section().click()
        print("Нажата кнопка раздела 'Диваны и кресла'")

    # METHODS
    def go_to_sofa(self):
        """Переход в раздел 'Диваны и кресла'"""
        self.check_logo()
        self.click_go_to_sofa()
