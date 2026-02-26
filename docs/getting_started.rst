Basic Understanding
===================

Argument
~~~~~~~~

Here is how to pass arguments into the plot function.

**Ordinary argument:**

.. code-block:: text

   arg = return

**Axes arguments:**

.. code-block:: text

   arg = return
   arg = {'[i,j]': return}
   arg = {return: '[i,j]'}
   arg = {return: ['[i,j]']}

**Axes-plot arguments:**

.. code-block:: text

   arg = return
   arg = {'plot': return}
   arg = {'[i,j]': {'plot': return}}
   arg = {'[i,j]': {return: 'plot'}}
   arg = {'[i,j]': {return: ['plot']}}
   arg = {'[i,j]': return}
   arg = {return: 'plot'}
   arg = {return: ['plot']}

**Axes-axislabel arguments:**

.. code-block:: text

   arg = return
   arg = {'axislabel': return}
   arg = {'[i,j]': {'axislabel': return}}
   arg = {'[i,j]': {return: 'axislabel'}}
   arg = {'[i,j]': {return: ['axislabel']}}
   arg = {'[i,j]': return}
   arg = {return: 'axislabel'}
   arg = {return: ['axislabel']}

.. note::

   - 1 row figure uses ``'[i]'`` axes argument, e.g. ``'[1]'``
   - Multi-rows figure uses ``'[i,j]'`` axes argument, e.g. ``'[1,1]'``
   - Axes argument starts from 1 (different from matplotlib which starts from 0)

Image Quality — Dots per Inch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pass the following argument before plotting. A bigger value produces a higher
quality image. Usually 300 is enough for publication.

.. code-block:: python

   import matplotlib as mpl
   mpl.rcParams['figure.dpi'] = 300

Unsupported de Python Locale Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not all environments support the de Python locale. So the implementation of
matplotlib axis formatter for thousand separators will not always work. The
other implementation by directly drawing the string will always work. To use it,
pass the following argument before plotting:

.. code-block:: python

   low = -5  # set this lower than the lowest number order in your dataframe
   hi = 18   # set this bigger than the biggest number order in your dataframe
   mpl.rcParams['axes.formatter.limits'] = [low, hi]

Localized Seaborn Dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As major updates of seaborn are released, grplot ships with ``grplot_seaborn``, a
localized version of seaborn that keeps your production software working regardless
of upstream seaborn changes.

.. code-block:: python

   import grplot_seaborn as gs
   gs.set_theme(context='notebook', style='darkgrid', palette='deep')

Automatic Analytic Tool
~~~~~~~~~~~~~~~~~~~~~~~~

grplot also provides automatic analytic tools including cohort analysis and
rank order / gain / KS / lift tables. See the :doc:`analytic` reference for details.
