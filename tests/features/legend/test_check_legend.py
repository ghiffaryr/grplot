from grplot.features.legend.check_legend import check_legend
import numpy as np
import matplotlib.pyplot as plt
import pytest

@pytest.fixture(scope='function')
def _plot(request):
    np.random.seed(10**7)
    n_bins = 20
    x = np.random.randn(10000, 2)
        
    colors = ['green', 'blue']

    fig, ax = plt.subplots(1, 1)

    if request.param == 'histplot':
        plot1 = ax.hist(x[:, 0], n_bins, density = True, 
             histtype ='bar',
             color=colors[0],
             label=colors[0])

        plot2  = ax.hist(x[:, 1], n_bins, density = True, 
             histtype ='bar',
             color=colors[1],
             label=colors[1])
        yield (list([plot1[-1], plot2[-1]]), ax, fig)
    elif request.param =='pieplot':
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        plot1 = ax.pie(sizes, labels=labels)
        ax.legend()
        yield (plot1, ax, fig)
    elif request.param == 'line':
        plot1, = ax.plot([1, 2, 3], color=colors[0] ,label=colors[0])
        plot2, = ax.plot([3, 2, 1], color=colors[1] ,label=colors[1])
        yield (list([plot1, plot2]), ax, fig)
    else:
        plot1, = ax.plot([1, 2, 3], color=colors[0])
        plot2, = ax.plot([3, 2, 1], color=colors[1])
        yield (list([plot1, plot2]), ax, fig)

    plt.close()

@pytest.mark.parametrize('_plot, input, expected', ([
    (
        'histplot',
        {
            'plot': 'histplot',
            'legend_fontsize': 14,
            'legend_loc': None,
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        [
            [880.305556, 583.911111, 252.25, 241.444444],
            4
        ]
    ), (
        'histplot',
        {
            'plot': 'histplot',
            'legend_fontsize': 14,
            'legend_loc': 'upper left',
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        [
            [179.444444, 583.911111, 252.25 , 241.444444],
            4
        ]
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': 'upper left',
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        [
            [179.444444, 698.8, 252.25, 126.555556],
            2
        ]
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': None,
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        [
            [880.305556, 411.922222, 252.25    , 126.555556],
            2
        ]
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': 'upper left',
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        [
            [179.444444, 698.8, 252.25, 126.555556],
            2
        ]
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': None,
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        [
            [880.305556, 411.922222, 252.25    , 126.555556],
            2
        ]
    ), (
        'pieplot',
        {
            'plot': 'pieplot',
            'legend_fontsize': 14,
            'legend_loc': None,
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        [
            [837.836111, 655.022222, 173.875   , 175.888889],
            4
        ]
    ), (
        'pieplot',
        {
            'plot': 'pieplot',
            'legend_fontsize': 14,
            'legend_loc': None,
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        [
            [837.836111, 655.022222, 173.875   , 175.888889],
            4
        ]
    ), ( #exception
        'histplot',
        {
            'plot': 'histplot',
            'legend_fontsize': 'halo',
            'legend_loc': None,
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        None
    ), (
        'histplot',
        {
            'plot': 'histplot',
            'legend_fontsize': 14,
            'legend_loc': 'halo',
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        None
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 'halo',
            'legend_loc': None,
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        None
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': 'halo',
            'hue': 0.5,
            'size': 14,
            'l': list(['color', 'color'])
        },
        None
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 'hola',
            'legend_loc': None,
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        [
            [179.444444, 698.8, 252.25, 126.555556],
            2
        ]
    ), (
        'line',
        {
            'plot': 'line',
            'legend_fontsize': 14,
            'legend_loc': 'hola',
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        None
    ), (
        'no label',
        {
            'plot': 'no label',
            'legend_fontsize': 14,
            'legend_loc': 'hola',
            'hue': None,
            'size': None,
            'l': list(['color', 'color'])
        },
        None
    ),   
]), indirect=['_plot'])
def test_check_legend(_plot, input, expected):
    try:
        plot_arr, ax, fig = _plot
        ax = check_legend(**input, h=plot_arr, ax=ax)
        fig.canvas.draw()
    except:
        with pytest.raises(Exception):
            check_legend(**input, h=plot_arr, ax=ax)
    else:
        if input['plot'] in ['pieplot', 'line', 'histplot']:
            np.testing.assert_array_almost_equal(ax.get_legend().get_frame().get_bbox().bounds, expected[0])
            assert len(ax.get_legend().get_texts()) == expected[1]
