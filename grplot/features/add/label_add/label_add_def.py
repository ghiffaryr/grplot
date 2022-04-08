def label_add_def(ax, axis, add):
    if axis == 'x':
        if '_' in add:
            if add[-1] == '_':
                ax.set_xlabel('{}{}'.format(add[:-1], ax.get_xlabel()))
            elif add[0] == '_':
                ax.set_xlabel('{}{}'.format(ax.get_xlabel(), add[1:]))
            else: 
                ax.set_xlabel('{}{}{}'.format(add.split('_')[0], ax.get_xlabel(), add.split('_')[-1]))
        else:
            raise Exception('Unknown label add argument!')
    elif axis == 'y':
        if '_' in add:
            if add[-1] == '_':
                ax.set_ylabel('{}{}'.format(add[:-1], ax.get_ylabel()))
            elif add[0] == '_':
                ax.set_ylabel('{}{}'.format(ax.get_ylabel(), add[1:]))
            else: 
                ax.set_ylabel('{}{}{}'.format(add.split('_')[0], ax.get_ylabel(), add.split('_')[-1]))
        else:
            raise Exception('Unknown label add argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax