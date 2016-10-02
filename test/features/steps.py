import os ,sys
from nose.tools import assert_equals
from lettuce import step, world
sys.path.insert(1,'/Users/temp/PycharmProjects/Test_task/')
from  app.FileOutput import Output

get_current_path = os.path.dirname(os.path.abspath(__file__))

@step(u'I am using the application')
def given_a_working_application(step):
    print('Attempting to use application...')
    world.app = Output()

@step(u'I input file with 7 lines "(\d+)"')
def given_i_input_test_file(step):
    test_file = get_current_path + '/test_input7_lines.txt'
    world.result = world.app.outputlast5lines(test_file,5)

@step(u'I see output of "([^"]+)"')
def result(step, expected_result):
    actual_result = world.result
    assert_equals(expected_result, actual_result)
