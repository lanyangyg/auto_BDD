import pytest


# Fixture: 提供购买流程事件流
@pytest.fixture
def purchase_workflow(browser):
    from workflows.purchase_workflow import PurchaseWorkflow
    return PurchaseWorkflow(browser)
