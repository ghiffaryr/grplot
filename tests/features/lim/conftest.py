import matplotlib.pyplot as plt
import numpy as np
import pytest

@pytest.fixture
def _ax():
    ax = plt.subplot(221)
    ax.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])
    yield ax
    plt.close()