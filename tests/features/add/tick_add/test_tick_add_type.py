from grplot.features.add.tick_add.tick_add_type import tick_add_type
import pytest


class TestTickAddType:
    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_add_is_none(self, _ax):
        ax = tick_add_type(_ax, axis='x', axes=None, add=None, axislabel='time')
        try:
            float(ax.get_xticklabels()[-1].get_text())
            float(ax.get_yticklabels()[-1].get_text())
        except ValueError as err:
            pytest.fail("value not a float")

    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_add_is_str(self, _ax):
        ax = tick_add_type(_ax, axis='x', axes=None, add="Rp(_)", axislabel='time')

        assert 'Rp' in ax.get_xticklabels()[-1].get_text()

    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_tick_add_argument_unknown(self, _ax):
        with pytest.raises(Exception) as exec_info:
            tick_add_type(_ax, axis='x', axes=None, add=[], axislabel='time')
        assert 'Unknown tick add argument' in str(exec_info.value)