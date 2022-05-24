from grplot.features.statdesc.check_statdesc import check_statdesc
import numpy as np
import pytest

data = [0, 100000, 200000, 300000, 400000, 500000]

@pytest.mark.parametrize('_ax, dataframe, input, expected', [
    (
        (0, 0),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': 'mean',
            'ystatdesc': 'mean',
            'sep': '.c',
            'xsep': '.c',
            'ysep': '.c',
            'add': 'Rp(_)',
            'xadd': 'Rp(_)',
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': 'Rp(_)',
            'axes': None
        },
        (
            ('mean: Rp250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: Rp250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (0, 0),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': 'mean',
            'ystatdesc': 'mean',
            'sep': '.c',
            'xsep': '.c',
            'ysep': '.c',
            'add': '$(_)',
            'xadd': None,
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': None,
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (1, 0),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': 'mean',
            'ystatdesc': 'mean',
            'sep': '.c',
            'xsep': None,
            'ysep': None,
            'add': '$(_)',
            'xadd': '$(_)',
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': 'Rp.(_)',
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: Rp.250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (1, 0),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': 'mean',
            'ystatdesc': 'mean',
            'sep': '.c',
            'xsep': None,
            'ysep': None,
            'add': '$(_)',
            'xadd': None,
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': None,
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (0, 1),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': None,
            'ystatdesc': None,
            'sep': '.c',
            'xsep': '.c',
            'ysep': '.c',
            'add': '$(_)',
            'xadd': 'ok(_)',
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': '$(_)',
            'axes': None
        },
        (
            ('mean: ok250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (0, 1),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': None,
            'ystatdesc': None,
            'sep': '.c',
            'xsep': '.c',
            'ysep': '.c',
            'add': '$(_)',
            'xadd': None,
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': None,
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (0, 1),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': None,
            'ystatdesc': None,
            'sep': '.c',
            'xsep': None,
            'ysep': None,
            'add': '$(_)',
            'xadd': '$(_)',
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': 'ok(_)',
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: ok250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (0, 1),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': None,
            'ystatdesc': None,
            'sep': '.c',
            'xsep': None,
            'ysep': None,
            'add': '$(_)',
            'xadd': None,
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'yadd': None,
            'axes': None
        },
        (
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        )
    ), (
        (1, 1),
        ['other', data],
        {
            'statdesc': 'mean',
            'xstatdesc': None,
            'ystatdesc': None,
            'sep': '.c',
            'xsep': None,
            'ysep': None,
            'add': '$(_)',
            'xadd': None,
            'xaxislabel': None,
            'yaxislabel': None,
            'yadd': None,
            'axes': None
        },
        None
    )
], indirect=['_ax', 'dataframe'])
def test_check_statdesc(_ax, dataframe, input, expected):
    ax = check_statdesc(
        df=dataframe,
        ax=_ax,
        **input
    )

    if len(ax.get_lines()) > 0:
        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)
    else:
        assert len(ax.get_lines()) == 0