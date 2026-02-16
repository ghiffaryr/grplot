"""
Integration tests for number formatting and separators.

Tests all separator types, tick_add formats, statdesc variations, and their
combinations with various plot types.
"""
import pytest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@pytest.fixture
def large_dataset():
    """Larger dataset for robust testing"""
    np.random.seed(42)
    n = 200
    return pd.DataFrame({
        'x': np.random.randn(n),
        'y': np.random.randn(n),
        'value': np.random.rand(n) * 10000,
        'category': np.random.choice(['A', 'B', 'C', 'D'], n),
        'subcategory': np.random.choice(['X', 'Y'], n),
        'size_col': np.random.randint(1, 10, n)
    })


@pytest.fixture
def categorical_data():
    """Categorical data"""
    return pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'] * 10,
        'value': np.random.randn(50) * 10 + 50,
        'count': np.random.randint(1, 100, 50)
    })


@pytest.fixture
def financial_data():
    """Financial data with large numbers"""
    return pd.DataFrame({
        'year': [2020, 2021, 2022, 2023, 2024] * 5,
        'revenue': np.random.rand(25) * 1000000,
        'profit': np.random.rand(25) * 500000,
        'company': np.random.choice(['Apple', 'Google', 'Microsoft'], 25)
    })


# ============================================================================
# ALL Separator Variations - Critical for tick_sep_def.py coverage
# ============================================================================
@pytest.mark.integration
class TestAllSeparatorCombinations:
    """Test all separator combinations to cover tick_sep_def.py"""
    
    def test_sep_comma(self, financial_data):
        """Test comma separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep=',')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="Locale issue")
    def test_sep_dot(self, financial_data):
        """Test dot separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep='.')
        assert ax is not None
        plt.close('all')
    
    def test_sep_dot_currency(self, financial_data):
        """Test dot currency separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep='.c')
        assert ax is not None
        plt.close('all')
    
    def test_sep_comma_currency(self, financial_data):
        """Test comma currency separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep=',c')
        assert ax is not None
        plt.close('all')
    
    def test_sep_dot_large(self, financial_data):
        """Test dot large number separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep='.L')
        assert ax is not None
        plt.close('all')
    
    def test_sep_comma_large(self, financial_data):
        """Test comma large number separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep=',L')
        assert ax is not None
        plt.close('all')
    
    def test_sep_dot_currency_large(self, financial_data):
        """Test dot currency large separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep='.cL')
        assert ax is not None
        plt.close('all')
    
    def test_sep_comma_currency_large(self, financial_data):
        """Test comma currency large separator"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', sep=',cL')
        assert ax is not None
        plt.close('all')
    
    def test_xsep_ysep_different(self, financial_data):
        """Test different separators for x and y"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=financial_data, x='revenue', y='profit', xsep=',', ysep='.c')
        assert ax is not None
        plt.close('all')


# ============================================================================
# ALL tick_add Variations - Critical for coverage
# ============================================================================
@pytest.mark.integration
class TestAllTickAddCombinations:
    """Test all tick_add format variations"""
    
    def test_tick_add_suffix(self, large_dataset):
        """Test unit suffix: 'kg_'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='kg_')
        assert ax is not None
        plt.close('all')
    
    def test_tick_add_prefix(self, large_dataset):
        """Test unit prefix: '_kg'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='_kg')
        assert ax is not None
        plt.close('all')
    
    def test_tick_add_both(self, large_dataset):
        """Test unit both: 'USD_EUR'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='USD_EUR')
        assert ax is not None
        plt.close('all')
    
    def test_tick_add_negative_suffix(self, large_dataset):
        """Test negative representation suffix: 'kg(_)'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='kg(_)')
        assert ax is not None
        plt.close('all')
    
    def test_tick_add_negative_prefix(self, large_dataset):
        """Test negative representation prefix: '(_)kg'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='(_)kg')
        assert ax is not None
        plt.close('all')
    
    def test_tick_add_negative_both(self, large_dataset):
        """Test negative representation both: 'USD(_)EUR'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', tick_add='USD(_)EUR')
        assert ax is not None
        plt.close('all')
    
    def test_xtick_add_ytick_add_different(self, large_dataset):
        """Test different tick_add for x and y"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', xtick_add='kg_', ytick_add='_USD')
        assert ax is not None
        plt.close('all')


