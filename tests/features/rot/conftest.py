import matplotlib.pyplot as plt
import numpy as np
import pytest

@pytest.fixture
def _ax():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    ax = plt.subplot(221)
    ax.plot(x,y)
    return ax
