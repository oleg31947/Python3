# Created by oleg3 at 7/3/2020
Feature: Verify Best sellers links and others links in the bloc in Amazon page
  # Enter feature description here

  Scenario: Verify Best sellers and others links
    Given Open Amazon page
    When Press on the name_button button
    Then Verify Best sellers and others links
