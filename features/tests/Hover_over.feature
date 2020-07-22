# Created by oleg3 at 7/21/2020
Feature: Users able to hover over
  # Enter feature description here

  Scenario: Users can hover over New Arrivals
    Given Open Amazon gp/product/B074TBCSC8 page
    When Hover over to New Arrivals button
    Then Verify selection tooltip is shown
#