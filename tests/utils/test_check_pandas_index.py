from unittest import result
import pandas as pd
from grplot.utils.check_pandas_index import check_pandas_index
import pytest
import numpy

df_columns = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).columns

@pytest.mark.parametrize('test_input,expected', [
    ((pd.Index([1, 2, 3]), pd.Index([1, 2, 3])), (pd.core.indexes.numeric.Int64Index, pd.core.indexes.numeric.Int64Index)),
    ((df_columns, df_columns), (numpy.ndarray, numpy.ndarray))
])
def test_check_pandas_index(test_input: tuple, expected: any) -> None:
   result = check_pandas_index(test_input[0], test_input[1])
   for input, output in zip(result, expected):
       assert type(input) is output