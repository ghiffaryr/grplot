def rot_def(ax, axis, rot):
    if axis == 'x':
        try:
            for label in ax.get_xticklabels():
                label.set_rotation(rot)
        except:
            raise Exception('Unknown rot argument!')
    elif axis == 'y':
        try:
            for label in ax.get_yticklabels():
                label.set_rotation(rot)
        except:
            raise Exception('Unknown rot argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax