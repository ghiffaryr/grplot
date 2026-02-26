Analytic
========

grplot ships two standalone analytic functions in ``grplot.analytic``.

----

Cohort
------

Cohort retention analysis. Builds a monthly retention heatmap from a
DataFrame containing a customer ID, a signup date, and a last-active date.

.. code-block:: python

   from grplot.analytic import cohort

**Signature**

.. code-block:: text

   cohort(df, customer_id, signup_date, last_active_date,
          figsize=[8, 6], fontsize=10,
          tick_fontsize=None, legend_fontsize=None, text_fontsize=None,
          label_fontsize=None, title_fontsize=None,
          sep=',', saveas=None, display_summary=False)

**Returns:** ``matplotlib.axes.Axes``

.. rubric:: Parameters

``df`` *(pandas.DataFrame)*
   Input DataFrame containing at minimum the customer ID column, the signup
   date column, and the last-active date column.

``customer_id`` *(str)*
   Name of the column that uniquely identifies each customer.

``signup_date`` *(str)*
   Name of the column holding the first order / signup date (must be
   parseable as datetime).

``last_active_date`` *(str)*
   Name of the column holding the most recent active date (must be
   parseable as datetime).

``figsize`` *([float, float], default: [8, 6])*
   Figure size as ``[width, height]`` in inches.

``fontsize`` *(int, default: 10)*
   Base font size applied to all text elements unless overridden by the
   more specific ``*_fontsize`` parameters below.

``tick_fontsize`` *(int or None, default: None)*
   Font size for axis tick labels. Falls back to ``fontsize`` when ``None``.

``legend_fontsize`` *(int or None, default: None)*
   Font size for the colorbar tick labels. Falls back to ``fontsize`` when
   ``None``.

``text_fontsize`` *(int or None, default: None)*
   Font size for the in-cell heatmap annotations. Falls back to ``fontsize``
   when ``None``.

``label_fontsize`` *(int or None, default: None)*
   Font size for the x/y axis labels. Falls back to ``fontsize`` when
   ``None``.

``title_fontsize`` *(int or None, default: None)*
   Font size for the plot title. Falls back to ``fontsize`` when ``None``.

``sep`` *(str, default: ',')*
   Thousand separator character used when formatting colorbar tick labels
   and heatmap cell annotations (e.g. ``'.'`` for European style).

``saveas`` *(str or None, default: None)*
   File path to save the figure. Supported extensions: ``.png``, ``.pdf``,
   ``.svg``, ``.eps``.

``display_summary`` *(bool, default: False)*
   If ``True``, display the intermediate cohort pivot table (cohort group ×
   cohort period) alongside the heatmap.

.. rubric:: Example

.. code-block:: python

   from grplot.analytic import cohort
   import grplot_seaborn as gs
   import pandas as pd

   gs.set_theme(context='notebook', style='darkgrid', palette='deep')

   df = pd.read_csv(
       'https://github.com/ghiffaryr/grplot_data/raw/main/retail_raw_reduced.csv',
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

----

Rank Order
----------

Rank Order table for binary classification model evaluation. Splits
predictions into deciles (highest predicted non-event probability first)
and computes cumulative Gain, KS statistic, and Lift for each decile.

.. code-block:: python

   from grplot.analytic import rank_order

**Signature**

.. code-block:: text

   rank_order(predict_proba, true_label,
              class_non_event=1, display_table=True)

**Returns:** ``pandas.DataFrame`` — one row per decile with the following
columns:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Column
     - Description
   * - ``Minimum Prediction Probability``
     - Lowest predicted probability in the decile
   * - ``Maximum Prediction Probability``
     - Highest predicted probability in the decile
   * - ``Mean Prediction Probability``
     - Mean predicted probability in the decile
   * - ``Count Customer``
     - Number of customers in the decile
   * - ``Count Non-event``
     - Number of non-event customers in the decile
   * - ``Count Event``
     - Number of event customers in the decile
   * - ``Non-event Rate``
     - Non-event count as a percentage of the decile (%)
   * - ``Cummulative Count Customer``
     - Running total of customers up to this decile
   * - ``Cummulative Count Non-event``
     - Running total of non-event customers up to this decile
   * - ``Cummulative Count Event``
     - Running total of event customers up to this decile
   * - ``Cummulative Customer Percentage``
     - Running customer count as % of all customers
   * - ``Cummulative Non-event Percentage``
     - Gain — running non-event count as % of all non-events
   * - ``Cummulative Event Percentage``
     - Running event count as % of all events
   * - ``KS``
     - Kolmogorov–Smirnov statistic: cumulative non-event % − cumulative event %
   * - ``Lift``
     - Cumulative non-event % ÷ cumulative customer %

.. rubric:: Parameters

``predict_proba`` *(numpy.ndarray or pandas.DataFrame)*
   Predicted class probabilities with shape ``(n_samples, n_classes)``.
   Each row must contain the probability for every class; at minimum two
   columns are required. Pass the full output of
   ``sklearn``'s ``predict_proba()`` directly.

``true_label`` *(list, numpy.ndarray, or pandas.Series)*
   Ground-truth binary labels with length ``n_samples``.

``class_non_event`` *(int, default: 1)*
   Column index (0-based) in ``predict_proba`` that corresponds to the
   **non-event** class. For a standard two-class model where index 1 is
   the positive/non-event class, use the default value of ``1``.

``display_table`` *(bool, default: True)*
   If ``True``, display the resulting rank order table in the notebook
   output before returning it.

.. rubric:: Example

.. code-block:: python

   from grplot.analytic import rank_order
   import numpy as np

   np.random.seed(0)
   predict_proba = np.array([
       np.random.uniform(low=0.1, high=1.0, size=10),   # class 0
       np.random.uniform(low=0.1, high=1.0, size=10),   # class 1
   ])
   predict_proba = np.swapaxes(predict_proba, 0, 1)
   true_label = np.random.randint(low=0, high=2, size=10)

   rank_order_table = rank_order(predict_proba=predict_proba,
                                 true_label=true_label,
                                 class_non_event=1)
