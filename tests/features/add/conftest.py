import pytest
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def _ax(request):
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    ax = plt.subplot(221)
    ax.plot(x,y)

    xlabel, ylabel = request.param
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    yield ax
    plt.close()