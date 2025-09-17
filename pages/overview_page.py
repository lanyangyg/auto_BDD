from selenium.webdriver.common.by import By
from bases.base_page import BasePage

class OverviewPage(BasePage):
    # element locator
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    def __init__(self, driver):
        super().__init__(driver)

    def finish_checkout(self):
        # 点击完成结算
        self.click_element(self.FINISH_BUTTON)
        from pages.complete_page import CompletePage
        return CompletePage(self.driver)

    def cancel_checkout(self):
        # 点击取消结算
        self.click_element(self.CANCEL_BUTTON)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)

