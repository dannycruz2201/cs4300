import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task4 import calculate_discount

def test_calculate_discount_with_integers():
    """Test calculate_discount with integer price and discount."""
    result = calculate_discount(100, 20)
    assert result == 80.0


def test_calculate_discount_with_float_price():
    """Test calculate_discount with float price and integer discount."""
    result = calculate_discount(99.99, 10)
    assert round(result, 2) == 89.99


def test_calculate_discount_with_float_discount():
    """Test calculate_discount with integer price and float discount."""
    result = calculate_discount(50, 12.5)
    assert result == 43.75


def test_calculate_discount_zero_discount():
    """Test calculate_discount with zero discount."""
    result = calculate_discount(100, 0)
    assert result == 100.0


def test_calculate_discount_hundred_percent():
    """Test calculate_discount with 100% discount (free item)."""
    result = calculate_discount(100, 100)
    assert result == 0.0


def test_calculate_discount_with_both_floats():
    """Test calculate_discount with both price and discount as floats."""
    result = calculate_discount(49.99, 25.5)
    # 49.99 * (1 - 0.255) = 49.99 * 0.745 = 37.24255
    assert round(result, 2) == 37.24
