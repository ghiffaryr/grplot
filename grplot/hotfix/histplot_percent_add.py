def histplot_percent_add(plot, tick_add, xtick_add, ytick_add, xaxislabel, yaxislabel):
    if plot == 'histplot':
        if xaxislabel == 'Percent':
            if xtick_add is None and tick_add is None :
                tick_add = {'Percent':'_%'}
            elif xtick_add is not None and tick_add is None:
                xtick_add['Percent'] = '_%'
            elif xtick_add is None and tick_add is not None:
                tick_add['Percent'] = '_%'
            else: # xtick_add is not None and tick_add is not None:
                xtick_add['Percent'] = '_%'
        elif yaxislabel == 'Percent':
            if ytick_add is None and tick_add is None :
                tick_add = {'Percent':'_%'}
            elif ytick_add is not None and tick_add is None:
                ytick_add['Percent'] = '_%'
            elif ytick_add is None and tick_add is not None:
                tick_add['Percent'] = '_%'
            else: # ytick_add is not None and tick_add is not None:
                ytick_add['Percent'] = '_%'
        else:
            pass
    else:
        pass
    return tick_add, xtick_add, ytick_add