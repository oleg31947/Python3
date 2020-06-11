# Created by oleg3 at 6/10/2020
Feature: Shopping card activities
  Opens amazon.com, clicks on the cart icon
  and verifies that Your Shopping Cart is empty.

  Scenario: User is able to verify that Shopping Cart is empty.
    Given Open Amazon page
    When Clicks on the shopping cart icon
    Then Verifies that Your Amazon Cart is empty

  Scenario: User is able to add item to the shopping card.
    Given Open Amazon page
    When Search men's caps
    And Click on the item
    And Add the item to the shopping card
    Then Verify 1 items
