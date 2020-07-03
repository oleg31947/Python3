# Created by oleg3 at 6/28/2020
Feature: Verify "Regular" text in each link
  # Enter feature description here

  Scenario: Verify "Regular" text in each link
    Given Open Amazon 'wholefoodsdeals'
    Then Each item has regular field and Product name