"""
Integration tests for plot combinations and complex layouts.

Tests plot overlays, multi-plot grids, text annotations, and edge cases.
"""
import pytest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@pytest.fixture
def rich_dataset():
    """Rich dataset with many columns"""
    np.random.seed(123)
    n = 150
    return pd.DataFrame({
        'A': np.random.randn(n),
        'B': np.random.randn(n) * 2,
        'C': np.random.rand(n) * 1000,
        'D': np.random.randint(0, 100, n),
        'cat1': np.random.choice(['X', 'Y', 'Z'], n),
        'cat2': np.random.choice(['P', 'Q'], n),
        'cat3': np.random.choice(['R', 'S', 'T', 'U'], n),
        'size': np.random.randint(10, 100, n),
        'weight': np.random.rand(n) * 10
    })


# ============================================================================
# All Possible Plot Combinations - Critical for plot_single_def.py
# ============================================================================
@pytest.mark.integration
class TestAllPlotCombinations:
    """Test all possible 2-plot and 3-plot combinations"""
    
    def test_lineplot_histplot(self, rich_dataset):
        """lineplot + histplot"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot+histplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_kdeplot(self, rich_dataset):
        """lineplot + kdeplot"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot+kdeplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="ecdfplot combo not supported")
    def test_lineplot_ecdfplot(self, rich_dataset):
        """lineplot + ecdfplot"""
        from grplot import plot2d
        ax = plot2d(plot='lineplot+ecdfplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_histplot(self, rich_dataset):
        """scatterplot + histplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+histplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_kdeplot(self, rich_dataset):
        """scatterplot + kdeplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+kdeplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="ecdfplot combo not supported")
    def test_scatterplot_ecdfplot(self, rich_dataset):
        """scatterplot + ecdfplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+ecdfplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_lineplot_histplot(self, rich_dataset):
        """3-plot combination: scatterplot + lineplot + histplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+lineplot+histplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_lineplot_kdeplot(self, rich_dataset):
        """3-plot combination: scatterplot + lineplot + kdeplot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+lineplot+kdeplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_violinplot(self, rich_dataset):
        """boxplot + violinplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot+violinplot', df=rich_dataset, x='cat1', y='C')
        assert ax is not None
        plt.close('all')
    
    def test_boxplot_swarmplot(self, rich_dataset):
        """boxplot + swarmplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot+swarmplot', df=rich_dataset.head(50), x='cat1', y='C')
        assert ax is not None
        plt.close('all')
    
    def test_violinplot_stripplot(self, rich_dataset):
        """violinplot + stripplot"""
        from grplot import plot2d
        ax = plot2d(plot='violinplot+stripplot', df=rich_dataset, x='cat1', y='C')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_lineplot(self, rich_dataset):
        """barplot + lineplot"""
        from grplot import plot2d
        ax = plot2d(plot='barplot+lineplot', df=rich_dataset.head(20), x='cat1', y='C')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_pointplot(self, rich_dataset):
        """barplot + pointplot"""
        from grplot import plot2d
        ax = plot2d(plot='barplot+pointplot', df=rich_dataset, x='cat1', y='C')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_ecdfplot(self, rich_dataset):
        """histplot + ecdfplot"""
        from grplot import plot2d
        ax = plot2d(plot='histplot+ecdfplot', df=rich_dataset, x='C')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_kdeplot(self, rich_dataset):
        """histplot + kdeplot"""
        from grplot import plot2d
        ax = plot2d(plot='histplot+kdeplot', df=rich_dataset, x='C')
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_ecdfplot(self, rich_dataset):
        """kdeplot + ecdfplot"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot+ecdfplot', df=rich_dataset, x='C')
        assert ax is not None
        plt.close('all')
    
    def test_kdeplot_rugplot(self, rich_dataset):
        """kdeplot + rugplot"""
        from grplot import plot2d
        ax = plot2d(plot='kdeplot+rugplot', df=rich_dataset, x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_ecdfplot_rugplot(self, rich_dataset):
        """ecdfplot + rugplot"""
        from grplot import plot2d
        ax = plot2d(plot='ecdfplot+rugplot', df=rich_dataset, x='C')
        assert ax is not None
        plt.close('all')
    
    def test_regplot_scatterplot(self, rich_dataset):
        """regplot + scatterplot"""
        from grplot import plot2d
        ax = plot2d(plot='regplot+scatterplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_regplot_residplot(self, rich_dataset):
        """regplot + residplot"""
        from grplot import plot2d
        ax = plot2d(plot='regplot+residplot', df=rich_dataset.head(30), x='A', y='B')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text Features Comprehensive - Critical for text_def.py coverage
# ============================================================================
@pytest.mark.integration
class TestTextFeatures:
    """Comprehensive text annotation tests"""
    
    def test_text_scatterplot_all_points(self, rich_dataset):
        """Text on all scatter points"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='B', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_barplot(self, rich_dataset):
        """Text on bar plot"""
        from grplot import plot2d
        df = rich_dataset.groupby('cat1')['C'].mean().reset_index()
        ax = plot2d(plot='barplot', df=df, x='cat1', y='C', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_lineplot(self, rich_dataset):
        """Text on line plot"""
        from grplot import plot2d
        df = rich_dataset.head(10).copy()
        ax = plot2d(plot='lineplot', df=df, x='A', y='B', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_hue(self, rich_dataset):
        """Text with hue grouping"""
        from grplot import plot2d
        df = rich_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='B', hue='cat1', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_separator_currency(self, rich_dataset):
        """Text with thousand separator and currency"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='C', y='D', text=True, sep=',c')
        assert ax is not None
        plt.close('all')
    
    def test_text_with_different_fontsize(self, rich_dataset):
        """Text with custom fontsize"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='B', text=True, text_fontsize=6)
        assert ax is not None
        plt.close('all')
    
    def test_xtext_ytext_independent(self, rich_dataset):
        """Independent x and y text control"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='C', xtext=True, ytext=False)
        assert ax is not None
        plt.close('all')
    
    def test_text_only_ytrue(self, rich_dataset):
        """Only y text shown"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='C', xtext=False, ytext=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_pointplot(self, rich_dataset):
        """Text on point plot"""
        from grplot import plot2d
        ax = plot2d(plot='pointplot', df=rich_dataset, x='cat1', y='C', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_tick_add_and_sep(self, rich_dataset):
        """Text with both tick_add and separator"""
        from grplot import plot2d
        df = rich_dataset.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='C', y='D', text=True, sep=',', tick_add='USD_')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Complex Multi-Plot Grids - Critical for plot_multi_def.py
# ============================================================================
@pytest.mark.integration
class TestComplexMultiPlots:
    """Complex multi-panel layouts"""
    
    def test_1x4_layout(self, rich_dataset):
        """1x4 layout"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'lineplot', '[3]': 'histplot', '[4]': 'boxplot'},
            df=rich_dataset,
            x=['A', 'A', 'C', 'cat1'],
            y=['B', 'B', None, 'C'],
            Nx=4, Ny=1
        )
        assert ax is not None
        plt.close('all')
    
    def test_4x1_layout(self, rich_dataset):
        """4x1 layout (vertical)"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'lineplot', '[3]': 'histplot', '[4]': 'boxplot'},
            df=rich_dataset,
            x=['A', 'A', 'C', 'cat1'],
            y=['B', 'B', None, 'C'],
            Nx=1, Ny=4
        )
        assert ax is not None
        plt.close('all')
    
    def test_3x3_grid(self, rich_dataset):
        """3x3 grid"""
        from grplot import plot2d
        ax = plot2d(
            plot={
                '[1,1]': 'scatterplot', '[1,2]': 'lineplot', '[1,3]': 'histplot',
                '[2,1]': 'boxplot', '[2,2]': 'violinplot', '[2,3]': 'kdeplot',
                '[3,1]': 'barplot', '[3,2]': 'pointplot', '[3,3]': 'stripplot'
            },
            df=rich_dataset,
            x=['A', 'A', 'C', 'cat1', 'cat1', 'C', 'cat1', 'cat1', 'cat1'],
            y=['B', 'B', None, 'C', 'C', None, 'C', 'C', 'C'],
            Nx=3, Ny=3
        )
        assert ax is not None
        plt.close('all')
    
    def test_mixed_combos_multiplot(self, rich_dataset):
        """Multi-plot with combo plots"""
        from grplot import plot2d
        ax = plot2d(
            plot={
                '[1,1]': 'scatterplot+lineplot',
                '[1,2]': 'histplot+kdeplot',
                '[2,1]': 'boxplot+stripplot',
                '[2,2]': 'violinplot+swarmplot'
            },
            df=rich_dataset,
            x=['A', 'C', 'cat1', 'cat1'],
            y=['B', None, 'C', 'C'],
            Nx=2, Ny=2
        )
        assert ax is not None
        plt.close('all')
    
    def test_multiplot_with_hue(self, rich_dataset):
        """Multi-plot with hue"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'boxplot'},
            df=rich_dataset,
            x=['A', 'cat1'],
            y=['B', 'C'],
            hue='cat2',
            Nx=2, Ny=1
        )
        assert ax is not None
        plt.close('all')
    
    def test_multiplot_different_separators(self, rich_dataset):
        """Multi-plot with different separators per panel"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'scatterplot'},
            df=rich_dataset,
            x=['C', 'C'],
            y=['D', 'D'],
            Nx=2, Ny=1,
            sep=','
        )
        assert ax is not None
        plt.close('all')
    
    def test_multiplot_with_log_scales(self, rich_dataset):
        """Multi-plot with log scales"""
        from grplot import plot2d
        df = rich_dataset[rich_dataset['C'] > 0]
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'scatterplot'},
            df=df,
            x=['C', 'C'],
            y=['D', 'D'],
            Nx=2, Ny=1,
            xlog='log'
        )
        assert ax is not None
        plt.close('all')
    
    def test_multiplot_with_limits(self, rich_dataset):
        """Multi-plot with axis limits"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'histplot'},
            df=rich_dataset,
            x=['A', 'C'],
            y=['B', None],
            Nx=2, Ny=1,
            xlim=[0, 100]
        )
        assert ax is not None
        plt.close('all')
    
    def test_multiplot_with_rotation(self, rich_dataset):
        """Multi-plot with label rotation"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'barplot', '[2]': 'boxplot'},
            df=rich_dataset,
            x=['cat3', 'cat3'],
            y=['C', 'C'],
            Nx=2, Ny=1,
            xrot=45
        )
        assert ax is not None
        plt.close('all')


# ============================================================================
# Separator + Tick_add Combinations
# ============================================================================
@pytest.mark.integration
class TestSeparatorTickAddCombos:
    """Test all combinations of separators and tick_add"""
    
    def test_comma_sep_with_prefix_tick(self, rich_dataset):
        """Comma separator with prefix tick_add"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='C', y='D', sep=',', tick_add='_USD')
        assert ax is not None
        plt.close('all')
    
    def test_dot_sep_with_suffix_tick(self, rich_dataset):
        """Dot separator with suffix tick_add"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='C', y='D', sep='.', tick_add='kg_')
        assert ax is not None
        plt.close('all')
    
    def test_currency_sep_with_both_tick(self, rich_dataset):
        """Currency separator with both prefix/suffix tick_add"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='C', y='D', sep='.c', tick_add='EUR_USD')
        assert ax is not None
        plt.close('all')
    
    def test_xtick_ytick_different_with_sep(self, rich_dataset):
        """Different xtick_add and ytick_add with separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='C', y='D', sep=',', xtick_add='_m', ytick_add='kg_')
        assert ax is not None
        plt.close('all')
    
    def test_xsep_ysep_xtick_ytick_all_different(self, rich_dataset):
        """All different: xsep, ysep, xtick_add, ytick_add"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='C', y='D', xsep=',', ysep='.c', xtick_add='_m', ytick_add='USD_')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Statdesc Comprehensive Tests
