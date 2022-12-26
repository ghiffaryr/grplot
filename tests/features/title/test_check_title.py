import pytest
from grplot.features.title.check_title import check_title


class TestCheckTitle:
    def test_title_is_none(self, _ax):
        axes = check_title(_ax, None, None, None)
        assert axes == _ax

    def test_title_have_value(self, _ax):
        check_title(_ax, 'hola', None, None)
        _ax.get_title == 'hola'

    def test_title_value_is_not_str(self, _ax):
        with pytest.raises(Exception) as exc_info:
            check_title(_ax, [], None, None)

        assert str(exc_info.value) == 'Unknown title argument!'
