import numpy as np
import pandas as pd
import grplot_seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from grplot.features.optimizer.optimizer_data import optimizer_data
from grplot.features.saveas.check_saveas import check_saveas
from grplot.features.sep.statdesc_sep.statdesc_sep_def import statdesc_sep_def


def cohort(df,
           signup_date, 
           last_active_date, 
           figsize=[8,6],
           fontsize=10, 
           tick_fontsize=None, 
           legend_fontsize=None, 
           text_fontsize=None, 
           label_fontsize=None, 
           title_fontsize=None, 
           sep=',',
           saveas=None,
           display_summary=False):
    '''
    -----------------------------------------------
    grplot: lazy statistical data visualization
    
    by ghiffary rifqialdi
    based on numpy, scipy, matplotlib, seaborn, squarify, and pandas
    
    version = '0.11'

    release date
    11/09/2022
    -----------------------------------------------

    documentation is available at https://github.com/ghiffaryr/grplot
    '''
    if type(signup_date) == str and type(last_active_date) == str:
        # preprocessing
        preprocessing = optimizer_data(plot='heatmap', 
                                       df=df, 
                                       x=signup_date, 
                                       y=last_active_date, 
                                       hue=None, 
                                       size=None, 
                                       style=None, 
                                       units=None, 
                                       axes=None, 
                                       mode='perf') \
                        .copy(deep=True)
        preprocessing['Customer ID'] = np.arange(len(preprocessing)) + 1
        preprocessing['Signup Date'] = pd.to_datetime(preprocessing[signup_date]).dt.tz_localize(None).dt.to_period('M').dt.to_timestamp()
        preprocessing['Last Active Date'] = pd.to_datetime(preprocessing[last_active_date]).dt.tz_localize(None).dt.to_period('M').dt.to_timestamp()
        preprocessing = preprocessing[['Customer ID', 'Signup Date', 'Last Active Date']]
        preprocessing.set_index('Customer ID', inplace=True)
        preprocessing['Metric'] = [pd.period_range(s, e, freq='m') for s, e in zip(preprocessing['Signup Date'], preprocessing['Last Active Date'])]
        preprocessing = preprocessing.explode('Metric')
        preprocessing['Cohort Group'] = preprocessing.groupby(level=0)['Metric'].min().dt.strftime('%Y-%m')
        preprocessing.reset_index(inplace=True)
        cohort = preprocessing.groupby(['Cohort Group', 'Metric']).agg({'Customer ID':pd.Series.nunique})
        cohort.rename(columns={'Customer ID': 'Total Account'}, inplace=True)    
        def cohort_period(df):
            df['Cohort Period'] = np.arange(len(df))
            return df
        cohort = cohort.groupby(level=0).apply(cohort_period)
        cohort.reset_index(inplace=True)
        cohort.set_index(['Cohort Group', 'Cohort Period'], inplace=True)
        # summary
        if display_summary == True: 
            display(cohort)
        else:
            pass
        cohort_group_size = cohort['Total Account'].groupby(level=0).first()
        user_retention = cohort['Total Account'].unstack(0).divide(cohort_group_size, axis=1)
        user_retention = user_retention.iloc[0:,:len(user_retention)]
        user_retention = user_retention * 100
        # plotting
        # creating figure
        fig, ax = plt.subplots(figsize=(figsize[0], 
                                        figsize[1]))
        # check fontsize
        if tick_fontsize is None:
            tick_fontsize = fontsize
        else:
            pass
        if legend_fontsize is None:
            legend_fontsize = fontsize
        else:
            pass
        if text_fontsize is None:
            text_fontsize = fontsize
        else:
            pass
        if label_fontsize is None:
            label_fontsize = fontsize
        else:
            pass
        if title_fontsize is None:
            title_fontsize = fontsize
        else:
            pass
        sns.heatmap(user_retention.T, mask=user_retention.T.isnull(), annot=True,  annot_kws={"size":text_fontsize}, fmt='.2f', cmap='RdYlGn', xticklabels=list(range(0, len(user_retention))), ax=ax)
        # fontsize
        ax.set_title(label="Monthly Retention Rate", fontsize=title_fontsize)
        ax.set_xlabel('Periods in Month', fontsize=label_fontsize)
        ax.set_ylabel('Cohort Group (Signup Month)', fontsize=label_fontsize)
        ax.tick_params(axis='both', labelsize=tick_fontsize)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=legend_fontsize)
        # rot
        for label in ax.get_yticklabels():
            label.set_rotation(0)
        # sep
        # sep cbar
        yticks = []
        for num in cbar.ax.get_yticks():
            num = round(float(num), 2)
            num = statdesc_sep_def(num, sep)
            yticks.append(num + '%')
        cbar.ax.set_yticks(cbar.ax.get_yticks())
        cbar.ax.set_yticklabels(yticks)
        # sep text
        for child in ax.get_children():
            if isinstance(child, matplotlib.text.Text) and (child.get_text().replace('.', '', 1).isdigit() == True):
                num = float(child.get_text())
                num = statdesc_sep_def(num, sep)
                child.set_text(num + '%')
            else:
                pass
        # save image as
        check_saveas(fig, saveas)
    else:
        raise Exception('Wrong data type of axis!')
    return ax