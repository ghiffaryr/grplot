from matplotlib import cbook
import numpy
from grplot.features.add.statdesc_add.statdesc_add_type import statdesc_add_type
from grplot.features.sep.statdesc_sep.statdesc_sep_type import statdesc_sep_type
from grplot.features.statdesc.statdesc_plot_def import statdesc_plot_def


def statdesc_multi_def(df, ax, axis, statdesc, sep, add, axislabel, axes):
    # check data type
    if type(df[axislabel]) == list:
        data = numpy.array(df[axislabel])
    elif numpy.issubdtype(type(df[axislabel]), numpy.ndarray) == True:
        data = df[axislabel]
    else:
        raise Exception('Unsupported dtype')
    # drop numpy.nan
    data = data[~numpy.isnan(data)]
    if type(statdesc) == str:
        if 'general' in statdesc:
            statdesc = statdesc.replace('general', 'count+unique+std+min+q1+median+mean+q3+max')
        elif 'boxplot' in statdesc:
            statdesc = statdesc.replace('boxplot', 'min+whislo+q1+cilo+median+mean+q3+cihi+whishi+max')
        else:
            pass
        for stat in statdesc.split('+'):
            if 'count' in stat:
                try:
                    count = numpy.count_nonzero(data)
                    count_sep = statdesc_sep_type(num=count, stat_label='count', sep=sep, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=count, color=None, stat_label='count', stat_fmt=count_sep)
            elif 'unique' in stat:
                try:
                    unique = len(numpy.unique(data))
                    unique_sep = statdesc_sep_type(num=unique, stat_label='unique count', sep=sep, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=unique, color=None, stat_label='unique count', stat_fmt=unique_sep)
            elif 'std' in stat:
                try:
                    std = numpy.std(data)
                    std_sep = statdesc_sep_type(num=std, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    std_add = statdesc_add_type(num=std_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=std, color=None, stat_label='std', stat_fmt=std_add)
            elif 'var' in stat:
                try:
                    var = numpy.var(data)
                    var_sep = statdesc_var_type(num=var, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    var_add = statdesc_add_type(num=var_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=var, color=None, stat_label='var', stat_fmt=var_add)
            elif 'min' in stat:
                try:
                    mini = numpy.min(data)
                    mini_sep = statdesc_sep_type(num=mini, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    mini_add = statdesc_add_type(num=mini_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=mini, color='red', stat_label='min', stat_fmt=mini_add)
            elif 'pct1' in stat:
                try:
                    pct1 = numpy.percentile(data, 1)
                    pct1_sep = statdesc_sep_type(num=pct1, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    pct1_add = statdesc_add_type(num=pct1_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=pct1, color='orange', stat_label='1st pct', stat_fmt=pct1_add)
            elif 'whislo' in stat:
                try:
                    whislo = cbook.boxplot_stats(data)[0]['whislo']
                    whislo_sep = statdesc_sep_type(num=whislo, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    whislo_add = statdesc_add_type(num=whislo_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=whislo, color='orange', stat_label='lower whisker', stat_fmt=whislo_add)
            elif 'cilo' in stat:
                try:
                    cilo = cbook.boxplot_stats(data)[0]['cilo']
                    cilo_sep = statdesc_sep_type(num=cilo, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    cilo_add = statdesc_add_type(num=cilo_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=cilo, color='yellow', stat_label='95% CI low', stat_fmt=cilo_add)
            elif 'pct5' in stat:
                try:
                    pct5 = numpy.percentile(data, 5)
                    pct5_sep = statdesc_sep_type(num=pct5, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    pct5_add = statdesc_add_type(num=pct5_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=pct5, color='yellow', stat_label='5th pct', stat_fmt=pct5_add)
            elif 'q1' in stat:
                try:
                    q1 = numpy.percentile(data, 25)
                    q1_sep = statdesc_sep_type(num=q1, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    q1_add = statdesc_add_type(num=q1_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=q1, color='green', stat_label='q1', stat_fmt=q1_add)
            elif 'median' in stat:
                try:
                    median = numpy.median(data)
                    median_sep = statdesc_sep_type(num=median, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    median_add = statdesc_add_type(num=median_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=median, color='blue', stat_label='median', stat_fmt=median_add)
            elif 'mean' in stat:
                try:
                    mean = numpy.mean(data)
                    mean_sep = statdesc_sep_type(num=mean, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    mean_add = statdesc_add_type(num=mean_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=mean, color='blue', stat_label='mean', stat_fmt=mean_add)
            elif 'q3' in stat:
                try:
                    q3 = numpy.percentile(data, 75)
                    q3_sep = statdesc_sep_type(num=q3, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    q3_add = statdesc_add_type(num=q3_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=q3, color='green', stat_label='q3', stat_fmt=q3_add)
            elif 'pct95' in stat:
                try:
                    pct95 = numpy.percentile(data, 95)
                    pct95_sep = statdesc_sep_type(num=pct95, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    pct95_add = statdesc_add_type(num=pct95_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=pct95, color='yellow', stat_label='95th pct', stat_fmt=pct95_add)
            elif 'cihi' in stat:
                try:
                    cihi = cbook.boxplot_stats(data)[0]['cihi']
                    cihi_sep = statdesc_sep_type(num=cihi, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    cihi_add = statdesc_add_type(num=cihi_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=cihi, color='yellow', stat_label='95% CI hi', stat_fmt=cihi_add)
            elif 'whishi' in stat:
                try:
                    whishi = cbook.boxplot_stats(data)[0]['whishi']
                    whishi_sep = statdesc_sep_type(num=whishi, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    whishi_add = statdesc_add_type(num=whishi_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=whishi, color='orange', stat_label='upper whisker', stat_fmt=whishi_add)
            elif 'pct99' in stat:
                try:
                    pct99 = numpy.percentile(data, 99)
                    pct99_sep = statdesc_sep_type(num=pct99, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    pct99_add = statdesc_add_type(num=pct99_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=pct99, color='orange', stat_label='99th pct', stat_fmt=pct99_add)
            elif 'max' in stat:
                try:
                    maxi = numpy.max(data)
                    maxi_sep = statdesc_sep_type(num=maxi, stat_label=None, sep=sep, axislabel=axislabel, axes=axes)
                    maxi_add = statdesc_add_type(num=maxi_sep, add=add, axislabel=axislabel, axes=axes)
                except:
                    raise Exception('Label not in the dataframe!')
                statdesc_plot_def(ax=ax, axis=axis, stat=maxi, color='red', stat_label='max', stat_fmt=maxi_add)
            else:
                pass
    else:
        raise Exception('Unknown statdesc argument!')
    return ax