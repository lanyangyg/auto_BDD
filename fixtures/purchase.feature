Feature: Complete Purchase Process
  As a logged-in user
  I want to complete a purchase from product selection to order confirmation
  So that I can buy products from the website

  Background:
    Given I am logged in as a standard user

  Scenario: Successful purchase of a single product
    When I complete the purchase process for "Sauce Labs Backpack" with:
      | first_name | last_name | zip_code |
      | John       | Doe       | 12345    |
    Then I should see the order confirmation message "Thank you for your order!"


  Scenario Outline: Purchase different products
    When I complete the purchase process for "<product_name>" with:
      | first_name | last_name | zip_code |
      | John       | Doe       | 12345    |
    Then I should see the order confirmation message "Thank you for your order!"

    Examples:
      | product_name            |
      | Sauce Labs Backpack     |
      | Sauce Labs Bike Light   |
      | Sauce Labs Bolt T-Shirt |


  Scenario: Failed purchase with invalid information
    When I attempt to complete the purchase process for "Sauce Labs Backpack" with invalid information
    Then I should see an error message