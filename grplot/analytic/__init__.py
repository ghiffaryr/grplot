import numpy
import pandas
import grplot_seaborn as gs
import matplotlib
from matplotlib import pyplot as plt
from grplot.features.optimizer.optimizer_analytic import optimizer_analytic
from grplot.features.saveas.check_saveas import check_saveas
from grplot.features.sep.statdesc_sep.statdesc_sep_def import statdesc_sep_def
from IPython.display import display


def cohort(df,
           customer_id,
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
    if type(customer_id) == str and type(signup_date) == str and type(last_active_date) == str:
        # preprocessing
        preprocessing = optimizer_analytic(df=df, 
                                           variables=numpy.array([customer_id,
                                                                  signup_date, 
                                                                  last_active_date]), 
                                           mode='perf')
        preprocessing = preprocessing.rename(columns={customer_id:'Customer ID', signup_date:'Signup Date', last_active_date:'Last Active Date'})
        preprocessing['Signup Date'] = pandas.to_datetime(preprocessing['Signup Date']).dt.tz_localize(None).dt.to_period('M').dt.to_timestamp()
        preprocessing['Last Active Date'] = pandas.to_datetime(preprocessing['Last Active Date']).dt.tz_localize(None).dt.to_period('M').dt.to_timestamp()
        preprocessing.set_index('Customer ID', inplace=True)
        preprocessing['Metric'] = [pandas.period_range(s, e, freq='m') for s, e in zip(preprocessing['Signup Date'], preprocessing['Last Active Date'])]
        preprocessing = preprocessing.explode('Metric')
        preprocessing['Cohort Group'] = preprocessing.groupby(level=0)['Metric'].min().dt.strftime('%Y-%m')
        preprocessing.reset_index(inplace=True)
        cohort = preprocessing.groupby(['Cohort Group', 'Metric']).agg({'Customer ID':pandas.Series.nunique})
        cohort.rename(columns={'Customer ID':'Total Account'}, inplace=True)    
        def cohort_period(df):
            df['Cohort Period'] = numpy.arange(len(df))
            return df
        cohort = cohort.groupby(level=0).apply(cohort_period)
        cohort.reset_index(inplace=True)
        cohort.set_index(['Cohort Group', 'Cohort Period'], inplace=True)
        # display summary
        if display_summary == True: 
            display(cohort)
        else:
            pass
        cohort_group_size = cohort['Total Account'].groupby(level=0).first()
        user_retention = cohort['Total Account'].unstack(0).divide(cohort_group_size, axis=1)
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
        gs.heatmap(user_retention.T, mask=user_retention.T.isnull(), annot=True,  annot_kws={"size":text_fontsize}, fmt='.2f', cmap='RdYlGn', xticklabels=list(range(0, len(user_retention))), vmin=0, vmax=100, ax=ax)
        # fontsize
        ax.set_title(label="Monthly Retention Rate", fontsize=title_fontsize)
        ax.set_xlabel('Cohort Period', fontsize=label_fontsize)
        ax.set_ylabel('Cohort Group', fontsize=label_fontsize)
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
            num = int(num)
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
        raise Exception('Wrong data type of customer_id, signup_date, or last_active_date!')
    return ax

def rank_order(predict_proba, true_label, class_non_event=1, display_table=True):
    if (type(predict_proba) in [numpy.ndarray, pandas.core.frame.DataFrame]) and (type(true_label) in [list, numpy.ndarray, pandas.core.series.Series]):
        # class_non_event
        if type(class_non_event) == int:
            if class_non_event >= 0 and class_non_event <= numpy.max(true_label):
                pass
            else:
                raise Exception(f'class_non_event must be integer bigger than 0 and smaller than {numpy.max(true_label)}')
        else:
                raise Exception(f'class_non_event must be integer bigger than 0 and smaller than {numpy.max(true_label)}')
        # predict_proba
        if type(predict_proba) == numpy.ndarray:
            if len(predict_proba.shape) >= 2:
                df_rank_order = pandas.DataFrame({'predict_proba':predict_proba[:, class_non_event], 'true_label':true_label})
            else:
                raise Exception('Pass all class prediction probability as 2 or more dimensional numpy.ndarray to predict_proba!')
        else: # type(predict_proba) == pandas.core.frame.DataFrame:
            if len(predict_proba.columns) >= 2:
                df_rank_order = pandas.DataFrame({'predict_proba':predict_proba[class_non_event], 'true_label':true_label})
            else:
                raise Exception('Pass all class prediction probability as 2 or more dimensional pandas.core.frame.DataFrame to predict_proba!')
        df_rank_order['Decile'] = pandas.qcut(df_rank_order['predict_proba'], 10, labels=False)
        df_rank_order = df_rank_order.groupby('Decile').apply(lambda x: pandas.Series([numpy.min(x['predict_proba']), numpy.max(x['predict_proba']), numpy.mean(x['predict_proba']), numpy.size(x['predict_proba']), numpy.size(x['true_label'][x['true_label']==class_non_event]), (numpy.size(x['true_label']) - numpy.size(x['true_label'][x['true_label']==class_non_event]))],
                                                            index=(['Minimum Prediction Probability', 'Maximum Prediction Probability', 'Mean Prediction Probability', 'Count Customer', 'Count Non-event', 'Count Event'])
                                                                        )
                                                    ).reset_index()
        df_rank_order = df_rank_order.sort_values(by='Decile',ascending=False)
        df_rank_order['Non-event Rate'] = round(df_rank_order['Count Non-event']*100/df_rank_order['Count Customer'], 2)
        df_rank_order['Cummulative Count Customer'] = numpy.cumsum(df_rank_order['Count Customer'])
        df_rank_order['Cummulative Count Non-event'] = numpy.cumsum(df_rank_order['Count Non-event'])
        df_rank_order['Cummulative Count Event'] = numpy.cumsum(df_rank_order['Count Event'])
        df_rank_order['Cummulative Customer Percentage'] = round(df_rank_order['Cummulative Count Customer']*100/numpy.sum(df_rank_order['Count Customer']), 2)
        df_rank_order['Cummulative Non-event Percentage'] = round(df_rank_order['Cummulative Count Non-event']*100/numpy.sum(df_rank_order['Count Non-event']), 2)
        df_rank_order['Cummulative Event Percentage'] = round(df_rank_order['Cummulative Count Event']*100/numpy.sum(df_rank_order['Count Event']), 2)
        df_rank_order['KS'] = round(df_rank_order['Cummulative Non-event Percentage'] - df_rank_order['Cummulative Event Percentage'], 2)
        df_rank_order['Lift'] = round(df_rank_order['Cummulative Non-event Percentage'] / df_rank_order['Cummulative Customer Percentage'], 2)
        for col in ['Count Customer', 'Count Non-event', 'Count Event', 'Cummulative Count Customer', 'Cummulative Count Non-event', 'Cummulative Count Event']:
            df_rank_order[col] = df_rank_order[col].astype(int)
        df_rank_order = df_rank_order.set_index('Decile')
        # display table
        if display_table == True: 
            display(df_rank_order)
        else:
            pass
    else:
            raise Exception('Wrong data type of predict_proba or true_label!')
    return df_rank_order