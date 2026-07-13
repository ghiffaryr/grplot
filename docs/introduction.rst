Introduction
============

grplot reduces the boilerplate of producing annotated, publication-ready
statistical figures: subplot layout, tick/number formatting, inset
statistical summaries, and value-label annotations are configured through
``plot2d`` parameters instead of separate Matplotlib/Seaborn calls per
figure. This page documents the hierarchical argument system and
configuration options that apply across *every* plot type. For a direct,
line-by-line comparison against equivalent Matplotlib/Seaborn code, see
:doc:`comparison`. For worked, runnable examples of each individual chart —
with rendered output — see :doc:`plot_types`; for multi-panel dashboards
combining several chart types in one call, see :doc:`plots/dashboard`.

Understanding the Argument System
---------------------------------

Arguments in grplot are processed at four different levels of granularity:

- **Ordinary arguments** — Apply to the entire figure (e.g., ``df``, ``figsize``, ``Nx``).
- **Axes arguments** — Apply to specific subplots (e.g., ``plot``, ``filter``, ``title``).
- **Axes-plot arguments** — Apply to specific plots within a subplot (e.g., ``zorder``).
- **Axes-axislabel arguments** — Apply to specific axes and labels (e.g., ``lim``, ``sep``).

💡 **Global Rule: The X and Y Counterparts**

To reduce repetition, almost all axes-axislabel arguments (like ``sep``, ``lim``, ``log``, ``dt``, ``tick_add``, ``label_add``, ``statdesc``, ``text``, ``rot``) apply to both axes by default.

You can easily target a specific axis by prefixing the argument with ``x`` or ``y``. (Example: ``lim`` sets both limits; ``xlim`` sets only the x-axis limit; ``ylim`` sets only the y-axis limit.)

Argument Syntax Guide
---------------------

Depending on the hierarchical level of the argument, grplot allows you to target specific subplots or layers using dictionary mapping. Below is the syntax guide showing how to assign a value (represented by ``return``) to an argument (``arg``).

.. note::

   - A 1-row figure uses a 1D axes index: ``'[i]'`` (e.g., ``'[1]'``).
   - A multi-row figure uses a 2D axes index: ``'[i,j]'`` (e.g., ``'[1,1]'``).
   - **Important:** Axes arguments start from 1 (unlike pure matplotlib, which starts from 0).

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

Core Data & Plot Setup
----------------------

These parameters define what you are plotting and the data behind it.

.. list-table::
   :header-rows: 1
   :widths: 15 15 40 30

   * - Parameter
     - Argument Level
     - Input
     - Description
   * - ``plot``
     - Axes
     - e.g., ``'scatterplot'`` (combine multiple plots using ``+`` such as ``'plot1+plot2'``)
     - Plot type
   * - ``df``
     - Ordinary
     - pandas.DataFrame, dict of lists, or dict of numpy.ndarray
     - Input data source
   * - ``x`` / ``y``
     - Ordinary
     - str, list, numpy.ndarray, pandas.Index, or None; returns key(s) mapping to ``df``
     - Input variable(s)
   * - ``filter``
     - Axes
     - Pandas query string or boolean pandas.Series
     - Data filtering prior to plotting

Figure & Subplot Layout
-----------------------

Control the grid structure and spacing of your overall figure. All are Ordinary arguments.

.. list-table::
   :header-rows: 1
   :widths: 15 30 20 40

   * - Parameter
     - Input
     - Default
     - Description
   * - ``Nx`` / ``Ny``
     - int (grid size) or ``None`` for auto
     - Dynamic
     - Grid columns (Nx) / rows (Ny). Defaults: Nx = max(Nx, Ny) if ≤ 2 else 2. Ny = 1 if max(Nx, Ny) ≤ 2 else ceil(max/2).
   * - ``figsize``
     - list/tuple of two numbers
     - ``[8, 6]``
     - Figure dimensions: Width, height in inches.
   * - ``pad``
     - numeric
     - ``6``
     - Outer padding between figure edge and subplots (fraction of font size).
   * - ``hpad`` / ``wpad``
     - numeric
     - ``pad``
     - Inner padding height/width between adjacent subplots.

Axis Controls & Scales
----------------------

Fine-tune the behavior of your x and y axes. All are Axes-axislabel arguments. *(Remember: prefix with x or y to target a single axis).* 

