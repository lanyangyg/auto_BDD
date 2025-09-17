from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
import allure

class PurchaseWorkflow:
    """封装完整购买流程的事件流"""

    def __init__(self, driver):
        self.driver = driver
        self.inventory_page = InventoryPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.overview_page = OverviewPage(driver)
        self.complete_page = CompletePage(driver)

    @allure.step("PurchaseWorkflow--Complete purchase")
    def complete_purchase(self, product_name, customer_info):
        """
        执行完整的购买流程

        Args:
            product_name: 要购买的商品名称
            customer_info: 客户信息字典，包含first_name, last_name, zip_code

        Returns:
            CompletePage: 订单完成页面对象
        """
        # 1. 选择商品
        self.inventory_page.select_product_by_name(product_name)
        # 2. 添加到购物车并返回商品列表页面
        self.product_details_page.add_to_cart_from_product_detail()
        self.product_details_page.back_to_inventory()
        # 3. 前往购物车
        self.inventory_page.go_to_cart()
        # 4. 进行结算
        self.cart_page.start_checkout()
        # 5. 填写结算信息并继续到订单预览
        self.checkout_page.fill_info(
            customer_info['first_name'],
            customer_info['last_name'],
            customer_info['zip_code']
        )
        self.checkout_page.continue_to_overview()
        # 6. 完成订单
        self.overview_page.finish_checkout()
        return self.complete_page


    # def complete_purchase_with_validation(self, product_name, customer_info, expected_message):
    #     """
    #     执行完整购买流程并进行验证
    #
    #     Args:
    #         product_name: 要购买的商品名称
    #         customer_info: 客户信息字典
    #         expected_message: 预期的确认消息
    #
    #     Returns:
    #         bool: 购买是否成功
    #     """
    #     complete_page = self.complete_purchase(product_name, customer_info)
    #     # 验证确认消息
    #     actual_message = complete_page.get_confirmation_message()
    #     if actual_message != expected_message:
    #         raise AssertionError(f"Expected message: '{expected_message}', but got: '{actual_message}'")
    #     # 验证页面状态
    #     if "complete" not in self.driver.current_url:
    #         raise AssertionError("Not on complete page after purchase")
    #     return True

    @allure.step("PurchaseWorkflow--Failed purchase")
    def failed_purchase_with_invalid_info(self, product_name, customer_info):
        """
        执行完整购买流程并验证错误信息

        Args:
            product_name: 要购买商品名称
            customer_info: 客户信息字典

        Returns:
            checkout_info_error: 错误消息
        """
        # 1. 选择商品
        self.inventory_page.select_product_by_name(product_name)
        # 2. 添加到购物车并返回商品列表页面
        self.product_details_page.add_to_cart_from_product_detail()
        self.product_details_page.back_to_inventory()
        # 3. 前往购物车
        self.inventory_page.go_to_cart()
        # 4. 进行结算
        self.cart_page.start_checkout()
        # 5.填写无效信息
        self.checkout_page.fill_info(
            customer_info['first_name'],
            customer_info['last_name'],
            customer_info['zip_code']
        )
        # 6. 尝试继续到订单预览
        self.checkout_page.continue_to_overview()
        # 返回错误消息文本
        return self.checkout_page.checkout_info_error()
