from selenium.webdriver.common.by import By
from bases.base_page import BasePage

class CartPage(BasePage):
    # element locator
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def start_checkout(self):
        # 进行结算
        self.click_element(self.CHECKOUT_BTN)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def get_cart_items(self):
        # 获取购物车中的所有商品
        return self.driver.find_elements(self.CART_ITEMS)

    def get_item_names(self):
        # 获取购物车中所有商品的名称
        # items = self.get_cart_items()
        # return [item.find_element(*self.ITEM_NAME).text for item in items]
        items = self.get_cart_items()
        item_names = []
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            item_names.append(name)
        return item_names
