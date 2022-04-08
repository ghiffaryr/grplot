def arg_ax_type(arg, axes):
    arg_ = None
    if type(arg) == dict:
        if axes in arg:
            # arg = {'[i,j]':return}
            if arg[axes] is None:
                arg_ = None
            else:
                arg_ = arg[axes]
        else:
            pass
        for key, value in arg.items(): 
            # arg = {return:'[i,j]'}
            if type(value) == str:
                if axes == value:
                    if key is None:
                        arg_ = None
                    else:
                        arg_ = key
                else:
                    pass
            # arg = {return:['[i,j]']}
            elif type(value) == list:
                if axes in value:
                    if key is None:
                        arg_ = None
                    else:
                        arg_ = key
                else:
                    pass
            else:
                pass
    else:
        # arg = return
        arg_ = arg
    return arg_