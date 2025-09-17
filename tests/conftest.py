import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from tests.fixtures.login_setup_fixture import *
# from tests.fixtures.purchase_fixture import *

# 注册模块化fixtures
pytest_plugins = ["tests.fixtures.login_setup_fixture", "tests.fixtures.purchase_fixture"]

@pytest.fixture(scope="session")
def browser():
    """提供浏览器实例的 fixture"""
    # 基础稳定性
    chrome_options = Options()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")  # 开启无痕模式
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")

    # 环境判断：CI 就跑 headless，本地就跑有头最大化
    if os.getenv("CI") == "true":
        chrome_options.add_argument("--headless=new")  # 无头模式
    else:
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
