from selenium.webdriver.common.by import By
from bases.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class InventoryPage(BasePage):
    # elements locator
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")     # 购物车图标商品数量
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")       # 购物车图标

    def __init__(self, driver):
        super().__init__(driver)

    def select_product_by_name(self, product_name):
        # 获取商品列表
        items = self.find_elements(self.PRODUCT_ITEMS)
        # 遍历商品列表
        for item in items:
            # 获取商品名称
            name = item.find_element(*self.PRODUCT_NAMES).text
            if name == product_name:
                # 点击商品
                item.find_element(*self.PRODUCT_NAMES).click()
                return ProductDetailsPage(self.driver)
        # 未找到商品时抛出异常
        raise ValueError(f"can not find product:{product_name}")

    def get_cart_item_count(self):
        # 获取购物车中商品数量
        try:
            return int(self.find_element(self.CART_BADGE).text)
        except:
            return 0

    def go_to_cart(self):
        # 前往购物车
        self.click_element(self.CART_ICON)
        from .cart_page import CartPage
        return CartPage(self.driver)

