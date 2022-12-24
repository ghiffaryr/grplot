from grplot.features.statdesc.check_statdesc import check_statdesc
import numpy as np
import pytest

data = [0, 100000, 200000, 300000, 400000, 500000]


class TestCheckStatdesc:
    @pytest.mark.parametrize('_ax, dataframe', [((0, 0), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_all_params_not_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc='mean',
            ystatdesc='mean',
            sep='.c',
            add='$(_)',
            xsep='.c',
            ysep='.c',
            axes='x',
            xadd='Rp(_)',
            xaxislabel='x',
            yadd='Rp(_)',
            yaxislabel='y',
        )

        expected = [
            ('mean: Rp250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: Rp250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((0, 0), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_and_y_add_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc='mean',
            ystatdesc='mean',
            sep='.c',
            add='$(_)',
            xsep='.c',
            ysep='.c',
            axes='x',
            xadd=None,
            xaxislabel='x',
            yadd=None,
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((1, 0), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_and_y_sep_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc='mean',
            ystatdesc='mean',
            sep='.c',
            add='$(_)',
            xsep=None,
            ysep=None,
            axes='x',
            xadd='$(_)',
            xaxislabel='x',
            yadd='Rp.(_)',
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: Rp.250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((1, 0), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_y_sep_add_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc='mean',
            ystatdesc='mean',
            sep='.c',
            add='$(_)',
            xsep=None,
            ysep=None,
            axes='x',
            xadd=None,
            xaxislabel='x',
            yadd=None,
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((1, 0), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_y_statdesc_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc=None,
            ystatdesc=None,
            sep='.c',
            add='$(_)',
            xsep='.c',
            ysep='.c',
            axes='x',
            xadd='ok(_)',
            xaxislabel='x',
            yadd='$(_)',
            yaxislabel='y',
        )

        expected = [
            ('mean: ok250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((0, 1), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_y_statdesc_add_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc=None,
            ystatdesc=None,
            sep='.c',
            add='$(_)',
            xsep='.c',
            ysep='.c',
            axes='x',
            xadd=None,
            xaxislabel='x',
            yadd=None,
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((0, 1), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_y_statdesc_sep_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc=None,
            ystatdesc=None,
            sep='.c',
            add='$(_)',
            xsep=None,
            ysep=None,
            axes='x',
            xadd='$(_)',
            xaxislabel='x',
            yadd='ok(_)',
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: ok250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((0, 1), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_x_y_statdesc_sep_add_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc=None,
            ystatdesc=None,
            sep='.c',
            add='$(_)',
            xsep=None,
            ysep=None,
            axes='x',
            xadd=None,
            xaxislabel='x',
            yadd=None,
            yaxislabel='y',
        )

        expected = [
            ('mean: $250.000,00', ([250000.0, 250000.0], [0, 1])),
            ('mean: $250.000,00', ([0, 1], [250000.0, 250000.0])),
        ]

        for line, (label, data) in zip(ax.get_lines(), expected):
            assert line.get_label() == label
            np.testing.assert_array_equal(line.get_data(), data)

    @pytest.mark.parametrize('_ax, dataframe', [((1, 1), ['other', data])], indirect=['_ax', 'dataframe'])
    def test_axis_label_is_none(self, _ax, dataframe):
        ax = check_statdesc(
            df=dataframe,
            ax=_ax,
            statdesc='mean',
            xstatdesc=None,
            ystatdesc=None,
            sep='.c',
            add='$(_)',
            xsep=None,
            ysep=None,
            axes=None,
            xadd=None,
            xaxislabel=None,
            yadd=None,
            yaxislabel=None,
        )

        assert len(ax.get_lines()) == 0
