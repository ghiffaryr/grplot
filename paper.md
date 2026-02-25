---
title: 'grplot: A Python Library for Lazy Statistical Data Visualization'
tags:
  - Python
  - data visualization
  - statistical graphics
  - matplotlib
  - seaborn
  - exploratory data analysis
authors:
  - name: Ghiffary Rifqialdi
    orcid: 0000-0003-2649-1947
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: 25 February 2025
bibliography: paper.bib
---

# Summary

`grplot` is an open-source Python library that compresses multi-step
statistical plotting workflows into a single high-level function call. Built on top
of Matplotlib [@Hunter2007], Seaborn [@Waskom2021], NumPy [@Harris2020], SciPy
[@Virtanen2020], and Pandas [@McKinney2010], it exposes a unified `plot2d` API that
automatically handles subplot creation, axis labeling, legends, statistical
annotations, number formatting, and figure export. Users specify what to plot via a
plot-type string or a dictionary mapping panel positions to plot types; the library
applies sensible defaults while accepting 100+ parameters for explicit overrides at
global, per-axis, or per-element granularity. As of version 0.14, `grplot` supports
Python 3.6+, is available on PyPI and conda-forge, and has been tested in Jupyter and
Google Colab environments.

# Statement of Need

Producing publication-quality figures in Python typically requires orchestrating
several libraries: constructing Figure/Axes objects in Matplotlib, calling Seaborn
chart functions, manually setting tick formats, adding text annotations, adjusting
legends, and finally saving the output. For practitioners who generate many plots
routinely—data analysts, researchers, and data scientists—this boilerplate is
repetitive and error-prone.

Existing libraries address parts of this problem. Matplotlib [@Hunter2007] provides
full control but verbose syntax. Seaborn [@Waskom2021] reduces setup for common
statistical charts. Altair [@VanderPlas2019] and `plotnine` [@Wickham2016] offer
declarative grammars, and Plotly [@Plotly2015] focuses on interactivity. None of
these, however, offers a single call that combines multi-panel layout, statistical
summaries, number formatting, annotation, and file export for static, reproducible
figures.

`grplot` fills this gap with a consistent imperative API. It is particularly suited
to data practitioners who need reproducible, annotated figures in notebooks or
technical reports without rebuilding formatting utilities for each project. It also
ships two domain-specific analytics utilities—cohort retention analysis and
rank-order/gain/KS/lift tables—that practitioners commonly reimplement from scratch.

# Design and API

## Hierarchical Parameter Model

`plot2d` accepts parameters at three scopes:

- **Global**: applied to all panels (e.g., `figsize`, `fontsize`).
- **Axes-level**: scoped to a panel by 1-based index `"[i]"` (1-D) or
  `"[row,col]"` (2-D), e.g., `title={"[2,1]": "My title"}`.
- **Axes-Plot-level**: element-level overrides within a panel, e.g.,
  `hue={"[1,2]": {"scatterplot": "species"}}`.

This hierarchy lets a single call express a complete multi-panel dashboard while
preserving per-panel control.

## Supported Chart Types

| Family       | Chart types |
|---|---|
| Relational   | `scatterplot`, `lineplot` |
| Distribution | `histplot`, `kdeplot`, `ecdfplot`, `rugplot` |
| Categorical  | `stripplot`, `swarmplot`, `boxplot`, `violinplot`, `boxenplot`, `pointplot`, `barplot`, `countplot` |
| Specialized  | `pieplot`, `treemapsplot`, `packedbubblesplot`, `paretoplot`, composite overlays (`kdeplot+rugplot`, `scatterplot+rugplot`, `violinplot+swarmplot`, `histplot+boxplot`, `stripplot+pointplot`) |
| Matrix       | `heatmap`, `clustermap` |
| Regression   | `regplot`, `residplot` |

Multiple chart types can be overlaid in one panel using `+` notation and composed
into grid dashboards using the `Nx` (columns) and `Ny` (rows) parameters.

## Analytic Utilities

`grplot.analytic.cohort` produces a cohort retention heatmap from a customer
transaction table, computing monthly retention rates and an optional summary row in a
single call.

`grplot.analytic.rank_order` generates a rank-order table with gain, KS statistic,
and lift curves from predicted probabilities and true binary labels, supporting
multi-class outputs via a class selector.

# Usage Example

```python
from grplot import plot2d
import grplot_seaborn as gs

tips = gs.load_dataset("tips")
ax = plot2d(
    plot={"[1,1]": "histplot", "[1,2]": "ecdfplot",
          "[2,1]": "paretoplot", "[2,2]": "boxplot+stripplot"},
    Nx=2, Ny=2,
    df=tips,
    x=["total_bill", "total_bill", "day", "total_bill"],
    y=[None, None, "total_bill", "day"],
    figsize=[14, 10],
    sep={"total_bill": ".c"},
    statdesc={"[1,1]": {"total_bill": "general"},
              "[2,2]": {"total_bill": "boxplot"}},
    title={"[1,1]": "Histogram of total_bill",
           "[1,2]": "ECDF of total_bill",
           "[2,1]": "Pareto total_bill by day",
           "[2,2]": "Box total_bill by day"},
    kde=True,
)
```

# Acknowledgements

The author thanks the maintainers of Matplotlib, Seaborn, NumPy, SciPy, and Pandas
for providing the foundational infrastructure on which `grplot` is built. No
financial support was received for this work.

## Conflict of Interest

The author declares no conflicts of interest.

## AI Usage Disclosure

AI was used to assist with copy-editing and grammar review of
this paper. All technical content, design decisions, code, and final text were
authored, reviewed, and validated by the human author.

# References
