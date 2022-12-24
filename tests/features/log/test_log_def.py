from grplot.features.log.log_def import log_def
import numpy
import pytest


class TestLogDef:
    def test_scale_x(self, _ax):
        ax = log_def(
            ax=_ax,
            axis='x',
            log='logit'
        )
        numpy.testing.assert_array_equal(ax.get_xticks(), [0.01, 0.1,  0.5,  0.9,  0.99])

    def test_scale_y(self, _ax):
        ax = log_def(
            ax=_ax,
            axis='y',
            log='logit'
        )
        numpy.testing.assert_array_equal(ax.get_yticks(), [0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999, 0.9999])

    @pytest.mark.parametrize('axis', [('x'), ('y')])
    def test_unknown_log_argument(self, _ax, axis):
        with pytest.raises(Exception) as exc_info:
            log_def(
                ax=_ax,
                axis=axis,
                log='boom'
            )

        assert str(exc_info.value) == 'Unknown log argument!'

    def test_unsupported_axis(self, _ax):
        with pytest.raises(Exception) as exc_info:
            log_def(
                ax=_ax,
                axis='y2k',
                log='logit'
            )

        assert str(exc_info.value) == 'Unsupported axis!'
