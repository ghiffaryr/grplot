from grplot.utils.check_axes import check_axes
import pytest

@pytest.mark.parametrize("input,expected", [
    ((1, 2, None, None), (1, 1)),
    ((1, [1, 2, 3], None, None), (2, 2)),
    (([1, 2, 3], 1, None, None), (2, 2)),
    (([1, 2, 3], 1, 1, 2), (1, 2))
])
def test_check_axes(input: tuple[any, any, any, any], expected: tuple[int, int]):
    axes = check_axes(*input)
    assert axes == expected