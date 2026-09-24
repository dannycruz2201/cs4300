import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import task2

def test_integer_data_type():
    result = task2.get_integer()
    # Verify the value matches
    assert result == 42
    # Verify the data type is explicitly an integer
    assert isinstance(result, int)

def test_float_data_type():
    result = task2.get_float()
    assert result == 3.14
    assert isinstance(result, float)

def test_string_data_type():
    result = task2.get_string()
    assert result == "Python"
    assert isinstance(result, str)

def test_boolean_data_type():
    result = task2.is_active()
    assert result is True
    assert isinstance(result, bool)