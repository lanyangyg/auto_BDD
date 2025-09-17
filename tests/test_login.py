import pytest
from pytest_bdd import scenario, given, when, then, parsers
import allure

# 场景定义（只是将测试与功能文件中的场景关联起来）
@allure.feature("Login flow")
@allure.story("1.Successful login")
@scenario("../fixtures/login.feature", "Successful login with valid credentials")
def test_successful_login():
    """这个函数体是空的，因为实际测试逻辑在步骤定义中"""
    pass

@allure.feature("Login flow")
@allure.story("2.Failed login")
@scenario("../fixtures/login.feature","Failed login with invalid credentials")
def test_failed_login():
    pass

@allure.feature("Login flow")
@allure.story("3.Login with different credentials")
@scenario("../fixtures/login.feature","Login with different credentials")
def test_login_with_different_credentials():
    pass


# 步骤定义（包含实际的测试逻辑）
@allure.step("Open login page")
@given("I am on the login page")
def get_to_login_page(login_page):
    # 这个步骤现在由 login_page fixtures 自动处理
    assert "saucedemo" in login_page.get_current_url().lower()

@allure.step('Enter credentials with username "{username}" and password "{password}"')
@when(parsers.parse('I enter username "{username}" and password "{password}"'))
def enter_credentials(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)

@allure.step("Click the login button")
@when("I click the login button")
def click_login_button(login_page):
    login_page.click_login()

@allure.step("Redirect_to_home_page")
@then("I should be redirected to the home page")
def verify_redirect_to_home_page(login_page):
    # 实现检查重定向
    # 等待URL包含特定文本
    login_page.wait_for_url_contains("inventory")
    # 断言inventory在当前URL中
    assert "inventory" in login_page.get_current_url()

@allure.step("Verify app logo")
@then("I should see a the app logo")
def verify_app_logo(login_page):
    assert "Swag Labs" in login_page.get_app_logo_message()

@allure.step("Verify error message")
@then("I should see an error message")
def verify_error_message(login_page):
    assert "Epic sadface" in login_page.get_error_message()

@allure.step("Verify expected result \"{expected_result}\" ")
@then(parsers.parse("I should see an expected result \"{expected_result}\""))
def verify_expected_result(login_page, expected_result):
    # if "inventory" in expected_result:
    #     login_page.wait_for_url_contains("inventory")
    #     assert "inventory" in login_page.get_current_url()
    # else:
    #     assert expected_result in login_page.get_error_message()
    if "Swag Labs" in expected_result:
        assert expected_result in login_page.get_app_logo_message()
    else:
        assert expected_result in login_page.get_error_message()
