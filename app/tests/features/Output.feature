 # Created by Denis Havriushenko at 10/1/16  
# Created by temp at 10/1/16

Feature: Test feature 1
   Print the last five lines of a file

#  Background:
#    Given I am using the application

  Scenario Outline: Output last/first line with differen data type
    Given File with following data types <input>
    When  I use given file
    Then  I should see following <output>

    Examples:
      | input                              | output                       |
      | '1'                                | '1'                          |
      | '@#$%^&*()_'                       | '@#$%^&*()_'                 |
      | 'one'                              | 'one'                        |
      | ''                                 | ''                           |

  Scenario Outline: Output must have only 5 lines
    Given File with <lines> lines <input>
    When  I use given file
    Then  I should see <output> lines

    Examples:
      | lines      | input         | output  |
      | '0'        | 'zero'        |  1      |
      | '1'        | 'one'         |  1      |
      | '4'        | 'four'        |  4      |
      | '5'        | 'five'        |  5      |
      | '6'        |  'six'        |  5      |

  Scenario: Output 5 last lines of the file that consist of 10 lines
    Given File of '10' lines '1 2 3 4 5 6 7 8 9 10'
    When I use given file
    Then I should see '6 7 8 9 10'
