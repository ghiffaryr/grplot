from grplot.features.add.label_add.check_label_add import check_label_add
import pytest


@pytest.mark.parametrize(
    "_ax, input, expected",
    [
        (
            ["time", "freq"],
            {
                "add": None,
                "axes": None,
                "xadd": "_ (s)",
                "yadd": "_ (Hz)",
                "xaxislabel": "time",
                "yaxislabel": "freq",
            },
            ["time (s)", "freq (Hz)"],
        ),
        (
            ["time", "freq"],
            {
                "add": "yo _",
                "axes": None,
                "xadd": None,
                "yadd": None,
                "xaxislabel": "time",
                "yaxislabel": "freq",
            },
            ["yo time", "yo freq"],
        ),
        (
            ["time", "freq"],
            {
                "add": "yo _",
                "axes": None,
                "xadd": None,
                "yadd": None,
                "xaxislabel": None,
                "yaxislabel": None,
            },
            ["time", "freq"],
        ),
    ],
    indirect=["_ax"],
)
def test_check_label_add(_ax, input, expected):
    ax = check_label_add(_ax, **input)
    expected_xlabel, expected_ylabel = expected

    assert ax.get_xlabel() == expected_xlabel
    assert ax.get_ylabel() == expected_ylabel
