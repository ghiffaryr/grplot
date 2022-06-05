import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

@pytest.fixture(scope='function')
def arg(request):
    fig, ax = plt.subplots(1, 1)
    df = None
    if request.param == 'x':
        df = pd.DataFrame({
            'x': np.array([chr(97 + i) for i in range(5)]),
            'y': np.array([i for i in range(5)])
            })
    elif request.param == 'y':
        df = pd.DataFrame({
            'y': np.array([chr(97 + i) for i in range(5)]),
            'x': np.array([i for i in range(5)])
            })
    else:
        df = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [1, 2, 3]
        })

    if request.param in ['x', 'y']:
        df[request.param or 'x'].astype('category', copy=False);

    ax.plot(df['x'], df['y'])
    ax.set_xlabel('time')
    ax.set_ylabel('freq')
    fig.canvas.draw()

    yield {
        'ax': ax,
        'df': df
    }
    plt.close()