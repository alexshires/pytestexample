"""
Pytest file
"""

import json

import pytest

from testdemo.example import ClassToTest
from testdemo.example import function_to_test

DATA_FILE = "test/data/data.json"


def test_example():
    """
    test the function
    :return:
    """
    res = function_to_test()
    assert (res == "Hello World")


def test_class():
    """
    test class
    :return:
    """
    c = ClassToTest()
    res = c.class_function()
    assert (res == "class function")


@pytest.mark.parametrize("input_val,output_val", ([1, 2], [2, 3]))
def test_to_param(input_val, output_val):
    """
    test params
    :return:
    """
    assert input_val + 1 == output_val


def test_data():
    """
    test data file
    :return:
    """
    with open(DATA_FILE) as f:
        data_json = json.load(f)
        assert (True)
