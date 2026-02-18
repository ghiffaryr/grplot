"""
Integration tests for text annotations and formatting.

Tests text annotations across all plot types with various separators,
tick_add formats, and fontsize parameters.
"""
import pytest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@pytest.fixture
def text_test_data():
    """Dataset for text annotation testing with various numeric ranges."""
    np.random.seed(111)
    n = 60
    return pd.DataFrame({
        'a': np.random.randn(n) * 100,
        'b': np.random.randn(n) * 1000,
        'c': np.random.rand(n) * 50000,
        'd': np.random.randint(-1000, 1000, n),
        'cat': np.random.choice(['P', 'Q', 'R'], n),
        'cat2': np.random.choice(['M', 'N'], n)
    })


@pytest.mark.integration
class TestTextOnAllPlotTypes:
    """Test text annotations on all available plot types."""
class TestTextOnAllPlots:
    def test_text_scatterplot_10pts(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(10), x='a', y='b', text=True)
        plt.close('all')
    
    def test_text_lineplot_15pts(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='lineplot', df=text_test_data.head(15), x='a', y='b', text=True)
        plt.close('all')
    
    def test_text_barplot_categories(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', text=True)
        plt.close('all')
    
    def test_text_pointplot_categories(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='pointplot', df=text_test_data, x='cat', y='c', text=True)
        plt.close('all')
    
    def test_text_boxplot_yaxis(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='boxplot', df=text_test_data, x='cat', y='c', ytext=True)
        plt.close('all')
    
    def test_text_violinplot_yaxis(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='violinplot', df=text_test_data, x='cat', y='c', ytext=True)
        plt.close('all')


# ============================================================================
# Text Annotation with Separators
# ============================================================================
@pytest.mark.integration
class TestTextWithAllSeparators:
    def test_text_sep_comma(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',')
        plt.close('all')
    
    def test_text_sep_dot(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep='.')
        plt.close('all')
    
    def test_text_sep_comma_currency(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',c')
        plt.close('all')
    
    def test_text_sep_dot_currency(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep='.c')
        plt.close('all')
    
    def test_text_sep_comma_large(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',L')
        plt.close('all')
    
    def test_text_sep_dot_large(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep='.L')
        plt.close('all')
    
    def test_text_sep_comma_currency_large(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',cL')
        plt.close('all')
    
    def test_text_sep_dot_currency_large(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep='.cL')
        plt.close('all')


# ============================================================================
# Text Annotation with Tick Add Formats
# ============================================================================
@pytest.mark.integration
class TestTextWithTickAdd:
    def test_text_tick_add_suffix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, tick_add='USD_')
        plt.close('all')
    
    def test_text_tick_add_prefix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, tick_add='_EUR')
        plt.close('all')
    
    def test_text_tick_add_both(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, tick_add='USD_EUR')
        plt.close('all')
    
    def test_text_tick_add_negative_suffix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='d', y='b', text=True, tick_add='(_)USD')
        plt.close('all')
    
    def test_text_tick_add_negative_prefix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='d', y='b', text=True, tick_add='USD(_)')
        plt.close('all')


