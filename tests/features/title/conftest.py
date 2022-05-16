import pytest
import matplotlib.pyplot as plt

@pytest.fixture
def _ax():
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])
    return ax