.. list-table::
   :header-rows: 1
   :widths: 15 30 20 40

   * - Parameter
     - Input
     - Default
     - Description
   * - ``lim``
     - ``[bottom, top]``
     - None
     - Axis limit.
   * - ``log``
     - ``'linear'``, ``'log'``, ``'symlog'``, or ``'logit'``
     - None
     - Axis scale.
   * - ``dt``
     - strftime date format (e.g., ``'%Y-%m-%d'``)
     - None
     - Datetime format using Python's standard strftime formats.
   * - ``rot``
     - float (degrees)
     - None
     - Tick rotation in degrees.

Formatting & Units
------------------

grplot provides powerful built-in string manipulation for numbers and labels. *(Remember: prefix with x or y to target a single axis).*

Number formatting uses the ``sep`` argument. Patterns may include separators, currency, and large-number abbreviations.

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
     - Currency-style formatting (adds trailing zeros)
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

   * - Parameter
     - Input
     - Effect
   * - ``tick_add``
     - ``'{}_'`` ``'_{}'`` ``'{}_{}'``
     - Prefix/suffix value with unit
   * - ``tick_add`` (negatives)
     - ``'{}(_)'`` ``'(_){}'`` ``'{}(_){}'``
     - Wrap negatives in parentheses: ``($100)``, ``(100)kg``
   * - ``label_add``
     - ``'{}_'`` ``'_{}'`` ``'{}_{}'``
     - Add unit to axis label itself

Annotations & Statistics
------------------------

Easily layer text and statistical descriptions over your data.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Argument Level
     - Description
   * - ``statdesc``
     - Axes-axislabel
     - Statistical summaries added to the plot. Combine using ``+`` (e.g., ``'mean+std'``). Prefix with ``x`` or ``y`` to apply only to one axis (``xstatdesc``, ``ystatdesc``).
   * - ``text``
     - Axes-axislabel
     - Data annotations (see details below). Prefix with ``x`` or ``y`` to target a single axis (``xtext``, ``ytext``).
   * - ``xlabel`` / ``ylabel``
     - Axes
     - Explicit axis labels (str). Overrides ``label_add`` configurations.
   * - ``title``
     - Axes
     - Plot/Subplot title (str).

**Text argument details:**

- **Type & default:** ``bool``/``str``/``None`` (default ``None``).
- **Both axes by default:** apply to x‑ and y‑axes unless prefixed with ``x`` or ``y``.
- **When `bool`:** toggles automatic labels on points/bars. Used by *scatterplot*, *lineplot*, *pieplot*, *treemapsplot*, *packedbubblesplot*, and *residplot*.
- **When `str`:** specifies base position(s) using ``'h'`` (horizontal), ``'v'`` (vertical), ``'i'`` (inside), or ``'o'`` (outside). Accepts a single position or a combination separated by ``+`` (e.g., ``'h+i'``). Used by *histplot*, *barplot*, *countplot*, and *paretoplot*.

**Available statdesc Returns:**

- **Grouped:** ``'general'``, ``'boxplot'``
- **Central & Spread:** ``'mean'``, ``'median'``, ``'std'``, ``'range'``, ``'min'``, ``'max'``
- **Counts:** ``'count'``, ``'nonzero'``, ``'unique'``
- **Quartiles & Bounds:** ``'q1'``, ``'q3'``, ``'pct1'``, ``'pct5'``, ``'pct95'``, ``'pct99'``, ``'whislo'``, ``'whishi'``, ``'cilo'``, ``'cihi'``

Styling, Typography & Drawing Order
-----------------------------------

Control the aesthetic elements of the plot. All font parameters belong to the Axes level.

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Parameter
     - Input
     - Default
     - Description
   * - ``fontsize``
     - numeric
     - ``10``
     - Base font size. Acts as the fallback for all text.
   * - ``*_fontsize``
     - numeric
     - ``fontsize``
     - Specific sizing for: tick, legend, text, label, or title.
   * - ``legend_loc``
     - str
     - ``'best'``
     - Legend position; valid keywords include:
       ``'best'``, ``'upper right'``, ``'upper left'``, ``'lower left'``,
       ``'lower right'``, ``'right'``, ``'center left'``, ``'center right'``,
       ``'lower center'``, ``'upper center'``, ``'center'``.

Performance & Export
--------------------

Manage system resources and save your output. Both are Ordinary arguments.

.. list-table::
   :header-rows: 1
   :widths: 15 15 15 55

   * - Parameter
     - Input
     - Default
     - Description
   * - ``optimizer``
     - str
     - ``'perf'``
     - ``'perf'``/``'pandas'`` — fast, more memory. ``'saver'``/``'numpy'`` — slower, less memory.
   * - ``saveas``
     - str or None
     - ``None``
     - Save figure as ``.png``, ``.pdf``, ``.svg``, or ``.eps``
