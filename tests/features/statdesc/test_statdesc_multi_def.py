from grplot.features.statdesc.statdesc_multi_def import statdesc_multi_def
import numpy as np
import pandas as pd
import pytest

statdesc_inputs = [
    'count',
    'unique',
    'std',
    'min',
    'pct1',
    'whislo',
    'pct5',
    'q1',
    'cilo',
    'median',
    'mean',
    'cihi',
    'q3',
    'pct95',
    'whishi',
    'pct99',
    'max'
]

input_for_exception_test = [
    (
        (0, 1),
        ['other'],
        {
            'axislabel': 'x',
            'statdesc': statdesc_input,
            'sep':[],
            'axis':'x',
            'axes': None,
            'add': []
        },
        None
    )
    for statdesc_input in statdesc_inputs
]

@pytest.mark.parametrize('_ax, dataframe, input, expected', [
    (
        (0, 0),
        ['other'],
        {
            'axislabel': 'x',
            'statdesc':'general',
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        [
            ('count', '6'),
            ('non zero count', '5'),
            ('unique count', '6'),
            ('std', '1,87'),
            ('range', '5,00'),
            ('min', '0'),
            ('q1', '1,25'),
            ('median', '2,50'),
            ('mean', '2,50'),
            ('q3', '3,75'),
            ('max', '5,00'),
        ]
    ), (
        (1, 0),
        ['numpy'],
        {
            'axislabel': 'x',
            'statdesc':'boxplot',
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        [
            ('min', '0'),
            ('lower whisker', '0'),
            ('q1', '1,25'),
            ('95% CI low', '0,8976254599293374'),
            ('median', '2,50'),
            ('mean', '2,50'),
            ('95% CI hi', '4,10'),
            ('q3', '3,75'),
            ('upper whisker', '5,00'),
            ('max', '5,00'),
        ]
    ), (
        (0, 1),
        ['other'],
        {
            'axislabel': 'x',
            'statdesc':'pct1+pct5+pct95+pct99+yolo',
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        [
            ('1st pct', '0,05'),
            ('5th pct', '0,25'),
            ('95th pct', '4,75'),
            ('99th pct', '4,95'),
        ]
    ), (
        (0, 1),
        ['other', 'hola'],
        {
            'axislabel': 'x',
            'statdesc':'',
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        None
    ), (
        (0, 1),
        ['other', [1, None, 2]],
        {
            'axislabel': 'x',
            'statdesc':'count',
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        [
            ('count', '3')
        ]
    ), (
        (0, 1),
        ['other'],
        {
            'axislabel': 'x',
            'statdesc': [],
            'sep':'.c',
            'axis':'x',
            'axes': None,
            'add': None
        },
        None
    ),
    *input_for_exception_test
], indirect=['_ax', 'dataframe'])
def test_statdesc_multi_def(_ax, dataframe, input, expected):
    print(dataframe)
    try:
        ax = statdesc_multi_def(ax=_ax, df=dataframe, **input)
    except:
        with pytest.raises(Exception):
            statdesc_multi_def(ax=_ax, df=dataframe, **input)
    else:
        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(':')
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]
