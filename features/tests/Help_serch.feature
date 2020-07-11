# Created by oleg3 at 6/2/2020
Feature: Help search
  # Enter feature description here

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help page
    When Use Find more solutions field and search for Cancel order
    And Click Go
    Then Check that Cancel Items or Orders text is present

