from grplot.features.add.tick_add.check_tick_add import check_tick_add
import pytest


class TestCheckTickAdd:
    @pytest.mark.parametrize("_ax", [(["Time", "Freq"])], indirect=['_ax'])
    def test_axis_label_none(self, _ax):
        input = {
                'xaxislabel': None,
                'yaxislabel': None,
                'add': 'Rp (_)',
                'xadd': None,
                'yadd': None,
                'axes': None
        }
        ax = check_tick_add(_ax, **input)
        assert 'Rp' not in ax.get_xticklabels()[0].get_text()

    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_x_and_y_add_is_none(self, _ax):
        input = {
                'xaxislabel': 'Time',
                'yaxislabel': 'Freq',
                'add': 'Rp (_)',
                'xadd': None,
                'yadd': None,
                'axes': None
        }
        ax = check_tick_add(_ax, **input)
        assert 'Rp' in ax.get_xticklabels()[0].get_text()
        assert 'Rp' in ax.get_yticklabels()[0].get_text()

    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_x_add_has_value(self, _ax):
        input = {
                'xaxislabel': 'Time',
                'yaxislabel': 'Freq',
                'add': 'Rp (_)',
                'xadd': 'USD (_)',
                'yadd': None,
                'axes': None
        }
        ax = check_tick_add(_ax, **input)
        assert 'USD' in ax.get_xticklabels()[0].get_text()
        assert 'Rp' in ax.get_yticklabels()[0].get_text()

    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_y_add_has_value(self, _ax):
        input = {
                'xaxislabel': 'Time',
                'yaxislabel': 'Freq',
                'add': 'Rp (_)',
                'xadd': None,
                'yadd': 'USD (_)',
                'axes': None
        }
        ax = check_tick_add(_ax, **input)
        assert 'Rp' in ax.get_xticklabels()[0].get_text()
        assert 'USD' in ax.get_yticklabels()[0].get_text()
