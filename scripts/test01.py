import pytest,allure
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("我是测试步骤名称")
def test_001():
    allure.attach("我是测试步骤内容","附件名称")
@allure.severity(allure.severity_level.BLOCKER)
def test_002():
    assert False
