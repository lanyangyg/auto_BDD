from selenium.webdriver.common.by import By
from bases.base_page import BasePage


class LoginPage(BasePage):
    """登录页面对象，封装了登录页面的所有元素和操作"""
    # element locator
    USERNAME_FIELD = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        # 输入用户名
        self.input_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        # 输入密码
        self.input_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        # 点击登录按钮
        self.click_element(self.LOGIN_BUTTON)

    def get_app_logo_message(self):
        # 获取登录成功后看到app logo
        return self.get_text(self.APP_LOGO)

    def get_error_message(self):
        # 获取错误消息
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_message_visible(self):
        # 检查错误消息是否可见
        return self.is_element_visible(self.ERROR_MESSAGE)

    def login(self, username, password):
        # 执行完整登录操作
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