# ============================================================================
@pytest.mark.integration
class TestStatdescComprehensive:
    """Comprehensive statdesc tests"""
    
    def test_ystatdesc_on_boxplot(self, rich_dataset):
        """Y-axis statdesc on boxplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=rich_dataset, x='cat1', y='C', ystatdesc='boxplot')
        assert ax is not None
        plt.close('all')
    
    def test_xstatdesc_on_categorical(self, rich_dataset):
        """X-axis statdesc on categorical"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=rich_dataset, x='cat1', y='C', xstatdesc='count')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_mean_on_barplot(self, rich_dataset):
        """Mean statdesc on barplot"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=rich_dataset, x='cat1', y='C', ystatdesc='mean')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_median_on_violinplot(self, rich_dataset):
        """Median statdesc on violinplot"""
        from grplot import plot2d
        ax = plot2d(plot='violinplot', df=rich_dataset, x='cat1', y='C', ystatdesc='median')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_sum(self, rich_dataset):
        """Sum statdesc"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=rich_dataset, x='cat1', y='C', ystatdesc='sum')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_var(self, rich_dataset):
        """Variance statdesc"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=rich_dataset, x='cat1', y='C', ystatdesc='var')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Font Size Variations
# ============================================================================
@pytest.mark.integration
class TestFontSizeVariations:
    """Test all fontsize parameters"""
    
    def test_all_fontsizes_custom(self, rich_dataset):
        """All custom fontsizes"""
        from grplot import plot2d
        ax = plot2d(
            plot='scatterplot',
            df=rich_dataset.head(20),
            x='A',
            y='B',
            title='Test',
            fontsize=14,
            tick_fontsize=10,
            label_fontsize=12,
            title_fontsize=16,
            legend_fontsize=9
        )
        assert ax is not None
        plt.close('all')
    
    def test_legend_fontsize_with_hue(self, rich_dataset):
        """Legend fontsize with hue"""
        from grplot import plot2d
        ax = plot2d(
            plot='scatterplot',
            df=rich_dataset.head(30),
            x='A',
            y='B',
            hue='cat1',
            legend_fontsize=8
        )
        assert ax is not None
        plt.close('all')
    
    def test_text_fontsize_on_plot(self, rich_dataset):
        """Text fontsize on scatter"""
        from grplot import plot2d
        df = rich_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='B', text=True, text_fontsize=7)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Pad and Spacing Tests
# ============================================================================
@pytest.mark.integration
class TestPadAndSpacing:
    """Test padding and spacing parameters"""
    
    def test_custom_hpad_wpad_multiplot(self, rich_dataset):
        """Custom hpad and wpad"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1,1]': 'scatterplot', '[1,2]': 'histplot'},
            df=rich_dataset,
            x=['A', 'C'],
            y=['B', None],
            Nx=2, Ny=1,
            hpad=5, wpad=10
        )
        assert ax is not None
        plt.close('all')
    
    def test_pad_parameter(self, rich_dataset):
        """General pad parameter"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(20), x='A', y='B', pad=8)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Edge Cases and Boundary Conditions
# ============================================================================
@pytest.mark.integration
class TestEdgeCases:
    """Edge cases and boundary conditions"""
    
    def test_single_data_point(self, rich_dataset):
        """Single data point"""
        from grplot import plot2d
        df = rich_dataset.head(1)
        ax = plot2d(plot='scatterplot', df=df, x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_two_data_points(self, rich_dataset):
        """Two data points"""
        from grplot import plot2d
        df = rich_dataset.head(2)
        ax = plot2d(plot='lineplot', df=df, x='A', y='B')
        assert ax is not None
        plt.close('all')
    
    def test_large_values(self):
        """Very large values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [1e6, 2e6, 3e6], 'y': [1e9, 2e9, 3e9]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', sep=',')
        assert ax is not None
        plt.close('all')
    
    def test_small_values(self):
        """Very small values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [0.0001, 0.0002, 0.0003], 'y': [0.00001, 0.00002, 0.00003]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_negative_values(self):
        """All negative values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [-100, -200, -300], 'y': [-50, -150, -250]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', tick_add='(_)USD')
        assert ax is not None
        plt.close('all')
    
    def test_mixed_positive_negative(self):
        """Mixed positive and negative"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [-100, 0, 100], 'y': [-50, 0, 50]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', sep=',')
        assert ax is not None
        plt.close('all')
    
    def test_many_categories(self):
        """Many categories (20+)"""
        from grplot import plot2d
        cats = [f'Cat{i}' for i in range(25)]
        df = pd.DataFrame({'category': cats, 'value': np.random.rand(25) * 100})
        ax = plot2d(plot='barplot', df=df, x='category', y='value', xrot=90)
        assert ax is not None
        plt.close('all')
    
    def test_long_category_names(self):
        """Long category names"""
        from grplot import plot2d
        df = pd.DataFrame({
            'category': ['VeryLongCategoryName1', 'VeryLongCategoryName2', 'VeryLongCategoryName3'],
            'value': [10, 20, 30]
        })
        ax = plot2d(plot='barplot', df=df, x='category', y='value', xrot=45)
        assert ax is not None
        plt.close('all')
    
    def test_uniform_data(self):
        """All same values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [5, 5, 5, 5], 'y': [10, 10, 10, 10]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_wide_range_values(self):
        """Wide range of values"""
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 10, 100, 1000, 10000], 'y': [0.01, 0.1, 1, 10, 100]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', xlog='log', ylog='log')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Optimizer Modes with Complex Plots
# ============================================================================
@pytest.mark.integration
class TestOptimizerModes:
    """Test different optimizer modes with various plots"""
    
    def test_saver_multiplot(self, rich_dataset):
        """Saver optimizer with multi-plot"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'boxplot'},
            df=rich_dataset,
            x=['A', 'cat1'],
            y=['B', 'C'],
            Nx=2, Ny=1,
            optimizer='saver'
        )
        assert ax is not None
        plt.close('all')
    
    def test_numpy_single_plot(self, rich_dataset):
        """Numpy optimizer with single plot"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=rich_dataset.head(50), x='A', y='B', optimizer='numpy')
        assert ax is not None
        plt.close('all')
    
    def test_pandas_multiplot(self, rich_dataset):
        """Pandas optimizer with multi-plot"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'lineplot', '[2]': 'histplot'},
            df=rich_dataset,
            x=['A', 'C'],
            y=['B', None],
            Nx=2, Ny=1,
            optimizer='pandas'
        )
        assert ax is not None
        plt.close('all')
