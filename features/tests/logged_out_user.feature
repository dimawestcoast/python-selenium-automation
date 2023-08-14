# Created by pfsnewsystem at 8/12/2023
Feature: Tests for logged out user

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When User clicks on returns and orders
    Then Verify user see sign in option


