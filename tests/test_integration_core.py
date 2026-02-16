"""
Basic integration tests for grplot visualization library.

Tests core plot types and fundamental functionality through the plot2d() API.
"""
import pytest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@pytest.fixture
def tips_sample():
    """Sample data similar to seaborn tips dataset"""
    return pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female'],
        'smoker': ['No', 'No', 'No', 'Yes', 'No'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner'],
        'size': [2, 3, 3, 2, 4]
    })


@pytest.fixture
def numeric_sample():
    """Numeric data for various plots"""
    np.random.seed(42)
    return pd.DataFrame({
        'x': np.random.randn(50),
        'y': np.random.randn(50),
        'value': np.random.rand(50) * 100,
        'category': np.random.choice(['A', 'B', 'C'], 50)
    })


@pytest.fixture
def time_series_sample():
    """Time series data"""
    dates = pd.date_range('2020-01-01', periods=50, freq='D')
    return pd.DataFrame({
        'date': dates,
        'value': np.cumsum(np.random.randn(50)) + 100,
        'category': np.random.choice(['A', 'B'], 50)
    })


# ============================================================================
# Relational Plots - Based on Documentation Notebook Examples
# ============================================================================
@pytest.mark.integration
class TestRelationalPlotsWorking:
    """Working integration tests for relational plots"""
    
    def test_scatterplot_basic(self, tips_sample):
        """Scatterplot from documentation"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=tips_sample,
            x='tip',
            y='total_bill',
            sep='.c',
            tick_add='Rp(_)',
            text=True,
            title='total_bill vs tip rate'
        )
        assert ax is not None
        plt.close('all')
    
    def test_lineplot_scatterplot_combo(self, tips_sample):
        """Combined lineplot + scatterplot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='lineplot+scatterplot',
            df=tips_sample,
            x='tip',
            y='total_bill',
            title='Combined Plot'
        )
        
        plt.close("all")
    
    def test_lineplot_with_hue(self, tips_sample):
        """Lineplot with hue grouping"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='lineplot',
            df=tips_sample,
            x='size',
            y='total_bill',
            hue='sex',
            title='Bill by Party Size and Gender'
        )
        
        plt.close("all")


# ============================================================================
# Distribution Plots - Based on Documentation Notebook
# ============================================================================
@pytest.mark.integration
class TestDistributionPlotsWorking:
    """Working integration tests for distribution plots"""
    
    def test_histplot_basic(self, numeric_sample):
        """Basic histogram"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='histplot',
            df=numeric_sample,
            x='x',
            title='Distribution of X'
        )
        
        plt.close("all")
    
    def test_histplot_with_hue(self, numeric_sample):
        """Histogram with category hue"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='histplot',
            df=numeric_sample,
            x='value',
            hue='category',
            title='Value Distribution by Category'
        )
        
        plt.close("all")
    
    def test_kdeplot_basic(self, numeric_sample):
        """Basic KDE plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='kdeplot',
            df=numeric_sample,
            x='x',
            title='Density Estimation'
        )
        
        plt.close("all")
    
    def test_ecdfplot_basic(self, numeric_sample):
        """ECDF plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='ecdfplot',
            df=numeric_sample,
            x='value',
            title='Empirical CDF'
        )
        
        plt.close("all")
    
    def test_rugplot_combo(self, numeric_sample):
        """KDE + rugplot combination"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='kdeplot+rugplot',
            df=numeric_sample,
            x='x',
            title='Density with Rug'
        )
        
        plt.close("all")


