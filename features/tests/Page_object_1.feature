# Created by oleg3 at 7/10/2020
Feature: Rewrite these scenarios to use Page Object pattern:
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Press on Amazon Orders link
    Then Verify 'Sign In' page is opened


  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Clicks on the shopping cart icon
    Then User can verify Your Amazon Cart is empty


  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click to hamburger menu
    And Click to Amazon Music menu item
    Then 6 menu items are present

