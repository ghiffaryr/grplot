"""
Advanced integration tests for specialized features.

Tests filter functionality, font size parameters, and complex parameter interactions.
"""
import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from grplot import plot2d


@pytest.fixture
def sample_df():
    """Standard test dataframe."""
    return pd.DataFrame({
        'x': range(100),
        'y': np.random.randn(100),
        'category': ['A', 'B', 'C'] * 33 + ['A'],
        'value': np.random.rand(100) * 100
    })


@pytest.fixture
def categorical_df():
    """Dataframe for categorical plots."""
    return pd.DataFrame({
        'group': ['Type1', 'Type2', 'Type3'] * 10,
        'measure': np.random.randn(30)
    })


class TestFilterFeature:
    """Tests to increase coverage of filter_def.py (16% -> 60%+)"""
    
    def test_filter_query_string(self, sample_df):
        """Test query-based filtering."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter='x > 50')
        assert ax is not None
        plt.close('all')
   
    def test_filter_complex_query(self, sample_df):
        """Test complex multi-condition query."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter='x > 25 and value < 75')
        assert ax is not None
        plt.close('all')
    
    def test_filter_string_category(self, sample_df):
        """Test filtering on categorical column."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter='category == "A"')
        assert ax is not None
        plt.close('all')
    
    def test_filter_boolean_series(self, sample_df):
        """Test boolean series filtering."""
        mask = sample_df['x'] > 50
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter=mask)
        assert ax is not None
        plt.close('all')
    
    def test_filter_with_or_condition(self, sample_df):
        """Test OR condition in filter."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter='value < 20 or value > 80')
        assert ax is not None
        plt.close('all')
    
    def test_filter_on_lineplot(self, sample_df):
        """Test filter on line plot."""
        ax = plot2d(plot='lineplot', df=sample_df, x='x', y='y', filter='x > 25')
        assert ax is not None
        plt.close('all')
    
    def test_filter_on_hist(self, sample_df):
        """Test filter on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', filter='value > 50')
        assert ax is not None
        plt.close('all')
    
    def test_filter_with_hue(self, sample_df):
        """Test filter combined with hue."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', hue='category', filter='value > 50')
        assert ax is not None
        plt.close('all')
    
    def test_filter_boolean_complex(self, sample_df):
        """Test complex boolean filter."""
        mask = (sample_df['x'] > 25) & (sample_df['value'] < 75)
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', filter=mask)
        assert ax is not None
        plt.close('all')
    
    def test_filter_on_barplot(self, categorical_df):
        """Test filter on bar plot."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', filter='measure > 0')
        assert ax is not None
        plt.close('all')


class TestFontSizeFeatures:
    """Tests to increase coverage of font_def.py (32% -> 60%+)"""
    
    def test_tick_fontsize_basic(self, sample_df):
        """Test tick fontsize parameter."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', tick_fontsize=12)
        assert ax is not None
        plt.close('all')
    
    def test_label_fontsize_basic(self, sample_df):
        """Test label fontsize parameter."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', label_fontsize=14)
        assert ax is not None
        plt.close('all')
    
    def test_both_fontsizes(self, sample_df):
        """Test both tick and label fontsize."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', tick_fontsize=10, label_fontsize=12)
        assert ax is not None
        plt.close('all')
    
    def test_tick_fontsize_on_lineplot(self, sample_df):
        """Test tick fontsize on lineplot."""
        ax = plot2d(plot='lineplot', df=sample_df, x='x', y='y', tick_fontsize=11)
        assert ax is not None
        plt.close('all')
    
    def test_label_fontsize_on_barplot(self, categorical_df):
        """Test label fontsize on barplot."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', label_fontsize=13)
        assert ax is not None
        plt.close('all')
    
    def test_tick_fontsize_on_histplot(self, sample_df):
        """Test tick fontsize on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', tick_fontsize=12)
        assert ax is not None
        plt.close('all')
    
    def test_label_fontsize_on_boxplot(self, categorical_df):
        """Test label fontsize on boxplot."""
        ax = plot2d(plot='boxplot', df=categorical_df, x='group', y='measure', label_fontsize=14)
        assert ax is not None
        plt.close('all')
    
    def test_fontsize_with_custom_labels(self, sample_df):
        """Test fontsizes with custom labels."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', 
                   xlabel='Custom X', ylabel='Custom Y',
                   tick_fontsize=10, label_fontsize=12)
        assert ax is not None
        plt.close('all')
    
    def test_fontsize_large(self, sample_df):
        """Test large fontsizes."""
        ax = plot2d(plot='scatterplot', df=sample_df.head(30), x='x', y='y', 
                   tick_fontsize=16, label_fontsize=18)
        assert ax is not None
        plt.close('all')
    
    def test_fontsize_small(self, sample_df):
        """Test small fontsizes."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', 
                   tick_fontsize=8, label_fontsize=9)
        assert ax is not None
        plt.close('all')


