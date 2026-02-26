Features
========

grplot introduces powerful features through its flexible argument system. Every
feature is accessible directly via ``plot2d`` parameters.

Flexible Argument System
------------------------

grplot uses a hierarchical argument system that is both intuitive and powerful:

- **Ordinary arguments** — apply to the entire figure (e.g. ``Nx=2, Ny=3``)
- **Axes arguments** — apply to specific subplots (e.g. ``title={'[1,1]': 'Histogram', '[1,2]': 'ECDF'}``)
- **Axes-plot arguments** — apply to specific plots within subplots
- **Axes-axislabel arguments** — apply to specific axis labels (e.g. ``sep={'total_bill': '.c'}``)

See :doc:`getting_started` for the full argument syntax reference.

Automatic Number Formatting
----------------------------

One of grplot's key features is built-in number formatting via the ``sep`` argument:

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Value
     - Example output
     - Description
   * - ``','``
     - 1,000,000
     - Comma thousand separator
   * - ``'.'``
     - 1.000.000
     - Period thousand separator
   * - ``',c'``
     - formatted as currency
     - Comma separator with currency
   * - ``'.c'``
     - formatted as currency
     - Period separator with currency
   * - ``',L'``
     - 1M, 1B, 1T
     - Large number abbreviation (K, M, B, T, Q)
   * - ``'.L'``
     - 1M, 1B, 1T
     - Large number abbreviation with period
   * - ``',cL'``
     - combined
     - Currency with large number abbreviation
   * - ``'.cL'``
     - combined
     - Currency with large number abbreviation

``sep`` applies to both axes. Use ``xsep`` or ``ysep`` to target a specific axis.

Example:

.. code-block:: python

   # Currency formatting on x-axis only
   ax = plot2d(plot='histplot', df=tips, x='total_bill',
               xsep='.c', xtick_add='Rp(_)')

Unit Addition
-------------

Add unit labels to ticks and text annotations with ``tick_add``:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Pattern
     - Description
   * - ``'{}_'``
     - Prefix with unit (e.g. ``'$_'`` → ``$100``)
   * - ``'_{}'``
     - Suffix with unit (e.g. ``'_kg'`` → ``100kg``)
   * - ``'{}_{}'``
     - Both prefix and suffix
   * - ``'{}(_)'``
     - Prefix; negatives shown as ``($100)``
   * - ``'(_){}'``
     - Suffix; negatives shown as ``(100)kg``
   * - ``'{}(_){}'``
     - Both; negatives wrapped in parentheses

Use ``xtick_add`` or ``ytick_add`` to target a specific axis.

Use ``label_add``, ``xlabel_add``, or ``ylabel_add`` for axis label units
(pattern: ``'{}_'``, ``'_{}'``, or ``'{}_{}'``).

Example:

.. code-block:: python

   ax = plot2d(plot='scatterplot', df=tips, x='tip', y='total_bill',
               sep='.c', tick_add='Rp(_)')

Statistical Descriptions
-------------------------

Display statistical summaries directly on your plots with ``statdesc``:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Value
     - Description
   * - ``'general'``
     - Comprehensive general statistics
   * - ``'boxplot'``
     - Box plot statistics (whiskers, quartiles, CIs)
   * - ``'count'``
     - Count
   * - ``'mean'``
     - Mean
   * - ``'median'``
     - Median
   * - ``'std'``
     - Standard deviation
   * - ``'min'`` / ``'max'``
     - Minimum / maximum
   * - ``'q1'`` / ``'q3'``
     - First / third quartile
   * - ``'pct1'``, ``'pct5'``, ``'pct95'``, ``'pct99'``
     - Percentiles
   * - ``'whislo'`` / ``'whishi'``
     - Lower / upper whisker
   * - ``'nonzero'``
     - Count of non-zero values
   * - ``'unique'``
     - Count of unique values
   * - ``'range'``
     - Range (max − min)
   * - ``'cilo'`` / ``'cihi'``
     - Lower / upper confidence interval

