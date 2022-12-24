from grplot.features.rot.rot_type import rot_type
import pytest


class TestRotType:
    def test_rot_is_none(self, _ax):
        rotated_ax = rot_type(
            ax=_ax,
            axes=None,
            axis='x',
            axislabel='x',
            rot=None
        )

        for label in rotated_ax.get_xticklabels():
            assert label.get_rotation() == 0

    def test_rot_has_value(self, _ax):
        rotated_ax = rot_type(
            ax=_ax,
            axes=None,
            axis='x',
            axislabel='x',
            rot=90
        )

        for label in rotated_ax.get_xticklabels():
            assert label.get_rotation() == 90

    def test_unknown_rot_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            rot_type(
                ax=_ax,
                axes=None,
                axis='x',
                axislabel='x',
                rot='keliling'
            )

        assert str(exc_info.value) == 'Unknown rot argument!'
