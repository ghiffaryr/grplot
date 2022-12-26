from matplotlib.figure import Figure
from grplot.features.pad.check_pad import check_pad
import pytest
import matplotlib.pyplot as plt


@pytest.fixture
def figure():
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(range(10), label='A simple plot')
    fig.canvas.draw()
    yield fig
    plt.close()


class TestCheckPad:
    @pytest.mark.parametrize('input, expected', [
        ({"wpad": 1.5, "hpad": None, "pad": None}, 'hpad argument must not be None!'),
        ({"wpad": None, "hpad": 1.5, "pad": None}, 'wpad argument must not be None!')
    ])
    def test_h_or_w_pad_is_none(self, figure: Figure, input, expected):
        with pytest.raises(Exception) as exc_info:
            check_pad(figure, **input)

        str(exc_info.value) == expected

    @pytest.mark.parametrize('input', [
        ({"wpad": 1.5, "hpad": 1.5, "pad": None}),
        ({"wpad": None, "hpad": None, "pad": 0.5}),
        ({"wpad": None, "hpad": None, "pad": None}),
    ])
    def test_test_no_error(self, figure: Figure, input):
        try:
            check_pad(figure, **input)
        except Exception:
            pytest.fail('there is error')
