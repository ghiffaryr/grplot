from grplot.utils.strtoarray import strtoarray
import numpy as np
import pytest
from typing import Union

@pytest.mark.parametrize('input,expected', [
    (('asu', 'jancuk'), (np.array(['asu' for i in range(6)]), 'jancuk')),
    (([1, 2, 3], 'jancuk'), ([1, 2, 3], np.array(['jancuk' for i in range(3)]))),
    (([1, 2, 3], [1, 2, 3]), ([1, 2, 3], [1, 2, 3])) 
])
def test_strtoarray(input: tuple[Union[list, str], Union[list, str]], expected: tuple[any, any]): 
    new_array = strtoarray(*input)
    for result, expectedOutput in zip(new_array, expected):
        if type(expectedOutput) == np.ndarray:
            np.testing.assert_equal(result, expectedOutput)
        else:
            assert result == expectedOutput
