# Created by temp at 10/1/16

Feature: Output of last 5 lines from input file
   Print the last five lines of a file

   Scenario Outline: Output 5 last lines of the file
    Given File with following lines <input>
    When  I use given file
    Then  I should see following <output>

    Examples:
      | input                              | output                       |
      | '1'                                | '1'                          |
      | 'one\ntwo\nthree\nfour\nfive'      | 'one\ntwo\nthree\nfour\nfive'|
      | 'one\ntwo\nthree\nfour\nfive\nsix' | 'two\nthree\nfour\nfive\nsix'|
      | 'one\ntwo\nthree\nfour'            | 'one\ntwo\nthree\nfour'      |
      | 'one'                              | 'one'                        |
      | ''                                 | ''                           |
      | '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'  | '6\n7\n8\n9\n10\n'           |
