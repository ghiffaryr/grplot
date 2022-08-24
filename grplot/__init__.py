from matplotlib import pyplot as plt
import numpy
from grplot.features.optimizer.optimizer_data import optimizer_data
from grplot.features.pad.check_pad import check_pad
from grplot.features.plot.plot_type import plot_type
from grplot.features.saveas.check_saveas import check_saveas
from grplot.setting import setting
from grplot.utils.check_axes import check_axes
from grplot.utils.check_pandas_index import check_pandas_index
from grplot.utils.strtoarray import strtoarray


def grplot(plot, # default general value
           df, 
           x=None, 
           y=None, 
           Nx=None, 
           Ny=None, 
           figsize=[8,6], 
           pad=6, 
           hpad=None, 
           wpad=None, 
           hue=None, 
           size=None, # {5:'stripplot+swarmplot'}
           fontsize=10, 
           tick_fontsize=None, 
           legend_fontsize=None, 
           text_fontsize=None, 
           label_fontsize=None, 
           title_fontsize=None, 
           sep=',', 
           xsep=None, 
           ysep=None, 
           lim=None, 
           xlim=None, 
           ylim=None, 
           log=None, 
           xlog=None, 
           ylog=None, 
           dt=None, 
           xdt=None, 
           ydt=None, 
           tick_add=None, 
           xtick_add=None, 
           ytick_add=None, 
           rot=None, 
           xrot=None, 
           yrot=None, 
           statdesc=None, 
           xstatdesc=None, 
           ystatdesc=None, 
           text=None, 
           xtext=None, 
           ytext=None, 
           label_add=None, 
           xlabel_add=None, 
           ylabel_add=None, 
           title=None, 
           legend_loc=None, 
           saveas=None,
           optimizer='numpy', 
           style=None, 
           palette=None, 
           hue_order=None, 
           hue_norm=None, 
           sizes=None, 
           size_order=None, 
           size_norm=None, 
           markers=None, # {True:'scatterplot', 'o':'pointplot', 'D':'paretplot'}
           dashes=None, # {True:'lineplot'}
           style_order=None, 
           legend=None, # {'auto':'scatterplot+lineplot', True:'histplot+kdeplot+ecdfplot+rugplot'}
           height=None, # {0.025:'rugplot'}
           units=None, 
           x_bins=None, 
           y_bins=None, 
           estimator=None, # {'mean':'lineplot'} 
           x_estimator=None, 
           ci=None, 
           n_boot=None, # {1000:'scatterplot+lineplot+pointplot+barplot+paretoplot+regplot'}
           alpha=None, 
           expand_margins=None, 
           jitter=None, # {True:'stripplot'}
           x_jitter=None, 
           y_jitter=None, 
           weights=None, 
           color=None, 
           seed=None, 
           sort=None, # {True:'lineplot'}
           err_style=None, # {'band':'lineplot'}
           err_kws=None, 
           stat=None, # {'count':'histplot+ecdfplot'}
           bins=None, # {'auto':'histplot'}
           binwidth=None, 
           binrange=None, 
           discrete=None, 
           cumulative=None, # {False:'histplot+kdeplot'}
           common_bins=None, # {True:'histplot'}
           common_norm=None, # {True:'histplot+kdeplot'}
           common_grid=None, # {False:'kdeplot'}
           multiple=None, # {'layer':'histplot+kdeplot'}
           element=None, # {'bars':'histplot'}
           fill=None, # {True:'histplot'}
           shrink=None, # {1:'histplot'}
           kde=None, # {False:'histplot'}
           kde_kws=None, 
           line_kws=None, 
           thresh=None, # '{0:histplot', 0.05:'kdeplot'}
           pthresh=None, 
           pmax=None, 
           cbar=None, # {False:'histplot+kdeplot'}
           cbar_ax=None, 
           cbar_kws=None, 
           shade=None, 
           vertical=None, # {False:'kdeplot'}
           kernel=None, 
           bw=None, # {'scott':'violinplot'}
           gridsize=None, # {200:'kdeplot', 100:'violinplot'}
           cut=None, # {3:'kdeplot', 2:'violinplot'}
           clip=None, 
           shade_lowest=None, 
           levels=None, # {10:'kdeplot'}
           bw_method=None, # {'scott':'kdeplot'}
           bw_adjust=None, # {1:'kdeplot'}
           df2=None, 
           warn_singular=None, # {True:'kdeplot'}
           complementary=None, # {False:'ecdfplot'}
           a=None, 
           order=None, # {1:'regplot+residplot'}
           orient=None, 
           edgecolor=None, # {'gray':'stripplot+swarmplot'}
           linewidth=None, # {0:'stripplot+swarmplot'}
           saturation=None, # {0.75:'boxplot+violinplot+boxenplot+barplot+paretoplot+countplot'}
           width=None, # {0.8:'boxplot+violinplot+boxenplot'}
           dodge=None, # {True:'boxplot+violinplot+boxenplot+barplot+countplot+paretoplot', False:'stripplot+swarmplot+pointplot'}
           fliersize=None, # {5:'boxplot'}
           whis=None, # {1.5:'boxplot'}
           scale=None, # {'area':'violinplot', 'exponential':'boxenplot', 1:'pointplot'}
           scale_hue=None, # {True:'violinplot'}
           inner=None, 
           split=None, # {False:'violinplot'}
           k_depth=None, # {'tukey':'boxenplot'}
           outlier_prop=None, # {0.007:'boxenplot'}
           trust_alpha=None, # {0.05:'boxenplot'}
           showfliers=None, # {True:'boxenplot'}
           linestyles=None, # {'-':'pointplot'}
           join=None, # {True:'pointplot'}
           errwidth=None, 
           capsize=None, 
           errcolor=None, # {'.26':'barplot+paretoplot'}
           x_ci=None, 
           scatter=None, # {True:'regplot'}
           fit_reg=None, # {True:'regplot'}
           logistic=None, # {False:'regplot'}
           lowess=None, # {False:'regplot+residplot'}
           robust=None, # {False:'regplot+residplot'}
           regplot_logx=None, # {False:'regplot'}
           x_partial=None, 
           y_partial=None, 
           truncate=None, # {True:'regplot'}
           scatter_kws=None, 
           marker=None, # {'o':'regplot', 'D':'paretoplot'}
           dropna=None, # {True:'regplot+residplot'}
           label=None, 
           zorder=None, 
           color2=None, # {'.26':'paretoplot'}
           markersize=None, # {7:'paretoplot'}
           explode=None, 
           colors=None, 
           autopct=None, 
           pctdistance=None, # {0.6:'pieplot'}
           shadow=None, # {False:'pieplot'}
           labeldistance=None, # {1.1:'pieplot'}
           startangle=None, # {0:'pieplot'}
           radius=None, # {1:'pieplot'}
           counterclock=None, # {True:'pieplot'}
           wedgeprops=None, 
           textprops=None, 
           center=None, # {(0, 0):'pieplot'}
           frame=None, # {False:'pieplot'}
           rotatelabels=None, # {False:'pieplot'}
           normalize=None, # {True:'pieplot'}
           norm_x=None, # {100:'treemapsplot'}
           norm_y=None, # {100:'treemapsplot'}
           treemaps_pad=None, # {False:'treemapsplot'}
           bar_kwargs=None, 
           text_kwargs=None, 
           bubble_spacing=None, # {0.1:'packedbubblesplot'}
           showmeans=None, # {False:'boxplot'}
           meanprops=None):
    '''
    -----------------------------------------------
    grplot: lazy statistical data visualization
    
    by ghiffary rifqialdi
    based on numpy, scipy, matplotlib, seaborn, squarify, and pandas
    
    version = '0.10'

    release date
    25/08/2022
    -----------------------------------------------

    documentation is available at https://github.com/ghiffaryr/grplot
    '''    
    # initialization
    # creating figure
    Nx, Ny = check_axes(x, y, Nx, Ny)
    fig, ax = plt.subplots(Ny, 
                           Nx, 
                           figsize=(figsize[0], 
                                    figsize[1]))
    # padding
    fig = check_pad(fig=fig, 
                    hpad=hpad, 
                    wpad=wpad, 
                    pad=pad)
    # pandas index to array
    x, y = check_pandas_index(x=x, 
                              y=y)
    # iteration starting point for multi axes plot
    flag = 0    
    # plot
    # single plot, x axis
    if (type(x) == str) and (y is None):
        i = 0
        df_optimized = optimizer_data(plot=plot, 
                                      df=df, 
                                      x=x, 
                                      y=None, 
                                      hue=hue, 
                                      size=size, 
                                      style=style, 
                                      units=units, 
                                      axes='[{}]'.format(i+1),
                                      mode=optimizer)
        plot_type(plot=plot, data=df_optimized, x=x, y=None, ax=ax, axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
        setting(plot=plot,
                df=df_optimized, 
                x=x,
                y=None,
                fig=fig, 
                ax=ax, 
                axes='[{}]'.format(i+1),
                xaxislabel=ax.get_xlabel(), 
                yaxislabel=ax.get_ylabel(), 
                hue=hue,
                size=size,
                ci=ci,
                multiple=multiple, 
                sep=sep, 
                xsep=xsep, 
                ysep=ysep, 
                lim=lim,
                xlim=xlim,
                ylim=ylim, 
                log=log, 
                xlog=xlog, 
                ylog=ylog, 
                dt=dt, 
                xdt=xdt, 
                ydt=ydt,
                tick_add=tick_add,
                xtick_add=xtick_add,
                ytick_add=ytick_add,
                rot=rot,
                xrot=xrot,
                yrot=yrot,
                statdesc=statdesc,
                xstatdesc=xstatdesc,
                ystatdesc=ystatdesc,
                text=text,
                xtext=xtext,
                ytext=ytext,
                label_add=label_add,
                xlabel_add=xlabel_add,
                ylabel_add=ylabel_add,
                title=title,
                fontsize=fontsize,
                tick_fontsize=tick_fontsize,
                legend_fontsize=legend_fontsize,
                text_fontsize=text_fontsize,
                label_fontsize=label_fontsize,
                title_fontsize=title_fontsize,
                legend_loc=legend_loc)        
    # single plot, y axis
    elif (x is None) and (type(y) == str):
        i = 0
        df_optimized = optimizer_data(plot=plot, 
                                      df=df, 
                                      x=None, 
                                      y=y, 
                                      hue=hue, 
                                      size=size, 
                                      style=style, 
                                      units=units, 
                                      axes='[{}]'.format(i+1),
                                      mode=optimizer)
        plot_type(plot=plot, data=df_optimized, x=None, y=y, ax=ax, axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
        setting(plot=plot,
                df=df_optimized, 
                x=None,
                y=y,
                fig=fig, 
                ax=ax, 
                axes='[{}]'.format(i+1), 
                xaxislabel=ax.get_xlabel(), 
                yaxislabel=ax.get_ylabel(), 
                hue=hue,
                size=size,
                ci=ci,
                multiple=multiple, 
                sep=sep, 
                xsep=xsep, 
                ysep=ysep, 
                lim=lim,
                xlim=xlim,
                ylim=ylim, 
                log=log, 
                xlog=xlog, 
                ylog=ylog, 
                dt=dt, 
                xdt=xdt, 
                ydt=ydt,
                tick_add=tick_add,
                xtick_add=xtick_add,
                ytick_add=ytick_add,
                rot=rot,
                xrot=xrot,
                yrot=yrot,
                statdesc=statdesc,
                xstatdesc=xstatdesc,
                ystatdesc=ystatdesc,
                text=text,
                xtext=xtext,
                ytext=ytext,
                label_add=label_add,
                xlabel_add=xlabel_add,
                ylabel_add=ylabel_add,
                title=title,
                fontsize=fontsize,
                tick_fontsize=tick_fontsize,
                legend_fontsize=legend_fontsize,
                text_fontsize=text_fontsize,
                label_fontsize=label_fontsize,
                title_fontsize=title_fontsize,
                legend_loc=legend_loc)        
    # single plot, x and y axis
    elif (type(x) == str) and (type(y) == str):
        i = 0
        df_optimized = optimizer_data(plot=plot, 
                                      df=df, 
                                      x=x, 
                                      y=y, 
                                      hue=hue, 
                                      size=size, 
                                      style=style, 
                                      units=units, 
                                      axes='[{}]'.format(i+1),
                                      mode=optimizer)
        plot_type(plot=plot, data=df_optimized, x=x, y=y, ax=ax, axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
        setting(plot=plot,
                df=df_optimized, 
                x=x,
                y=y,
                fig=fig, 
                ax=ax,
                axes='[{}]'.format(i+1), 
                xaxislabel=ax.get_xlabel(), 
                yaxislabel=ax.get_ylabel(), 
                hue=hue,
                size=size,
                ci=ci,
                multiple=multiple, 
                sep=sep, 
                xsep=xsep, 
                ysep=ysep, 
                lim=lim,
                xlim=xlim,
                ylim=ylim, 
                log=log, 
                xlog=xlog, 
                ylog=ylog, 
                dt=dt, 
                xdt=xdt, 
                ydt=ydt,
                tick_add=tick_add,
                xtick_add=xtick_add,
                ytick_add=ytick_add,
                rot=rot,
                xrot=xrot,
                yrot=yrot,
                statdesc=statdesc,
                xstatdesc=xstatdesc,
                ystatdesc=ystatdesc,
                text=text,
                xtext=xtext,
                ytext=ytext,
                label_add=label_add,
                xlabel_add=xlabel_add,
                ylabel_add=ylabel_add,
                title=title,
                fontsize=fontsize,
                tick_fontsize=tick_fontsize,
                legend_fontsize=legend_fontsize,
                text_fontsize=text_fontsize,
                label_fontsize=label_fontsize,
                title_fontsize=title_fontsize,
                legend_loc=legend_loc)    
    # multi axes plot, x axis
    elif (type(x) in [list, numpy.ndarray]) and (y is None):
        # multi axes plot, 1D, x axis
        if (Nx == 1) or (Ny == 1):
            for i in range(max(Nx,Ny)):
                # stopper
                if flag == len(x): 
                    break
                else:
                    pass
                df_optimized = optimizer_data(plot=plot, 
                                              df=df, 
                                              x=x[flag], 
                                              y=None, 
                                              hue=hue, 
                                              size=size, 
                                              style=style, 
                                              units=units, 
                                              axes='[{}]'.format(i+1),
                                              mode=optimizer)
                plot_type(plot=plot, data=df_optimized, x=x[flag], y=None, ax=ax[i], axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                setting(plot=plot,
                        df=df_optimized, 
                        x=x[flag],
                        y=None,
                        fig=fig, 
                        ax=ax[i], 
                        axes='[{}]'.format(i+1), 
                        xaxislabel=ax[i].get_xlabel(), 
                        yaxislabel=ax[i].get_ylabel(), 
                        hue=hue,
                        size=size,
                        ci=ci,
                        multiple=multiple, 
                        sep=sep, 
                        xsep=xsep, 
                        ysep=ysep, 
                        lim=lim,
                        xlim=xlim,
                        ylim=ylim, 
                        log=log, 
                        xlog=xlog, 
                        ylog=ylog, 
                        dt=dt, 
                        xdt=xdt, 
                        ydt=ydt,
                        tick_add=tick_add,
                        xtick_add=xtick_add,
                        ytick_add=ytick_add,
                        rot=rot,
                        xrot=xrot,
                        yrot=yrot,
                        statdesc=statdesc,
                        xstatdesc=xstatdesc,
                        ystatdesc=ystatdesc,
                        text=text,
                        xtext=xtext,
                        ytext=ytext,
                        label_add=label_add,
                        xlabel_add=xlabel_add,
                        ylabel_add=ylabel_add,
                        title=title,
                        fontsize=fontsize,
                        tick_fontsize=tick_fontsize,
                        legend_fontsize=legend_fontsize,
                        text_fontsize=text_fontsize,
                        label_fontsize=label_fontsize,
                        title_fontsize=title_fontsize,
                        legend_loc=legend_loc)
                flag += 1
        # multi axes plot, 2D, x axis
        elif (Nx > 1) and (Ny > 1):
            for i in range(Ny):
                for j in range(Nx):
                    # stopper
                    if flag == len(x): 
                        break
                    else:
                        pass
                    df_optimized = optimizer_data(plot=plot, 
                                                  df=df, 
                                                  x=x[flag], 
                                                  y=None, 
                                                  hue=hue, 
                                                  size=size, 
                                                  style=style, 
                                                  units=units, 
                                                  axes='[{},{}]'.format(i+1,j+1),
                                                  mode=optimizer)
                    plot_type(plot=plot, data=df_optimized, x=x[flag], y=None, ax=ax[i,j], axes='[{},{}]'.format(i+1,j+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                    setting(plot=plot,
                            df=df_optimized, 
                            x=x[flag],
                            y=None,
                            fig=fig, 
                            ax=ax[i,j], 
                            axes='[{},{}]'.format(i+1,j+1), 
                            xaxislabel=ax[i,j].get_xlabel(), 
                            yaxislabel=ax[i,j].get_ylabel(), 
                            hue=hue,
                            size=size,
                            ci=ci,
                            multiple=multiple, 
                            sep=sep, 
                            xsep=xsep, 
                            ysep=ysep, 
                            lim=lim,
                            xlim=xlim,
                            ylim=ylim, 
                            log=log, 
                            xlog=xlog, 
                            ylog=ylog, 
                            dt=dt, 
                            xdt=xdt, 
                            ydt=ydt,
                            tick_add=tick_add,
                            xtick_add=xtick_add,
                            ytick_add=ytick_add,
                            rot=rot,
                            xrot=xrot,
                            yrot=yrot,
                            statdesc=statdesc,
                            xstatdesc=xstatdesc,
                            ystatdesc=ystatdesc,
                            text=text,
                            xtext=xtext,
                            ytext=ytext,
                            label_add=label_add,
                            xlabel_add=xlabel_add,
                            ylabel_add=ylabel_add,
                            title=title,
                            fontsize=fontsize,
                            tick_fontsize=tick_fontsize,
                            legend_fontsize=legend_fontsize,
                            text_fontsize=text_fontsize,
                            label_fontsize=label_fontsize,
                            title_fontsize=title_fontsize,
                            legend_loc=legend_loc)
                    flag += 1
    # multi axes plot, y axis
    elif (x is None) and (type(y) in [list, numpy.ndarray]):
        # multi axes plot, 1D, y axis
        if (Nx == 1) or (Ny == 1):
            for i in range(max(Nx,Ny)):
                # stopper
                if flag == len(y): 
                    break
                else:
                    pass
                df_optimized = optimizer_data(plot=plot, 
                                              df=df, 
                                              x=None, 
                                              y=y[flag], 
                                              hue=hue, 
                                              size=size, 
                                              style=style, 
                                              units=units, 
                                              axes='[{}]'.format(i+1),
                                              mode=optimizer)
                plot_type(plot=plot, data=df_optimized, x=None, y=y[flag], ax=ax[i], axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                setting(plot=plot,
                        df=df_optimized, 
                        x=None,
                        y=y[flag],
                        fig=fig, 
                        ax=ax[i], 
                        axes='[{}]'.format(i+1), 
                        xaxislabel=ax[i].get_xlabel(), 
                        yaxislabel=ax[i].get_ylabel(), 
                        hue=hue,
                        size=size,
                        ci=ci,
                        multiple=multiple, 
                        sep=sep, 
                        xsep=xsep, 
                        ysep=ysep, 
                        lim=lim,
                        xlim=xlim,
                        ylim=ylim, 
                        log=log, 
                        xlog=xlog, 
                        ylog=ylog, 
                        dt=dt, 
                        xdt=xdt, 
                        ydt=ydt,
                        tick_add=tick_add,
                        xtick_add=xtick_add,
                        ytick_add=ytick_add,
                        rot=rot,
                        xrot=xrot,
                        yrot=yrot,
                        statdesc=statdesc,
                        xstatdesc=xstatdesc,
                        ystatdesc=ystatdesc,
                        text=text,
                        xtext=xtext,
                        ytext=ytext,
                        label_add=label_add,
                        xlabel_add=xlabel_add,
                        ylabel_add=ylabel_add,
                        title=title,
                        fontsize=fontsize,
                        tick_fontsize=tick_fontsize,
                        legend_fontsize=legend_fontsize,
                        text_fontsize=text_fontsize,
                        label_fontsize=label_fontsize,
                        title_fontsize=title_fontsize,
                        legend_loc=legend_loc)
                flag += 1
        # multi axes plot, 2D, y axis
        elif (Nx > 1) and (Ny > 1):
            for i in range(Ny):
                for j in range(Nx):
                    # stopper
                    if flag == len(y): 
                        break
                    else:
                        pass
                    df_optimized = optimizer_data(plot=plot, 
                                                  df=df, 
                                                  x=None, 
                                                  y=y[flag], 
                                                  hue=hue, 
                                                  size=size, 
                                                  style=style, 
                                                  units=units, 
                                                  axes='[{},{}]'.format(i+1,j+1),
                                                  mode=optimizer)
                    plot_type(plot=plot, data=df_optimized, x=None, y=y[flag], ax=ax[i,j], axes='[{},{}]'.format(i+1,j+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                    setting(plot=plot,
                            df=df_optimized, 
                            x=None,
                            y=y[flag],
                            fig=fig, 
                            ax=ax[i,j], 
                            axes='[{},{}]'.format(i+1,j+1), 
                            xaxislabel=ax[i,j].get_xlabel(), 
                            yaxislabel=ax[i,j].get_ylabel(), 
                            hue=hue,
                            size=size,
                            ci=ci,
                            multiple=multiple, 
                            sep=sep, 
                            xsep=xsep, 
                            ysep=ysep, 
                            lim=lim,
                            xlim=xlim,
                            ylim=ylim, 
                            log=log, 
                            xlog=xlog, 
                            ylog=ylog, 
                            dt=dt, 
                            xdt=xdt, 
                            ydt=ydt,
                            tick_add=tick_add,
                            xtick_add=xtick_add,
                            ytick_add=ytick_add,
                            rot=rot,
                            xrot=xrot,
                            yrot=yrot,
                            statdesc=statdesc,
                            xstatdesc=xstatdesc,
                            ystatdesc=ystatdesc,
                            text=text,
                            xtext=xtext,
                            ytext=ytext,
                            label_add=label_add,
                            xlabel_add=xlabel_add,
                            ylabel_add=ylabel_add,
                            title=title,
                            fontsize=fontsize,
                            tick_fontsize=tick_fontsize,
                            legend_fontsize=legend_fontsize,
                            text_fontsize=text_fontsize,
                            label_fontsize=label_fontsize,
                            title_fontsize=title_fontsize,
                            legend_loc=legend_loc)
                    flag += 1
    # multi axes plot, (x string and y list-array axis) or (x list-array and y string axis) or (x list-array and y list-array axis)
    elif ((type(x) == str) and (type(y) in [list, numpy.ndarray])) or ((type(x) in [list, numpy.ndarray]) and (type(y) == str)) or ((type(x) in [list, numpy.ndarray]) and (type(y) in [list, numpy.ndarray])):
        x, y = strtoarray(x, y)
        # multi axes plot, 1D, x list and y list axis
        if (Nx == 1) or (Ny == 1):
            for i in range(max(Nx,Ny)):
                # stopper
                if (flag == len(x)) and (flag == len(y)): 
                    break
                else:
                    pass
                df_optimized = optimizer_data(plot=plot, 
                                              df=df, 
                                              x=x[flag], 
                                              y=y[flag], 
                                              hue=hue, 
                                              size=size, 
                                              style=style, 
                                              units=units, 
                                              axes='[{}]'.format(i+1),
                                              mode=optimizer)
                plot_type(plot=plot, data=df_optimized, x=x[flag], y=y[flag], ax=ax[i], axes='[{}]'.format(i+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                setting(plot=plot,
                        df=df_optimized, 
                        x=x[flag],
                        y=y[flag],
                        fig=fig, 
                        ax=ax[i], 
                        axes='[{}]'.format(i+1), 
                        xaxislabel=ax[i].get_xlabel(), 
                        yaxislabel=ax[i].get_ylabel(), 
                        hue=hue,
                        size=size,
                        ci=ci,
                        multiple=multiple, 
                        sep=sep, 
                        xsep=xsep, 
                        ysep=ysep, 
                        lim=lim,
                        xlim=xlim,
                        ylim=ylim, 
                        log=log, 
                        xlog=xlog, 
                        ylog=ylog, 
                        dt=dt, 
                        xdt=xdt, 
                        ydt=ydt,
                        tick_add=tick_add,
                        xtick_add=xtick_add,
                        ytick_add=ytick_add,
                        rot=rot,
                        xrot=xrot,
                        yrot=yrot,
                        statdesc=statdesc,
                        xstatdesc=xstatdesc,
                        ystatdesc=ystatdesc,
                        text=text,
                        xtext=xtext,
                        ytext=ytext,
                        label_add=label_add,
                        xlabel_add=xlabel_add,
                        ylabel_add=ylabel_add,
                        title=title,
                        fontsize=fontsize,
                        tick_fontsize=tick_fontsize,
                        legend_fontsize=legend_fontsize,
                        text_fontsize=text_fontsize,
                        label_fontsize=label_fontsize,
                        title_fontsize=title_fontsize,
                        legend_loc=legend_loc)
                flag += 1
        # multi axes plot, 2D, x list and y list axis
        elif (Nx > 1) and (Ny > 1):
            for i in range(Ny):
                for j in range(Nx):
                    if (flag == len(x)) and (flag == len(y)): 
                        break
                    else:
                        pass
                    df_optimized = optimizer_data(plot=plot, 
                                                  df=df, 
                                                  x=x[flag], 
                                                  y=y[flag], 
                                                  hue=hue, 
                                                  size=size, 
                                                  style=style, 
                                                  units=units, 
                                                  axes='[{},{}]'.format(i+1,j+1),
                                                  mode=optimizer)
                    plot_type(plot=plot, data=df_optimized, x=x[flag], y=y[flag], ax=ax[i,j], axes='[{},{}]'.format(i+1,j+1), hue=hue, size=size, style=style, palette=palette, hue_order=hue_order, hue_norm=hue_norm, sizes=sizes, size_order=size_order, size_norm=size_norm, markers=markers, dashes=dashes, style_order=style_order, legend=legend, height=height, units=units, x_bins=x_bins, y_bins=y_bins, estimator=estimator, x_estimator=x_estimator, ci=ci, n_boot=n_boot, alpha=alpha, expand_margins=expand_margins, jitter=jitter, x_jitter=x_jitter, y_jitter=y_jitter, weights=weights, color=color, seed=seed, sort=sort, err_style=err_style, err_kws=err_kws, stat=stat, bins=bins, binwidth=binwidth, binrange=binrange, discrete=discrete, cumulative=cumulative, common_bins=common_bins, common_norm=common_norm, common_grid=common_grid, multiple=multiple, element=element, fill=fill, shrink=shrink, kde=kde, kde_kws=kde_kws, line_kws=line_kws, thresh=thresh, pthresh=pthresh, pmax=pmax, cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, shade=shade, vertical=vertical, kernel=kernel, bw=bw, gridsize=gridsize, cut=cut, clip=clip, shade_lowest=shade_lowest, levels=levels, bw_method=bw_method, bw_adjust=bw_adjust, data2=df2, warn_singular=warn_singular, complementary=complementary, a=a, order=order, orient=orient, edgecolor=edgecolor, linewidth=linewidth, saturation=saturation, width=width, dodge=dodge, fliersize=fliersize, whis=whis, scale=scale, scale_hue=scale_hue, inner=inner, split=split, k_depth=k_depth, outlier_prop=outlier_prop, trust_alpha=trust_alpha, showfliers=showfliers, linestyles=linestyles, join=join, errwidth=errwidth, capsize=capsize, errcolor=errcolor, x_ci=x_ci, scatter=scatter, fit_reg=fit_reg, logistic=logistic, lowess=lowess, robust=robust, regplot_logx=regplot_logx, x_partial=x_partial, y_partial=y_partial, truncate=truncate, scatter_kws=scatter_kws, marker=marker, dropna=dropna, label=label, zorder=zorder, color2=color2, markersize=markersize, explode=explode, colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow, labeldistance=labeldistance, startangle=startangle, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops, center=center, frame=frame, rotatelabels=rotatelabels, normalize=normalize, norm_x=norm_x, norm_y=norm_y, treemaps_pad=treemaps_pad, bar_kwargs=bar_kwargs, text_kwargs=text_kwargs, bubble_spacing=bubble_spacing, showmeans=showmeans, meanprops=meanprops, text=text)
                    setting(plot=plot,
                            df=df_optimized, 
                            x=x[flag],
                            y=y[flag],
                            fig=fig, 
                            ax=ax[i,j], 
                            axes='[{},{}]'.format(i+1,j+1), 
                            xaxislabel=ax[i,j].get_xlabel(), 
                            yaxislabel=ax[i,j].get_ylabel(), 
                            hue=hue,
                            size=size,
                            ci=ci,
                            multiple=multiple, 
                            sep=sep, 
                            xsep=xsep, 
                            ysep=ysep, 
                            lim=lim,
                            xlim=xlim,
                            ylim=ylim, 
                            log=log, 
                            xlog=xlog, 
                            ylog=ylog, 
                            dt=dt, 
                            xdt=xdt, 
                            ydt=ydt,
                            tick_add=tick_add,
                            xtick_add=xtick_add,
                            ytick_add=ytick_add,
                            rot=rot,
                            xrot=xrot,
                            yrot=yrot,
                            statdesc=statdesc,
                            xstatdesc=xstatdesc,
                            ystatdesc=ystatdesc,
                            text=text,
                            xtext=xtext,
                            ytext=ytext,
                            label_add=label_add,
                            xlabel_add=xlabel_add,
                            ylabel_add=ylabel_add,
                            title=title,
                            fontsize=fontsize,
                            tick_fontsize=tick_fontsize,
                            legend_fontsize=legend_fontsize,
                            text_fontsize=text_fontsize,
                            label_fontsize=label_fontsize,
                            title_fontsize=title_fontsize,
                            legend_loc=legend_loc)
                    flag += 1
    else:
        raise Exception('Wrong data type of axis!')
    # save image as
    check_saveas(fig, saveas)
    return ax