# ============================================================================
# Categorical Plots - Based on Documentation Notebook
# ============================================================================
@pytest.mark.integration
class TestCategoricalPlotsWorking:
    """Working integration tests for categorical plots"""
    
    def test_stripplot_basic(self, tips_sample):
        """Basic strip plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='stripplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            title='Bills by Day'
        )
        
        plt.close("all")
    
    def test_boxplot_stripplot_combo(self, tips_sample):
        """Boxplot + stripplot combination"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='boxplot+stripplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            hue='sex',
            title='Bills by Day and Gender'
        )
        
        plt.close("all")
    
    def test_violinplot_basic(self, tips_sample):
        """Basic violin plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='violinplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            title='Bill Distribution by Day'
        )
        
        plt.close("all")
    
    def test_boxplot_basic(self, tips_sample):
        """Basic box plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='boxplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            title='Bill Statistics by Day'
        )
        
        plt.close("all")
    
    def test_pointplot_basic(self, tips_sample):
        """Basic point plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='pointplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            title='Average Bill by Day'
        )
        
        plt.close("all")
    
    def test_barplot_basic(self, tips_sample):
        """Basic bar plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='barplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            title='Total Bill by Day'
        )
        
        plt.close("all")
    
    def test_barplot_with_hue(self, tips_sample):
        """Bar plot with hue"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='barplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            hue='sex',
            title='Bill by Day and Gender'
        )
        
        plt.close("all")


# ============================================================================
# Regression Plots - Based on Documentation Notebook
# ============================================================================
@pytest.mark.integration
class TestRegressionPlotsWorking:
    """Working integration tests for regression plots"""
    
    def test_regplot_basic(self, numeric_sample):
        """Basic regression plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='regplot',
            df=numeric_sample,
            x='x',
            y='y',
            title='Regression Analysis'
        )
        
        plt.close("all")
    
    def test_residplot_basic(self, numeric_sample):
        """Basic residual plot"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='residplot',
            df=numeric_sample,
            x='x',
            y='y',
            title='Residuals'
        )
        
        plt.close("all")


# ============================================================================
# Advanced Features - sep, tick_add, text, limits
# ============================================================================
@pytest.mark.integration
class TestAdvancedFeaturesWorking:
    """Test advanced features like separators, tick additions, text"""
    
    def test_thousand_separator(self, numeric_sample):
        """Test thousand separator feature"""
        from grplot import plot2d
        
        df = numeric_sample.copy()
        df['large_value'] = df['value'] * 1000
        
        ax = plot2d(
            plot='scatterplot',
            df=df,
            x='x',
            y='large_value',
            sep=',',
            title='With Thousand Separator'
        )
        
        plt.close("all")
    
    def test_currency_separator(self, tips_sample):
        """Test currency separator (.c)"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=tips_sample,
            x='tip',
            y='total_bill',
            sep='.c',
            title='Currency Format'
        )
        
        plt.close("all")
    
    def test_tick_add_unit(self, numeric_sample):
        """Test tick_add for units"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=numeric_sample,
            x='x',
            y='value',
            tick_add='kg_',
            title='With Unit'
        )
        
        plt.close("all")
    
    def test_log_scale(self):
        """Test logarithmic scale"""
        from grplot import plot2d
        
        df = pd.DataFrame({
            'x': [1, 10, 100, 1000, 10000],
            'y': [1, 10, 100, 1000, 10000]
        })
        
        ax = plot2d(
            plot='scatterplot',
            df=df,
            x='x',
            y='y',
            xlog='log',
            ylog='log',
            title='Log Scale'
        )
        
        plt.close("all")
    
    def test_axis_limits(self, numeric_sample):
        """Test xlim and ylim"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=numeric_sample,
            x='x',
            y='y',
            xlim=[-2, 2],
            ylim=[-2, 2],
            title='With Limits'
        )
        
        plt.close("all")
    
    def test_custom_labels(self, numeric_sample):
        """Test custom axis labels"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=numeric_sample,
            x='x',
            y='y',
            xlabel='Custom X Label',
            ylabel='Custom Y Label',
            title='Custom Labels'
        )
        
        plt.close("all")
    
    def test_filter_data(self, numeric_sample):
        """Test data filtering"""
        from grplot import plot2d
        
        df_filtered = numeric_sample[numeric_sample['category'] == 'A']
        ax = plot2d(
            plot='scatterplot',
            df=df_filtered,
            x='x',
            y='y',
            title='Filtered Data'
        )
        
        plt.close("all")


# ============================================================================
# Multi-plot Layouts - Based on Documentation Notebook
# ============================================================================
@pytest.mark.integration
class TestMultiPlotLayouts:
    """Test multi-panel plot layouts"""
    
    def test_two_plots_horizontal(self, tips_sample):
        """Two plots side by side"""
        from grplot import plot2d
        
        ax = plot2d(
            plot={'[1]': 'lineplot+scatterplot', '[2]': 'histplot'},
            df=tips_sample,
            x=['tip', 'total_bill'],
            y=['total_bill', None],
            Nx=2,
            Ny=1
        )
        
        plt.close("all")
    
    def test_grid_layout(self, tips_sample):
        """2x2 grid of plots"""
        from grplot import plot2d
        
        ax = plot2d(
            plot={
                '[1,1]': 'histplot',
                '[1,2]': 'boxplot',
                '[2,1]': 'violinplot',
                '[2,2]': 'stripplot'
            },
            df=tips_sample,
            x=['total_bill', 'day', 'day', 'day'],
            y=[None, 'total_bill', 'total_bill', 'total_bill'],
            Nx=2,
            Ny=2
        )
        
        plt.close("all")


# ============================================================================
# Font and Styling Tests
# ============================================================================
@pytest.mark.integration
class TestFontAndStyling:
    """Test font sizes and styling options"""
    
    def test_custom_fontsize(self, numeric_sample):
        """Test custom font sizes"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=numeric_sample,
            x='x',
            y='y',
            fontsize=12,
            tick_fontsize=10,
            label_fontsize=14,
            title_fontsize=16,
            title='Custom Fonts'
        )
        
        plt.close("all")
    
    def test_legend_location(self, tips_sample):
        """Test legend location"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='scatterplot',
            df=tips_sample,
            x='tip',
            y='total_bill',
            hue='sex',
            legend_loc='upper right',
            title='Legend Test'
        )
        
        plt.close("all")
    
    def test_rotation(self, tips_sample):
        """Test tick rotation"""
        from grplot import plot2d
        
        ax = plot2d(
            plot='barplot',
            df=tips_sample,
            x='day',
            y='total_bill',
            xrot=45,
            title='Rotated Ticks'
        )
        
        plt.close("all")


# ============================================================================
# Edge Cases and Error Handling
# ============================================================================
@pytest.mark.integration
class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_single_point(self):
        """Test with single data point"""
        from grplot import plot2d
        
        df = pd.DataFrame({'x': [1], 'y': [1]})
        
        ax = plot2d(
            plot='scatterplot',
            df=df,
            x='x',
            y='y',
            title='Single Point'
        )
        
        plt.close("all")
    
    def test_empty_categories(self):
        """Test with minimal category data"""
        from grplot import plot2d
        
        df = pd.DataFrame({
            'cat': ['A', 'A'],
            'val': [1, 2]
        })
        
        ax = plot2d(
            plot='barplot',
            df=df,
            x='cat',
            y='val',
            title='Minimal Categories'
        )
        
        plt.close("all")
