#Author: ArunkumarS

Feature: Trello Assignment
  Scenario Outline: Login to Trello
    Given I launch the trello website
    And I login to the application arunreigns169@gmail.com and test@123#
    When The login is done new board is getting created <boardName>
    And Im checking whether the board is ready 
    Then I create a four new lists
    And I create a four new cards under a newly created list
    Then Im moving card two to the list inprogress
    And Im moving card three to the list QA
    And Im moving card two from inprogress to the list QA
    And Im opening card one and assigning it to current user
    Then Im leaving a comment on card one <comments>
    Examples:
      | boardName | comments|
      | project   | I am done|
