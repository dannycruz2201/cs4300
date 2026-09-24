import pytest
import sys
import os
import numpy as np

# Add the src directory to Python's path so we can import task modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the function to test from task7.py file
from task7 import scale_and_offset_signal

"""
Test file for Task 7: Scale and Offset Signal
This file contains pytest tests to verify the scale_and_offset_signal functionality, which utlizes numpy installed
with pip install numpy then imported numpy as np
"""

class TestScaleAndOffsetSignal:
    """
    Test cases for the scale_and_offset_signal() function.
    
    The function should take:
    - data: a numpy array
    - scale_factor: a scalar to multiply each element by
    - offset: a scalar to add to each element
    
    And return: (data * scale_factor) + offset
    """
    
    def test_scale_and_offset_signal_returns_array(self):
        """
        Test that scale_and_offset_signal returns a numpy array.
        """
        data = np.array([1, 2, 3, 4, 5])
        result = scale_and_offset_signal(data, 2.0, 1.0)
        assert isinstance(result, np.ndarray)
    
    
    def test_scale_and_offset_signal_simple_case(self):
        """
        Test scale and offset with simple integer values.
        
        Input: [1, 2, 3] with scale=2 and offset=1
        Expected: [1*2+1, 2*2+1, 3*2+1] = [3, 5, 7]
        """
        data = np.array([1, 2, 3])
        result = scale_and_offset_signal(data, 2, 1)
        expected = np.array([3, 5, 7])
        np.testing.assert_array_equal(result, expected)
    
    
    def test_scale_factor_of_one_no_offset(self):
        """
        Test with scale factor of 1 and offset of 0.
        Should return the original array unchanged.
        """
        data = np.array([10, 20, 30, 40])
        result = scale_and_offset_signal(data, 1, 0)
        np.testing.assert_array_equal(result, data)
    
  
    def test_negative_scale_factor(self):
        """
        Test with a negative scale factor.
        
        Input: [1, 2, 3, 4] with scale=-1 and offset=0
        Expected: [-1, -2, -3, -4]
        """
        data = np.array([1, 2, 3, 4])
        result = scale_and_offset_signal(data, -1, 0)
        expected = np.array([-1, -2, -3, -4])
        np.testing.assert_array_equal(result, expected)
    
    def test_negative_offset(self):
        """
        Test with a negative offset.
        
        Input: [5, 10, 15] with scale=1 and offset=-5
        Expected: [0, 5, 10]
        """
        data = np.array([5, 10, 15])
        result = scale_and_offset_signal(data, 1, -5)
        expected = np.array([0, 5, 10])
        np.testing.assert_array_equal(result, expected)
        
    def test_float_scale_and_offset(self):
        """
        Test with floating point scale and offset values.
        
        Input: [1.0, 2.0, 3.0] with scale=0.5 and offset=10.0
        Expected: [10.5, 11.0, 11.5]
        """
        data = np.array([1.0, 2.0, 3.0])
        result = scale_and_offset_signal(data, 0.5, 10.0)
        expected = np.array([10.5, 11.0, 11.5])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_empty_array(self):
        """
        Test with an empty array.
        """
        data = np.array([])
        result = scale_and_offset_signal(data, 2, 1)
        assert len(result) == 0
        assert isinstance(result, np.ndarray)
    
    def test_single_element_array(self):
        """
        Test with a single element array.
        
        Input: [42] with scale=3 and offset=8
        Expected: [42*3+8] = [134]
        """
        data = np.array([42])
        result = scale_and_offset_signal(data, 3, 8)
        expected = np.array([134])
        np.testing.assert_array_equal(result, expected)
    
   
    def test_2d_array(self):
        """
        Test with a 2D array (matrix).
        
        Input: [[1, 2], [3, 4]] with scale=2 and offset=1
        Expected: [[3, 5], [7, 9]]
        """
        data = np.array([[1, 2], [3, 4]])
        result = scale_and_offset_signal(data, 2, 1)
        expected = np.array([[3, 5], [7, 9]])
        np.testing.assert_array_equal(result, expected)
    
   
    def test_original_data_unchanged(self):
        """
        Test that the original data array is not modified.
        """
        original = np.array([1, 2, 3])
        original_copy = original.copy()
        result = scale_and_offset_signal(original, 2, 1)
        np.testing.assert_array_equal(original, original_copy)


if __name__ == "__main__":
    # This allows running the tests directly with: python tests/test_task7.py from terminal
    pytest.main([__file__, "-v"])