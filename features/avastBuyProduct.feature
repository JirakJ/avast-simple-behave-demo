# Created by jirakj at 14.07.2021
Feature: Buy
  # Just example test how we can use behave to buy Avast products
  Background:
    Given launch chrome browser
    When open avast homepage
    Then close cookie modal by click on OK
    Then go to eshop page

  Scenario Outline: Avast Ultimate Edition By Payment Card
    Then choose just for one PC in <cell>
    And click on buy in <cell>
    Then fill <name>, <surname> and <email>
#    And select payment card as payment method #default option
    And click on continue
    Then fill in <cardNumber>, <expireMonth>, <expireYear>, <cvv>
    #    And click on pay button
    Then close browser

    Examples: Ultimate Security Edition
      | cell | name | surname | email | cardNumber | expireMonth | expireYear | cvv |
      | 4 | Karel | Tester | karel.prochazka@text.com | 1111 2222 3333 4444 | 07 | 22 | 705 |
      | 4 | Martin | Tester | martin.jirman@text.com | 5555 2222 3333 4444 | 02 | 24 | 425 |

  Scenario Outline: Avast Premium Security Edition By Payment Card
    Then choose just for one PC in <cell>
    And click on buy in <cell>
    Then fill <name>, <surname> and <email>
#    And select payment card as payment method #default option
    And click on continue
    Then fill in <cardNumber>, <expireMonth>, <expireYear>, <cvv>
    #    And click on pay button
    Then close browser

    Examples: Premium Security Edition
      | cell | name | surname | email | cardNumber | expireMonth | expireYear | cvv |
      | 3 | Karel | Tester | karel.prochazka@text.com | 1111 2222 3333 4444 | 07 | 22 | 705 |
      | 3 | Martin | Tester | martin.jirman@text.com | 5555 2222 3333 4444 | 02 | 24 | 425 |