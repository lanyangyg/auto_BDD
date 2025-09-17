from selenium.webdriver.common.by import By
from bases.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    # element locator
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container.error")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_info(self, firstname, lastname, zipcode):
        # 填写结算信息并继续到订单预览
        self.input_text(self.FIRST_NAME_FIELD, firstname)
        self.input_text(self.LAST_NAME_FIELD, lastname)
        self.input_text(self.ZIP_CODE_FIELD, zipcode)

    def continue_to_overview(self):
        # 点击继续按钮，跳转OverviewPage
        self.click_element(self.CONTINUE_BUTTON)
        from .overview_page import OverviewPage
        return OverviewPage(self.driver)

    def cancel_checkout(self):
        # 取消结算，返回CartPage
        self.click_element(self.CANCEL_BUTTON)
        from .cart_page import CartPage
        return CartPage(self.driver)

    def click_continue(self):
        # 点击继续按钮，不期望页面跳转
        self.click_element(self.CONTINUE_BUTTON)

    def checkout_info_error(self):
        # 获取错误信息
        return self.get_text(self.ERROR_MESSAGE)
