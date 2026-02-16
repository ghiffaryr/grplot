"""
Unit tests for grplot.utils module.

Tests utility functions including data structure validation, string manipulation,
and formatting helpers.
"""
import pytest
import numpy as np
from grplot.utils.strtoarray import strtoarray
from grplot.utils.check_axes import check_axes
from grplot.utils.scientific_superscript import scientific_superscript
from grplot.utils.trim_to_3_nonzero_after_decimal import trim_to_3_nonzero_after_decimal


class TestStrToArray:
    """Tests for strtoarray function"""
    
    def test_string_x_to_array(self):
        """Test converting string x to array"""
        x = "test"
        y = [1, 2, 3, 4, 5]
        result_x, result_y = strtoarray(x, y)
        
        assert isinstance(result_x, np.ndarray)
        assert len(result_x) == len(y)
        assert all(result_x == "test")
        assert result_y == y
    
    def test_string_y_to_array(self):
        """Test converting string y to array"""
        x = [1, 2, 3, 4, 5]
        y = "test"
        result_x, result_y = strtoarray(x, y)
        
        assert isinstance(result_y, np.ndarray)
        assert len(result_y) == len(x)
        assert all(result_y == "test")
        assert result_x == x
    
    def test_both_arrays(self):
        """Test when both inputs are already arrays"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        result_x, result_y = strtoarray(x, y)
        
        assert result_x == x
        assert result_y == y
    
    def test_numpy_arrays(self):
        """Test with numpy arrays"""
        x = np.array([1, 2, 3])
        y = np.array([4, 5, 6])
        result_x, result_y = strtoarray(x, y)
        
        np.testing.assert_array_equal(result_x, x)
        np.testing.assert_array_equal(result_y, y)


class TestCheckAxes:
    """Tests for check_axes function"""
    
    def test_both_none_single_values(self):
        """Test with single values and Nx, Ny as None"""
        x = 1
        y = 2
        Nx, Ny = check_axes(x, y, None, None)
        
        assert Nx == 1
        assert Ny == 1
    
    def test_both_none_two_elements(self):
        """Test with 2 elements"""
        x = [1, 2]
        y = [3, 4]
        Nx, Ny = check_axes(x, y, None, None)
        
        assert Nx == 2
        assert Ny == 1
    
    def test_both_none_more_than_two(self):
        """Test with more than 2 elements"""
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        Nx, Ny = check_axes(x, y, None, None)
        
        assert Nx == 2
        assert Ny == 3  # ceil(5/2)
    
    def test_explicit_nx_ny(self):
        """Test with explicit Nx and Ny"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        Nx, Ny = check_axes(x, y, 3, 2)
        
        assert Nx == 3
        assert Ny == 2
    
    def test_numpy_arrays(self):
        """Test with numpy arrays"""
        x = np.array([1, 2, 3, 4])
        y = np.array([5, 6, 7, 8])
        Nx, Ny = check_axes(x, y, None, None)
        
        assert Nx == 2
        assert Ny == 2
    
    def test_unequal_lengths(self):
        """Test with different length arrays"""
        x = [1, 2, 3]
        y = [1, 2, 3, 4, 5]
        Nx, Ny = check_axes(x, y, None, None)
        
        assert Nx == 2
        assert Ny == 3


class TestScientificSuperscript:
    """Tests for scientific_superscript function"""
    
    def test_basic_conversion(self):
        """Test basic scientific notation conversion"""
        result = scientific_superscript(1000, digits=1)
        assert '×10' in result
        assert '³' in result or '3' in result
    
    def test_negative_exponent(self):
        """Test with negative exponent"""
        result = scientific_superscript(0.001, digits=1)
        assert '×10' in result
        assert '⁻' in result or '-' in result
    
    def test_custom_digits(self):
        """Test with custom precision"""
        result = scientific_superscript(1234.567, digits=2)
        assert '×10' in result
        assert '1.23' in result or '12.3' in result
    
    def test_zero_value(self):
        """Test with zero"""
        result = scientific_superscript(0, digits=1)
        assert '0' in result
    
    def test_custom_exp(self):
        """Test with custom exponent"""
        result = scientific_superscript(1000, digits=1, exp='2')
        assert '×10' in result


class TestTrimTo3NonzeroAfterDecimal:
    """Tests for trim_to_3_nonzero_after_decimal function"""
    
    def test_trim_simple_decimal(self):
        """Test trimming simple decimal"""
        result = trim_to_3_nonzero_after_decimal(1.23456789)
        assert isinstance(result, str)
        # Should trim to 3 nonzero decimals
    
    def test_trim_with_leading_zeros(self):
        """Test with leading zeros after decimal"""
        result = trim_to_3_nonzero_after_decimal(0.0001234)
        assert isinstance(result, str)
    
    def test_integer_value(self):
        """Test with integer value"""
        result = trim_to_3_nonzero_after_decimal(5.0)
        assert isinstance(result, str)
    
    def test_negative_value(self):
        """Test with negative value"""
        result = trim_to_3_nonzero_after_decimal(-1.23456)
        assert isinstance(result, str)
        assert '-' in result


@pytest.mark.unit
class TestCheckPandasIndex:
    """Tests for check_pandas_index function"""
    
    def test_with_dataframe(self, sample_dataframe):
        """Test with a pandas DataFrame"""
        from grplot.utils.check_pandas_index import check_pandas_index
        import pandas as pd
        
        # Create index data
        x_index = sample_dataframe.index
        y_index = sample_dataframe.index
        
        result_x, result_y = check_pandas_index(x_index, y_index)
        assert result_x is not None
        assert result_y is not None


@pytest.mark.unit
class TestFirstValidIndex:
    """Tests for first_valid_index function"""
    
    def test_first_valid_basic(self):
        """Test finding first valid index"""
        from grplot.utils.first_valid_index import first_valid_index
        import pandas as pd
        
        series = pd.Series([None, None, 1, 2, 3])
        result = first_valid_index(series)
        assert result is not None


@pytest.mark.unit
class TestCheckDataStructure:
    """Tests for check_data_structure function"""
    
    def test_check_dataframe(self, sample_dataframe):
        """Test checking DataFrame structure"""
        from grplot.utils.check_data_structure import check_data_structure
        # This should not raise an error
        check_data_structure(sample_dataframe)
