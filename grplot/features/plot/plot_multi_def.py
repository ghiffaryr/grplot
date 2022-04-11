import numpy
from grplot.features.plot.plot_single_def import plot_single_def
from grplot.utils.arg_plot_ax_type import arg_plot_ax_type


def plot_multi_def(plot,
                   x,
                   y,
                   ax,
                   axes,
                   hue, 
                   size, 
                   style, 
                   data, 
                   palette, 
                   hue_order, 
                   hue_norm, 
                   sizes, 
                   size_order, 
                   size_norm, 
                   markers, 
                   dashes, 
                   style_order, 
                   legend, 
                   height, 
                   units, 
                   x_bins,
                   y_bins,
                   estimator, 
                   x_estimator,
                   ci,
                   n_boot,
                   alpha,
                   expand_margins,
                   jitter,
                   x_jitter,
                   y_jitter,
                   weights,
                   color,
                   seed,
                   sort,
                   err_style,
                   err_kws,
                   stat, 
                   bins,
                   binwidth,
                   binrange,
                   discrete,
                   cumulative,
                   common_bins,
                   common_norm,
                   common_grid,
                   multiple,
                   element,
                   fill, 
                   shrink,
                   kde,
                   kde_kws,
                   line_kws,
                   thresh, 
                   pthresh,
                   pmax,
                   cbar,
                   cbar_ax,
                   cbar_kws,
                   shade,
                   vertical,
                   kernel,
                   bw, 
                   gridsize, 
                   cut, 
                   clip, 
                   shade_lowest,
                   levels,
                   bw_method,
                   bw_adjust,
                   data2,
                   warn_singular,
                   complementary,
                   a,
                   order, 
                   orient,
                   edgecolor,
                   linewidth, 
                   saturation,
                   width,
                   dodge, 
                   fliersize,
                   whis,
                   scale, 
                   scale_hue,
                   inner,
                   split,
                   k_depth,
                   outlier_prop,
                   trust_alpha,
                   showfliers,
                   linestyles,
                   join,
                   errwidth,
                   capsize,
                   errcolor,
                   x_ci,
                   scatter,
                   fit_reg,
                   logistic,
                   lowess,
                   robust,
                   x_partial,
                   y_partial,
                   truncate,
                   scatter_kws,
                   marker,
                   dropna, 
                   label,
                   zorder,
                   color2,
                   markersize,
                   text, 
                   explode, 
                   colors, 
                   autopct, 
                   pctdistance, 
                   shadow, 
                   labeldistance, 
                   startangle, 
                   radius, 
                   counterclock, 
                   wedgeprops, 
                   textprops, 
                   center, 
                   frame, 
                   rotatelabels, 
                   normalize, 
                   norm_x, 
                   norm_y, 
                   treemaps_pad, 
                   bar_kwargs, 
                   text_kwargs,
                   bubble_spacing):
    plot_, hue_, size_, style_, palette_, hue_order_, hue_norm_, sizes_, size_order_, size_norm_, markers_, dashes_, style_order_, legend_, height_, units_, x_bins_, y_bins_, estimator_, x_estimator_, ci_, n_boot_, alpha_, expand_margins_, jitter_, x_jitter_, y_jitter_, ax_, weights_, color_, seed_, sort_, err_style_, stat_, bins_, binwidth_, binrange_, discrete_, cumulative_, common_bins_, common_norm_, common_grid_, multiple_, element_, fill_, shrink_, kde_, thresh_, pthresh_, pmax_, cbar_, cbar_ax_, shade_, vertical_, kernel_, bw_, gridsize_, cut_, clip_, shade_lowest_, levels_, bw_method_, bw_adjust_, warn_singular_, complementary_, a_, order_, orient_, edgecolor_, linewidth_, saturation_, width_, dodge_, fliersize_, whis_, scale_, scale_hue_, inner_, split_, k_depth_, outlier_prop_, trust_alpha_, showfliers_, linestyles_, join_, errwidth_, capsize_, errcolor_, x_ci_, scatter_, fit_reg_, logistic_, lowess_, robust_, x_partial_, y_partial_, truncate_, marker_, dropna_, label_, zorder_, color2_, markersize_, text_, explode_, colors_, autopct_, pctdistance_, shadow_, labeldistance_, startangle_, radius_, counterclock_, center_, frame_, rotatelabels_, normalize_, norm_x_, norm_y_, treemaps_pad_, bubble_spacing_ = plot, hue, size, style, palette, hue_order, hue_norm, sizes, size_order, size_norm, markers, dashes, style_order, legend, height, units, x_bins, y_bins, estimator, x_estimator, ci, n_boot, alpha, expand_margins, jitter, x_jitter, y_jitter, ax, weights, color, seed, sort, err_style, stat, bins, binwidth, binrange, discrete, cumulative, common_bins, common_norm, common_grid, multiple, element, fill, shrink, kde, thresh, pthresh, pmax, cbar, cbar_ax, shade, vertical, kernel, bw, gridsize, cut, clip, shade_lowest, levels, bw_method, bw_adjust, warn_singular, complementary, a, order, orient, edgecolor, linewidth, saturation, width, dodge, fliersize, whis, scale, scale_hue, inner, split, k_depth, outlier_prop, trust_alpha, showfliers, linestyles, join, errwidth, capsize, errcolor, x_ci, scatter, fit_reg, logistic, lowess, robust, x_partial, y_partial, truncate, marker, dropna, label, zorder, color2, markersize, text, explode, colors, autopct, pctdistance, shadow, labeldistance, startangle, radius, counterclock, center, frame, rotatelabels, normalize, norm_x, norm_y, treemaps_pad, bubble_spacing
    # plotting
    for count, plot in enumerate(plot_.split('+')):
        # column name and dictionary based on matplotlib, seaborn, and squarify skipped: x, y, data, err_kws, kde_kws, line_kws, cbar_kws, data2, scatter_kws, wedgeprops, textprops, bar_kwargs, text_kwargs
        hue, size, style, palette, hue_order, hue_norm, sizes, size_order, size_norm, markers, dashes, style_order, legend, height, units, x_bins, y_bins, estimator, x_estimator, ci, n_boot, alpha, expand_margins, jitter, x_jitter, y_jitter, ax, weights, color, seed, sort, err_style, stat, bins, binwidth, binrange, discrete, cumulative, common_bins, common_norm, common_grid, multiple, element, fill, shrink, kde, thresh, pthresh, pmax, cbar, cbar_ax, shade, vertical, kernel, bw, gridsize, cut, clip, shade_lowest, levels, bw_method, bw_adjust, warn_singular, complementary, a, order, orient, edgecolor, linewidth, saturation, width, dodge, fliersize, whis, scale, scale_hue, inner, split, k_depth, outlier_prop, trust_alpha, showfliers, linestyles, join, errwidth, capsize, errcolor, x_ci, scatter, fit_reg, logistic, lowess, robust, x_partial, y_partial, truncate, marker, dropna, label, zorder, color2, markersize, text, explode, colors, autopct, pctdistance, shadow, labeldistance, startangle, radius, counterclock, center, frame, rotatelabels, normalize, norm_x, norm_y, treemaps_pad, bubble_spacing = map(arg_plot_ax_type, (hue_, size_, style_, palette_, hue_order_, hue_norm_, sizes_, size_order_, size_norm_, markers_, dashes_, style_order_, legend_, height_, units_, x_bins_, y_bins_, estimator_, x_estimator_, ci_, n_boot_, alpha_, expand_margins_, jitter_, x_jitter_, y_jitter_, ax_, weights_, color_, seed_, sort_, err_style_, stat_, bins_, binwidth_, binrange_, discrete_, cumulative_, common_bins_, common_norm_, common_grid_, multiple_, element_, fill_, shrink_, kde_, thresh_, pthresh_, pmax_, cbar_, cbar_ax_, shade_, vertical_, kernel_, bw_, gridsize_, cut_, clip_, shade_lowest_, levels_, bw_method_, bw_adjust_, warn_singular_, complementary_, a_, order_, orient_, edgecolor_, linewidth_, saturation_, width_, dodge_, fliersize_, whis_, scale_, scale_hue_, inner_, split_, k_depth_, outlier_prop_, trust_alpha_, showfliers_, linestyles_, join_, errwidth_, capsize_, errcolor_, x_ci_, scatter_, fit_reg_, logistic_, lowess_, robust_, x_partial_, y_partial_, truncate_, marker_, dropna_, label_, zorder_, color2_, markersize_, text_, explode_, colors_, autopct_, pctdistance_, shadow_, labeldistance_, startangle_, radius_, counterclock_, center_, frame_, rotatelabels_, normalize_, norm_x_, norm_y_, treemaps_pad_, bubble_spacing_), numpy.hstack([plot]*120), numpy.hstack([axes]*120))
        # automatic order for plot aggregation
        if zorder is None:
            zorder = count + 1
        else:
            pass
        # template value based on seaborn gallery
        if plot_ == 'boxplot+stripplot':
            if plot == 'boxplot':
                if whis is None:
                    whis = [0,100]
                else:
                    pass
                if width is None:
                    width = .6
                else:
                    pass
            else:
                pass
            if plot == 'stripplot':
                if size is None:
                    size = 4
                else:
                    pass
                if color is None:
                    color = '.3'
                else:
                    pass
                if linewidth is None:
                    linewidth = 0
                else:
                    pass
            else:
                pass
        else:
            pass
        if plot_ == 'stripplot+pointplot':
            if plot == 'stripplot':
                if hue is not None:
                    if dodge is None:
                        dodge = True
                    else:
                        pass
                else:
                    pass
                if alpha is None:
                    alpha = .25
                else:
                    pass
            else:
                pass
            if plot == 'pointplot':
                if hue is not None:
                    if dodge is None:
                        # check data type
                        if type(data[hue]) == list:
                            data_hue = numpy.array(data[hue])
                        elif numpy.issubdtype(type(data[hue]), numpy.ndarray) == True:
                            data_hue = data[hue]
                        else:
                            raise Exception('Unsupported dtype')
                        # drop numpy.nan
                        unique_data_hue = numpy.unique(data_hue)
                        unique_data_hue_not_nan = unique_data_hue[unique_data_hue != 'nan']
                        # set dodge
                        dodge = .8 - .8 / len(unique_data_hue_not_nan)
                    else:
                        pass
                else:
                    pass
                if join is None:
                    join = False 
                else:
                    pass
                if palette is None:
                    palette = 'dark'
                else:
                    pass
                if markers is None:
                    markers = 'd' 
                else:
                    pass
                if scale is None:
                    scale = 1.5
                else:
                    pass
            else:
                pass
        else:
            pass
        # plot each
        plot_single_def(plot=plot, 
                        x=x,
                        y=y, 
                        hue=hue, 
                        size=size, 
                        style=style, 
                        data=data, 
                        palette=palette, 
                        hue_order=hue_order, 
                        hue_norm=hue_norm, 
                        sizes=sizes, 
                        size_order=size_order, 
                        size_norm=size_norm, 
                        markers=markers, 
                        dashes=dashes, 
                        style_order=style_order, 
                        legend=legend, 
                        height=height, 
                        units=units, 
                        x_bins=x_bins,
                        y_bins=y_bins,
                        estimator=estimator, 
                        x_estimator=x_estimator,
                        ci=ci,
                        n_boot=n_boot,
                        alpha=alpha,
                        expand_margins=expand_margins,
                        jitter=jitter,
                        x_jitter=x_jitter,
                        y_jitter=y_jitter,
                        ax=ax,
                        weights=weights,
                        color=color,
                        seed=seed,
                        sort=sort,
                        err_style=err_style,
                        err_kws=err_kws,
                        stat=stat, 
                        bins=bins,
                        binwidth=binwidth,
                        binrange=binrange,
                        discrete=discrete,
                        cumulative=cumulative,
                        common_bins=common_bins,
                        common_norm=common_norm,
                        common_grid=common_grid,
                        multiple=multiple,
                        element=element,
                        fill=fill, 
                        shrink=shrink,
                        kde=kde,
                        kde_kws=kde_kws,
                        line_kws=line_kws,
                        thresh=thresh, 
                        pthresh=pthresh,
                        pmax=pmax,
                        cbar=cbar,
                        cbar_ax=cbar_ax,
                        cbar_kws=cbar_kws,
                        shade=shade,
                        vertical=vertical,
                        kernel=kernel,
                        bw=bw, 
                        gridsize=gridsize, 
                        cut=cut, 
                        clip=clip, 
                        shade_lowest=shade_lowest,
                        levels=levels,
                        bw_method=bw_method,
                        bw_adjust=bw_adjust,
                        data2=data2,
                        warn_singular=warn_singular,
                        complementary=complementary,
                        a=a,
                        order=order, 
                        orient=orient,
                        edgecolor=edgecolor,
                        linewidth=linewidth, 
                        saturation=saturation,
                        width=width,
                        dodge=dodge, 
                        fliersize=fliersize,
                        whis=whis,
                        scale=scale, 
                        scale_hue=scale_hue,
                        inner=inner,
                        split=split,
                        k_depth=k_depth,
                        outlier_prop=outlier_prop,
                        trust_alpha=trust_alpha,
                        showfliers=showfliers,
                        linestyles=linestyles,
                        join=join,
                        errwidth=errwidth,
                        capsize=capsize,
                        errcolor=errcolor,
                        x_ci=x_ci,
                        scatter=scatter,
                        fit_reg=fit_reg,
                        logistic=logistic,
                        lowess=lowess,
                        robust=robust,
                        x_partial=x_partial,
                        y_partial=y_partial,
                        truncate=truncate,
                        scatter_kws=scatter_kws,
                        marker=marker,
                        dropna=dropna, 
                        label=label,
                        zorder=zorder,
                        color2=color2,
                        markersize=markersize,
                        text=text, 
                        explode=explode, 
                        colors=colors, 
                        autopct=autopct, 
                        pctdistance=pctdistance, 
                        shadow=shadow, 
                        labeldistance=labeldistance, 
                        startangle=startangle, 
                        radius=radius, 
                        counterclock=counterclock, 
                        wedgeprops=wedgeprops, 
                        textprops=textprops, 
                        center=center, 
                        frame=frame, 
                        rotatelabels=rotatelabels, 
                        normalize=normalize, 
                        norm_x=norm_x, 
                        norm_y=norm_y, 
                        treemaps_pad=treemaps_pad, 
                        bar_kwargs=bar_kwargs, 
                        text_kwargs=text_kwargs,
                        bubble_spacing=bubble_spacing)
    return ax