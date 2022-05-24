from grplot.features.statdesc.statdesc_type import statdesc_type
import pytest

@pytest.mark.parametrize('_ax, dataframe, input, expected', [
    (
        (0, 0),
        ['other'],
        {
            'axis': 'x',
            'statdesc': 'general',
            'sep': '.c',
            'add': None,
            'axislabel': 'x',
            'axes': None
        },
        [
            ('test', '1'),
            ('count', '5'),
            ('unique count', '6'),
            ('std', '1,71'),
            ('min', '0'),
            ('q1', '1,25'),
            ('median', '2,50'),
            ('mean', '2,50'),
            ('q3', '3,75'),
            ('max', '5,00'),
        ]
    ), (
        (1, 0),
        ['other'],
        {
            'axis': 'x',
            'statdesc': None,
            'sep': '.c',
            'add': None,
            'axislabel': 'x',
            'axes': None
        },
        [('test', '1')]
    ), (
        (1, 0),
        ['other'],
        {
            'axis': 'x',
            'statdesc': [],
            'sep': '.c',
            'add': None,
            'axislabel': 'x',
            'axes': None
        },
        [('test', '1')]
    )
], indirect=['_ax', 'dataframe'])
def test_statdesc_multi_def(_ax, dataframe, input, expected):
    _ax.axvline(0.5, color='green', linestyle=':', label='{}: {}'.format('test', '1'))
    try:
        ax = statdesc_type(
            ax=_ax,
            df=dataframe,
            **input
        )
    except:
        with pytest.raises(Exception):
            statdesc_type(
                ax=_ax,
                df=dataframe,
                **input
            )
    else:
        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(':')
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]


