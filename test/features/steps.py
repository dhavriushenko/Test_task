from lettuce import *
from nose.tools import assert_equals
from app.FileOutput import Output



@step(u'I am using the application')
def given_a_working_application(step):
    print('Attempting to use application...')
    world.app= Output()


#@step(u'I input file with 7 lines')
#def given_i_input_group1_add_group1(step, x, 5):
#    world.result = world.calc.add(int(x), int(y))
