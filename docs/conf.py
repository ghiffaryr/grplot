# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "grplot"
copyright = "2026, Ghiffary Rifqialdi"
author = "Ghiffary Rifqialdi"
release = "1.0.4"
version = "1.0.4"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "grlogo_black_border.svg",
    "dark_logo": "grlogo_white_border.svg",
    "light_css_variables": {
        # GitHub light palette
        "color-brand-primary": "#0969da",
        "color-brand-content": "#0969da",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f6f8fa",
        "color-foreground-primary": "#1f2328",
        "color-foreground-secondary": "#636c76",
        "color-sidebar-background": "#f6f8fa",
        "color-highlight-on-target": "#fffbdd",
        "font-stack": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif",
        "font-stack--monospace": "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace",
    },
    "dark_css_variables": {
        # GitHub dark palette
        "color-brand-primary": "#58a6ff",
        "color-brand-content": "#58a6ff",
        "color-background-primary": "#0d1117",
        "color-background-secondary": "#161b22",
        "color-foreground-primary": "#e6edf3",
        "color-foreground-secondary": "#8b949e",
        "color-sidebar-background": "#161b22",
        "color-sidebar-background-border": "#30363d",
        "color-sidebar-brand-text": "#e6edf3",
        "color-sidebar-caption-text": "#8b949e",
        "color-sidebar-link-text": "#c9d1d9",
        "color-sidebar-link-text--top-level": "#e6edf3",
        "color-sidebar-item-background--hover": "#21262d",
        "color-sidebar-item-background--current": "#21262d",
        "color-sidebar-item-expander-background": "transparent",
        "color-sidebar-item-expander-background--hover": "#21262d",
        "color-highlight-on-target": "#1d2d3e",
        "color-background-hover": "#21262d",
        "color-background-border": "#30363d",
        "color-api-background": "#161b22",
        "color-api-background-hover": "#1c2128",
        "color-link": "#58a6ff",
        "color-link--hover": "#79c0ff",
        "color-link--visited": "#bc8cff",
        "font-stack": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif",
        "font-stack--monospace": "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace",
    },
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
}
html_css_files = ["custom.css"]

# -- Source suffix -----------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
