Features
========

grplot introduces powerful features through an intuitive, hierarchical argument system. Every feature is directly accessible via ``plot2d`` parameters.

The Hierarchical Argument System
--------------------------------

Arguments in grplot are processed at four different levels of granularity:

- **Ordinary arguments** — Apply to the entire figure (e.g., ``df``, ``figsize``, ``Nx``).
- **Axes arguments** — Apply to specific subplots (e.g., ``plot``, ``filter``, ``title``).
- **Axes-plot arguments** — Apply to specific plots within a subplot (e.g., ``zorder``).
- **Axes-axislabel arguments** — Apply to specific axes and labels (e.g., ``lim``, ``sep``).

💡 **Global Rule: The X and Y Counterparts**

To reduce repetition, almost all axes-axislabel arguments (like ``sep``, ``lim``, ``log``, ``dt``, ``tick_add``, ``label_add``, ``statdesc``, ``text``, ``rot``) apply to both axes by default.

You can easily target a specific axis by prefixing the argument with ``x`` or ``y``. (Example: ``lim`` sets both limits; ``xlim`` sets only the x-axis limit; ``ylim`` sets only the y-axis limit.)

Core Data & Plot Setup
----------------------

These parameters define what you are plotting and the data behind it.

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Level
     - Description & Expected Values
   * - ``plot``
     - Axes
     - Plot type (e.g., ``'scatterplot'``). Combine multiple plots using ``+`` (e.g., ``'plot1+plot2'``).
   * - ``df``
     - Ordinary
     - Input data. Accepts pandas.DataFrame, dict of lists, or dict of numpy.ndarray.
   * - ``x`` / ``y``
     - Ordinary
     - Axis positions. Accepts str, list, numpy.ndarray, pandas.Index, or None. Returns a key or list of keys mapped to df.
   * - ``filter``
     - Axes
     - Data filtering prior to plotting (Pandas only). Accepts a query str or a boolean pandas.Series.

Figure & Subplot Layout
-----------------------

Control the grid structure and spacing of your overall figure.

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Parameter
     - Default
     - Description (All are Ordinary arguments)
   * - ``Nx`` / ``Ny``
     - Dynamic
     - Grid columns (Nx) / rows (Ny). Defaults: Nx = max(Nx, Ny) if ≤ 2 else 2. Ny = 1 if max(Nx, Ny) ≤ 2 else ceil(max/2).
   * - ``figsize``
     - ``[8, 6]``
     - Figure dimensions: Width, height in inches.
   * - ``pad``
     - ``6``
     - Outer padding between figure edge and subplots (fraction of font size).
   * - ``hpad`` / ``wpad``
     - ``pad``
     - Inner padding height/width between adjacent subplots.

Axis Controls & Scales
----------------------

Fine-tune the behavior of your x and y axes. (Remember: prefix with x or y to target a single axis.)

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Parameter
     - Default
     - Description (All are Axes-axislabel arguments)
   * - ``lim``
     - None
     - Axis limits formatted as ``[bottom, top]``.
   * - ``log``
     - None
     - Axis scale. Accepts: ``'linear'``, ``'log'``, ``'symlog'``, or ``'logit'``.
   * - ``dt``
     - None
     - Datetime format using Python's standard strftime formats (e.g., ``'%Y-%m-%d'``).
   * - ``rot``
     - None
     - Tick rotation in degrees (float).

Formatting & Units
------------------

grplot provides powerful built-in string manipulation for numbers and labels. (Remember: prefix with x or y to target a specific axis.)

Number formatting uses the ``sep`` argument. Patterns may include separators,
currency, and large-number abbreviations.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Pattern
     - Meaning
     - Example
   * - ``','`` / ``'.'``
     - Thousand separator
     - ``1,000`` / ``1.000``
   * - ``',c'`` / ``'.c'``
     - Currency-style formatting (adds two trailing zeros and thousands separators without symbol)
     - ``1000`` → ``1,000.00`` or ``1.000,00``
   * - ``',L'`` / ``'.L'``
     - Large-number abbreviation (K, M, B, T, Q)
     - ``1.5M``, ``1,000`` / ``1,5M``, ``1.000``
   * - ``',cL'`` / ``'.cL'``
     - Currency + abbreviation
     - ``1.5M``, ``1,000.00`` / ``1,5M``, ``1.000,00``

Unit patterns are specified separately for ticks and labels:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Argument
     - Pattern(s)
     - Effect
   * - ``tick_add``
     - ``'{}_'`` ``'_{}'`` ``'{}_{}'``
     - Prefix/suffix value with unit
   * - ``tick_add`` (negatives)
     - ``'{}(_)'`` ``'(_){}'`` ``'{}(_){}'``
     - Wrap negatives in parentheses: ``($100)``, ``(100)kg``
   * - ``label_add``
     - ``'{}_'`` ``'_{}'``
     - Add unit to axis label itself

.. note::
   Most formatting options apply to both axes by default; use ``xsep``,
   ``xtick_add``/``xlabel_add`` or the corresponding ``y``-prefixed
   arguments to target a single axis.
.. note::
   Most formatting options apply to both axes by default; use ``xsep``,
   ``xtick_add``/``xlabel_add`` or the corresponding ``y``-prefixed
   arguments to target a single axis.

Annotations & Statistics
------------------------

Easily layer text and statistical descriptions over your data.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Level
     - Description
   * - ``statdesc``
     - Axes-axislabel
     - Statistical summaries added to the plot. Combine multiple using ``+`` (e.g., ``'mean+std'``).
   * - ``text``
     - Axes-axislabel
     - Data annotations. Set to True/False to toggle automatic text labeling on points/bars.
   * - ``xlabel`` / ``ylabel``
     - Axes
     - Explicit axis labels (str). This will override any label_add configurations.
   * - ``title``
     - Axes
     - Plot/Subplot title (str).

Available statdesc Returns:

- Grouped: ``'general'``, ``'boxplot'``
- Central & Spread: ``'mean'``, ``'median'``, ``'std'``, ``'range'``, ``'min'``, ``'max'``
- Counts: ``'count'``, ``'nonzero'``, ``'unique'``
- Quartiles & Bounds: ``'q1'``, ``'q3'``, ``'pct1'``, ``'pct5'``, ``'pct95'``, ``'pct99'``, ``'whislo'``, ``'whishi'``, ``'cilo'``, ``'cihi'``

Styling, Typography & Drawing Order
----------------------------------

Control the aesthetic elements of the plot. All font parameters belong to the Axes level.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Default
     - Description
   * - ``fontsize``
     - ``10``
     - Base font size. Acts as the fallback for all text.
   * - ``*_fontsize``
     - ``fontsize``
     - Specific sizing for: tick_fontsize, legend_fontsize, text_fontsize, label_fontsize, title_fontsize.
   * - ``legend_loc``
     - ``'best'``
     - Legend position (e.g., ``'upper right'``, ``'center left'``, ``'lower center'``, etc.).
   * - ``zorder``
     - None
     - Drawing order (Axes-plot level). Default order is patches (bottom), lines (middle), text (top).

Performance and Export
----------------------

Manage system resources and save your output. Both are Ordinary arguments.

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Parameter
     - Default
     - Description
   * - ``optimizer``
     - ``'perf'``
     - ``'perf'``/``'pandas'`` — fast, more memory. ``'saver'``/``'numpy'`` — slower, less memory.
   * - ``saveas``
     - ``None``
     - Save figure as ``.png``, ``.pdf``, ``.svg``, or ``.eps``
