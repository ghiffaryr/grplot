def saveas_type(fig, saveas):
    if type(saveas) == str:
        fig.savefig(fname=saveas, bbox_inches='tight')
    else:
        raise Exception('Unknown saveas argument!')