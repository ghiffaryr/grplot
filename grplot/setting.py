import numpy
from grplot.hotfix.axislabel_fix import axislabel_fix
from grplot.features.font.check_fontsize import check_fontsize
from grplot.hotfix.histplot_legend_fix import histplot_legend_fix
from grplot.features.lim.check_lim import check_lim
from grplot.features.log.check_log import check_log
from grplot.features.sep.tick_sep.check_tick_sep import check_tick_sep
from grplot.features.dt.check_dt import check_dt
from grplot.hotfix.histplot_percent_add import histplot_percent_add
from grplot.features.add.tick_add.check_tick_add import check_tick_add
from grplot.features.rot.check_rot import check_rot
from grplot.features.statdesc.check_statdesc import check_statdesc
from grplot.features.text.check_text import check_text
from grplot.features.add.label_add.check_label_add import check_label_add
from grplot.features.add.log_label_add.check_log_label_add import check_log_label_add
from grplot.features.title.check_title import check_title
from grplot.features.font.font_def import font_def
from grplot.features.legend.check_legend import check_legend
from grplot.utils.arg_ax_type import arg_ax_type
from grplot.utils.arg_plot_ax_type import arg_plot_ax_type


def setting(plot,
            df, 
            x,
            y,
            fig,
            ax, 
            axes,
            hue,
            size,
            ci,
            multiple,
            sep, 
            xsep, 
            ysep, 
            lim,
            xlim,
            ylim,
            log, 
            xlog, 
            ylog, 
            dt, 
            xdt, 
            ydt,
            tick_add,
            xtick_add,
            ytick_add,
            rot,
            xrot,
            yrot,
            statdesc,
            xstatdesc,
            ystatdesc,
            text,
            xtext,
            ytext,
            label_add,
            xlabel_add,
            ylabel_add,
            title,
            fontsize,
            tick_fontsize,
            legend_fontsize,
            text_fontsize,
            label_fontsize,
            title_fontsize,
            legend_loc):
    plot, legend_loc = map(arg_ax_type, (plot, legend_loc), numpy.hstack([axes]*2))
    if plot is None:
        pass
    elif type(plot) == str:
        ax = axislabel_fix(ax, x, y)
        xaxislabel = ax.get_xlabel()
        yaxislabel = ax.get_ylabel()
        plot_, hue_, size_, ci_, multiple_ = plot, hue, size, ci, multiple
        tick_fontsize, \
        legend_fontsize, \
        text_fontsize, \
        label_fontsize, \
        title_fontsize = check_fontsize(fontsize=fontsize, 
                                        tick_fontsize=tick_fontsize, 
                                        legend_fontsize=legend_fontsize, 
                                        text_fontsize=text_fontsize, 
                                        label_fontsize=label_fontsize, 
                                        title_fontsize=title_fontsize, 
                                        axes=axes)
        h, l = [], []
        for plot in plot_.split('+'):
                hue, size = map(arg_plot_ax_type, (hue_, size_), numpy.hstack([plot]*2), numpy.hstack([axes]*2))
                h_, l_ = histplot_legend_fix(plot=plot_, # only for single histplot
                                             ax=ax,
                                             hue=hue,
                                             size=size,
                                             legend_fontsize=legend_fontsize)
                h.extend(h_)
                l.extend(l_)
        check_lim(ax=ax, 
                  lim=lim, 
                  xlim=xlim, 
                  ylim=ylim, 
                  xaxislabel=xaxislabel, 
                  yaxislabel=yaxislabel, 
                  axes=axes)
        check_log(ax=ax, 
                  log=log,
                  xlog=xlog, 
                  ylog=ylog, 
                  xaxislabel=xaxislabel, 
                  yaxislabel=yaxislabel,
                  axes=axes)
        fig.canvas.draw() # draw the actual value
        check_tick_sep(df=df,  
                       ax=ax, 
                       sep=sep, 
                       xsep=xsep,
                       ysep=ysep,
                       xaxislabel=xaxislabel, 
                       yaxislabel=yaxislabel,
                       axes=axes)
        check_dt(ax=ax, 
                 dt=dt,
                 xdt=xdt, 
                 ydt=ydt, 
                 xaxislabel=xaxislabel, 
                 yaxislabel=yaxislabel,
                 axes=axes)
        for plot in plot_.split('+'):
                tick_add, xtick_add, ytick_add = histplot_percent_add(plot=plot, 
                                                                      tick_add=tick_add,
                                                                      xtick_add=xtick_add, 
                                                                      ytick_add=ytick_add, 
                                                                      xaxislabel=xaxislabel, 
                                                                      yaxislabel=yaxislabel)
        check_tick_add(ax=ax, 
                       add=tick_add,
                       xadd=xtick_add, 
                       yadd=ytick_add, 
                       xaxislabel=xaxislabel, 
                       yaxislabel=yaxislabel,
                       axes=axes)
        check_rot(ax=ax, 
                  rot=rot,
                  xrot=xrot, 
                  yrot=yrot, 
                  xaxislabel=xaxislabel, 
                  yaxislabel=yaxislabel,
                  axes=axes)
        check_statdesc(df=df, 
                       ax=ax, 
                       statdesc=statdesc, 
                       xstatdesc=xstatdesc, 
                       ystatdesc=ystatdesc, 
                       sep=sep,
                       xsep=xsep,
                       ysep=ysep,
                       add=tick_add,
                       xadd=xtick_add, 
                       yadd=ytick_add, 
                       xaxislabel=xaxislabel, 
                       yaxislabel=yaxislabel,
                       axes=axes)
        for plot in plot_.split('+'):
                ci, hue, multiple  = map(arg_plot_ax_type, (ci_, hue_, multiple_), numpy.hstack([plot]*3), numpy.hstack([axes]*3))
                check_text(plot=plot, 
                           df=df, 
                           x=x,
                           y=y, 
                           ax=ax, 
                           ci=ci, 
                           hue=hue, 
                           multiple=multiple, 
                           text=text, 
                           xtext=xtext, 
                           ytext=ytext, 
                           sep=sep,
                           xsep=xsep,
                           ysep=ysep,
                           add=tick_add, 
                           xadd=xtick_add, 
                           yadd=ytick_add, 
                           text_fontsize=text_fontsize, 
                           xaxislabel=xaxislabel, 
                           yaxislabel=yaxislabel, 
                           axes=axes)
        check_label_add(ax=ax, 
                        add=label_add,
                        xadd=xlabel_add, 
                        yadd=ylabel_add, 
                        xaxislabel=xaxislabel, 
                        yaxislabel=yaxislabel,
                        axes=axes)
        check_log_label_add(ax=ax, 
                            add=log,
                            xadd=xlog, 
                            yadd=ylog, 
                            xaxislabel=xaxislabel, 
                            yaxislabel=yaxislabel,
                            axes=axes)
        check_title(ax=ax,
                    title=title,
                    title_fontsize=title_fontsize,
                    axes=axes)
        for plot in plot_.split('+'):
                font_def(plot=plot, 
                         df=df, 
                         x=x, 
                         y=y, 
                         ax=ax, 
                         tick_fontsize=tick_fontsize, 
                         label_fontsize=label_fontsize)
                hue, size = map(arg_plot_ax_type, (hue_, size_), numpy.hstack([plot]*2), numpy.hstack([axes]*2))
                check_legend(plot=plot, 
                             ax=ax, 
                             legend_fontsize=legend_fontsize, 
                             legend_loc=legend_loc, 
                             hue=hue, 
                             size=size, 
                             h=h, 
                             l=l)
    else:
        raise Exception('Unknown plot argument!')
    return ax