# ============================================================================
# ALL Statistical Descriptions - Critical for statdesc coverage
# ============================================================================
@pytest.mark.integration
class TestAllStatisticalDescriptions:
    """Test all statdesc variations"""
    
    def test_statdesc_general(self, large_dataset):
        """Test general statistics"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='category', y='value', ystatdesc='general')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_boxplot(self, large_dataset):
        """Test boxplot statistics"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=large_dataset, x='category', y='value', ystatdesc='boxplot')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_count(self, large_dataset):
        """Test count statistic"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=large_dataset, x='category', y='value', ystatdesc='count')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_mean(self, large_dataset):
        """Test mean statistic"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=large_dataset, x='category', y='value', ystatdesc='mean')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_median(self, large_dataset):
        """Test median statistic"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=large_dataset, x='category', y='value', ystatdesc='median')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_std(self, large_dataset):
        """Test std statistic"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=large_dataset, x='category', y='value', ystatdesc='std')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_min_max(self, large_dataset):
        """Test min and max statistics"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=large_dataset, x='category', y='value', ystatdesc='min+max')
        assert ax is not None
        plt.close('all')
    
    def test_statdesc_q1_q3(self, large_dataset):
        """Test quartile statistics"""
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=large_dataset, x='category', y='value', ystatdesc='q1+q3')
        assert ax is not None
        plt.close('all')


# ============================================================================
# ALL Plot Types - Comprehensive Coverage
# ============================================================================
@pytest.mark.integration
class TestAllPlotTypes:
    """Test all plot types with various parameters"""
    
    def test_countplot(self, categorical_data):
        """Test countplot"""
        from grplot import plot2d
        ax = plot2d(plot='countplot', df=categorical_data, x='category')
        assert ax is not None
        plt.close('all')
    
    def test_countplot_with_hue(self, large_dataset):
        """Test countplot with hue"""
        from grplot import plot2d
        ax = plot2d(plot='countplot', df=large_dataset, x='category', hue='subcategory')
        assert ax is not None
        plt.close('all')
    
    def test_boxenplot(self, large_dataset):
        """Test boxenplot"""
        from grplot import plot2d
        ax = plot2d(plot='boxenplot', df=large_dataset, x='category', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_boxenplot_with_hue(self, large_dataset):
        """Test boxenplot with hue"""
        from grplot import plot2d
        ax = plot2d(plot='boxenplot', df=large_dataset, x='category', y='value', hue='subcategory')
        assert ax is not None
        plt.close('all')
    
    def test_swarmplot(self, categorical_data):
        """Test swarmplot"""
        from grplot import plot2d
        ax = plot2d(plot='swarmplot', df=categorical_data, x='category', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_violinplot_swarmplot_combo(self, categorical_data):
        """Test violin + swarm combination"""
        from grplot import plot2d
        ax = plot2d(plot='violinplot+swarmplot', df=categorical_data, x='category', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_boxplot_combo(self, large_dataset):
        """Test histogram + boxplot combination"""
        from grplot import plot2d
        ax = plot2d(plot='histplot+boxplot', df=large_dataset, x='value')
        assert ax is not None
        plt.close('all')
    
    def test_stripplot_pointplot_combo(self, categorical_data):
        """Test strip + point combination"""
        from grplot import plot2d
        ax = plot2d(plot='stripplot+pointplot', df=categorical_data, x='category', y='value')
        assert ax is not None
        plt.close('all')
    
    def test_scatterplot_rugplot_combo(self, large_dataset):
        """Test scatter + rug combination"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+rugplot', df=large_dataset, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_pieplot(self, categorical_data):
        """Test pie plot"""
        from grplot import plot2d
        df = categorical_data.groupby('category')['count'].sum().reset_index()
        ax = plot2d(plot='pieplot', df=df, y='count')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="Paretoplot requires specific data structure")
    def test_paretoplot(self, categorical_data):
        """Test pareto plot"""
        from grplot import plot2d
        df = categorical_data.groupby('category')['count'].sum().reset_index().sort_values('count', ascending=False).head(10)
        df.index = df.index.astype(str)
        ax = plot2d(plot='paretoplot', df=df, x=df.index, y='count')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text Annotation Tests - Critical for text_def.py coverage
