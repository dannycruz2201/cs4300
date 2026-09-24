"""
Test file for Task 6: Word Counter

This file contains pytest tests to verify the word counting functionality.
Run with: pytest tests/test_task6.py -v
"""

import pytest
import sys
import os

# Add the src directory to Python's path so we can import task modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the function to test from task6.py
from task6 import count_words


class TestCountWords:
    """
    Test for the count_words() function.
    
    """
    
    def test_count_words_returns_integer(self):
        """
        Test that count_words returns an integer value.
        """
        result = count_words()
        assert isinstance(result, int)
    
    def test_count_words_returns_positive_value(self):
        """
        Test that count_words returns a positive number.
        """
        result = count_words()
        assert result > 0
    
    def test_count_words_expected_count(self):
        """
        Test that count_words returns the expected word count.
        """
        result = count_words()
        expected_count = 104 
        
        assert result == expected_count, (
            f"Expected {expected_count} words, but got {result}. "
            f"Reading 'src/task6_read_me.txt' and counting words."
        )
    
    def test_count_words_consistency(self):
        """
        Test that count_words returns the same result on multiple calls.
        
        This verifies the function is deterministic.
        """
        result1 = count_words()
        result2 = count_words()
        assert result1 == result2, "count_words should return consistent results"


if __name__ == "__main__":
    # This allows running the tests directly with: python tests/test_task6.py
    pytest.main([__file__, "-v"])