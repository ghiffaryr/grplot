from grplot.utils.scientific_superscript import scientific_superscript
import pytest

@pytest.mark.parametrize('input,expected', [
    ([1000], '1.0×10$³$'),
    ([1000, 1, 2], '10.0×10$²$'),
    ([1000, 1, -4], '10000000.00000000×10$⁻⁴$'),
    ([1000, 1, 5], '0.0×10$⁵$')
])
def test_scientific_superscript(input: list[any], expected: str):
    assert scientific_superscript(*input) == expected