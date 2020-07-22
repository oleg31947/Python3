# Created by oleg3 at 7/20/2020
Feature: User can select Baby department
  # Enter feature description here

  Scenario: User can select Baby department
    Given Open Amazon page
    When Select baby-products department
    And Search Toys
    Then Baby department was selected
