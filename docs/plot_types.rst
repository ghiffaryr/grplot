Plot Types
==========

grplot supports four major plot families with 20+ plot types, all accessible
through the ``plot2d`` function. Plot types are combined using ``+`` to overlay
multiple plots in a single subplot (e.g. ``'boxplot+stripplot'``).

Relational Plots
----------------

Visualize relationships between two or more numeric variables.

.. toctree::
   :maxdepth: 1

   plots/scatterplot
   plots/lineplot

Distribution Plots
------------------

Visualize the statistical distribution of one or more variables.

.. toctree::
   :maxdepth: 1

   plots/histplot
   plots/kdeplot
   plots/ecdfplot
   plots/rugplot
   plots/pieplot
   plots/treemapsplot
   plots/packedbubblesplot

Categorical Plots
-----------------

Visualize the distribution of values across categorical levels.

.. toctree::
   :maxdepth: 1

   plots/stripplot
   plots/swarmplot
   plots/boxplot
   plots/violinplot
   plots/boxenplot
   plots/pointplot
   plots/barplot
   plots/countplot
   plots/paretoplot

Regression Plots
----------------

Visualize linear relationships and regression fits.

.. toctree::
   :maxdepth: 1

   plots/regplot
   plots/residplot

Dashboard-Like
--------------

Combine multiple plot types and subplots in a single ``plot2d`` call.

.. toctree::
   :maxdepth: 1

   plots/dashboard
