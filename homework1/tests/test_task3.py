import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task3 import greet, check_number, get_first_n_primes, sum_to_n

def test_greet_output(capsys):
    # Call the function that prints text
    greet("Danny")

    # Capture stdout and stderr
    captured = capsys.readouterr()

    # Verify the output by using the assert statement
    assert captured.out == "Hello, Danny\n"

# Tests for check_number

def test_check_positive():
    # TODO: Test check_number with a positive number
    # The result should be "positive"
    assert check_number(5) == "positive"

def test_check_negative():
    # TODO: Test check_number with a negative number
    # The result should be "negative"
    assert check_number(-5) == "negative"


def test_check_zero():
    # TODO: Test check_number with zero
    # The result should be "zero"
    assert check_number(0) == "zero"

# Tests for get_first_n_primes

def test_first_10_primes():
    # Complete: Test that get_first_n_primes(10) returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert get_first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Tests for sum_to_n

def test_sum_to_100():
    # Test that sum_to_n(100) returns 5050 (sum of 1 to 100 using while loop)
    assert sum_to_n(100) == 5050
