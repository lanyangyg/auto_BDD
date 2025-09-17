from selenium.webdriver.common.by import By
from bases.base_page import BasePage


class ProductDetailsPage(BasePage):
    # elements locator
    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_details_name')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart')
    SHOPPING_CART_BTN = (By.CSS_SELECTOR, '.shopping_cart_link')
    BACK_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart_from_product_detail(self):
        # 点击添加到购物车
        self.click_element(self.ADD_TO_CART_BTN)

    def back_to_inventory(self):
        # 点击返回
        self.click_element(self.BACK_BUTTON)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def from_details_navigate_to_cart(self):
        # 点击购物车
        self.click_element(self.SHOPPING_CART_BTN)
        from .cart_page import CartPage
        return CartPage(self.driver)

