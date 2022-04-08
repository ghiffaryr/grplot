import numpy
import seaborn as sns
import squarify as sfy
from pandas.api.types import is_numeric_dtype, is_object_dtype, is_categorical_dtype


def plot_single_def(plot,
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
                    text_kwargs): #disini default kalau nilai khusus plotnya none diganti default seaborn per plot
    # relational plot family
    if plot == 'scatterplot':
        if x is not None or y is not None:
            # default value
            if markers is None:
                markers = True
            else:
                pass
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            sns.scatterplot(x=x, 
                            y=y, 
                            hue=hue, 
                            style=style, 
                            size=size, 
                            data=data, 
                            palette=palette, 
                            hue_order=hue_order, 
                            hue_norm=hue_norm, 
                            sizes=sizes, 
                            size_order=size_order, 
                            size_norm=size_norm, 
                            markers=markers, 
                            style_order=style_order, 
                            x_bins=x_bins, 
                            y_bins=y_bins, 
                            units=units, 
                            estimator=None, 
                            ci=ci, 
                            n_boot=n_boot, 
                            alpha=alpha, 
                            x_jitter=x_jitter, 
                            y_jitter=y_jitter, 
                            legend=legend, 
                            ax=ax,
                            zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'lineplot':
        if x is not None or y is not None:
            # default value
            if dashes is None:
                dashes = True
            else:
                pass
            if estimator is None:
                estimator = 'mean'
            else:
                pass
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if sort is None:
                sort = True
            else:
                pass
            if err_style is None:
                err_style = 'band'
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            sns.lineplot(x=x, 
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
                         dashes=dashes, 
                         markers=markers, 
                         style_order=style_order, 
                         units=units, 
                         estimator=estimator, 
                         ci=ci, 
                         n_boot=n_boot, 
                         seed=seed, 
                         sort=sort, 
                         err_style=err_style, 
                         err_kws=err_kws, 
                         legend=legend, 
                         ax=ax,
                         alpha=alpha,
                         zorder=zorder)
        else:
            raise Exception('Define axis label!')
    # distribution plot family
    elif plot == 'histplot':
        if x is not None or y is not None:
            # default value
            if stat is None: 
                stat = 'count'
            else: 
                pass
            if bins is None: 
                bins = 'auto'
            else: 
                pass
            if cumulative is None: 
                cumulative = False
            else: 
                pass
            if common_bins is None: 
                common_bins = True
            else: 
                pass
            if common_norm is None: 
                common_norm = True
            else: 
                pass
            if multiple is None: 
                multiple = 'layer'
            else: 
                pass
            if element is None: 
                element = 'bars'
            else: 
                pass
            if fill is None: 
                fill = True
            else: 
                pass
            if shrink is None: 
                shrink = 1
            else: 
                pass
            if kde is None: 
                kde = False
            else: 
                pass
            if thresh is None: 
                thresh = 0
            else: 
                pass
            if cbar is None: 
                cbar = False
            else: 
                pass
            if legend is None:
                legend = True
            else:
                pass
            # plot
            sns.histplot(data=data, 
                         x=x, 
                         y=y, 
                         hue=hue, 
                         weights=weights, 
                         stat=stat, 
                         bins=bins, 
                         binwidth=binwidth, 
                         binrange=binrange, 
                         discrete=discrete, 
                         cumulative=cumulative, 
                         common_bins=common_bins, 
                         common_norm=common_norm, 
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
                         palette=palette, 
                         hue_order=hue_order, 
                         hue_norm=hue_norm, 
                         color=color, 
                         log_scale=None, 
                         legend=legend, 
                         ax=ax,
                         alpha=alpha,
                         zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'kdeplot':
        if x is not None or y is not None:
            # default value
            if vertical is None:
                vertical = False
            else:
                pass
            if gridsize is None:
                gridsize = 200
            else:
                pass
            if cut is None:
                cut = 3
            else:
                pass
            if cumulative is None: 
                cumulative = False
            else: 
                pass
            if cbar is None: 
                cbar = False
            else:
                pass
            if multiple is None: 
                multiple = 'layer'
            else: 
                pass
            if common_norm is None: 
                common_norm = True
            else: 
                pass
            if common_grid is None: 
                common_grid = False
            else: 
                pass
            if levels is None: 
                levels = 10
            else: 
                pass
            if thresh is None:
                thresh = 0.05
            else:
                pass
            if bw_method is None:
                bw_method = 'scott'
            else:
                pass
            if bw_adjust is None:
                bw_adjust = 1
            else:
                pass
            if warn_singular is None:
                warn_singular = True
            else:
                pass
            if legend is None:
                legend = True
            else:
                pass
            # plot
            sns.kdeplot(x=x, 
                        y=y, 
                        shade=shade, 
                        vertical=vertical, 
                        kernel=kernel, 
                        bw=bw, 
                        gridsize=gridsize, 
                        cut=cut, 
                        clip=clip, 
                        legend=legend, 
                        cumulative=cumulative, 
                        shade_lowest=shade_lowest, 
                        cbar=cbar, 
                        cbar_ax=cbar_ax, 
                        cbar_kws=cbar_kws, 
                        ax=ax, 
                        weights=weights, 
                        hue=hue, 
                        palette=palette, 
                        hue_order=hue_order, 
                        hue_norm=hue_norm, 
                        multiple=multiple, 
                        common_norm=common_norm, 
                        common_grid=common_grid, 
                        levels=levels, 
                        thresh=thresh, 
                        bw_method=bw_method, 
                        bw_adjust=bw_adjust, 
                        log_scale=None, 
                        color=color, 
                        fill=fill, 
                        data=data, 
                        data2=data2, 
                        warn_singular=warn_singular,
                        alpha=alpha,
                        zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'ecdfplot':
        if x is not None or y is not None:
            # default value
            if stat is None:
                stat = 'proportion'
            else:
                pass
            if complementary is None:
                complementary = False
            else:
                pass
            if legend is None:
                legend = True
            else:
                pass
            # plot
            sns.ecdfplot(data=data, 
                         x=x, 
                         y=y, 
                         hue=hue, 
                         weights=weights, 
                         stat=stat, 
                         complementary=complementary, 
                         palette=palette, 
                         hue_order=hue_order, 
                         hue_norm=hue_norm, 
                         log_scale=None, 
                         legend=legend, 
                         ax=ax,
                         alpha=alpha,
                         zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'rugplot':
        if x is not None or y is not None:
            # default value
            if height is None:
                height = 0.025
            else:
                pass
            if expand_margins is None:
                expand_margins = True
            else:
                pass
            if legend is None:
                legend = True
            else:
                pass
            # plot
            sns.rugplot(x=x, 
                        height=height, 
                        ax=ax, 
                        data=data, 
                        y=y, 
                        hue=hue, 
                        palette=palette, 
                        hue_order=hue_order, 
                        hue_norm=hue_norm, 
                        expand_margins=expand_margins, 
                        legend=legend, 
                        a=a,
                        alpha=alpha,
                        zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'pieplot':
        if x is not None and y is None:
            label, count = numpy.unique(data[x], return_counts=True)
        elif x is None and y is not None:
            label, count = numpy.unique(data[y], return_counts=True)
        elif x is not None and y is not None:
            raise Exception('Ambiguous axis label!')
        else:
            raise Exception('Define axis label!')
        # default value
        if pctdistance is None:
            pctdistance = 0.6
        else:
            pass
        if shadow is None:
            shadow = False
        else:
            pass
        if labeldistance is None:
            labeldistance = 1.1
        else:
            pass
        if startangle is None:
            startangle = 0
        else:
            pass
        if radius is None:
            radius = 1
        else:
            pass
        if counterclock is None:
            counterclock = True
        else:
            pass
        if center is None:
            center = (0, 0)
        else:
            pass
        if frame is None:
            frame = False
        else:
            pass
        if rotatelabels is None:
            rotatelabels = False
        else:
            pass
        if normalize is None:
            normalize = True
        else:
            pass
        if autopct is None and text == True:
            autopct = '%1.2f%%'
        else:
            pass
        # plot
        ax.pie(x=count, 
               labels=label,
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
               )
    elif plot == 'treemapsplot':
        if x is not None and y is None:
            label, count = numpy.unique(data[x], return_counts=True)
        elif x is None and y is not None:
            label, count = numpy.unique(data[y], return_counts=True)
        elif x is not None and y is not None:
            raise Exception('Ambiguous axis label!')
        else:
            raise Exception('Define axis label!')
        # default value
        if norm_x is None:
            norm_x = 100
        else:
            pass
        if norm_y is None:
            norm_y = 100
        else:
            pass
        if text == True:
            value = count
        else:
            value = None
        if treemaps_pad is None:
            treemaps_pad = False
        else:
            pass
        # plot
        sfy.plot(sizes=count, 
                 norm_x=norm_x, 
                 norm_y=norm_y, 
                 color=color, 
                 label=label, 
                 value=value, 
                 ax=ax, 
                 pad=treemaps_pad, 
                 bar_kwargs=bar_kwargs, 
                 text_kwargs=text_kwargs)
    # categorical plot family
    elif plot == 'stripplot':
        if x is not None or y is not None:
            # default value
            if jitter is None:
                jitter = True
            else:
                pass
            if size is None:
                size = 5
            else:
                pass
            if edgecolor is None:
                edgecolor = 'gray'
            else:
                pass
            if linewidth is None:
                linewidth = 0
            else:
                pass
            # plot
            sns.stripplot(x=x, 
                          y=y, 
                          hue=hue, 
                          data=data, 
                          order=order, 
                          hue_order=hue_order, 
                          jitter=jitter, 
                          dodge=dodge, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          size=size, 
                          edgecolor=edgecolor, 
                          linewidth=linewidth, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'swarmplot':
        if x is not None or y is not None:
            # default value
            if size is None:
                size = 5
            else:
                pass
            if edgecolor is None:
                edgecolor = 'gray'
            else:
                pass
            if linewidth is None:
                linewidth = 0
            else:
                pass
            # plot
            sns.swarmplot(x=x, 
                          y=y, 
                          hue=hue, 
                          data=data, 
                          order=order, 
                          hue_order=hue_order, 
                          dodge=dodge, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          size=size, 
                          edgecolor=edgecolor, 
                          linewidth=linewidth, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'boxplot':
        if x is not None or y is not None:
            # default value
            if saturation is None:
                saturation = 0.75
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            if fliersize is None:
                fliersize = 5
            else:
                pass
            if whis is None:
                whis = 1.5
            else:
                pass
            # plot
            sns.boxplot(x=x, 
                        y=y, 
                        hue=hue, 
                        data=data, 
                        order=order, 
                        hue_order=hue_order, 
                        orient=orient, 
                        color=color, 
                        palette=palette, 
                        saturation=saturation, 
                        width=width, 
                        dodge=dodge, 
                        fliersize=fliersize, 
                        linewidth=linewidth, 
                        whis=whis, 
                        ax=ax,
                        zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'violinplot':
        if x is not None or y is not None:
            # default value
            if bw is None:
                bw = 'scott'
            else:
                pass
            if cut is None:
                cut = 2
            else:
                pass
            if scale is None:
                scale = 'area'
            else:
                pass
            if gridsize is None:
                gridsize = 100
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if inner is None:
                inner = 'box'
            else:
                pass
            if split is None:
                split = False
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            if saturation is None:
                saturation = 0.75
            else:
                pass
            # plot
            sns.violinplot(x=x, 
                           y=y, 
                           hue=hue, 
                           data=data, 
                           order=order, 
                           hue_order=hue_order, 
                           bw=bw, 
                           cut=cut, 
                           scale=scale, 
                           scale_hue=scale_hue, 
                           gridsize=gridsize, 
                           width=width, 
                           inner=inner, 
                           split=split, 
                           dodge=dodge, 
                           orient=orient, 
                           linewidth=linewidth, 
                           color=color, 
                           palette=palette, 
                           saturation=saturation, 
                           ax=ax,
                           alpha=alpha,
                           zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'boxenplot':
        if x is not None or y is not None:
            # default value
            if saturation is None:
                saturation = 0.75
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            if k_depth is None:
                k_depth = 'tukey'
            else:
                pass
            if outlier_prop is None:
                outlier_prop = 0.007
            else:
                pass
            if trust_alpha is None:
                trust_alpha = 0.05
            else:
                pass
            if showfliers is None:
                showfliers = True
            else:
                pass
            if scale is None:
                scale = 'exponential'
            else:
                pass
            # plot
            sns.boxenplot(x=x, 
                          y=y, 
                          hue=hue, 
                          data=data, 
                          order=order, 
                          hue_order=hue_order, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          saturation=saturation, 
                          width=width, 
                          dodge=dodge, 
                          k_depth=k_depth, 
                          linewidth=linewidth, 
                          scale=scale, 
                          outlier_prop=outlier_prop, 
                          trust_alpha=trust_alpha, 
                          showfliers=showfliers, 
                          ax=ax,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'pointplot':
        if x is not None or y is not None:
            # default value
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if markers is None:
                markers = 'o'
            else:
                pass
            if linestyles is None:
                linestyles = '-'
            else:
                pass
            if dodge is None:
                dodge = False
            else:
                pass
            if join is None:
                join = True
            else:
                pass
            if scale is None:
                scale = 1
            else:
                pass
            # plot
            sns.pointplot(x=x, 
                          y=y, 
                          hue=hue, 
                          data=data, 
                          order=order, 
                          hue_order=hue_order, 
                          ci=ci, 
                          n_boot=n_boot, 
                          units=units, 
                          seed=seed, 
                          markers=markers, 
                          linestyles=linestyles, 
                          dodge=dodge, 
                          join=join, 
                          scale=scale, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          errwidth=errwidth, 
                          capsize=capsize, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'barplot':
        if x is not None or y is not None:
            # default value
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if saturation is None:
                saturation = 0.75
            else:
                pass
            if errcolor is None:
                errcolor = '.26'
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            # plot
            sns.barplot(x=x, 
                        y=y, 
                        hue=hue, 
                        data=data, 
                        order=order, 
                        hue_order=hue_order, 
                        ci=ci, 
                        n_boot=n_boot, 
                        units=units, 
                        seed=seed, 
                        orient=orient, 
                        color=color, 
                        palette=palette, 
                        saturation=saturation, 
                        errcolor=errcolor, 
                        errwidth=errwidth, 
                        capsize=capsize, 
                        dodge=dodge, 
                        ax=ax,
                        alpha=alpha,
                        zorder=zorder)
            if x is not None:
                ax.set_xlabel(x)
            else:
                pass
            if y is not None:
                ax.set_ylabel(y)
            else:
                pass
        else:
            raise Exception('Define axis label!')
    elif plot == 'countplot':
        if x is not None or y is not None:
            # default value
            if saturation is None:
                saturation = 0.75
            else:
                pass
            sns.countplot(x=x, 
                          y=y, 
                          hue=hue, 
                          data=data, 
                          order=order, 
                          hue_order=hue_order, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          saturation=saturation, 
                          dodge=dodge, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'paretoplot':
        if x is not None and y is not None:
            if ((is_object_dtype(data[x]) == True) or (is_object_dtype(type(data[x][0])) == True) or (is_categorical_dtype(data[x]) == True) or (is_categorical_dtype(type(data[x][0])) == True)) and ((is_numeric_dtype(data[y]) == True) or (is_numeric_dtype(type(data[y][0])) == True)):
                data_pareto_x, idx, counts = numpy.unique(data[x], return_inverse=True, return_counts=True)
                data_bin_y = numpy.bincount(idx, weights=data[y])
                data_pareto_y = data_bin_y / counts
                sorting_formula = numpy.flip(data_pareto_y.argsort())
                data_pareto_x, data_pareto_y = data_pareto_x[sorting_formula], data_pareto_y[sorting_formula]
                # default value
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if saturation is None:
                    saturation = 0.75
                else:
                    pass
                if errcolor is None:
                    errcolor = '.26'
                else:
                    pass
                if dodge is None:
                    dodge = True
                else:
                    pass
                if color2 is None:
                    color2 = '.26'
                else:
                    pass
                if marker is None:
                    marker = 'D'
                else:
                    pass
                if markersize is None:
                    markersize = 7
                else:
                    pass
                # plot
                sns.barplot(x=x, 
                            y=y, 
                            hue=hue, 
                            data=data, 
                            order=data_pareto_x, 
                            hue_order=data_pareto_x, 
                            ci=ci, 
                            n_boot=n_boot, 
                            units=units, 
                            seed=seed, 
                            orient=orient, 
                            color=color, 
                            palette=palette, 
                            saturation=saturation, 
                            errcolor=errcolor, 
                            errwidth=errwidth, 
                            capsize=capsize, 
                            dodge=dodge, 
                            ax=ax,
                            alpha=alpha,
                            zorder=zorder)
                if x is not None:
                    ax.set_xticks(ax.get_xticks())
                    ax.set_xlabel(x)
                else:
                    pass
                if y is not None:
                    ax.set_yticks(ax.get_yticks())
                    ax.set_ylabel(y)
                else:
                    pass
                data_cum_percentage = numpy.cumsum(data_pareto_y)/numpy.sum(data_pareto_y)*100
                ax2 = ax.twinx()
                ax2.plot(data_pareto_x, data_cum_percentage, color=color2, marker=marker, markersize=markersize)
                ax2.set_ylabel('Cumulative Percentage')
                ax.get_shared_x_axes().get_siblings(ax)[0].set_yticks(ax.get_shared_x_axes().get_siblings(ax)[0].get_yticks())
                ax.get_shared_x_axes().get_siblings(ax)[0].set_yticklabels(['{:1.0f}%'.format(y) for y in ax.get_shared_x_axes().get_siblings(ax)[0].get_yticks()])
            elif ((is_numeric_dtype(data[x]) == True) or (is_numeric_dtype(type(data[x][0])) == True)) and ((is_object_dtype(data[y]) == True) or (is_object_dtype(type(data[y][0])) == True) or (is_categorical_dtype(data[y]) == True) or (is_categorical_dtype(type(data[y][0])) == True)):
                data_pareto_y, idx, counts = numpy.unique(data[y], return_inverse=True, return_counts=True)
                data_bin_x = numpy.bincount(idx, weights=data[x])
                data_pareto_x = data_bin_x / counts
                sorting_formula = numpy.flip(data_pareto_x.argsort())
                data_pareto_x, data_pareto_y = data_pareto_x[sorting_formula], data_pareto_y[sorting_formula]
                # default value
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if saturation is None:
                    saturation = 0.75
                else:
                    pass
                if errcolor is None:
                    errcolor = '.26'
                else:
                    pass
                if dodge is None:
                    dodge = True
                else:
                    pass
                if color2 is None:
                    color2 = '.26'
                else:
                    pass
                if marker is None:
                    marker = 'D'
                else:
                    pass
                if markersize is None:
                    markersize = 7
                else:
                    pass
                # plot
                sns.barplot(x=x, 
                            y=y, 
                            hue=hue, 
                            data=data, 
                            order=data_pareto_y, 
                            hue_order=data_pareto_y, 
                            ci=ci, 
                            n_boot=n_boot, 
                            units=units, 
                            seed=seed, 
                            orient=orient, 
                            color=color, 
                            palette=palette, 
                            saturation=saturation, 
                            errcolor=errcolor, 
                            errwidth=errwidth, 
                            capsize=capsize, 
                            dodge=dodge, 
                            ax=ax,
                            alpha=alpha,
                            zorder=zorder)
                if x is not None:
                    ax.set_xticks(ax.get_xticks())
                    ax.set_xlabel(x)
                else:
                    pass
                if y is not None:
                    ax.set_yticks(ax.get_yticks())
                    ax.set_ylabel(y)
                else:
                    pass
                data_cum_percentage = numpy.cumsum(data_pareto_x)/numpy.sum(data_pareto_x)*100
                ax2 = ax.twiny()
                ax2.plot(data_cum_percentage, data_pareto_y, color=color2, marker=marker, markersize=markersize)
                ax2.set_xlabel('Cumulative Percentage')
                ax.get_shared_y_axes().get_siblings(ax)[0].set_xticks(ax.get_shared_y_axes().get_siblings(ax)[0].get_xticks())
                ax.get_shared_y_axes().get_siblings(ax)[0].set_xticklabels(['{:1.0f}%'.format(x) for x in ax.get_shared_y_axes().get_siblings(ax)[0].get_xticks()])
            else:
                raise Exception('x and y must be a pair of numeric and object data types!')
        else:
            raise Exception('Define axis label!')
    # regression plot family
    elif plot == 'regplot':
        if x is not None or y is not None:
            # default value
            if x_ci is None:
                x_ci = 'ci'
            else:
                pass
            if scatter is None:
                scatter = True
            else:
                pass
            if fit_reg is None:
                fit_reg = True
            else:
                pass
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if order is None:
                order = 1
            else:
                pass
            if logistic is None:
                logistic = False
            else:
                pass
            if lowess is None:
                lowess = False
            else:
                pass
            if robust is None:
                robust = False
            else:
                pass
            if truncate is None:
                truncate = True
            else:
                pass
            if dropna is None:
                dropna = True
            else:
                pass
            if marker is None:
                marker = 'o'
            else:
                pass
            # plot
            sns.regplot(x=x, 
                        y=y, 
                        data=data, 
                        x_estimator=x_estimator, 
                        x_bins=x_bins, 
                        x_ci=x_ci, 
                        scatter=scatter, 
                        fit_reg=fit_reg, 
                        ci=ci, 
                        n_boot=n_boot, 
                        units=units, 
                        seed=seed, 
                        order=order, 
                        logistic=logistic, 
                        lowess=lowess, 
                        robust=robust, 
                        logx=False, 
                        x_partial=x_partial, 
                        y_partial=y_partial, 
                        truncate=truncate, 
                        dropna=dropna, 
                        x_jitter=x_jitter, 
                        y_jitter=y_jitter, 
                        label=label, 
                        color=color, 
                        marker=marker, 
                        scatter_kws=scatter_kws, 
                        line_kws=line_kws, 
                        ax=ax,
                        alpha=alpha,
                        zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'residplot':
        if x is not None or y is not None:
            # default value
            if lowess is None:
                lowess = False
            else:
                pass
            if order is None:
                order = 1
            else:
                pass
            if robust is None:
                robust = False
            else:
                pass
            if dropna is None:
                dropna = True
            else:
                pass
            # plot
            sns.residplot(x=x, 
                          y=y, 
                          data=data, 
                          lowess=lowess, 
                          x_partial=x_partial, 
                          y_partial=y_partial, 
                          order=order, 
                          robust=robust, 
                          dropna=dropna, 
                          label=label, 
                          color=color, 
                          scatter_kws=scatter_kws, 
                          line_kws=line_kws, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    else:
        raise Exception('Unsupported plot!')
    return ax