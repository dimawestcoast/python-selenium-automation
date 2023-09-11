# Created by pfsnewsystem at 8/21/2023
Feature: Tests for main page UI


  Scenario: Verify that footer has correct amount of links
    Given Open amazon page
    Then Verify footer has 35 links

  Scenario: Verify that footer has many links
    Given Open amazon page
    Then Verify many link are shown in the footer

  Scenario: Verify there are 5 links on the amazon bestsellers page
    Given Open Amazon page
    When User clicks on bestsellers page
    Then Verify there are 5 links on the page

  Scenario:  User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present