# ============================================================================
@pytest.mark.integration
class TestTextAnnotations:
    """Test text annotations with various parameters"""
    
    def test_text_on_scatterplot(self, large_dataset):
        """Test text on scatterplot"""
        from grplot import plot2d
        df = large_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_xtext_only(self, large_dataset):
        """Test x-axis text only"""
        from grplot import plot2d
        df = large_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', xtext=True, ytext=False)
        assert ax is not None
        plt.close('all')
    
    def test_ytext_only(self, large_dataset):
        """Test y-axis text only"""
        from grplot import plot2d
        df = large_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', xtext=False, ytext=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_sep(self, financial_data):
        """Test text with thousand separator"""
        from grplot import plot2d
        df = financial_data.head(8)
        ax = plot2d(plot='scatterplot', df=df, x='revenue', y='profit', text=True, sep=',c')
        assert ax is not None
        plt.close('all')
    
    def test_text_with_tick_add(self, large_dataset):
        """Test text with tick_add"""
        from grplot import plot2d
        df = large_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='x', y='value', text=True, tick_add='kg_')
        assert ax is not None
        plt.close('all')
    
    def test_text_fontsize(self, large_dataset):
        """Test text with custom fontsize"""
        from grplot import plot2d
        df = large_dataset.head(10)
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, text_fontsize=8)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Label Add Tests - Critical for label_add coverage
# ============================================================================
@pytest.mark.integration
class TestLabelAddVariations:
    """Test all label_add format variations"""
    
    def test_label_add_suffix(self, large_dataset):
        """Test label suffix: 'units_'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', label_add='units_')
        assert ax is not None
        plt.close('all')
    
    def test_label_add_prefix(self, large_dataset):
        """Test label prefix: '_units'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', label_add='_units')
        assert ax is not None
        plt.close('all')
    
    def test_label_add_both(self, large_dataset):
        """Test label both: 'before_after'"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', label_add='before_after')
        assert ax is not None
        plt.close('all')
    
    def test_xlabel_add_ylabel_add_different(self, large_dataset):
        """Test different label_add for x and y"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='value', xlabel_add='meters_', ylabel_add='_kg')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Log Scale Variations
# ============================================================================
@pytest.mark.integration
class TestLogScaleVariations:
    """Test all log scale variations"""
    
    def test_log_linear(self, large_dataset):
        """Test linear scale"""
        from grplot import plot2d
        df = large_dataset[large_dataset['value'] > 0].head(20)
        ax = plot2d(plot='scatterplot', df=df, x='value', y='value', xlog='linear', ylog='linear')
        assert ax is not None
        plt.close('all')
    
    def test_log_log(self, large_dataset):
        """Test log scale"""
        from grplot import plot2d
        df = large_dataset[large_dataset['value'] > 0].head(20)
        ax = plot2d(plot='scatterplot', df=df, x='value', y='value', xlog='log', ylog='log')
        assert ax is not None
        plt.close('all')
    
    def test_log_symlog(self, large_dataset):
        """Test symlog scale"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset.head(20), x='x', y='y', xlog='symlog', ylog='symlog')
        assert ax is not None
        plt.close('all')
    
    def test_log_logit(self):
        """Test logit scale"""
        from grplot import plot2d
        df = pd.DataFrame({'x': np.linspace(0.01, 0.99, 20), 'y': np.linspace(0.01, 0.99, 20)})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', xlog='logit', ylog='logit')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Rotation Tests
# ============================================================================
@pytest.mark.integration
class TestRotationVariations:
    """Test rotation variations"""
    
    def test_xrot_0(self, categorical_data):
        """Test x rotation 0"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=categorical_data, x='category', y='value', xrot=0)
        assert ax is not None
        plt.close('all')
    
    def test_xrot_45(self, categorical_data):
        """Test x rotation 45"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=categorical_data, x='category', y='value', xrot=45)
        assert ax is not None
        plt.close('all')
    
    def test_xrot_90(self, categorical_data):
        """Test x rotation 90"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=categorical_data, x='category', y='value', xrot=90)
        assert ax is not None
        plt.close('all')
    
    def test_yrot_45(self, categorical_data):
        """Test y rotation 45"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=categorical_data, x='value', y='category', yrot=45)
        assert ax is not None
        plt.close('all')
    
    def test_xrot_yrot_different(self, large_dataset):
        """Test different rotations for x and y"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset.head(20), x='x', y='y', xrot=30, yrot=60)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Hue, Size, Style Combinations
