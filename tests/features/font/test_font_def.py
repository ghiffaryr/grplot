from grplot.features.font.font_def import font_def
import pytest

@pytest.mark.parametrize('arg, input, expected', [
    (
        'x',
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 14,
            'label_fontsize': 14          
        },
        14
    ), (
        'y',
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 14,
            'label_fontsize': 14          
        },
        14
    ), (
        'x',
        {
            'plot': 'line',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 14,
            'label_fontsize': 14          
        },
        14
    ), (
        'x',
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': None,
            'label_fontsize': None          
        },
        10
    ), (
        'x',
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 'hola',
            'label_fontsize': 14          
        },
        None
    ), (
        'x',
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 14,
            'label_fontsize': 'hola'          
        },
        None
    ), (
        None,
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': 14,
            'label_fontsize': None        
        },
        None
    ), (
        None,
        {
            'plot': 'paretoplot',
            'x': 'x',
            'y': 'y',
            'tick_fontsize': None,
            'label_fontsize': 14        
        },
        None
    )
], indirect=['arg'])
def test_font_def(arg, input, expected):
    try:
        ax  = font_def(**arg, **input)
    except:
        with pytest.raises(Exception):
            font_def(**arg, **input)
    else:
        assert ax.get_xticklabels()[0].get_fontsize() == expected
