API Reference
=============

plot2d
------

``plot2d`` is the main plotting function. It accepts any of the 20+ supported
plot types and renders one or more subplots in a single call.

.. code-block:: python

   from grplot import plot2d

**Signature:**

.. code-block:: text

   plot2d(plot, df, x=None, y=None, Nx=..., Ny=..., figsize=[8,6], pad=6,
          hpad=pad, wpad=pad, filter=None, title=None,
          fontsize=10, tick_fontsize=fontsize, legend_fontsize=fontsize,
          text_fontsize=fontsize, label_fontsize=fontsize, title_fontsize=fontsize,
          legend_loc='best', sep=',', xsep=sep, ysep=sep,
          lim=None, xlim=lim, ylim=lim, log=None, xlog=log, ylog=log,
          dt=None, xdt=dt, ydt=dt, tick_add=None, xtick_add=tick_add,
          ytick_add=tick_add, rot=None, xrot=rot, yrot=rot,
          statdesc=None, xstatdesc=statdesc, ystatdesc=statdesc,
          text=None, xtext=text, ytext=text,
          label_add=None, xlabel_add=label_add, ylabel_add=label_add,
          xlabel=None, ylabel=None, saveas=None, optimizer='perf',
          **plot_specific_kwargs)

**Returns:** ``matplotlib.axes.Axes``

Key Parameters
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Parameter
     - Type
     - Description
   * - ``plot``
     - ``str`` or ``dict``
     - Plot type (e.g. ``'scatterplot'``) or per-subplot dict
       (e.g. ``{'[1,1]': 'histplot', '[1,2]': 'ecdfplot'}``).
       Combine types with ``+`` (e.g. ``'boxplot+stripplot'``).
   * - ``df``
     - pandas DataFrame, dict-list, or dict-ndarray
     - Input data structure
   * - ``x``
     - ``str``, ``list``, ndarray, Index, or ``None``
     - Variable(s) for x positions
   * - ``y``
     - ``str``, ``list``, ndarray, Index, or ``None``
     - Variable(s) for y positions
   * - ``Nx``
     - ``int``
     - Figure columns
   * - ``Ny``
     - ``int``
     - Figure rows
   * - ``figsize``
     - ``[float, float]``
     - Width, height in inches. Default: ``[8, 6]``
   * - ``filter``
     - ``str``, ``Series``, or ``None``
     - Filter dataframe before plotting (pandas query or boolean Series)
   * - ``sep``
     - ``str`` or ``None``
     - Thousand separator. ``','``, ``'.'``, ``'.c'``, ``',c'``, ``'.L'``,
       ``',L'``, ``'.cL'``, ``',cL'``
   * - ``tick_add``
     - ``str`` or ``None``
     - Unit to add to ticks. Pattern: ``'{}_'``, ``'_{}'``, ``'{}(_)'``, etc.
   * - ``statdesc``
     - ``str`` or ``None``
     - Statistical description. ``'general'``, ``'boxplot'``, ``'mean+median'``, etc.
   * - ``text``
     - ``bool``, ``str``, or ``None``
     - Text annotation. ``True`` for point annotations; ``'h'``, ``'v'``, ``'i'``
       for bar positions.
   * - ``optimizer``
     - ``str``
     - ``'perf'`` (fast, more memory) or ``'saver'`` (slow, less memory)
   * - ``saveas``
     - ``str`` or ``None``
     - Save as ``.png``, ``.pdf``, ``.svg``, or ``.eps``

For full parameter documentation for each plot type, including plot-specific
kwargs such as ``hue``, ``kde``, ``estimator``, ``orient``, and more, see the
:doc:`plot type pages <plot_types>`.
