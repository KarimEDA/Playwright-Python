Feature: Order Transaction
  Test related to order Transaction
  Scenario Outline: Verify Order success message shown in details page:
    Given create order with <username> and <password>
    And  user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select the orderID
    Then order message is successfully displayed
    Examples:
      | username                  | password         |
      | eduardwayne1987@gmail.com | Eduardwayne1987* |