Combine multiple statistics with ``+``:

.. code-block:: python

   ystatdesc='count+unique'
   statdesc={'total_bill': 'general'}
   statdesc={'[1,1]': {'total_bill': 'general'}, '[3,2]': {'total_bill': 'boxplot'}}

Use ``xstatdesc`` or ``ystatdesc`` to target a specific axis.

Text Annotations
----------------

Control automatic data annotations with ``text``:

- For scatter and line plots: ``text=True`` enables annotations.
- For histogram, bar, count, and pareto plots: pass a position string.

  - ``'h'`` — horizontal
  - ``'v'`` — vertical
  - ``'i'`` — inside the bar

Combine positions with ``+`` (e.g. ``'h+i'``). Use ``xtext`` / ``ytext`` to
target a specific axis.

Example:

.. code-block:: python

   text={'Count': 'h', True: ['[2,1]', '[2,2]'], '[3,1]': {'total_bill': 'h+i'}}

Data Filtering
--------------

Filter the dataframe before plotting with ``filter``. Accepts a pandas query
string or a boolean Series:

.. code-block:: python

   ax = plot2d(plot='histplot', df=tips,
               filter=(tips['total_bill'] > 10), ...)

Multi-Plot Layouts
------------------

Create grids of subplots with ``Nx`` (columns) and ``Ny`` (rows):

.. code-block:: python

   ax = plot2d(plot={'[1,1]': 'histplot',
                     '[1,2]': 'ecdfplot',
                     '[2,1]': 'treemapsplot',
                     '[2,2]': 'pieplot',
                     '[3,1]': 'paretoplot',
                     '[3,2]': 'boxplot+stripplot'},
               Nx=2, Ny=3, ...)

All arguments that support axes addressing (e.g. ``title``, ``sep``, ``statdesc``,
``text``, ``tick_add``, ``alpha``) can be set independently per subplot.

Figure Layout
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Default
     - Description
   * - ``figsize``
     - ``[8, 6]``
     - Width, height in inches
   * - ``pad``
     - ``6``
     - Padding between figure edge and subplot edges (fraction of font size)
   * - ``hpad``
     - ``pad``
     - Height padding between adjacent subplots
   * - ``wpad``
     - ``pad``
     - Width padding between adjacent subplots

Axis Control
------------

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Parameter
     - Description
   * - ``xlim`` / ``ylim``
     - Set axis limits: ``[bottom, top]``
   * - ``xlog`` / ``ylog``
     - Set axis scale: ``'linear'``, ``'log'``, ``'symlog'``, or ``'logit'``
   * - ``xdt`` / ``ydt``
     - Date/time format string (e.g. ``'%Y-%m-%d'``)
   * - ``xrot`` / ``yrot``
     - Tick rotation in degrees

Use ``lim``, ``log``, ``dt``, or ``rot`` to set both axes at once.

Font Sizes
----------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Parameter
     - Default
     - Description
   * - ``fontsize``
     - ``10``
     - Base font size; applies to all text unless overridden
   * - ``tick_fontsize``
     - ``fontsize``
     - Tick label font size
   * - ``legend_fontsize``
     - ``fontsize``
     - Legend font size
   * - ``text_fontsize``
     - ``fontsize``
     - Data annotation font size
   * - ``label_fontsize``
     - ``fontsize``
     - Axis label font size
   * - ``title_fontsize``
     - ``fontsize``
     - Title font size

Performance and Export
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Default
     - Description
   * - ``optimizer``
     - ``'perf'``
     - ``'perf'``/``'pandas'`` — fast, more memory. ``'saver'``/``'numpy'`` — slower, less memory.
   * - ``saveas``
     - ``None``
     - Save figure as ``.png``, ``.pdf``, ``.svg``, or ``.eps``
