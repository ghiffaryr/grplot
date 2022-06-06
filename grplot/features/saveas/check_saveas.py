from grplot.features.saveas.saveas_type import saveas_type


def check_saveas(fig, saveas):
    if saveas is not None:
        saveas_type(fig, saveas)
    else:
        pass