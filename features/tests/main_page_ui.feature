# Created by pfsnewsystem at 8/21/2023
Feature: Tests for main page UI
  # Enter feature description here

  Scenario: Verify that footer has correct amount of links
    Given Open amazon page
    Then Verify footer has 35 links

  Scenario: Verify that footer has many links
    Given Open amazon page
    Then Verify many link are shown in the footer