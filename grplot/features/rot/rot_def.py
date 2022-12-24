import matplotlib.text as mpl_text


def rot_def(ax, axis, rot):
    labels: mpl_text.Text= None

    if axis == 'x':
        labels = ax.get_xticklabels()
    elif axis == 'y':
        labels = ax.get_yticklabels()
    else:
        raise Exception('Unsupported axis!')

    try:
        for label in labels:
            label.set_rotation(rot)
    except Exception:
        raise Exception('Unknown rot argument!')

    return ax
