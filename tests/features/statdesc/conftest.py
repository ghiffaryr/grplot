import matplotlib.pyplot as plt
import numpy as np
import pytest

@pytest.fixture
def _ax(request):
    req_param = request.param
    fig, axs = plt.subplots(2, 2)
    yield axs[req_param[0]][req_param[1]]
    plt.close()

@pytest.fixture
def dataframe(request):
    default_content = [0, 1, 2, 3, 4, 5]
    dtype = ''
    value = None

    try:
        dtype, value = request.param
    except:
        dtype, value = request.param[0], default_content

    df_content= {
        'other': {
            'x': value,
            'y': value
        },
        'numpy':  {
            'x': np.asarray(value),
            'y': np.asarray(value)
        }
    }

    return df_content[dtype]