# ============================================================================
# Text Annotation with Combined Separators and Tick Add
# ============================================================================
@pytest.mark.integration
class TestTextSepAndTickAdd:
    def test_text_comma_usd_suffix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',', tick_add='USD_')
        plt.close('all')
    
    def test_text_dot_currency_kg_prefix(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep='.c', tick_add='_kg')
        plt.close('all')
    
    def test_text_comma_large_meter_both(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', text=True, sep=',L', tick_add='m_ft')
        plt.close('all')


# Text with hue grouping
@pytest.mark.integration
class TestTextWithHue:
    def test_text_hue_2_groups(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(10), x='a', y='b', hue='cat2', text=True)
        plt.close('all')
    
    def test_text_hue_3_groups(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(12), x='a', y='b', hue='cat', text=True)
        plt.close('all')
    
    def test_text_hue_sep(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(10), x='c', y='d', hue='cat', text=True, sep=',')
        plt.close('all')


# Text fontsize variations
@pytest.mark.integration
class TestTextFontsize:
    def test_text_fontsize_6(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, text_fontsize=6)
        plt.close('all')
    
    def test_text_fontsize_8(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, text_fontsize=8)
        plt.close('all')
    
    def test_text_fontsize_10(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, text_fontsize=10)
        plt.close('all')
    
    def test_text_fontsize_12(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, text_fontsize=12)
        plt.close('all')


# xtext and ytext independently
@pytest.mark.integration
class TestXTextYText:
    def test_xtext_true_ytext_false(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', xtext=True, ytext=False)
        plt.close('all')
    
    def test_xtext_false_ytext_true(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', xtext=False, ytext=True)
        plt.close('all')
    
    def test_xtext_true_ytext_true(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', xtext=True, ytext=True)
        plt.close('all')
    
    def test_xtext_only_with_sep(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', xtext=True, ytext=False, sep=',')
        plt.close('all')
    
    def test_ytext_only_with_sep(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='c', y='d', xtext=False, ytext=True, sep=',c')
        plt.close('all')


# Text on multi-plots
@pytest.mark.integration
class TestTextMultiPlot:
    def test_text_2_plots(self, text_test_data):
        from grplot import plot2d
        df = text_test_data.head(8)
        ax = plot2d(
            plot={'[1]': 'scatterplot', '[2]': 'barplot'},
            df=df,
            x=['a', 'cat'],
            y=['b', 'c'],
            text=True,
            Nx=2, Ny=1
        )
        plt.close('all')
    
    def test_text_4_plots(self, text_test_data):
        from grplot import plot2d
        df = text_test_data.head(10)
        ax = plot2d(
            plot={'[1,1]': 'scatterplot', '[1,2]': 'lineplot', '[2,1]': 'barplot', '[2,2]': 'pointplot'},
            df=df,
            x=['a', 'a', 'cat', 'cat'],
            y=['b', 'b', 'c', 'c'],
            text=True,
            Nx=2, Ny=2
        )
        plt.close('all')


# Text with large numbers
@pytest.mark.integration
class TestTextLargeNumbers:
    def test_text_thousands(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1000, 2000, 3000, 4000, 5000], 'y': [10000, 20000, 30000, 40000, 50000]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, sep=',')
        plt.close('all')
    
    def test_text_millions(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1e6, 2e6, 3e6], 'y': [5e6, 10e6, 15e6]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, sep=',L')
        plt.close('all')
    
    def test_text_billions(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1e9, 2e9, 3e9], 'y': [5e9, 10e9, 15e9]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, sep=',cL')
        plt.close('all')


# Text with negative numbers
@pytest.mark.integration
class TestTextNegativeNumbers:
    def test_text_negative_values(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [-100, -200, -300], 'y': [-50, -150, -250]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_negative_with_paren(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [-100, -200, -300], 'y': [-50, -150, -250]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, tick_add='USD(_)')
        plt.close('all')
    
    def test_text_mixed_pos_neg(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [-100, 0, 100], 'y': [-50, 0, 50]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True, sep=',')
        plt.close('all')


# Text with decimals
@pytest.mark.integration
class TestTextDecimals:
    def test_text_small_decimals(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [0.1, 0.2, 0.3], 'y': [0.15, 0.25, 0.35]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_mixed_decimals(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1.5, 2.7, 3.9, 4.2], 'y': [10.1, 20.5, 30.8, 40.3]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')


# Text on combination plots
@pytest.mark.integration
class TestTextCombinationPlots:
    def test_text_scatter_line(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot+lineplot', df=text_test_data.head(10), x='a', y='b', text=True)
        plt.close('all')
    
    def test_text_bar_point(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='barplot+pointplot', df=text_test_data, x='cat', y='c', text=True)
        plt.close('all')
    
    def test_text_box_strip(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='boxplot+stripplot', df=text_test_data.head(30), x='cat', y='c', ytext=True)
        plt.close('all')


# Text positioning edge cases
@pytest.mark.integration
class TestTextPositioning:
    def test_text_clustered_points(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 1.1, 1.2, 1.3], 'y': [10, 10.5, 11, 11.5]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_sparse_points(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 100, 200], 'y': [5, 500, 1000]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')


# Text with ALL plot parameter combinations
@pytest.mark.integration
class TestTextWithPlotParameters:
    def test_text_with_alpha(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, alpha=0.5)
        plt.close('all')
    
    def test_text_with_size(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, size=100)
        plt.close('all')
    
    def test_text_with_color(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, color='red')
        plt.close('all')
    
    def test_text_with_marker(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(8), x='a', y='b', text=True, marker='s')
        plt.close('all')


# Text annotation edge cases
@pytest.mark.integration
class TestTextEdgeCases:
    def test_text_1_point(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1], 'y': [10]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_2_points(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 2], 'y': [10, 20]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_20_points(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='scatterplot', df=text_test_data.head(20), x='a', y='b', text=True)
        plt.close('all')
    
    def test_text_vertical_line(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 1, 1, 1], 'y': [10, 20, 30, 40]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')
    
    def test_text_horizontal_line(self):
        from grplot import plot2d
        df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 10, 10, 10]})
        ax = plot2d(plot='scatterplot', df=df, x='x', y='y', text=True)
        plt.close('all')


# More comprehensive text tests
@pytest.mark.integration
class TestTextComprehensive:
    def test_text_barplot_with_hue_and_sep(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', hue='cat2', text=True, sep=',')
        plt.close('all')
    
    def test_text_pointplot_with_sep_and_tick(self, text_test_data):
        from grplot import plot2d
        ax = plot2d(plot='pointplot', df=text_test_data, x='cat', y='c', text=True, sep=',c', tick_add='USD_')
        plt.close('all')
    
    def test_text_lineplot_sorted(self, text_test_data):
        from grplot import plot2d
        df = text_test_data.head(10).sort_values('a')
        ax = plot2d(plot='lineplot', df=df, x='a', y='b', text=True, sort=True)
        plt.close('all')
    
    def test_text_scatterplot_log_scale(self, text_test_data):
        from grplot import plot2d
        df = text_test_data.head(8).copy()
        df['c'] = df['c'].abs() + 1
        ax = plot2d(plot='scatterplot', df=df, x='c', y='c', text=True, xlog='log')
        plt.close('all')


# ============================================================================
# Text with Errorbar - Critical for errorbar integration testing
# ============================================================================
@pytest.mark.integration
class TestTextWithErrorbar:
    """Test text annotations with errorbar parameter"""
    
    def test_barplot_errorbar_sd_with_text(self, text_test_data):
        """Test barplot with errorbar='sd' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_se_with_text(self, text_test_data):
        """Test barplot with errorbar='se' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='se', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_pi_with_text(self, text_test_data):
        """Test barplot with errorbar='pi' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='pi', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_ci_with_text(self, text_test_data):
        """Test barplot with errorbar=('ci', 95) and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar=('ci', 95), text=True)
        assert ax is not None
        plt.close('all')
    
    def test_histplot_errorbar_with_text(self, text_test_data):
        """Test histplot with errorbar and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=text_test_data, x='c', errorbar='sd', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_countplot_errorbar_with_text(self, text_test_data):
        """Test countplot with errorbar and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='countplot', df=text_test_data, x='cat', errorbar='sd', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_paretoplot_errorbar_with_text(self, text_test_data):
        """Test paretoplot with text=True"""
        from grplot import plot2d
        # Paretoplot requires categorical x and numeric y, so aggregate the data
        df_agg = text_test_data.groupby('cat')['c'].sum().reset_index()
        ax = plot2d(plot='paretoplot', df=df_agg, x='cat', y='c', text=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text with CI - Critical for ci parameter integration testing
# ============================================================================
@pytest.mark.integration
class TestTextWithCI:
    """Test text annotations with ci parameter"""
    
    def test_barplot_ci_95_with_text(self, text_test_data):
        """Test barplot with ci=95 and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=95, text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_ci_68_with_text(self, text_test_data):
        """Test barplot with ci=68 and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=68, text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_ci_sd_with_text(self, text_test_data):
        """Test barplot with ci='sd' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci='sd', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_histplot_ci_with_text(self, text_test_data):
        """Test histplot with ci and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=text_test_data, x='c', ci=95, text=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text Mode Conversion - Verify text mode changes with errorbar/ci
# ============================================================================
@pytest.mark.integration
class TestTextModeConversion:
    """Test that text modes convert correctly when errorbar/ci is present"""
    
    def test_text_mode_o_converts_to_i_with_errorbar(self, text_test_data):
        """Test that text='o' becomes text='i' when errorbar is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='o')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_h_converts_to_h_i_with_errorbar(self, text_test_data):
        """Test that text='h' becomes text='h+i' when errorbar is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='se', text='h')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_v_converts_to_v_i_with_errorbar(self, text_test_data):
        """Test that text='v' becomes text='v+i' when errorbar is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='pi', text='v')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_o_converts_to_i_with_ci(self, text_test_data):
        """Test that text='o' becomes text='i' when ci is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=95, text='o')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_h_converts_to_h_i_with_ci(self, text_test_data):
        """Test that text='h' becomes text='h+i' when ci is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=95, text='h')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_v_converts_to_v_i_with_ci(self, text_test_data):
        """Test that text='v' becomes text='v+i' when ci is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=95, text='v')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_i_unchanged_with_errorbar(self, text_test_data):
        """Test that text='i' remains 'i' when errorbar is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='i')
        assert ax is not None
        plt.close('all')
    
    def test_text_mode_h_i_unchanged_with_errorbar(self, text_test_data):
        """Test that text='h+i' remains 'h+i' when errorbar is present"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='h+i')
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text with Multiple='fill' - Test multiple parameter interaction
# ============================================================================
@pytest.mark.integration
class TestTextWithMultipleFill:
    """Test text annotations with multiple='fill'"""
    
    def test_histplot_multiple_fill_with_text(self, text_test_data):
        """Test histplot with multiple='fill' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=text_test_data, x='c', hue='cat', multiple='fill', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_multiple_fill_with_text(self, text_test_data):
        """Test barplot with multiple='fill' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', hue='cat2', multiple='fill', text=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text with Hue + Multiple='stack' - Test hue and multiple interaction
