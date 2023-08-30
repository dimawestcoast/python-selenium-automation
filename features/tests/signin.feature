Feature: Sign in tests

  Scenario: Sign in page can be opened from SingIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opened

  Scenario: Amazon User see sign in button
    Given Open Amazon page
    Then Verify Sign in is clickable
    When Wait for 3 sec
    Then Verify Sign in is clickable
    Then Verify Sign In disappears