from grplot.features.statdesc.statdesc_type import statdesc_type
import pytest


class TestStatdescType:
    def set_ax_vline(self, _ax):
        _ax.axvline(0.5, color='green', linestyle=':', label='{}: {}'.format('test', '1'))
        return _ax

    @pytest.mark.parametrize('_ax, dataframe', [((1, 0), ['other'])], indirect=['_ax', 'dataframe'])
    def test_when_statdesc_is_none(self, _ax, dataframe):
        ax = self.set_ax_vline(_ax)
        ax = statdesc_type(
            ax=ax,
            df=dataframe,
            add=None,
            axes=None,
            axis='x',
            axislabel='x',
            sep='.c',
            statdesc=None
        )

        expected = [('test', '1')]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(':')
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]

    @pytest.mark.parametrize('_ax, dataframe', [((0, 0), ['other'])], indirect=['_ax', 'dataframe'])
    def test_when_statdesc_is_not_none(self, _ax, dataframe):
        ax = self.set_ax_vline(_ax)
        ax = statdesc_type(
            ax=ax,
            df=dataframe,
            add=None,
            axes=None,
            axis='x',
            axislabel='x',
            sep='.c',
            statdesc='general'
        )

        expected = [
            ('test', '1'),
            ('count', '6'),
            ('non zero count', '5'),
            ('unique count', '6'),
            ('std', '1,87'),
            ('range', '5,00'),
            ('min', '0'),
            ('q1', '1,25'),
            ('median', '2,50'),
            ('mean', '2,50'),
            ('q3', '3,75'),
            ('max', '5,00'),
        ]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(':')
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]

    @pytest.mark.parametrize('_ax, dataframe', [((1, 0), ['other'])], indirect=['_ax', 'dataframe'])
    def test_error_when_unknown_statdesc_argument(self, _ax, dataframe):
        with pytest.raises(Exception) as exc_info:
            statdesc_type(
                ax=_ax,
                df=dataframe,
                add=None,
                axes=None,
                axis='x',
                axislabel='x',
                sep='.c',
                statdesc=[]
            )

        assert str(exc_info.value) == 'Unknown statdesc argument!'
