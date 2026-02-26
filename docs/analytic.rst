Analytic
========

grplot ships two automatic analytic tools as standalone functions in
``grplot.analytic``.

Cohort
------

Cohort retention analysis. Given a DataFrame with a customer ID, a signup date,
and a last-active date, ``cohort`` builds and renders the cohort retention
heatmap automatically.

.. code-block:: python

   from grplot.analytic import cohort
   import grplot_seaborn as gs
   import pandas as pd

   gs.set_theme(context='notebook', style='darkgrid', palette='deep')

   df = pd.read_csv('https://github.com/ghiffaryr/grplot_data/raw/main/retail_raw_reduced.csv',
                    parse_dates=['order_date'])
   df['last_active_date'] = df.groupby('customer_id')['order_date'].transform('max')
   ax = cohort(df=df,
               customer_id='customer_id',
               signup_date='order_date',
               last_active_date='last_active_date',
               figsize=[16, 12],
               fontsize=16,
               sep='.',
               display_summary=True)

Rank Order, Gain, KS, and Lift
-------------------------------

Rank Order table for binary classification model evaluation. Returns a table
containing rank order, gain, KS statistic, and lift for each decile.

.. code-block:: python

   from grplot.analytic import rank_order
   import numpy as np

   np.random.seed(0)
   predict_proba = np.array([np.random.uniform(low=0.1, high=1.0, size=10),  # class 0
                              np.random.uniform(low=0.1, high=1.0, size=10)])  # class 1
   predict_proba = np.swapaxes(predict_proba, 0, 1)
   true_label = np.random.randint(low=0, high=2, size=10)
   rank_order_table = rank_order(predict_proba=predict_proba,
                                 true_label=true_label,
                                 class_non_event=1)
