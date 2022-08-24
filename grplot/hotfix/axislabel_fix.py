def axislabel_fix(ax, x, y):
    # x
    if x is not None and (ax.get_xlabel() == ''):
        ax.set_xlabel(x)
    else: 
        pass
    # y
    if y is not None and (ax.get_ylabel() == ''):
        ax.set_ylabel(y)
    else: 
        pass
    return ax