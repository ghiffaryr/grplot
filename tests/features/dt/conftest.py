import pytest
import matplotlib.pyplot as plt
from datetime import datetime

@pytest.fixture(scope='function')
def _ax():
    fig, ax = plt.subplots(1, 1)

    dates = [f"2022-0{date}" for date in range(1, 6)]
    y = [i for i in range(1, 6)]
    x = [datetime.strptime(d, "%Y-%m") for d in dates]

    ax.plot(x, y)
    yield (ax, fig)
    plt.close()