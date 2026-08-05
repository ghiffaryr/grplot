Configuration
=============

The following configurations help you optimize grplot for your specific environment.

Image Quality (Dots per Inch)
-----------------------------

By default, `grplot` ensures figures use a high-resolution DPI of 300. This
happens automatically when you import the library, so you normally don't need
any additional configuration. If you override the value yourself, make sure to
set it before creating any plots, for example:

.. code-block:: python

   import matplotlib as mpl
   mpl.rcParams['figure.dpi'] = 150

Unsupported de Python Locale Solution
-------------------------------------

Not all environments support the `de` Python locale, which can break the matplotlib axis formatter for thousand separators. The alternative implementation (directly drawing the string) will always work. To use it, pass the following argument before plotting:

.. code-block:: python

   low = -5  # set lower than the lowest number order in your dataframe
   hi = 18   # set bigger than the biggest number order in your dataframe
   mpl.rcParams['axes.formatter.limits'] = [low, hi]

Localized Seaborn Dependency
----------------------------

As major updates of seaborn are released, grplot ships with ``grplot_seaborn``, a localized version of seaborn that keeps your production software working regardless of upstream seaborn changes.

.. code-block:: python

   import grplot_seaborn as gs
   gs.set_theme(context='notebook', style='darkgrid', palette='deep')