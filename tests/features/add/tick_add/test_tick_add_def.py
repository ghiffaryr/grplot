from grplot.features.add.tick_add.tick_add_def import tick_add_def
import pytest


class TestTickAddDef:
    @pytest.mark.parametrize('_ax', [(['Time', 'Freq'])], indirect=['_ax'])
    def test_error_if_there_is_unsupported_axis(self, _ax):
        input = {
            'axis': 'k',
            'add': '(_) km',
        }

        with pytest.raises(Exception) as exc_info:
            tick_add_def(_ax, **input)

        assert 'Unsupported axis!' in str(exc_info.value)

    @pytest.mark.parametrize('_ax, axis', [
        (['Time', 'Freq'], 'x'),
        (['Time', 'Freq'], 'y')
    ], indirect=['_ax'])
    def test_error_if_there_is_unknown_tick_add_argument(self, axis, _ax):
        input = {
            'axis': axis,
            'add': 'yoyoma',
        }

        with pytest.raises(Exception) as exc_info:
            tick_add_def(_ax, **input)

        assert 'Unknown tick add argument' in str(exc_info.value)

    @pytest.mark.parametrize('_ax, axis, add, expected', [
        *[(['Time', 'Freq'], 'x', add, (expect, '1.25')) for add, expect in zip(['Rp (_)', '(_) km', 'huge (_) km'], ['Rp 12', '12 km', 'huge 12 km'])],
        *[(['Time', 'Freq'], 'y', add, ('12', expect)) for add, expect in zip(['Rp (_)', '(_) km', 'huge (_) km'], ['Rp 1.25', '1.25 km', 'huge 1.25 km'])],
    ], indirect=['_ax'])
    def test_when_add_is_underscore_inside_parenthesis(self, axis, _ax, add, expected):
        ax = tick_add_def(_ax, axis, add)

        expected_xlabel, expected_ylabel = expected
        assert ax.get_xticklabels()[-1].get_text() == expected_xlabel
        assert ax.get_yticklabels()[-1].get_text() == expected_ylabel

    @pytest.mark.parametrize('_ax, axis, add, expected', [
        *[(['Time', 'Freq'], 'x', add, (expect, '1.25')) for add, expect in zip(['Rp _', '_ km', 'huge _ km'], ['Rp 12', '12 km', 'huge 12 km'])],
        *[(['Time', 'Freq'], 'y', add, ('12', expect)) for add, expect in zip(['Rp _', '_ km', 'huge _ km'], ['Rp 1.25', '1.25 km', 'huge 1.25 km'])],
    ], indirect=['_ax'])
    def test_when_add_is_just_underscore(self, axis, _ax, add, expected):
        ax = tick_add_def(_ax, axis, add)

        expected_xlabel, expected_ylabel = expected
        assert ax.get_xticklabels()[-1].get_text() == expected_xlabel
        assert ax.get_yticklabels()[-1].get_text() == expected_ylabel
