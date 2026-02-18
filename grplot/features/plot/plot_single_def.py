import numpy
import grplot_seaborn as gs
from matplotlib.ticker import PercentFormatter
from pandas.api.types import is_numeric_dtype, is_object_dtype, is_categorical_dtype, is_string_dtype
from grplot.features.plot.packedbubbles import plot as pb
from grplot.features.plot.treemaps import plot as tms
from grplot.utils.first_valid_index import first_valid_index


def plot_single_def(plot,
                    data, 
                    x,
                    y, 
                    ax, 
                    hue, 
                    size, 
                    style, 
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
                    gridsize, 
                    cut, 
                    clip, 
                    levels,
                    bw_method,
                    bw_adjust,
                    warn_singular,
                    complementary,
                    order, 
                    orient,
                    edgecolor,
                    linewidth, 
                    saturation,
                    width,
                    dodge, 
                    fliersize,
                    whis,
                    inner,
                    split,
                    k_depth,
                    outlier_prop,
                    trust_alpha,
                    showfliers,
                    linestyles,
                    capsize,
                    x_ci,
                    scatter,
                    fit_reg,
                    logistic,
                    lowess,
                    robust,
                    regplot_logx,
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
                    alpha2,
                    explode, 
                    colors, 
                    hatch, 
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
                    bubble_spacing,
                    showmeans, 
                    meanprops, 
                    errorbar,
                    gap,
                    log_scale,
                    native_scale,
                    formatter,
                    linecolor,
                    width_method,
                    box_kws,
                    flier_kws,
                    density_norm,
                    inner_kws, 
                    text):
    # relational plot family
    if plot == 'scatterplot':
        if x is not None or y is not None:
            # default value
            if markers is None:
                markers = True
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.scatterplot(data=data, 
                            x=x, 
                            y=y, 
                            hue=hue, 
                             size=size,
                            style=style, 
                            palette=palette, 
                            hue_order=hue_order, 
                            hue_norm=hue_norm, 
                            sizes=sizes, 
                            size_order=size_order, 
                            size_norm=size_norm, 
                            markers=markers, 
                            style_order=style_order, 
                            legend=legend, 
                            alpha=alpha, 
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
            if orient is None:
                orient = 'x'
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
            gs.lineplot(data=data, 
                         x=x, 
                         y=y, 
                         hue=hue, 
                         size=size, 
                         style=style, 
                         units=units, 
                         weights=weights, 
                         palette=palette, 
                         hue_order=hue_order, 
                         hue_norm=hue_norm, 
                         sizes=sizes, 
                         size_order=size_order, 
                         size_norm=size_norm,
                         dashes=dashes, 
                         marker=marker, 
                         markers=markers, 
                         style_order=style_order, 
                         estimator=estimator, 
                         errorbar=errorbar, 
                         n_boot=n_boot, 
                         seed=seed, 
                         orient=orient, 
                         sort=sort, 
                         err_style=err_style, 
                         err_kws=err_kws, 
                         legend=legend, 
                        #  ci=ci, 
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
            gs.histplot(data=data, 
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
                         log_scale=log_scale, 
                         legend=legend, 
                         ax=ax,
                         alpha=alpha,
                         zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'kdeplot':
        if x is not None or y is not None:
            # default value
            # if vertical is None:
            #     vertical = False
            # else:
            #     pass
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
            if cumulative is None: 
                cumulative = False
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
            if levels is None: 
                levels = 10
            else: 
                pass
            if thresh is None:
                thresh = 0.05
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
            if legend is None:
                legend = True
            else:
                pass
            if cbar is None: 
                cbar = False
            else:
                pass
            # plot
            gs.kdeplot(data=data, 
                        x=x, 
                        y=y, 
                        hue=hue, 
                        weights=weights, 
                        palette=palette, 
                        hue_order=hue_order, 
                        hue_norm=hue_norm, 
                        color=color, 
                        fill=fill, 
                        multiple=multiple, 
                        common_norm=common_norm, 
                        common_grid=common_grid, 
                        cumulative=cumulative, 
                        bw_method=bw_method, 
                        bw_adjust=bw_adjust, 
                        warn_singular=warn_singular,
                        log_scale=log_scale, 
                        levels=levels, 
                        thresh=thresh, 
                        gridsize=gridsize, 
                        cut=cut, 
                        clip=clip, 
                        legend=legend, 
                        cbar=cbar, 
                        cbar_ax=cbar_ax, 
                        cbar_kws=cbar_kws, 
                        ax=ax, 
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
            gs.ecdfplot(data=data, 
                         x=x, 
                         y=y, 
                         hue=hue, 
                         weights=weights, 
                         stat=stat, 
                         complementary=complementary, 
                         palette=palette, 
                         hue_order=hue_order, 
                         hue_norm=hue_norm, 
                         log_scale=log_scale,  
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
            gs.rugplot(data=data, 
                        x=x, 
                        height=height, 
                        ax=ax,                         
                        y=y, 
                        hue=hue, 
                        expand_margins=expand_margins, 
                        palette=palette, 
                        hue_order=hue_order, 
                        hue_norm=hue_norm, 
                        legend=legend, 
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
               hatch=hatch, 
               autopct=autopct,
               pctdistance=pctdistance,
               labeldistance=labeldistance,
               shadow=shadow,
               startangle=startangle,
               radius=radius,
               counterclock=counterclock,
               wedgeprops=wedgeprops, 
               textprops=textprops, 
               center=center, 
               frame=frame, 
               rotatelabels=rotatelabels,
               normalize=normalize)
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
        tms(sizes=count, 
            norm_x=norm_x, 
            norm_y=norm_y, 
            color=color, 
            label=label, 
            value=value, 
            ax=ax, 
            pad=treemaps_pad, 
            bar_kwargs=bar_kwargs, 
            text_kwargs=text_kwargs)
    elif plot == 'packedbubblesplot':
        if x is not None and y is None:
            label, count = numpy.unique(data[x], return_counts=True)
        elif x is None and y is not None:
            label, count = numpy.unique(data[y], return_counts=True)
        elif x is not None and y is not None:
            raise Exception('Ambiguous axis label!')
        else:
            raise Exception('Define axis label!')
        # default value
        if bubble_spacing is None:
            bubble_spacing = 0.1
        else:
            pass
        if text == True:
            value = count
        else:
            value = None
        # plot
        pb(area=count,
           bubble_spacing=bubble_spacing,
           color=color,
           label=label,
           value=value,
           ax=ax)
    # categorical plot family
    elif plot == 'stripplot':
        if x is not None or y is not None:
            # default value
            if jitter is None:
                jitter = True
            else:
                pass
            if dodge is None:
                dodge = False
            else:
                pass
            if size is None:
                size = 5
            else:
                pass
            if edgecolor is None:
                edgecolor = 'auto'
            else:
                pass
            if linewidth is None:
                linewidth = 0
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.stripplot(data=data, 
                          x=x, 
                          y=y, 
                          hue=hue, 
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
                          hue_norm=hue_norm, 
                          log_scale=log_scale, 
                          native_scale=native_scale, 
                          formatter=formatter, 
                          legend=legend, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'swarmplot':
        if x is not None or y is not None:
            # default value
            if dodge is None:
                dodge = False
            else:
                pass
            if size is None:
                size = 5
            else:
                pass
            if linewidth is None:
                linewidth = 0
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.swarmplot(data=data, 
                          x=x, 
                          y=y, 
                          hue=hue, 
                          order=order, 
                          hue_order=hue_order, 
                          dodge=dodge, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          size=size, 
                          edgecolor=edgecolor, 
                          linewidth=linewidth, 
                          log_scale=log_scale, 
                          native_scale=native_scale, 
                          formatter=formatter, 
                          legend=legend, 
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
            if fill is None:
                fill = True
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if gap is None:
                gap = 0
            else:
                pass
            if whis is None:
                whis = 1.5
            else:
                pass
            if linecolor is None:
                linecolor = 'auto'
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            if showmeans is None:
                showmeans = False
            else:
                pass
            if meanprops is None:
                meanprops = {'marker':'s',
                             'markerfacecolor':'white', 
                             'markeredgecolor':'.3'}
            else:
                pass
            # plot
            gs.boxplot(data=data, 
                        x=x, 
                        y=y, 
                        hue=hue, 
                        order=order, 
                        hue_order=hue_order, 
                        orient=orient, 
                        color=color, 
                        palette=palette, 
                        saturation=saturation, 
                        fill=fill, 
                        dodge=dodge, 
                        width=width, 
                        gap=gap, 
                        whis=whis, 
                        linecolor=linecolor, 
                        linewidth=linewidth, 
                        fliersize=fliersize, 
                        hue_norm=hue_norm, 
                        log_scale=log_scale, 
                        native_scale=native_scale, 
                        formatter=formatter, 
                        legend=legend, 
                        showmeans=showmeans,
                        meanprops=meanprops,
                        ax=ax,
                        zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'violinplot':
        if x is not None or y is not None:
            # default value
            if saturation is None:
                saturation = 0.75
            else:
                pass
            if fill is None:
                fill = True
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
            if width is None:
                width = 0.8
            else:
                pass
            if dodge is None:
                dodge = 'auto'
            else:
                pass
            if gap is None:
                gap = 0
            else:
                pass
            if linecolor is None:
                linecolor = 'auto'
            else:
                pass
            if cut is None:
                cut = 2
            else:
                pass
            if gridsize is None:
                gridsize = 100
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
            if density_norm is None:
                density_norm = 'area'
            else:
                pass
            if common_norm is None:
                common_norm = True
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.violinplot(data=data, 
                           x=x, 
                           y=y, 
                           hue=hue, 
                           order=order, 
                           hue_order=hue_order, 
                           orient=orient, 
                           color=color, 
                           palette=palette, 
                           saturation=saturation, 
                           fill=fill, 
                           inner=inner, 
                           split=split, 
                           width=width, 
                           dodge=dodge, 
                           gap=gap, 
                           linewidth=linewidth, 
                           linecolor=linecolor, 
                           cut=cut, 
                           gridsize=gridsize, 
                           bw_method=bw_method, 
                           bw_adjust=bw_adjust, 
                           density_norm=density_norm, 
                           common_norm=common_norm, 
                           hue_norm=hue_norm, 
                           formatter=formatter, 
                           log_scale=log_scale, 
                           native_scale=native_scale, 
                           inner_kws=inner_kws, 
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
            if fill is None:
                fill = True
            else:
                pass
            if dodge is None:
                dodge = True
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if gap is None:
                gap = 0
            else:
                pass
            if width_method is None:
                width_method = 'exponential'
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
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.boxenplot(data=data, 
                          x=x, 
                          y=y, 
                          hue=hue, 
                          order=order, 
                          hue_order=hue_order, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          saturation=saturation, 
                          fill=fill, 
                          dodge=dodge, 
                          width=width, 
                          gap=gap, 
                          linewidth=linewidth, 
                          linecolor=linecolor, 
                          width_method=width_method, 
                          k_depth=k_depth, 
                          outlier_prop=outlier_prop, 
                          trust_alpha=trust_alpha, 
                          showfliers=showfliers, 
                          hue_norm=hue_norm, 
                          log_scale=log_scale, 
                          native_scale=native_scale, 
                          formatter=formatter, 
                          legend=legend, 
                          box_kws=box_kws, 
                          line_kws=line_kws, 
                          flier_kws=flier_kws, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'pointplot':
        if x is not None or y is not None:
            # default value
            if estimator is None:
                estimator = 'mean'
            else:
                pass
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
            if native_scale is None:
                native_scale = False
            else:
                pass
            if capsize is None:
                capsize = 0
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot            
            gs.pointplot(data=data,
                            x=x,  
                            y=y, 
                            hue=hue, 
                            order=order, 
                            hue_order=hue_order, 
                            estimator=estimator, 
                            errorbar=errorbar, 
                            n_boot=n_boot, 
                            seed=seed, 
                            units=units, 
                            weights=weights, 
                            color=color, 
                            palette=palette, 
                            markers=markers, 
                            linestyles=linestyles, 
                            dodge=dodge, 
                            log_scale=log_scale, 
                            native_scale=native_scale, 
                            orient=orient, 
                            capsize=capsize, 
                            formatter=formatter, 
                            legend=legend, 
                            err_kws=err_kws, 
                            ax=ax,
                            alpha=0.5,
                            zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'barplot':
        if x is not None or y is not None:
            # default value
            if estimator is None:
                estimator = 'mean'
            else:
                pass
            if n_boot is None:
                n_boot = 1000
            else:
                pass
            if saturation is None:
                saturation = 0.75
            else:
                pass
            if fill is None:
                fill = True
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if dodge is None:
                dodge = 'auto'
            else:
                pass
            if gap is None:
                gap = 0
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            if capsize is None:
                capsize = 0
            else:
                pass
            # plot
            gs.barplot(data=data, 
                        x=x, 
                        y=y, 
                        hue=hue,                             
                        order=order, 
                        hue_order=hue_order, 
                        estimator=estimator, 
                        errorbar=errorbar, 
                        n_boot=n_boot, 
                        seed=seed, 
                        units=units, 
                        weights=weights, 
                        orient=orient, 
                        color=color, 
                        palette=palette, 
                        saturation=saturation, 
                        fill=fill, 
                        hue_norm=hue_norm, 
                        width=width, 
                        dodge=dodge, 
                        gap=gap, 
                        log_scale=log_scale, 
                        native_scale=native_scale, 
                        formatter=formatter, 
                        legend=legend, 
                        capsize=capsize, 
                        err_kws=err_kws, 
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
            if fill is None:
                fill = True
            else:
                pass
            if stat is None:
                stat = 'count'
            else:
                pass
            if width is None:
                width = 0.8
            else:
                pass
            if dodge is None:
                dodge = 'auto'
            else:
                pass
            if native_scale is None:
                native_scale = False
            else:
                pass
            if legend is None:
                legend = 'auto'
            else:
                pass
            # plot
            gs.countplot(data=data, 
                          x=x, 
                          y=y, 
                          hue=hue, 
                          order=order, 
                          hue_order=hue_order, 
                          orient=orient, 
                          color=color, 
                          palette=palette, 
                          saturation=saturation, 
                          hue_norm=hue_norm, 
                          stat=stat, 
                          width=width, 
                          dodge=dodge, 
                          log_scale=log_scale, 
                          native_scale=native_scale, 
                          formatter=formatter, 
                          legend=legend, 
                          ax=ax,
                          alpha=alpha,
                          zorder=zorder)
        else:
            raise Exception('Define axis label!')
    elif plot == 'paretoplot':
        if x is not None and y is not None:
            if ((is_object_dtype(data[x]) == True) or (is_string_dtype(data[x]) == True) or (is_object_dtype(type(data[x][first_valid_index(data[x])])) == True) or (is_categorical_dtype(data[x]) == True) or (is_categorical_dtype(type(data[x][first_valid_index(data[x])])) == True)) and ((is_numeric_dtype(data[y]) == True) or (is_numeric_dtype(type(data[y][first_valid_index(data[y])])) == True)):
                data_pareto_x, idx, counts = numpy.unique(data[x], return_inverse=True, return_counts=True)
                data_bin_y = numpy.bincount(idx, weights=data[y])
                data_pareto_y = data_bin_y / counts
                sorting_formula = numpy.flip(data_pareto_y.argsort())
                data_pareto_x, data_pareto_y = data_pareto_x[sorting_formula], data_pareto_y[sorting_formula]
                # default value
                if estimator is None:
                    estimator = 'mean'
                else:
                    pass
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if saturation is None:
                    saturation = 0.75
                else:
                    pass
                if fill is None:
                    fill = True
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
                if gap is None:
                    gap = 0
                else:
                    pass
                if native_scale is None:
                    native_scale = False
                else:
                    pass
                if legend is None:
                    legend = 'auto'
                else:
                    pass
                if capsize is None:
                    capsize = 0
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
                gs.barplot(data=data, 
                            x=x, 
                            y=y, 
                            hue=hue,                             
                            order=data_pareto_x, 
                            hue_order=hue_order, 
                            estimator=estimator, 
                            errorbar=errorbar, 
                            n_boot=n_boot, 
                            seed=seed, 
                            units=units, 
                            weights=weights, 
                            orient=orient, 
                            color=color, 
                            palette=palette, 
                            saturation=saturation, 
                            fill=fill, 
                            hue_norm=hue_norm, 
                            width=width, 
                            dodge=dodge, 
                            gap=gap, 
                            log_scale=log_scale, 
                            native_scale=native_scale, 
                            formatter=formatter, 
                            legend=legend, 
                            capsize=capsize, 
                            err_kws=err_kws, 
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
                ax2.plot(data_pareto_x, data_cum_percentage, color=color2, marker=marker, markersize=markersize, alpha=alpha2)
                ax2.yaxis.set_major_formatter(PercentFormatter())
                ax2.grid(False)
                ax2.set_ylabel('Cumulative Percentage')
                ax.get_shared_x_axes().get_siblings(ax)[0].set_ylim([0,110])
            elif ((is_numeric_dtype(data[x]) == True) or (is_numeric_dtype(type(data[x][first_valid_index(data[x])])) == True)) and ((is_object_dtype(data[y]) == True) or (is_string_dtype(data[y]) == True) or (is_object_dtype(type(data[y][first_valid_index(data[y])])) == True) or (is_categorical_dtype(data[y]) == True) or (is_categorical_dtype(type(data[y][first_valid_index(data[y])])) == True)):
                data_pareto_y, idx, counts = numpy.unique(data[y], return_inverse=True, return_counts=True)
                data_bin_x = numpy.bincount(idx, weights=data[x])
                data_pareto_x = data_bin_x / counts
                sorting_formula = numpy.flip(data_pareto_x.argsort())
                data_pareto_x, data_pareto_y = data_pareto_x[sorting_formula], data_pareto_y[sorting_formula]
                # default value
                if estimator is None:
                    estimator = 'mean'
                else:
                    pass
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if n_boot is None:
                    n_boot = 1000
                else:
                    pass
                if saturation is None:
                    saturation = 0.75
                else:
                    pass
                if fill is None:
                    fill = True
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
                if gap is None:
                    gap = 0
                else:
                    pass
                if native_scale is None:
                    native_scale = False
                else:
                    pass
                if legend is None:
                    legend = 'auto'
                else:
                    pass
                if capsize is None:
                    capsize = 0
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
                gs.barplot(data=data, 
                            x=x, 
                            y=y, 
                            hue=hue,                             
                            order=data_pareto_y, 
                            hue_order=hue_order, 
                            estimator=estimator, 
                            errorbar=errorbar, 
                            n_boot=n_boot, 
                            seed=seed, 
                            units=units, 
                            weights=weights, 
                            orient=orient, 
                            color=color, 
                            palette=palette, 
                            saturation=saturation, 
                            fill=fill, 
                            hue_norm=hue_norm, 
                            width=width, 
                            dodge=dodge, 
                            gap=gap, 
                            log_scale=log_scale, 
                            native_scale=native_scale, 
                            formatter=formatter, 
                            legend=legend, 
                            capsize=capsize, 
                            err_kws=err_kws, 
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
                ax2.plot(data_cum_percentage, data_pareto_y, color=color2, marker=marker, markersize=markersize, alpha=alpha2)
                ax2.xaxis.set_major_formatter(PercentFormatter())
                ax2.grid(False)
                ax2.set_xlabel('Cumulative Percentage')
                ax.get_shared_y_axes().get_siblings(ax)[0].set_xlim([0,110])
            else:
                raise Exception('x and y must be a pair of numeric and object data types!')
        else:
            raise Exception('Define axis label!')
    # regression plot family
    elif plot == 'regplot':
        if x is not None or y is not None:
            # default value
            if scatter is None:
                scatter = True
            else:
                pass
            if fit_reg is None:
                fit_reg = True
            else:
                pass
            if ci is None:
                ci = 95
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
            if regplot_logx is None:
                regplot_logx = False
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
            gs.regplot(x=x, 
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
                        logx=regplot_logx, 
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
                        ax=ax)
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
            gs.residplot(data=data, 
                          x=x, 
                          y=y, 
                          x_partial=x_partial, 
                          y_partial=y_partial, 
                          lowess=lowess, 
                          order=order, 
                          robust=robust, 
                          dropna=dropna, 
                          label=label, 
                          color=color, 
                          scatter_kws=scatter_kws, 
                          line_kws=line_kws, 
                          ax=ax)
        else:
            raise Exception('Define axis label!')
    else:
        raise Exception('Unsupported plot!')
    return ax