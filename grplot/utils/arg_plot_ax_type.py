def arg_plot_ax_type(arg, plot, axes):
    arg_ = None
    if type(arg) == dict:
        # arg = {'plot':return}
        if plot in arg:
            if arg[plot] is None:
                arg_ = None
            else:
                arg_ = arg[plot]
        else:
            pass        
        if axes in arg:
            if arg[axes] is None:
                arg_ = None            
            elif type(arg[axes]) == dict:
                # arg = {'[i,j]':{'plot':return}}
                if plot in arg[axes]:
                    if arg[axes][plot] is None:
                        arg_ = None
                    else:
                        arg_ = arg[axes][plot]
                else:
                    pass                
                for key, value in arg[axes].items(): 
                    # arg = {'[i,j]':{return:'plot'}}
                    if type(value) == str:
                        if plot == value:
                            if key is None:
                                arg_ = None
                            else:
                                arg_ = key
                        else:
                            pass
                    # arg = {'[i,j]':{return:['plot']}}
                    elif type(value) == list:
                        if plot in value:
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
            # arg = {return:'plot'}
            if type(value) == str:
                if plot == value:
                    if key is None:
                        arg_ = None
                    else:
                        arg_ = key
                else:
                    pass
            # arg = {return:['plot']}
            elif type(value) == list:
                if plot in value:
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