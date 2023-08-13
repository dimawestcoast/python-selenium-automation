# Created by pfsnewsystem at 8/12/2023
Feature: Tests for amazon search
  # Enter feature description here

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct