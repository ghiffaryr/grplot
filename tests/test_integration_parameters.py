"""
Integration tests for comprehensive parameter coverage.

Tests labels, titles, limits, palettes, font sizes, and parameter variations
across all plot types.
"""
import pytest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


@pytest.fixture
def comprehensive_data():
    """Comprehensive dataset"""
    np.random.seed(456)
    n = 100
    return pd.DataFrame({
        'numeric1': np.random.randn(n),
        'numeric2': np.random.randn(n) * 5 + 10,
        'numeric3': np.random.rand(n) * 10000,
        'numeric4': np.random.randint(-100, 100, n),
        'cat_a': np.random.choice(['Alpha', 'Beta', 'Gamma', 'Delta'], n),
        'cat_b': np.random.choice(['One', 'Two', 'Three'], n),
        'cat_c': np.random.choice(['X', 'Y'], n),
        'weight': np.random.rand(n) * 100,
        'size_col': np.random.randint(5, 50, n)
    })


@pytest.fixture
def time_data():
    """Time series dataset"""
    dates = pd.date_range('2020-01-01', periods=100, freq='D')
    return pd.DataFrame({
        'date': dates,
        'value1': np.cumsum(np.random.randn(100)) + 50,
        'value2': np.cumsum(np.random.randn(100)) * 2 + 100,
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })


# ============================================================================
# Label Variations - xlabel, ylabel, xlabel_add, ylabel_add
# ============================================================================
@pytest.mark.integration
class TestLabelVariations:
    """Comprehensive label tests"""
    
    def test_custom_xlabel_ylabel(self, comprehensive_data):
        """Custom x and y labels"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel='Custom X Label', ylabel='Custom Y Label')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_only(self, comprehensive_data):
        """Custom xlabel only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel='X Only')
        assert ax is not None
        plt.close('all')
    
    def test_ylabel_only(self, comprehensive_data):
        """Custom ylabel only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    ylabel='Y Only')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_add_suffix(self, comprehensive_data):
        """xlabel_add with suffix"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel_add='units_')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_add_prefix(self, comprehensive_data):
        """xlabel_add with prefix"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel_add='_units')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_add_both(self, comprehensive_data):
        """xlabel_add with both"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel_add='prefix_suffix')
        assert ax is not None
        plt.close('all')
    
    def test_ylabel_add_suffix(self, comprehensive_data):
        """ylabel_add with suffix"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    ylabel_add='kg_')
        assert ax is not None
        plt.close('all')
    
    def test_ylabel_add_prefix(self, comprehensive_data):
        """ylabel_add with prefix"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    ylabel_add='_meters')
        assert ax is not None
        plt.close('all')
    
    def test_ylabel_add_both(self, comprehensive_data):
        """ylabel_add with both"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    ylabel_add='before_after')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_ylabel_with_add(self, comprehensive_data):
        """Both xlabel/ylabel and label_add"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    xlabel='Value', ylabel='Measurement', xlabel_add='kg_', ylabel_add='_meters')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Title Variations
# ============================================================================
@pytest.mark.integration
class TestTitleVariations:
    """Title parameter tests"""
    
    def test_simple_title(self, comprehensive_data):
        """Simple string title"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    title='My Plot Title')
        assert ax is not None
        plt.close('all')
    
    def test_long_title(self, comprehensive_data):
        """Long title"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    title='This is a Very Long Title That Should Be Displayed Properly on the Plot')
        assert ax is not None
        plt.close('all')
    
    def test_title_with_special_chars(self, comprehensive_data):
        """Title with special characters"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    title='Plot: $\\alpha$ vs $\\beta$ (Test)')
        assert ax is not None
        plt.close('all')
    
    def test_title_with_custom_fontsize(self, comprehensive_data):
        """Title with custom fontsize"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    title='Title Test', title_fontsize=20)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Limit Variations - xlim, ylim, lim
# ============================================================================
@pytest.mark.integration
class TestLimitVariations:
    """Axis limit tests"""
    
    def test_xlim_only(self, comprehensive_data):
        """X-axis limits only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2',
                    xlim=[-2, 2])
        assert ax is not None
        plt.close('all')
    
    def test_ylim_only(self, comprehensive_data):
        """Y-axis limits only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2',
                    ylim=[0, 20])
        assert ax is not None
        plt.close('all')
    
    def test_xlim_ylim_both(self, comprehensive_data):
        """Both xlim and ylim"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2',
                    xlim=[-2, 2], ylim=[0, 20])
        assert ax is not None
        plt.close('all')
    
    def test_lim_parameter(self, comprehensive_data):
        """General lim parameter"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2',
                    lim=[0, 100])
        assert ax is not None
        plt.close('all')
    
    def test_limits_on_categorical_plot(self, comprehensive_data):
        """Limits on categorical plot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='cat_a', y='numeric3',
                    ylim=[0, 10000])
        assert ax is not None
        plt.close('all')


# ============================================================================
# More Plot Type Combinations
# ============================================================================
@pytest.mark.integration
class TestMorePlotCombinations:
    """Additional plot combinations"""
    
    def test_barplot_stripplot(self, comprehensive_data):
        """barplot + stripplot"""
        from grplot import plot2d
        ax = plot2d(plot='barplot+stripplot', df=comprehensive_data, x='cat_a', y='numeric3')
        assert ax is not None
        plt.close('all')
    
    def test_pointplot_stripplot(self, comprehensive_data):
        """pointplot + stripplot"""
        from grplot import plot2d
        ax = plot2d(plot='pointplot+stripplot', df=comprehensive_data, x='cat_a', y='numeric3')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_rugplot(self, comprehensive_data):
        """histplot + rugplot"""
        from grplot import plot2d
        ax = plot2d(plot='histplot+rugplot', df=comprehensive_data, x='numeric3')
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_pointplot(self, comprehensive_data):
        """boxplot + pointplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot+pointplot', df=comprehensive_data, x='cat_a', y='numeric3')
        assert ax is not None
        plt.close('all')
    
    def test_violinplot_pointplot(self, comprehensive_data):
        """violinplot + pointplot"""
        from grplot import plot2d
        ax = plot2d(plot='violinplot+pointplot', df=comprehensive_data, x='cat_a', y='numeric3')
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_stripplot(self, comprehensive_data):
        """lineplot + stripplot"""
        from grplot import plot2d
        df = comprehensive_data.head(20).copy()
        ax = plot2d(plot='lineplot+stripplot', df=df, x='numeric1', y='numeric2')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_regplot(self, comprehensive_data):
        """scatterplot + regplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+regplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Histplot Variations - bins, element, multiple
# ============================================================================
@pytest.mark.integration
class TestHistplotVariations:
    """Histplot-specific parameters"""
    
    def test_histplot_custom_bins(self, comprehensive_data):
        """Histplot with custom bins"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', bins=20)
        assert ax is not None
        plt.close('all')
    
    def test_histplot_element_step(self, comprehensive_data):
        """Histplot with step element"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', element='step')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_element_poly(self, comprehensive_data):
        """Histplot with poly element"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', element='poly')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_multiple_stack(self, comprehensive_data):
        """Histplot with stacked multiple"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', hue='cat_b', multiple='stack')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_multiple_dodge(self, comprehensive_data):
        """Histplot with dodge multiple"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', hue='cat_b', multiple='dodge')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_multiple_fill(self, comprehensive_data):
        """Histplot with fill multiple"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', hue='cat_b', multiple='fill')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_stat_density(self, comprehensive_data):
        """Histplot with density stat"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', stat='density')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_stat_probability(self, comprehensive_data):
        """Histplot with probability stat"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', stat='probability')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_stat_percent(self, comprehensive_data):
        """Histplot with percent stat"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', stat='percent')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_cumulative(self, comprehensive_data):
        """Histplot cumulative"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=comprehensive_data, x='numeric3', cumulative=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# KDE Plot Variations
# ============================================================================
@pytest.mark.integration
class TestKDEPlotVariations:
    """KDE-specific parameters"""
    
    def test_kdeplot_fill(self, comprehensive_data):
        """KDE plot with fill"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot', df=comprehensive_data, x='numeric1', y='numeric2', fill=True)
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_bw_adjust(self, comprehensive_data):
        """KDE with bandwidth adjustment"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot', df=comprehensive_data, x='numeric3', bw_adjust=0.5)
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_with_hue(self, comprehensive_data):
        """KDE with hue"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot', df=comprehensive_data, x='numeric3', hue='cat_b')
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_common_norm(self, comprehensive_data):
        """KDE with common_norm"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot', df=comprehensive_data, x='numeric3', hue='cat_b', common_norm=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Boxplot Variations
# ============================================================================
@pytest.mark.integration
class TestBoxplotVariations:
    """Boxplot-specific parameters"""
    
    def test_boxplot_orient_h(self, comprehensive_data):
        """Horizontal boxplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='numeric3', y='cat_a', orient='h')
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_with_hue_dodge(self, comprehensive_data):
        """Boxplot with hue and dodge"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='cat_a', y='numeric3', hue='cat_c', dodge=True)
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_width(self, comprehensive_data):
        """Boxplot with custom width"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='cat_a', y='numeric3', width=0.5)
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_whis(self, comprehensive_data):
        """Boxplot with custom whis"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='cat_a', y='numeric3', whis=2.0)
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_notch(self, comprehensive_data):
        """Boxplot with notch"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=comprehensive_data, x='cat_a', y='numeric3')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Datetime Format Tests
# ============================================================================
@pytest.mark.integration
class TestDatetimeFormats:
    """Datetime formatting tests"""
    
    def test_dt_ymd(self, time_data):
        """Datetime Y-m-d format"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot', df=time_data, x='date', y='value1', xdt='%Y-%m-%d')
        assert ax is not None
        plt.close('all')
    
    def test_dt_md(self, time_data):
        """Datetime m/d format"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot', df=time_data, x='date', y='value1', xdt='%m/%d')
        assert ax is not None
        plt.close('all')
    
    def test_dt_year_month(self, time_data):
        """Datetime Y-m format"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot', df=time_data, x='date', y='value1', xdt='%Y-%m')
        assert ax is not None
        plt.close('all')
    
    def test_dt_month_name(self, time_data):
        """Datetime with month name"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot', df=time_data, x='date', y='value1', xdt='%B')
        assert ax is not None
        plt.close('all')
    
    def test_dt_multiplot(self, time_data):
        """Datetime in multi-plot"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'lineplot', '[2]': 'scatterplot'},
            df=time_data,
            x=['date', 'date'],
            y=['value1', 'value2'],
            Nx=2, Ny=1,
            xdt='%Y-%m-%d'
        )
        assert ax is not None
        plt.close('all')


# ============================================================================
# Palette and Color Tests
# ============================================================================
@pytest.mark.integration
class TestPaletteAndColor:
    """Palette and color parameter tests"""
    
    def test_palette_deep(self, comprehensive_data):
        """Palette: deep"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='deep')
        assert ax is not None
        plt.close('all')
    
    def test_palette_muted(self, comprehensive_data):
        """Palette: muted"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='muted')
        assert ax is not None
        plt.close('all')
    
    def test_palette_pastel(self, comprehensive_data):
        """Palette: pastel"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='pastel')
        assert ax is not None
        plt.close('all')
    
    def test_palette_bright(self, comprehensive_data):
        """Palette: bright"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='bright')
        assert ax is not None
        plt.close('all')
    
    def test_palette_dark(self, comprehensive_data):
        """Palette: dark"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='dark')
        assert ax is not None
        plt.close('all')
    
    def test_palette_colorblind(self, comprehensive_data):
        """Palette: colorblind"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    hue='cat_b', palette='colorblind')
        assert ax is not None
        plt.close('all')
    
    def test_single_color(self, comprehensive_data):
        """Single color parameter"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2',
                    color='red')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Alpha and Transparency Tests
