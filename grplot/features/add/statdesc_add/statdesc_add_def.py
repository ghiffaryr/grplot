def statdesc_add_def(num, add):
    if '(_)' in add:
        if add[-3:] == '(_)':
            if '-' in num[0]:
                num = '({}{})'.format(add[:-3], num[1:])
            else:
                num = '{}{}'.format(add[:-3], num)
        elif add[:3] == '(_)':
            if '-' in num[0]:
                num = '({}{})'.format(num[1:], add[3:])
            else:
                num = '{}{}'.format(num, add[3:])
        else: 
            if '-' in num[0]:
                num = '({}{}{})'.format(add.split('(_)')[0], num[1:], add.split('(_)')[-1])
            else:
                num = '{}{}{}'.format(add.split('(_)')[0], num, add.split('(_)')[-1])
    elif '_' in add:
        if add[-1] == '_':
            if '-' in num[0]:
                num = '-{}{}'.format(add[:-1], num[1:])
            else:
                num = '{}{}'.format(add[:-1], num)
        elif add[0] == '_':
                num = '{}{}'.format(num, add[1:])
        else: 
            if '-' in num[0]:
                num = '-{}{}{}'.format(add.split('_')[0], num[1:], add.split('_')[-1])
            else:
                num = '{}{}{}'.format(add.split('_')[0], num, add.split('_')[-1])
    else:
        raise Exception('Unknown statdesc add argument!')
    return num