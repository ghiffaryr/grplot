def rot_def(ax, axis, rot):
    if axis == 'x':
        if (type(rot) == int) or (rot in ['horizontal', 'vertical']):
            for label in ax.get_xticklabels():
                label.set_rotation(rot)
        else:
            raise Exception('Unknown rot argument!')
    elif axis == 'y':
        if (type(rot) == int) or (rot in ['horizontal', 'vertical']):
            for label in ax.get_yticklabels():
                label.set_rotation(rot)
        else:
            raise Exception('Unknown rot argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax