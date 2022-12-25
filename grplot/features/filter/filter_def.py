import numpy
import pandas
from grplot.utils.check_data_structure import check_data_structure


def filter_def(df, logic):
    # data structure
    data_structure = check_data_structure(df)
    if data_structure == 'pandas dataframe':
        if type(logic) == str:
            try:
                df_filter = df.query(logic)
            except:
                raise Exception('Wrong pandas query argument!')
        elif (type(logic) == pandas.core.series.Series) and (logic.dtype == bool):
            try:
                df_filter = df[logic]
            except:
                raise Exception('Wrong pandas filter argument!')
        else:
            raise Exception('Unsupported filter argument for pandas data type!')    
    else:
        raise Exception('Unsupported data structure for filter argument!')
    return df_filter