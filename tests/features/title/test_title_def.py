import pytest
from grplot.features.title.title_def import title_def


class TestTitleDef:
    @pytest.mark.parametrize('input', [
        (('halo', None)),
        (('halo', 15)),
    ])
    def test_set_title(self, _ax, input):
        title_def(_ax, *input)
        assert _ax.get_title() == 'halo'

    def test_unknown_fontsize_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            title_def(_ax, title='hola', title_fontsize='y')

        assert str(exc_info.value) == 'Unknown title fontsize argument!'
