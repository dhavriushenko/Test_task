 # Created by Denis Havriushenko at 10/1/16  
  
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
