from grplot.features.filter.filter_def import filter_def
from grplot.utils.arg_ax_type import arg_ax_type

def check_filter(df, logic, axes):
    logic = arg_ax_type(arg=logic, axes=axes)
    # check logic
    if logic is None:
        return df
    else:
        df_filter = filter_def(df=df, logic=logic)
        return df_filter