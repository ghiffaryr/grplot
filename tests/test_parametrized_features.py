"""
Comprehensive parametrized tests for systematic parameter coverage.

Uses pytest.mark.parametrize for efficient testing of parameter matrices
across separators, aesthetics, and plot configurations.
"""
import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from grplot import plot2d


@pytest.fixture
def sample_data_simple():
    """Simple dataset with numeric and categorical columns."""
    return pd.DataFrame({'x': range(50), 'y': np.random.randn(50), 'cat': ['A', 'B'] * 25})


@pytest.fixture
def sample_data_groups():
    """Dataset with grouped categorical data."""
    return pd.DataFrame({'group': ['X', 'Y', 'Z'] * 15, 'value': np.random.randn(45)})


@pytest.fixture
def sample_data_complex():
    """Complex dataset with multiple numeric and categorical columns."""
    return pd.DataFrame({'a': range(80), 'b': np.random.randn(80), 'c': np.random.rand(80) * 100, 'd': ['P', 'Q', 'R', 'S'] * 20})


class TestSeparatorCombinations:
    """Test separator formatting across different plot types."""
    """Systematic separator testing across plot types"""
    
    @pytest.mark.parametrize("sep", [',', '.', '.c', ',c', '.L', ',L', '.cL', ',cL'])
    def test_scatterplot_separators(self, sample_data_simple, sep):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', sep=sep)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("sep", [',', '.', '.c', ',c'])
    def test_lineplot_separators(self, sample_data_simple, sep):
        ax = plot2d(plot='lineplot', df=sample_data_simple, x='x', y='y', sep=sep)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("sep", [',', '.'])
    def test_barplot_separators(self, sample_data_groups, sep):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', sep=sep)
        assert ax is not None
        plt.close('all')


class TestTickAddCombinations:
    """Systematic tick_add testing"""
    
    @pytest.mark.parametrize("tick_add", ['USD_', '_EUR', 'USD_EUR', '(_)USD', 'USD(_)'])
    def test_scatterplot_tick_add(self, sample_data_simple, tick_add):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', tick_add=tick_add)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("tick_add", ['$_', '_kg', 'value_units'])
    def test_barplot_tick_add(self, sample_data_groups, tick_add):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', tick_add=tick_add)
        assert ax is not None
        plt.close('all')


class TestHueStyleSize:
    """Test hue, size, style parameters"""
    
    @pytest.mark.parametrize("aesthetic", ['hue', 'size', 'style'])
    def test_scatterplot_aesthetics(self, sample_data_simple, aesthetic):
        kwargs = {aesthetic: 'cat'}
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', **kwargs)
        assert ax is not None
        plt.close('all')
    
    def test_all_three_aesthetics(self, sample_data_complex):
        ax = plot2d(plot='scatterplot', df=sample_data_complex.head(60), x='a', y='b', hue='d', size='c', style='d')
        assert ax is not None
        plt.close('all')


class TestPaletteVariations:
    """Test different palettes"""
    
    @pytest.mark.parametrize("palette", ['Set1', 'Set2', 'Set3', 'Paired', 'Dark2', 'Pastel1', 'Pastel2'])
    def test_scatterplot_palettes(self, sample_data_simple, palette):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', hue='cat', palette=palette)
        assert ax is not None
        plt.close('all')


class TestAlphaValues:
    """Test alpha transparency"""
    
    @pytest.mark.parametrize("alpha", [0.3, 0.5, 0.7, 0.9])
    def test_scatterplot_alpha(self, sample_data_simple, alpha):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', alpha=alpha)
        assert ax is not None
        plt.close('all')


class TestHistplotParameters:
    """Comprehensive histplot parameter testing"""
    
    @pytest.mark.parametrize("bins", [10, 20, 30, 'auto'])
    def test_histplot_bins(self, sample_data_simple, bins):
        ax = plot2d(plot='histplot', df=sample_data_simple, x='y', bins=bins)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("element", ['bars', 'step', 'poly'])
    def test_histplot_element(self, sample_data_simple, element):
        ax = plot2d(plot='histplot', df=sample_data_simple, x='y', element=element)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("stat", ['count', 'frequency', 'density', 'probability'])
    def test_histplot_stat(self, sample_data_simple, stat):
        ax = plot2d(plot='histplot', df=sample_data_simple, x='y', stat=stat)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("multiple", ['layer', 'dodge', 'stack', 'fill'])
    def test_histplot_multiple(self, sample_data_simple, multiple):
        ax = plot2d(plot='histplot', df=sample_data_simple, x='y', hue='cat', multiple=multiple)
        assert ax is not None
        plt.close('all')


