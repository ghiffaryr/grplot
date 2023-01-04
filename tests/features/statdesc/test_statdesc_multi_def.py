from grplot.features.statdesc.statdesc_multi_def import statdesc_multi_def
import pytest
import numpy

statdesc_inputs = [
    "count",
    "unique",
    "std",
    "min",
    "pct1",
    "whislo",
    "pct5",
    "q1",
    "cilo",
    "median",
    "mean",
    "cihi",
    "q3",
    "pct95",
    "whishi",
    "pct99",
    "max",
]

input_for_exception_test = [
    ((0, 1), ["other"], {"axislabel": "x", "statdesc": statdesc_input, "sep": [], "axis": "x", "axes": None, "add": []})
    for statdesc_input in statdesc_inputs
]


class TestStatdescMultiDef:
    @pytest.mark.parametrize("_ax, dataframe", [((0, 0), ["other"])], indirect=["_ax", "dataframe"])
    def test_statdesc_general(self, _ax, dataframe):
        ax = statdesc_multi_def(
            ax=_ax, df=dataframe, axislabel="x", statdesc="general", sep=".c", axis="x", axes=None, add=None
        )

        expected = [
            ("count", "6"),
            ("non zero count", "5"),
            ("unique count", "6"),
            ("std", "1,87"),
            ("range", "5,00"),
            ("min", "0"),
            ("q1", "1,25"),
            ("median", "2,50"),
            ("mean", "2,50"),
            ("q3", "3,75"),
            ("max", "5,00"),
        ]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(":")
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]

    @pytest.mark.parametrize("_ax, dataframe", [((1, 0), ["numpy"])], indirect=["_ax", "dataframe"])
    def test_statdesc_boxplot(self, _ax, dataframe):
        ax = statdesc_multi_def(
            ax=_ax, df=dataframe, axislabel="x", statdesc="boxplot", sep=".c", axis="x", axes=None, add=None
        )

        expected = [
            ("min", "0"),
            ("lower whisker", "0"),
            ("q1", "1,25"),
            ("95% CI low", "0,8976254599293374"),
            ("median", "2,50"),
            ("mean", "2,50"),
            ("95% CI hi", "4,10"),
            ("q3", "3,75"),
            ("upper whisker", "5,00"),
            ("max", "5,00"),
        ]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(":")
            assert label[0] == expected_val[0]
            numpy.testing.assert_almost_equal(
                float(label[1].strip().replace(",", ".")), float(expected_val[1].replace(",", ".")), 2
            )

    @pytest.mark.parametrize("_ax, dataframe", [((0, 1), ["other"])], indirect=["_ax", "dataframe"])
    def test_statdesc_else(self, _ax, dataframe):
        ax = statdesc_multi_def(
            ax=_ax,
            df=dataframe,
            axislabel="x",
            statdesc="pct1+pct5+pct95+pct99+yolo",
            sep=".c",
            axis="x",
            axes=None,
            add=None,
        )

        expected = [
            ("1st pct", "0,05"),
            ("5th pct", "0,25"),
            ("95th pct", "4,75"),
            ("99th pct", "4,95"),
        ]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(":")
            assert label[0] == expected_val[0]
            numpy
            assert label[1].strip() == expected_val[1]

    @pytest.mark.parametrize("_ax, dataframe", [((0, 1), ["other", "hola"])], indirect=["_ax", "dataframe"])
    def test_df_value_unsupported(self, _ax, dataframe):
        with pytest.raises(Exception) as exc_info:
            statdesc_multi_def(
                ax=_ax, df=dataframe, axislabel="x", statdesc="", sep=".c", axis="x", axes=None, add=None
            )

        assert "Unsupported dtype" in str(exc_info.value)

    @pytest.mark.parametrize("_ax, dataframe", [((0, 1), ["other", [1, None, 2]])], indirect=["_ax", "dataframe"])
    def test_df_value_contains_none(self, _ax, dataframe):
        ax = statdesc_multi_def(
            ax=_ax, df=dataframe, axislabel="x", statdesc="count", sep=".c", axis="x", axes=None, add=None
        )

        expected = [("count", "3")]

        for line, expected_val in zip(ax.get_lines(), expected):
            label = line.get_label().split(":")
            assert label[0] == expected_val[0]
            assert label[1].strip() == expected_val[1]

    @pytest.mark.parametrize("_ax, dataframe", [((0, 1), ["other"])], indirect=["_ax", "dataframe"])
    def test_statdesc_argument_unknown(self, _ax, dataframe):
        with pytest.raises(Exception) as exc_info:
            statdesc_multi_def(
                ax=_ax, df=dataframe, axislabel="x", statdesc=[], sep=".c", axis="x", axes=None, add=None
            )

        assert "Unknown statdesc argument" in str(exc_info.value)

    @pytest.mark.parametrize("_ax, dataframe, input", [*input_for_exception_test], indirect=["_ax", "dataframe"])
    def test_label_not_in_dataframe(self, _ax, dataframe, input):
        with pytest.raises(Exception) as exc_info:
            statdesc_multi_def(ax=_ax, df=dataframe, **input)

        assert "Label not in the dataframe" in str(exc_info.value)
