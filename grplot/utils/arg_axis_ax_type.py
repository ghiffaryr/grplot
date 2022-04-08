def arg_axis_ax_type(arg, axislabel, axes):
    arg_ = None
    if type(arg) == dict:
        # arg = {'axislabel':return}
        if axislabel in arg:
            if arg[axislabel] is None:
                arg_ = None
            else:
                arg_ = arg[axislabel]
        else:
            pass        
        if axes in arg:
            if arg[axes] is None:
                arg_ = None            
            elif type(arg[axes]) == dict:
                # arg = {'[i,j]':{'axislabel':return}}
                if axislabel in arg[axes]:
                    if arg[axes][axislabel] is None:
                        arg_ = None
                    else:
                        arg_ = arg[axes][axislabel]
                else:
                    pass                
                for key, value in arg[axes].items(): 
                    # arg = {'[i,j]':{return:'axislabel'}}
                    if type(value) == str:
                        if axislabel == value:
                            if key is None:
                                arg_ = None
                            else:
                                arg_ = key
                        else:
                            pass
                    # arg = {'[i,j]':{return:['axislabel']}}
                    elif type(value) == list:
                        if axislabel in value:
                            if key is None:
                                arg_ = None
                            else:
                                arg_ = key
                        else:
                            pass
                    else:
                        pass
            # arg = {'[i,j]':return}}
            else:
                arg_ = arg[axes]
        else:
            pass
        for key, value in arg.items(): 
            # arg = {return:'axislabel'}
            if type(value) == str:
                if axislabel == value:
                    if key is None:
                        arg_ = None
                    else:
                        arg_ = key
                else:
                    pass
            # arg = {return:['axislabel']}
            elif type(value) == list:
                if axislabel in value:
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