class TestLineplotParameters:
    """Comprehensive lineplot parameter testing"""
    
    @pytest.mark.parametrize("estimator", ['mean', 'median', 'min', 'max'])
    def test_lineplot_estimator(self, sample_data_simple, estimator):
        ax = plot2d(plot='lineplot', df=sample_data_simple, x='cat', y='y', estimator=estimator)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("ci", [68, 95, None])
    def test_lineplot_ci(self, sample_data_simple, ci):
        ax = plot2d(plot='lineplot', df=sample_data_simple, x='cat', y='y', ci=ci)
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_markers(self, sample_data_simple):
        ax = plot2d(plot='lineplot', df=sample_data_simple.head(30), x='x', y='y', markers=True)
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_dashes(self, sample_data_simple):
        ax = plot2d(plot='lineplot', df=sample_data_simple.head(30), x='x', y='y', hue='cat', dashes=True)
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_sort(self, sample_data_simple):
        ax = plot2d(plot='lineplot', df=sample_data_simple, x='y', y='x', sort=True)
        assert ax is not None
        plt.close('all')


class TestBoxplotViolinplot:
    """Box and violin plot parameters"""
    
    @pytest.mark.parametrize("whis", [1.5, 2.0])
    def test_boxplot_whis(self, sample_data_groups, whis):
        ax = plot2d(plot='boxplot', df=sample_data_groups, x='group', y='value', whis=whis)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("inner", ['box', 'quartile', 'stick'])
    def test_violinplot_inner(self, sample_data_groups, inner):
        ax = plot2d(plot='violinplot', df=sample_data_groups, x='group', y='value', inner=inner)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("saturation", [0.5, 0.75, 1.0])
    def test_boxplot_saturation(self, sample_data_groups, saturation):
        ax = plot2d(plot='boxplot', df=sample_data_groups, x='group', y='value', saturation=saturation)
        assert ax is not None
        plt.close('all')


class TestRotationParameters:
    """Test rotation parameters"""
    
    @pytest.mark.parametrize("rot", [0, 30, 45, 90])
    def test_barplot_rotation(self, sample_data_groups, rot):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', rot=rot)
        assert ax is not None
        plt.close('all')


