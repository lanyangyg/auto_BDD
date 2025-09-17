from selenium.webdriver.common.by import By
from bases.base_page import BasePage

class CompletePage(BasePage):
    # element locator
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)


    # 用于断言是否已经完成checkout
    def get_confirmation_message(self):
        # 获取确认消息
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self):
        # 获取完成文本
        return self.get_text(self.COMPLETE_TEXT)

    def back_to_home(self):
        # 返回首页
        self.click_element(self.BACK_HOME_BUTTON)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)