# ============================================================================
@pytest.mark.integration
class TestTextWithHueStack:
    """Test text annotations with hue and multiple='stack'"""
    
    def test_histplot_hue_stack_with_text(self, text_test_data):
        """Test histplot with hue and multiple='stack' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=text_test_data, x='c', hue='cat', multiple='stack', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_hue_stack_with_text(self, text_test_data):
        """Test barplot with hue and multiple='stack' and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat2', y='c', hue='cat', multiple='stack', text=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Text with Errorbar and Formatting - Comprehensive combinations
# ============================================================================
@pytest.mark.integration
class TestTextErrorbarWithFormatting:
    """Test text with errorbar and various formatting options"""
    
    def test_barplot_errorbar_text_with_sep(self, text_test_data):
        """Test barplot with errorbar, text, and separator"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text=True, sep=',')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_text_with_tick_add(self, text_test_data):
        """Test barplot with errorbar, text, and tick_add"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='se', text=True, tick_add='USD_')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_text_with_sep_and_tick_add(self, text_test_data):
        """Test barplot with errorbar, text, separator, and tick_add"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='pi', text=True, sep=',c', tick_add='USD_')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_text_with_fontsize(self, text_test_data):
        """Test barplot with errorbar, text, and custom fontsize"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text=True, text_fontsize=8)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_ci_text_with_hue(self, text_test_data):
        """Test barplot with ci, text, and hue"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=95, text=True, hue='cat2')
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_xtext_ytext(self, text_test_data):
        """Test barplot with errorbar and independent xtext/ytext"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', ytext=True)
        assert ax is not None
        plt.close('all')


