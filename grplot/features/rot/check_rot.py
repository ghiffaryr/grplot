from grplot.features.rot.rot_type import rot_type


def check_rot(ax, rot, xrot, yrot, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xrot is not None:
            rot_type(ax=ax, axis='x', rot=xrot, axislabel=xaxislabel, axes=axes)
        else:
            rot_type(ax=ax, axis='x', rot=rot, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if yrot is not None:
            rot_type(ax=ax, axis='y', rot=yrot, axislabel=yaxislabel, axes=axes)
        else:
            rot_type(ax=ax, axis='y', rot=rot, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax