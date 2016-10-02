# Created by temp at 10/1/16

Feature: Test feature
   Print the last five lines of a file

  Background:
    Given I am using the application

  Scenario: Output 5 last lines of the file that consist of 5 lines
    Given File with 5 lines
    When I use given file with following lines
         """one\ntwo\nthree\nfour\nfive"""
    Then I should see following output:
         """one\ntwo\nthree\nfour\nfive"""

  Scenario: Output 5 last lines of the file that consist of >5 lines
    Given File with 6 lines
    When I use given file with following lines
         """one\ntwo\nthree\nfour\nfive\nsix"""
    Then I should see following output:
         """two\nthree\nfour\nfive\nsix"""

  Scenario: Output 5 last lines of the file that consist of <5 lines
    Given File with 4 lines
    When I use given file with following lines
         """one\ntwo\nthree\nfour"""
    Then I should see following output:
         """one\ntwo\nthree\nfour"""