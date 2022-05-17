from matplotlib.figure import Figure
from grplot.features.pad.check_pad import check_pad
import pytest
import matplotlib as mpl
import matplotlib.pyplot as plt

@pytest.fixture
def figure():
    fig = plt.figure()
    return fig

@pytest.mark.parametrize('input,expected', [
    ({ "wpad": 1.5, "hpad": None, "pad": None }, (None)),
    ({ "wpad": None, "hpad": 1.5, "pad": None }, (None)),
    ({ "wpad": 1.5, "hpad": 1.5, "pad": None }, (None)),
    ({ "wpad": None, "hpad": None, "pad": 0.5 }, (None)),
    ({ "wpad": None, "hpad": None, "pad": None }, (None))
])
def test_check_pad(figure: Figure, input, expected):
    try:
        new_fig = check_pad(figure, **input)
    except:
        with pytest.raises(Exception):
            check_pad(figure, **input)
    else:
        assert type(new_fig) == mpl.figure.Figure
    
