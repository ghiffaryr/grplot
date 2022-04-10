import numpy
from grplot.features.alpha.check_alpha import check_alpha
from grplot.features.plot.plot_single_def import plot_single_def


def plot_multi_def(plot,
                   x,
                   y, 
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
                   ax,
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
    alpha_ = alpha
    dodge_ = dodge
    # plotting
    if type(plot) == str:
        for count, plt in enumerate(plot.split('+')):
            # order for plot aggregation
            zorder = count + 1
            # check alpha
            alpha = check_alpha(alpha=alpha_, count=count)
            # template value based on seaborn gallery
            if plot == 'boxplot+stripplot':
                if plt == 'boxplot':
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
                if plt == 'stripplot':
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
            if plot == 'stripplot+pointplot':
                if plt == 'stripplot':
                    if hue is not None:
                        if dodge_ is None:
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
                if plt == 'pointplot':
                    if hue is not None:
                        if dodge_ is None:
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
                            dodge = .8 - .8 / len(numpy.unique(unique_data_hue_not_nan))
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
            plot_single_def(plot=plt, 
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
    else:
        raise Exception('Wrong plot argument!')
    return ax