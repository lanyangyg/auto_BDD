import pytest


# Fixture: 提供登录页面对象
@pytest.fixture(scope="function")
def login_page(browser):
    """提供一个未登录页面对象的 fixtures"""
    from pages.login_page import LoginPage
    page = LoginPage(browser)
    page.navigate("https://www.saucedemo.com/")
    return page


# Fixture: 提供标准用户登录
@pytest.fixture
def logged_in_standard_user(login_page):
    login_page.login("standard_user", "secret_sauce")
    # 确保在库存页面
    assert "inventory" in login_page.driver.current_url
    return login_page


