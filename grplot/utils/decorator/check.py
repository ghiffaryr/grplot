from grplot.utils.template.annotate_template import Annotate

def check_supported_axis(axis: list):
    def return_func(func):
        def wrapper(*args, **kwargs):
            obj: Annotate = args[0]

            if obj.axis not in axis:
                raise Exception(f'Unsupported axis, axis should be of {" or ".join(axis)}!')

            returned_value = func(*args, **kwargs)
            return returned_value
        return wrapper
    return return_func

def check_text_fontsize_type(types: list):
    def return_func(func):
        def wrapper(*args, **kwargs):
            obj = args[0]

            if obj.text_fontsize is not None and type(obj.text_fontsize) is not types:
                raise Exception(f'Unknown text fontsize argument, fontsize shoul be of types {" or ".join(types)}')

            returned_value = func(*args, **kwargs)
            return returned_value
        return wrapper
    return return_func
