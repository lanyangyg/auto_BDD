from pytest_bdd import given, when, then, parsers
import allure

# 步骤定义
@allure.step("Logged in user")
@given("I am logged in as a standard user")
def logged_in(logged_in_standard_user):     # 使用 logged_in_standard_user fixture
    pass

@allure.step('Complete purchase for "{product_name}"')
@when(parsers.parse('I complete the purchase process for "{product_name}" with:'))
def complete_purchase_process(purchase_workflow, product_name, datatable):
    # 将数据表转换为字典
    # datatable 是一个列表，第一行是表头，第二行是数据
    headers = datatable[0]  # ['first_name', 'last_name', 'zip_code']
    data = datatable[1]     # ['John', 'Doe', '12345']
    customer_info = {
        'first_name': data[0],  # John
        'last_name': data[1],   # Doe
        'zip_code': data[2]     # 12345
    }
    # 执行购买流程并保存结果供后续步骤使用
    purchase_workflow.result = purchase_workflow.complete_purchase(product_name, customer_info)

@allure.step('Attempt to purchase for "{product_name}" but failed')
@when(parsers.parse('I attempt to complete the purchase process for "{product_name}" with invalid information'))
def attempt_complete_purchase_with_invalid_info(purchase_workflow, product_name):
    # 使用无效信息尝试购买
    invalid_info = {
        'first_name': '',
        'last_name': '',
        'zip_code': ''
    }
    # 保存结果供后续步骤使用
    purchase_workflow.result = purchase_workflow.failed_purchase_with_invalid_info(product_name, invalid_info)

@allure.step('Confirmation message "{message}"')
@then(parsers.parse('I should see the order confirmation message "{message}"'))
def verify_confirmation_message(purchase_workflow, message):
    # 验证订单确认消息
    assert purchase_workflow.result.get_confirmation_message() == message

@allure.step('Error message "{message}"')
@then("I should see a purchase error message")
def verify_error_message(purchase_workflow):
    # 验证错误消息
    assert "Error" in purchase_workflow.result