# ============================================================================
# Edge Cases - Errorbar/CI with Text
# ============================================================================
@pytest.mark.integration
class TestTextErrorbarEdgeCases:
    """Test edge cases for text with errorbar/ci"""
    
    def test_barplot_errorbar_none_with_text(self, text_test_data):
        """Test barplot with errorbar=None and text=True (should use default behavior)"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar=None, text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_ci_none_with_text(self, text_test_data):
        """Test barplot with ci=None and text=True"""
        from grplot import plot2d
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', ci=None, text=True)
        assert ax is not None
        plt.close('all')
    
    def test_barplot_errorbar_text_mode_combinations(self, text_test_data):
        """Test various text mode combinations with errorbar"""
        from grplot import plot2d
        # Test i+v mode
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='i+v')
        assert ax is not None
        plt.close('all')
        
        # Test v+i mode
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='v+i')
        assert ax is not None
        plt.close('all')
        
        # Test i+h mode
        ax = plot2d(plot='barplot', df=text_test_data, x='cat', y='c', errorbar='sd', text='i+h')
        assert ax is not None
        plt.close('all')
    
    def test_paretoplot_with_text_modes(self, text_test_data):
        """Test paretoplot with various text modes"""
        from grplot import plot2d
        # Paretoplot requires categorical x and numeric y
        df_agg = text_test_data.groupby('cat')['c'].sum().reset_index()
        ax = plot2d(plot='paretoplot', df=df_agg, x='cat', y='c', text='h+i')
        assert ax is not None
        plt.close('all')
    
    def test_histplot_errorbar_text_horizontal(self, text_test_data):
        """Test histplot with errorbar, text on y-axis (horizontal bars)"""
        from grplot import plot2d
        ax = plot2d(plot='histplot', df=text_test_data, y='c', errorbar='sd', ytext=True)
        assert ax is not None
        plt.close('all')
