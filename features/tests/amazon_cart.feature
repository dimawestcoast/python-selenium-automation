# Created by pfsnewsystem at 8/13/2023
Feature: amazon cart

  Scenario: Verify that Your Amazon Cart is empty when clicking on the cart icon
    Given Open Amazon page
    When Clicking on cart icon
    Then Verify cart if empty