class TestLimitParameters:
    """Test limit parameters"""
    
    def test_xlim(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', xlim=[10, 40])
        assert ax is not None
        plt.close('all')
    
    def test_ylim(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', ylim=[-2, 2])
        assert ax is not None
        plt.close('all')
    
    def test_both_lim(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', xlim=[10, 40], ylim=[-2, 2])
        assert ax is not None
        plt.close('all')


class TestFontsizeVariations:
    """Comprehensive fontsize testing"""
    
    @pytest.mark.parametrize("tick_size", [8, 10, 12, 14])
    def test_tick_fontsize(self, sample_data_simple, tick_size):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', tick_fontsize=tick_size)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("label_size", [10, 12, 14, 16])
    def test_label_fontsize(self, sample_data_simple, label_size):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', label_fontsize=label_size)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("title_size", [14, 16, 18])
    def test_title_fontsize(self, sample_data_simple, title_size):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', title='Test', title_fontsize=title_size)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.parametrize("legend_size", [8, 10, 12])
    def test_legend_fontsize(self, sample_data_simple, legend_size):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', hue='cat', legend_fontsize=legend_size)
        assert ax is not None
        plt.close('all')


class TestRegplotResidplot:
    """Regression and residual plot tests"""
    
    @pytest.mark.parametrize("order", [1, 2, 3])
    def test_regplot_order(self, sample_data_simple, order):
        ax = plot2d(plot='regplot', df=sample_data_simple.head(40), x='x', y='y', order=order)
        assert ax is not None
        plt.close('all')
    
    def test_regplot_no_scatter(self, sample_data_simple):
        ax = plot2d(plot='regplot', df=sample_data_simple.head(40), x='x', y='y', scatter=False)
        assert ax is not None
        plt.close('all')
    
    def test_regplot_no_fit(self, sample_data_simple):
        ax = plot2d(plot='regplot', df=sample_data_simple.head(40), x='x', y='y', fit_reg=False)
        assert ax is not None
        plt.close('all')
    
    def test_residplot(self, sample_data_simple):
        ax = plot2d(plot='residplot', df=sample_data_simple.head(40), x='x', y='y')
        assert ax is not None
        plt.close('all')


class TestCategoricalPlots:
    """Tests for categorical plot types"""
    
    def test_stripplot(self, sample_data_groups):
        ax = plot2d(plot='stripplot', df=sample_data_groups, x='group', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_pointplot(self, sample_data_groups):
        ax = plot2d(plot='pointplot', df=sample_data_groups, x='group', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_countplot(self, sample_data_groups):
        ax = plot2d(plot='countplot', df=sample_data_groups, x='group')
        assert ax is not None
        plt.close('all')


class TestMultiplotLayouts:
    """Test various multiplot layouts"""
    
    @pytest.mark.skip(reason="multiplot with y list needs specific setup")
    def test_1x2_multiplot(self, sample_data_complex):
        ax = plot2d(plot='scatterplot', df=sample_data_complex.head(50), x='a', y=['b', 'c'], multiplot=[1, 2])
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="multiplot with y list needs specific setup")
    def test_2x1_multiplot(self, sample_data_complex):
        ax = plot2d(plot='scatterplot', df=sample_data_complex.head(50), x='a', y=['b', 'c'], multiplot=[2, 1])
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="multiplot with y list needs specific setup")
    def test_2x2_multiplot(self, sample_data_complex):
        ax = plot2d(plot='scatterplot', df=sample_data_complex.head(50), x='a', y=['b', 'c', 'b', 'c'], multiplot=[2, 2])
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="multiplot with y list needs specific setup")
    def test_1x3_multiplot(self, sample_data_complex):
        ax = plot2d(plot='lineplot', df=sample_data_complex.head(60), x='a', y=['b', 'c', 'b'], multiplot=[1, 3])
        assert ax is not None
        plt.close('all')


class TestKDEPlot:
    """KDE plot specific tests"""
    
    def test_kdeplot_basic(self, sample_data_simple):
        ax = plot2d(plot='kdeplot', df=sample_data_simple, x='y')
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_with_hue(self, sample_data_simple):
        ax = plot2d(plot='kdeplot', df=sample_data_simple, x='y', hue='cat')
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_fill(self, sample_data_simple):
        ax = plot2d(plot='kdeplot', df=sample_data_simple, x='y', fill=True)
        assert ax is not None
        plt.close('all')


class TestLegendParameters:
    """Test legend-related parameters"""
    
    @pytest.mark.parametrize("loc", ['best', 'upper right', 'upper left', 'lower right', 'lower left'])
    def test_legend_loc(self, sample_data_simple, loc):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', hue='cat', legend_loc=loc)
        assert ax is not None
        plt.close('all')


class TestTextAnnotations:
    """Text annotation tests"""
    
    def test_text_on_barplot(self, sample_data_groups):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_fontsize(self, sample_data_groups):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', text=True, text_fontsize=9)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_sep(self, sample_data_groups):
        ax = plot2d(plot='barplot', df=sample_data_groups, x='group', y='value', text=True, sep=',')
        assert ax is not None
        plt.close('all')


class TestSeparateXYParameters:
    """Test xparam/yparam variations"""
    
    def test_xsep_ysep(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', xsep=',', ysep='.')
        assert ax is not None
        plt.close('all')
    
    def test_xtick_add_ytick_add(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', xtick_add='_x', ytick_add='_y')
        assert ax is not None
        plt.close('all')
    
    def test_xrot_yrot(self, sample_data_simple):
        ax = plot2d(plot='scatterplot', df=sample_data_simple, x='x', y='y', xrot=30, yrot=0)
        assert ax is not None
        plt.close('all')


class TestLargeDataset:
    """Test with larger datasets to trigger optimizers"""
    
    def test_large_scatterplot(self):
        df = pd.DataFrame({
            'x': range(1000),
            'y': np.cumsum(np.random.randn(1000)),
            'cat': np.random.choice(['A', 'B', 'C'], 1000)
        })
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_large_lineplot(self):
        df = pd.DataFrame({
            'x': range(800),
            'y': np.cumsum(np.random.randn(800))
        })
        ax = plot2d(plot='lineplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_large_histplot(self):
        df = pd.DataFrame({'values': np.random.randn(2000)})
        ax = plot2d(plot='histplot', df=df, x='values')
        assert ax is not None
        plt.close('all')


class TestDatetime:
    """Datetime-related tests"""
    
    def test_datetime_lineplot(self):
        df = pd.DataFrame({
            'date': pd.date_range('2020-01-01', periods=100),
            'value': np.cumsum(np.random.randn(100))
        })
        ax = plot2d(plot='lineplot', df=df, x='date', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_datetime_with_format(self):
        df = pd.DataFrame({
            'date': pd.date_range('2020-01-01', periods=50),
            'value': np.random.randn(50)
        })
        ax = plot2d(plot='scatterplot', df=df, x='date', y='value', dt='%Y-%m')
        assert ax is not None
        plt.close('all')


class TestEdgeCases:
    """Edge case tests"""
    
    def test_single_point(self):
        df = pd.DataFrame({'x': [1], 'y': [1]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_few_points(self):
        df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 4, 2]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_many_categories(self):
        df = pd.DataFrame({
            'cat': [f'Cat{i}' for i in range(20)],
            'val': np.random.randint(1, 50, 20)
        })
        ax = plot2d(plot='barplot', df=df, x='cat', y='val')
        assert ax is not None
        plt.close('all')
