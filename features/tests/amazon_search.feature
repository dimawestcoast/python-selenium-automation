# Created by pfsnewsystem at 8/12/2023
Feature: Tests for amazon search
  # Enter feature description here

#  Scenario: Verify that a user can search for a table
#    Given Open Amazon page
#    When Search for table
#    Then Verify search result is "table"

#  Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for cup
#    Then Verify search result is "cup"

#  Scenario Outline: Verify that a user can search for a product
#    Given Open Amazon page
#    When Search for <search_word>
#    Then Verify search result is <search_result>
#    Examples:
#    |search_word    |search_result   |
#    |cup            |"cup"           |
#    |dress          |"dress"         |

#  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
#    Given Open Amazon page
#    When User clicks on returns and orders
#    Then Verify user see sign in option

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for dell computer
    When Click on the first product
    When Click on Add to cart button
#    When Open cart page
    Then Verify cart has 1 item(s)