from grplot.features.add.label_add.check_label_add import check_label_add
from grplot.features.add.log_label_add.check_log_label_add import check_log_label_add
from grplot.features.add.tick_add.check_tick_add import check_tick_add
from grplot.features.dt.check_dt import check_dt
from grplot.features.font.check_fontsize import check_fontsize
from grplot.features.font.font_def import font_def
from grplot.features.log.check_log import check_log
from grplot.features.rot.check_rot import check_rot
from grplot.features.sep.tick_sep.check_tick_sep import check_tick_sep
from grplot.features.statdesc.check_statdesc import check_statdesc
from grplot.features.text.check_text import check_text
from grplot.features.title.check_title import check_title
from grplot.hotfix.histplot_legend_fix import histplot_legend_fix
from grplot.hotfix.histplot_percent_add import histplot_percent_add


def setting(plot,
            df, 
            x,
            y,
            fig,
            ax, 
            axes,
            xaxislabel, 
            yaxislabel,  
            hue,
            size,
            ci,
            multiple,
            cumulative, 
            sep, 
            xsep, 
            ysep, 
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
            title_fontsize):
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
    h, l = histplot_legend_fix(plot=plot,
                               ax=ax,
                               hue=hue,
                               size=size,
                               legend_fontsize=legend_fontsize,
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
    tick_add, xtick_add, ytick_add = histplot_percent_add(plot=plot, 
                                                          tick_add=tick_add,
                                                          xtick_add=xtick_add, 
                                                          ytick_add=ytick_add, 
                                                          xaxislabel=xaxislabel, 
                                                          yaxislabel=yaxislabel,
                                                          axes=axes)
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
    check_text(plot=plot, 
               df=df, 
               x=x,
               y=y,
               ax=ax, 
               ci=ci, 
               cumulative=cumulative, 
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
    font_def(plot=plot, 
             df=df,
             x=x,
             y=y,
             ax=ax,
             axes=axes,
             tick_fontsize=tick_fontsize,
             legend_fontsize=legend_fontsize, 
             label_fontsize=label_fontsize, 
             hue=hue,
             size=size,
             h=h, 
             l=l)
    return ax