from grplot.features.rot.rot_def import rot_def
import pytest


class TestRotDef:
    def test_x_rot(self, _ax):
        rotated_tick_ax = rot_def(
            ax=_ax,
            axis='x',
            rot=90
        )

        for label in rotated_tick_ax.get_xticklabels():
            assert label.get_rotation() == 90

    def test_y_rot(self, _ax):
        rotated_tick_ax = rot_def(
            ax=_ax,
            axis='y',
            rot=90
        )

        for label in rotated_tick_ax.get_yticklabels():
            assert label.get_rotation() == 90

    def test_unsupported_axis(self, _ax):
        with pytest.raises(Exception) as exc_info:
            rot_def(
                ax=_ax,
                axis='ok',
                rot=90
            )

        assert str(exc_info.value) == 'Unsupported axis!'
