# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """所有页面对象的基类，封装了常用的 Selenium 操作方法"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """查找单个元素"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """查找多个元素"""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """点击元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_element(self, locator):
        """点击元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """在输入框中输入文本"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """获取元素文本内容，带显式等待"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element.text

    def is_element_visible(self, locator):
        """检查元素是否可见"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_present(self, locator):
        """检查元素是否存在（不一定可见）"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def wait_for_url_contains(self, text):
        """等待URL包含特定文本"""
        self.wait.until(EC.url_contains(text))

    def get_current_url(self):
        """获取当前URL"""
        return self.driver.current_url

    def navigate(self, url):
        """导航到指定URL"""
        self.driver.get(url)