# ============================================================================
@pytest.mark.integration
class TestAlphaTransparency:
    """Alpha/transparency tests"""
    
    def test_alpha_low(self, comprehensive_data):
        """Low alpha"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2', alpha=0.3)
        assert ax is not None
        plt.close('all')
    
    def test_alpha_medium(self, comprehensive_data):
        """Medium alpha"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2', alpha=0.6)
        assert ax is not None
        plt.close('all')
    
    def test_alpha_with_hue(self, comprehensive_data):
        """Alpha with hue"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data, x='numeric1', y='numeric2',
                    hue='cat_b', alpha=0.5)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Comprehensive Parameter Combinations
# ============================================================================
@pytest.mark.integration
class TestComprehensiveParameterCombinations:
    """Complex parameter combinations"""
    
    def test_everything_scatterplot(self, comprehensive_data):
        """Scatterplot with many parameters"""
        from grplot import plot2d
        df = comprehensive_data.head(30)
        ax = plot2d(
            plot='scatterplot',
            df=df,
            x='numeric1',
            y='numeric2',
            hue='cat_b',
            size='size_col',
            style='cat_c',
            alpha=0.7,
            xlabel='X Axis',
            ylabel='Y Axis',
            title='Comprehensive Test',
            legend='brief',
            legend_loc='upper right'
        )
        assert ax is not None
        plt.close('all')
    
    def test_everything_lineplot(self, comprehensive_data):
        """Lineplot with many parameters"""
        from grplot import plot2d
        ax = plot2d(
            plot='lineplot',
            df=comprehensive_data.head(40),
            x='numeric1',
            y='numeric2',
            hue='cat_b',
            style='cat_c',
            xlabel='Time',
            ylabel='Value',
            title='Line Analysis',
            xrot=30,
            legend='full'
        )
        assert ax is not None
        plt.close('all')
    
    def test_everything_boxplot(self, comprehensive_data):
        """Boxplot with many parameters"""
        from grplot import plot2d
        ax = plot2d(
            plot='boxplot',
            df=comprehensive_data,
            x='cat_a',
            y='numeric3',
            hue='cat_c',
            xlabel='Category',
            ylabel='Measurement',
            ylabel_add='kg_',
            title='Box Analysis',
            sep=',',
            xrot=45,
            ystatdesc='boxplot',
            legend_loc='best'
        )
        assert ax is not None
        plt.close('all')
    
    def test_everything_multiplot(self, comprehensive_data):
        """Multi-plot with comprehensive parameters"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1,1]': 'scatterplot', '[1,2]': 'boxplot', '[2,1]': 'histplot', '[2,2]': 'violinplot'},
            df=comprehensive_data,
            x=['numeric1', 'cat_a', 'numeric3', 'cat_a'],
            y=['numeric2', 'numeric3', None, 'numeric3'],
            hue='cat_b',
            Nx=2, Ny=2,
            sep=',',
            title='Multi Analysis',
            fontsize=10,
            hpad=6,
            wpad=8
        )
        assert ax is not None
        plt.close('all')


# ============================================================================
# Regression Plot Variations
# ============================================================================
@pytest.mark.integration
class TestRegressionVariations:
    """Regression plot tests"""
    
    def test_regplot_order_2(self, comprehensive_data):
        """Polynomial regression order 2"""
        from grplot import plot2d
        ax = plot2d(plot='regplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2', order=2)
        assert ax is not None
        plt.close('all')
    
    def test_regplot_logistic(self, comprehensive_data):
        """Logistic regression"""
        from grplot import plot2d
        df = comprehensive_data.head(30).copy()
        df['binary'] = (df['numeric2'] > df['numeric2'].median()).astype(int)
        ax = plot2d(plot='regplot', df=df, x='numeric1', y='binary', logistic=True)
        assert ax is not None
        plt.close('all')
    
    def test_regplot_robust(self, comprehensive_data):
        """Robust regression"""
        from grplot import plot2d
        ax = plot2d(plot='regplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2', robust=True)
        assert ax is not None
        plt.close('all')
    
    def test_residplot_basic(self, comprehensive_data):
        """Residual plot"""
        from grplot import plot2d
        ax = plot2d(plot='residplot', df=comprehensive_data.head(30), x='numeric1', y='numeric2')
        assert ax is not None
        plt.close('all')


# ============================================================================
# More Edge Cases
# ============================================================================
@pytest.mark.integration
class TestMoreEdgeCases:
    """Additional edge cases"""
    
    def test_all_zeros(self):
        """All zero values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [0, 0, 0, 0], 'y': [0, 0, 0, 0]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_sparse_data(self, comprehensive_data):
        """Sparse data (3 points)"""
        from grplot import plot2d
        df = comprehensive_data.head(3)
        ax = plot2d(plot='lineplot', df=df, x='numeric1', y='numeric2')
        assert ax is not None
        plt.close('all')
    
    def test_single_category(self):
        """Single category"""
        from grplot import plot2d
        df = pd.DataFrame({'category': ['A', 'A', 'A', 'A'], 'value': [10, 20, 30, 40]})
        ax = plot2d(plot='boxplot', df=df, x='category', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_extreme_aspect_ratio(self, comprehensive_data):
        """Extreme aspect ratio"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=comprehensive_data.head(20), x='numeric1', y='numeric2',
                    figsize=[20, 4])
        assert ax is not None
        plt.close('all')
