def tick_add_def(ax, axis, add):
    if axis == 'x':
        if '(_)' in add:
            if add[-3:] == '(_)':
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['({}{})'.format(add[:-3], x.get_text()[1:]) if '-' in x.get_text()[0] else '{}{}'.format(add[:-3], x.get_text()) for x in ax.get_xticklabels()])
            elif add[:3] == '(_)':
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['({}{})'.format(x.get_text()[1:], add[3:]) if '-' in x.get_text()[0] else '{}{}'.format(x.get_text(), add[3:]) for x in ax.get_xticklabels()])
            else: 
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['({}{}{})'.format(add.split('(_)')[0], x.get_text()[1:], add.split('(_)')[-1]) if '-' in x.get_text()[0] else '{}{}{}'.format(add.split('(_)')[0], x.get_text(), add.split('(_)')[-1]) for x in ax.get_xticklabels()])
        elif '_' in add:
            if add[-1] == '_':
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['-{}{}'.format(add[:-1], x.get_text()[1:]) if '-' in x.get_text()[0] else '{}{}'.format(add[:-1], x.get_text()) for x in ax.get_xticklabels()])
            elif add[0] == '_':
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['{}{}'.format(x.get_text(), add[1:]) for x in ax.get_xticklabels()])
            else: 
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(['-{}{}{}'.format(add.split('_')[0], x.get_text()[1:], add.split('_')[-1]) if '-' in x.get_text()[0] else '{}{}{}'.format(add.split('_')[0], x.get_text(), add.split('_')[-1]) for x in ax.get_xticklabels()])
        else:
            raise Exception('Unknown tick add argument!')
    elif axis == 'y':
        if '(_)' in add:
            if add[-3:] == '(_)':
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['({}{})'.format(add[:-3], y.get_text()[1:]) if '-' in y.get_text()[0] else '{}{}'.format(add[:-3], y.get_text()) for y in ax.get_yticklabels()])
            elif add[:3] == '(_)':
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['({}{})'.format(y.get_text()[1:], add[3:]) if '-' in y.get_text()[0] else '{}{}'.format(y.get_text(), add[3:]) for y in ax.get_yticklabels()])
            else: 
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['({}{}{})'.format(add.split('(_)')[0], y.get_text()[1:], add.split('(_)')[-1]) if '-' in y.get_text()[0] else '{}{}{}'.format(add.split('(_)')[0], y.get_text(), add.split('(_)')[-1]) for y in ax.get_yticklabels()])
        elif '_' in add:
            if add[-1] == '_':
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['-{}{}'.format(add[:-1], y.get_text()[1:]) if '-' in y.get_text()[0] else '{}{}'.format(add[:-1], y.get_text()) for y in ax.get_yticklabels()])
            elif add[0] == '_':
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['{}{}'.format(y.get_text(), add[1:]) for y in ax.get_yticklabels()])
            else: 
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(['-{}{}{}'.format(add.split('_')[0], y.get_text()[1:], add.split('_')[-1]) if '-' in y.get_text()[0] else '{}{}{}'.format(add.split('_')[0], y.get_text(), add.split('_')[-1]) for y in ax.get_yticklabels()])
        else:
            raise Exception('Unknown tick add argument!')
    else:
        raise Exception('Unsupported axis!')

    return ax