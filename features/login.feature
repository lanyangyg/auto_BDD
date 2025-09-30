Feature: User Login
  As a user
  I want to login to the website
  So that I can access inventory page

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be redirected to the home page
    And I should see a the app logo

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "testuser" and password "secret_sauce"
    And I click the login button
    Then I should see a login fail error message

  # 场景大纲(参数化测试)
  Scenario Outline: Login with different credentials
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see an expected login result "<expected_result>"

    Examples:
      | username        | password       | expected_result |
      | standard_user   | secret_sauce   | Swag Labs       |
      | user            | secret_sauce   | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.                       |