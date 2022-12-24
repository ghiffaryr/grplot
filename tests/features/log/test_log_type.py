from grplot.features.log.log_type import log_type
import numpy
import pytest


class TestLogType:
    def test_log_value_is_none(self, _ax):
        ax = log_type(
            ax=_ax,
            axes=None,
            axis='x',
            axislabel='time',
            log=None
        )

        numpy.testing.assert_array_equal(ax.get_xticks(), [-2.5,  0.,  2.5,  5., 7.5, 10., 12.5])

    def test_log_has_str_value(self, _ax):
        ax = log_type(
            ax=_ax,
            axes=None,
            axis='x',
            axislabel='time',
            log='logit'
        )

        numpy.testing.assert_array_equal(ax.get_xticks(), [0.01, 0.1,  0.5,  0.9,  0.99])

    def test_unknown_log_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            log_type(
                ax=_ax,
                axes=None,
                axis='x',
                axislabel='time',
                log=[]
            )

        assert str(exc_info.value) == 'Unknown log argument!'
