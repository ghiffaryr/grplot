"""
Pytest fixtures and configuration for grplot tests
"""
import pytest
import numpy as np
import pandas as pd

# Set matplotlib backend before importing pyplot to avoid display issues
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing"""
    np.random.seed(42)
    return pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'value': np.random.randint(0, 100, 100)
    })


@pytest.fixture
def sample_numeric_data():
    """Create sample numeric arrays"""
    np.random.seed(42)
    return {
        'x': np.random.randn(50),
        'y': np.random.randn(50)
    }


@pytest.fixture
def matplotlib_figure():
    """Create a matplotlib figure and axes"""
    fig, ax = plt.subplots(figsize=(8, 6))
    yield fig, ax
    plt.close(fig)


@pytest.fixture
def matplotlib_multiple_axes():
    """Create figure with multiple subplots"""
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    yield fig, axes
    plt.close(fig)


@pytest.fixture(autouse=True)
def cleanup_matplotlib():
    """Clean up matplotlib figures after each test"""
    yield
    plt.close('all')
