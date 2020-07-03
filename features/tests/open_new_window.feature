# Created by oleg3 at 7/1/2020
Feature: Open and change windows
  # Enter feature description here

  Scenario: User can open and close Today's deals under $25
    Given Open Amazon page
    When Store original windows
    And Click to open See more from Gift finder
#    And Switch to the newly opened window
#    Then Today's Deals are shown
#    [Add steps to put any product into a cart]
#    And User can close new window and switch back to original
#    [Add a step to refresh the page]
#    [Add a step to verify cart has 1 item]
