import pytest
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def _ax(request):
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    fig, ax = plt.subplots(1, 1)
    ax.plot(x,y)

    xlabel, ylabel = request.param
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.canvas.draw()
    yield ax
    plt.close()