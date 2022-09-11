import warnings
from grplot_seaborn import *  # noqa
reset_orig()  # noqa

msg = (
    "As seaborn no longer sets a default style on import, the grplot_seaborn.apionly "
    "module is deprecated. It will be removed in a future version."
)
warnings.warn(msg, UserWarning)