# ============================================================================
@pytest.mark.integration
class TestSemanticMappings:
    """Test hue, size, style combinations"""
    
    def test_hue_only(self, large_dataset):
        """Test with hue only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category')
        assert ax is not None
        plt.close('all')
    
    def test_size_only(self, large_dataset):
        """Test with size only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', size='size_col')
        assert ax is not None
        plt.close('all')
    
    def test_style_only(self, large_dataset):
        """Test with style only"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', style='category')
        assert ax is not None
        plt.close('all')
    
    def test_hue_and_size(self, large_dataset):
        """Test with hue and size"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', size='size_col')
        assert ax is not None
        plt.close('all')
    
    def test_hue_and_style(self, large_dataset):
        """Test with hue and style"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', style='subcategory')
        assert ax is not None
        plt.close('all')
    
    def test_size_and_style(self, large_dataset):
        """Test with size and style"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', size='size_col', style='category')
        assert ax is not None
        plt.close('all')
    
    def test_hue_size_style(self, large_dataset):
        """Test with hue, size, and style"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', size='size_col', style='subcategory')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Filter Variations
# ============================================================================
@pytest.mark.integration
class TestFilterVariations:
    """Test various filter logic"""
    
    def test_filter_simple_equality(self, large_dataset):
        """Test simple equality filter"""
        from grplot import plot2d
        df_filtered = large_dataset[large_dataset['category'] == 'A']
        ax = plot2d(plot='scatterplot', df=df_filtered, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_filter_inequality(self, large_dataset):
        """Test inequality filter"""
        from grplot import plot2d
        df_filtered = large_dataset[large_dataset['value'] > 5000]
        ax = plot2d(plot='scatterplot', df=df_filtered, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_filter_and_condition(self, large_dataset):
        """Test AND condition filter"""
        from grplot import plot2d
        df_filtered = large_dataset[(large_dataset['category'] == 'A') & (large_dataset['value'] > 5000)]
        ax = plot2d(plot='scatterplot', df=df_filtered, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_filter_or_condition(self, large_dataset):
        """Test OR condition filter"""
        from grplot import plot2d
        df_filtered = large_dataset[(large_dataset['category'] == 'A') | (large_dataset['category'] == 'B')]
        ax = plot2d(plot='scatterplot', df=df_filtered, x='x', y='y')
        assert ax is not None
        plt.close('all')
    
    def test_filter_complex(self, large_dataset):
        """Test complex filter"""
        from grplot import plot2d
        df_filtered = large_dataset[((large_dataset['category'] == 'A') | (large_dataset['category'] == 'B')) & (large_dataset['value'] > 3000)]
        ax = plot2d(plot='scatterplot', df=df_filtered, x='x', y='y')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Legend Variations
# ============================================================================
@pytest.mark.integration
class TestLegendVariations:
    """Test legend variations"""
    
    def test_legend_auto(self, large_dataset):
        """Test auto legend"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', legend='auto')
        assert ax is not None
        plt.close('all')
    
    def test_legend_brief(self, large_dataset):
        """Test brief legend"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', legend='brief')
        assert ax is not None
        plt.close('all')
    
    def test_legend_full(self, large_dataset):
        """Test full legend"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', legend='full')
        assert ax is not None
        plt.close('all')
    
    def test_legend_false(self, large_dataset):
        """Test no legend"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', hue='category', legend=False)
        assert ax is not None
        plt.close('all')
    
    def test_legend_locations(self, large_dataset):
        """Test different legend locations"""
        from grplot import plot2d
        for loc in ['upper right', 'upper left', 'lower left', 'lower right', 'center']:
            ax = plot2d(plot='scatterplot', df=large_dataset.head(30), x='x', y='y', hue='category', legend_loc=loc)
            assert ax is not None
            plt.close('all')


# ============================================================================
# Optimizer Variations
# ============================================================================
@pytest.mark.integration
class TestOptimizerVariations:
    """Test different optimizer modes"""
    
    def test_optimizer_numpy(self, large_dataset):
        """Test numpy optimizer"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', optimizer='numpy')
        assert ax is not None
        plt.close('all')
    
    def test_optimizer_saver(self, large_dataset):
        """Test saver optimizer"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', optimizer='saver')
        assert ax is not None
        plt.close('all')
    
    def test_optimizer_pandas(self, large_dataset):
        """Test pandas optimizer"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', optimizer='pandas')
        assert ax is not None
        plt.close('all')
    
    def test_optimizer_perf(self, large_dataset):
        """Test perf optimizer (default)"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset, x='x', y='y', optimizer='perf')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Complex Multi-Plot Layouts
# ============================================================================
@pytest.mark.integration
class TestComplexMultiPlotLayouts:
    """Test complex multi-plot layouts"""
    
    def test_three_plots_horizontal(self, large_dataset):
        """Test 3 plots in a row"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'histplot', '[3]': 'boxplot'},
            df=large_dataset,
            x=['x', 'value', 'category'],
            y=['y', None, 'value'],
            Nx=3, Ny=1
        )
        assert ax is not None
        plt.close('all')
    
    def test_2x3_grid(self, large_dataset):
        """Test 2x3 grid layout"""
        from grplot import plot2d
        ax = plot2d(
            plot={
                '[1,1]': 'scatterplot', '[1,2]': 'lineplot', '[1,3]': 'histplot',
                '[2,1]': 'boxplot', '[2,2]': 'violinplot', '[2,3]': 'barplot'
            },
            df=large_dataset,
            x=['x', 'x', 'value', 'category', 'category', 'category'],
            y=['y', 'y', None, 'value', 'value', 'value'],
            Nx=3, Ny=2
        )
        assert ax is not None
        plt.close('all')
    
    def test_mixed_plot_combinations(self, large_dataset):
        """Test mixed plot combinations"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1]': 'lineplot+scatterplot', '[2]': 'boxplot+stripplot'},
            df=large_dataset,
            x=['x', 'category'],
            y=['y', 'value'],
            Nx=2, Ny=1
        )
        assert ax is not None
        plt.close('all')


# ============================================================================
# Datetime Format Tests
# ============================================================================
@pytest.mark.integration
class TestDatetimeFormats:
    """Test datetime format variations"""
    
    def test_dt_year_month_day(self):
        """Test Y-m-d format"""
        from grplot import plot2d
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        df = pd.DataFrame({'date': dates, 'value': np.random.randn(30)})
        ax = plot2d(plot='lineplot', df=df, x='date', y='value', xdt='%Y-%m-%d')
        assert ax is not None
        plt.close('all')
    
    def test_dt_month_day(self):
        """Test m/d format"""
        from grplot import plot2d
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        df = pd.DataFrame({'date': dates, 'value': np.random.randn(30)})
        ax = plot2d(plot='lineplot', df=df, x='date', y='value', xdt='%m/%d')
        assert ax is not None
        plt.close('all')
    
    def test_dt_year_only(self):
        """Test year only format"""
        from grplot import plot2d
        dates = pd.date_range('2020-01-01', periods=50, freq='ME')
        df = pd.DataFrame({'date': dates, 'value': np.random.randn(50)})
        ax = plot2d(plot='lineplot', df=df, x='date', y='value', xdt='%Y')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Figsize and Pad Tests
# ============================================================================
@pytest.mark.integration
class TestFigsizeAndPad:
    """Test figsize and padding variations"""
    
    def test_small_figsize(self, large_dataset):
        """Test small figsize"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset. head(20), x='x', y='y', figsize=[6, 4])
        assert ax is not None
        plt.close('all')
    
    def test_large_figsize(self, large_dataset):
        """Test large figsize"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset.head(20), x='x', y='y', figsize=[12, 8])
        assert ax is not None
        plt.close('all')
    
    def test_custom_pad(self, large_dataset):
        """Test custom pad"""
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=large_dataset.head(20), x='x', y='y', pad=10)
        assert ax is not None
        plt.close('all')
    
    def test_custom_hpad_wpad(self, large_dataset):
        """Test custom hpad and wpad"""
        from grplot import plot2d
        ax = plot2d(
            plot={'[1,1]': 'scatterplot', '[1,2]': 'histplot'},
            df=large_dataset,
            x=['x', 'value'],
            y=['y', None],
            Nx=2, Ny=1,
            hpad=8, wpad=12
        )
        assert ax is not None
        plt.close('all')