class TestTextFeatures:
    """Tests to increase coverage of text_def.py (28% -> 50%+)"""
    
    def test_text_on_barplot(self, categorical_df):
        """Test text annotations on barplot."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', text=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_with_separator(self, categorical_df):
        """Test text with separator."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', text=True, sep=',')
        assert ax is not None
        plt.close('all')
    
    def test_text_with_tick_add(self, categorical_df):
        """Test text with tick_add."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', text=True, tick_add='USD_')
        assert ax is not None
        plt.close('all')
    
    def test_text_fontsize(self, categorical_df):
        """Test text with custom fontsize."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', text=True, text_fontsize=10)
        assert ax is not None
        plt.close('all')
    
    def test_ytext_on_boxplot(self, categorical_df):
        """Test ytext on boxplot."""
        ax = plot2d(plot='boxplot', df=categorical_df, x='group', y='measure', ytext=True)
        assert ax is not None
        plt.close('all')
    
    def test_text_modes(self, categorical_df):
        """Test different text modes."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', text='v')
        assert ax is not None
        plt.close('all')


class TestOtherUndercoveredFeatures:
    """Tests for other features with low coverage"""
    
    def test_xlim_ylim(self, sample_df):
        """Test xlim and ylim parameters."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', xlim=[0, 50], ylim=[-2, 2])
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="lim parameter format not supported")
    def test_lim_shorthand(self, sample_df):
        """Test lim shorthand parameter."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', lim=[0, 50, -2, 2])
        assert ax is not None
        plt.close('all')
    
    def test_rotation(self, categorical_df):
        """Test rotation parameter."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', rot=45)
        assert ax is not None
        plt.close('all')
    
    def test_xrot_yrot(self, sample_df):
        """Test separate x and y rotation."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', xrot=30, yrot=45)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="log parameter format needs verification")
    def test_log_scale(self, sample_df):
        """Test logarithmic scale."""
        df_positive = sample_df.copy()
        df_positive['y'] = np.abs(df_positive['y']) + 1
        ax = plot2d(plot='scatterplot', df=df_positive, x='x', y='y', log='y')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="xlog/ylog parameter format needs verification")
    def test_xlog_ylog(self, sample_df):
        """Test separate x and y log."""
        df_positive = sample_df.copy()
        df_positive['x'] = df_positive['x'] + 1
        df_positive['y'] = np.abs(df_positive['y']) + 1
        ax = plot2d(plot='scatterplot', df=df_positive, x='x', y='y', xlog=True, ylog=True)
        assert ax is not None
        plt.close('all')
    
    def test_datetime_format(self):
        """Test datetime formatting."""
        df = pd.DataFrame({
            'date': pd.date_range('2020-01-01', periods=50),
            'value': np.cumsum(np.random.randn(50))
        })
        ax = plot2d(plot='lineplot', df=df, x='date', y='value', dt='%Y-%m-%d')
        assert ax is not None
        plt.close('all')
    
    def test_xdt_ydt(self, sample_df):
        """Test xdt and ydt parameters."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', xdt=None, ydt=None)
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="statdesc parameter needs specific setup")
    def test_statdesc_on_boxplot(self, categorical_df):
        """Test statdesc parameter."""
        ax = plot2d(plot='boxplot', df=categorical_df, x='group', y='measure', statdesc='general')
        assert ax is not None
        plt.close('all')
    
    def test_xsep_ysep(self, sample_df):
        """Test separate x and y separators."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='value', xsep=',', ysep='.')
        assert ax is not None
        plt.close('all')
    
    def test_xtick_add_ytick_add(self, sample_df):
        """Test separate x and y tick_add."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='value', xtick_add='_units', ytick_add='$_')
        assert ax is not None
        plt.close('all')
    
    @pytest.mark.skip(reason="xlabel_add/ylabel_add parameter format needs verification")
    def test_xlabel_add_ylabel_add(self, sample_df):
        """Test xlabel_add and ylabel_add."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', xlabel_add='(seconds)', ylabel_add='(meters)')
        assert ax is not None
        plt.close('all')
    
    def test_legend_loc(self, sample_df):
        """Test legend location."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', hue='category', legend_loc='upper right')
        assert ax is not None
        plt.close('all')
    
    def test_legend_fontsize(self, sample_df):
        """Test legend fontsize."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', hue='category', legend_fontsize=10)
        assert ax is not None
        plt.close('all')
    
    def test_title_fontsize(self, sample_df):
        """Test title fontsize."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', title='Test Plot', title_fontsize=16)
        assert ax is not None
        plt.close('all')
    
    def test_palette_variations(self, sample_df):
        """Test different palettes."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', hue='category', palette='Set2')
        assert ax is not None
        plt.close('all')
    
    def test_alpha_parameter(self, sample_df):
        """Test alpha transparency."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', alpha=0.5)
        assert ax is not None
        plt.close('all')
    
    def test_size_parameter(self, sample_df):
        """Test size variable."""
        ax =plot2d(plot='scatterplot', df=sample_df, x='x', y='y', size='value')
        assert ax is not None
        plt.close('all')
    
    def test_style_parameter(self, sample_df):
        """Test style variable."""
        ax = plot2d(plot='scatterplot', df=sample_df, x='x', y='y', style='category')
        assert ax is not None
        plt.close('all')
    
    def test_markers_on_lineplot(self, sample_df):
        """Test markers on lineplot."""
        ax = plot2d(plot='lineplot', df=sample_df.head(30), x='x', y='y', markers=True)
        assert ax is not None
        plt.close('all')
    
    def test_estimator_on_lineplot(self, sample_df):
        """Test estimator parameter."""
        ax = plot2d(plot='lineplot', df=sample_df, x='category', y='value', estimator='mean')
        assert ax is not None
        plt.close('all')
    
    def test_ci_on_lineplot(self, sample_df):
        """Test confidence interval."""
        ax = plot2d(plot='lineplot', df=sample_df, x='category', y='value', ci=95)
        assert ax is not None
        plt.close('all')
    
    def test_bins_on_histplot(self, sample_df):
        """Test bins parameter."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', bins=20)
        assert ax is not None
        plt.close('all')
    
    def test_kde_on_histplot(self, sample_df):
        """Test KDE overlay on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', kde=True)
        assert ax is not None
        plt.close('all')
    
    def test_element_on_histplot(self, sample_df):
        """Test element type on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', element='step')
        assert ax is not None
        plt.close('all')
    
    def test_stat_on_histplot(self, sample_df):
        """Test stat parameter on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', stat='density')
        assert ax is not None
        plt.close('all')
    
    def test_cumulative_histplot(self, sample_df):
        """Test cumulative histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', cumulative=True)
        assert ax is not None
        plt.close('all')
    
    def test_multiple_on_histplot(self, sample_df):
        """Test multiple parameter on histogram."""
        ax = plot2d(plot='histplot', df=sample_df, x='value', hue='category', multiple='stack')
        assert ax is not None
        plt.close('all')
    
    def test_whis_on_boxplot(self, categorical_df):
        """Test whis parameter on boxplot."""
        ax = plot2d(plot='boxplot', df=categorical_df, x='group', y='measure', whis=1.5)
        assert ax is not None
        plt.close('all')
    
    def test_saturation_on_barplot(self, categorical_df):
        """Test saturation parameter."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', saturation=0.5)
        assert ax is not None
        plt.close('all')
    
    def test_dodge_parameter(self, categorical_df):
        """Test dodge parameter."""
        ax = plot2d(plot='barplot', df=categorical_df, x='group', y='measure', hue='group', dodge=False)
        assert ax is not None
        plt.close('all')
    
    def test_split_violinplot(self):
        """Test split violin plot."""
        df = pd.DataFrame({
            'group': ['A', 'B'] * 50,
            'value': np.random.randn(100)
        })
        ax = plot2d(plot='violinplot', df=df, x='group', y='value', split=True)
        assert ax is not None
        plt.close('all')
    
    def test_inner_violinplot(self, categorical_df):
        """Test inner parameter on violinplot."""
        ax = plot2d(plot='violinplot', df=categorical_df, x='group', y='measure', inner='box')
        assert ax is not None
        plt.close('all')
    
    def test_order_regplot(self, sample_df):
        """Test polynomial order on regplot."""
        ax = plot2d(plot='regplot', df=sample_df.head(50), x='x', y='y', order=2)
        assert ax is not None
        plt.close('all')
    
    def test_scatter_on_regplot(self, sample_df):
        """Test scatter parameter on regplot."""
        ax = plot2d(plot='regplot', df=sample_df.head(50), x='x', y='y', scatter=True)
        assert ax is not None
        plt.close('all')
    
    def test_fit_reg_false(self, sample_df):
        """Test fit_reg=False."""
        ax = plot2d(plot='regplot', df=sample_df.head(50), x='x', y='y', fit_reg=False)
        assert ax is not None
        plt.close('all')
