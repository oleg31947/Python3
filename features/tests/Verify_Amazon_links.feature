# Created by oleg3 at 6/16/2020
Feature: Verify links
  # Enter feature description here

  Scenario: Verify 5 Amazon links in the header
    Given Open Amazon best sellers page
    Then Verify 5 Amazon links