# -*- coding: utf-8 -*-

import sys, os
from nose.tools import assert_equals
from lettuce import *
#from tempfile import NamedTemporaryFile
#only if ypu do not set PYTHONPATH
sys.path.insert(1,'/Users/temp/PycharmProjects/Test_task/')
from app.FileOutput import Output

get_current_path = os.path.dirname(os.path.abspath(__file__))

@step(u'I am using the application')
def given_a_working_application(step):
    print("Attempting to use application...")
    world.app = Output()


@step(u'File with following data types \'(.*)\'')
def given_test_file(step, input):
    with open(world.path,'w') as inf:
        inf.write(bytes(input))


@step(u'I use given file')
def given_i_input_test_file(step):
    world.app = Output()
    world.result = world.app.outputlast5lines(world.path, 5)


@step(u'I should see following \'(.*)\'')
def result(step, expected_result):
    actual_result = world.result
    assert_equals(expected_result, actual_result)


@step(u'File with \'(.*)\' lines \'(.*)\'')
def given_test_file(step, line, input):
    with open(world.path,'w') as inf:
        i=1
        j=int(line)
        while j >= i:
            if j == i:
                inf.writelines([input])
            else:
                inf.write(input)
                inf.write('\n')
            i+=1

@step(u'I use given file')
def given_i_input_test_file(step):
    world.app = Output()
    world.result = world.app.outputlast5lines(world.path, 5)


@step(u'I should see (.*) lines')
def result(step, expected_result):
    result = world.result
    actual_result = len(result.split('\n'))
    assert_equals(int(expected_result), actual_result)

