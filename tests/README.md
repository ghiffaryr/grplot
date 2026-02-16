# grplot Test Suite

Comprehensive test suite for the grplot visualization library.

## Test Structure

### Integration Tests

Integration tests verify real-world usage patterns through the public `plot2d()` API:

- **`test_integration_core.py`** (31 tests)
  - Foundation tests covering all major plot types
  - Scatter, line, hist, kde, box, violin, bar, point, strip plots
  - Regression and residual plots
  - Basic multi-plot layouts

- **`test_integration_separators.py`** (84 tests)
  - All separator types: `,` `.` `.c` `,c` `.L` `,L` `.cL` `,cL`
  - Tick_add formats: suffix, prefix, both, negative handling
  - Statdesc types: general, boxplot, count, mean, median, std, min+max, q1+q3
  - Combinations with plots, log scales, filters

- **`test_integration_combinations.py`** (95 tests)
  - Plot overlays (2-3 plot combinations)
  - Multi-plot grids (1x4, 4x1, 3x3)
  - Text annotations with various parameters
  - Edge cases: single points, extreme values, many categories

- **`test_integration_parameters.py`** (89 tests)
  - Labels, titles, limits, datetime formats
  - Palettes, alpha transparency, font sizes
  - Histplot variations (bins, elements, stats)
  - KDE and boxplot parameter matrices

- **`test_integration_text.py`** (63 tests)
  - Text annotations on all plot types
  - Text with separators and tick_add variations
  - Positioning and formatting
  - Edge cases: large numbers, decimals, negatives

- **`test_integration_filters.py`** (62 tests, 5 skipped)
  - Filter features (query strings, boolean series)
  - Font size parameters across all plot types
  - Complex parameter interactions
  - Stress testing and edge cases

### Parametrized Tests

- **`test_parametrized_plots.py`** (256 tests, 6 skipped)
  - Systematic parameter matrices using \`pytest.mark.parametrize\`
  - Scatterplot: hue, size, style, alpha, palette combinations
  - Lineplot: estimators, confidence intervals, markers
  - Histplot: bins, elements, stat modes
  - Box/violin: aesthetic parameters
  - Legend, rotation, limits, multi-plot configurations

- **`test_parametrized_features.py`** (117 tests, 4 skipped)
  - Separator combinations across plot types
  - Aesthetic parameters (hue, size, style, alpha, palettes)
  - Histplot parameters (bins, element, stat, multiple)
  - Lineplot parameters (estimator, CI, markers, sort)
  - Box/violin parameters (whis, inner, saturation)
  - Font sizes, rotations, limits
  - Large datasets (optimizer triggers), datetime formats
  - Edge cases (single point, few points, many categories)

### Unit Tests

- **`test_utils.py`** (25 tests)
  - Utility function validation
  - Data structure checks
  - String manipulation and formatting

## Running Tests

```bash
# All tests
pytest tests/

# With coverage
pytest tests/ --cov=grplot --cov-report=html

# Specific file
pytest tests/test_integration_core.py -v

# Pattern matching
pytest tests/ -k "separator" -v

# By marker
pytest tests/ -m integration -v
```

## Test Fixtures

**Shared Fixtures** (\`conftest.py\`):
- \`matplotlib_figure\`: Clean matplotlib context
- \`sample_dataframe\`: Generic test data

**Per-file Fixtures**: Each test file defines fixtures optimized for its scenarios.

## Coverage Metrics

**Current**: 50.97% (1,880 of 3,549 statements)  
**Tests**: 797 passing, 15 skipped, 812 total  
**Execution**: ~95 seconds (~0.12s per test)  
**Updated**: February 16, 2026

### Historical Trends

| Date | Coverage | Tests | Milestone |
|------|----------|-------|-----------|
| 2026-02-16 | 50.97% | 797 | Advanced filters (+52% on filter_def.py) |
| 2026-02-16 | 49.46% | 618 | Cleanup and formalization |
| 2026-02-15 | 47.09% | 282 | Integration test expansion |
| 2026-02-14 | 31.65% | 31 | First working integration tests |

### Coverage by Module

#### Excellent Coverage (>80%)
| Module | Coverage | Notes |
|--------|----------|-------|
| setting.py | 97% | Configuration management |
| check_*.py | 80-100% | Validation modules |
| utils/* | 66-100% | Utility functions |
| hotfix/* | 83-100% | Bug fix implementations |

#### Good Coverage (40-80%)
| Module | Coverage | Notes |
|--------|----------|-------|
| plot_multi_def.py | 69% | Multi-plot rendering |
| filter_def.py | 68% | Query & boolean filters |
| plot_single_def.py | 52% | Single plot rendering |
| check_text.py | 46% | Text validation |
| optimizer_data.py | 45% | Data optimization |
| tick_sep_def.py | 41% | Number formatting |
| statdesc/* | 56-73% | Statistical descriptions |

#### Limited Coverage (<40%)
| Module | Coverage | Notes |
|--------|----------|-------|
| analytic/* | 0% | Internal analytics (not public API) |
| optimizer_analytic.py | 0% | Internal optimization algorithms |
| text_def.py | 32% | Text positioning internals |
| font_def.py | 32% | Font handling (paretoplot special cases) |
| packedbubbles_def.py | 12% | Specialized hierarchical plot |
| treemaps_def.py | 8% | Specialized hierarchical plot |

### Coverage Limitations

The remaining ~49% uncovered code consists primarily of:

- **Internal modules**: Analytics and optimization algorithms not exposed via public API
- **Specialized plots**: Hierarchical plots requiring complex data structures
- **Implementation internals**: Text positioning, font rendering special cases
- **Edge cases**: Rare parameter combinations, platform-specific branches

Current coverage validates all public API functionality and realistic usage patterns. Higher coverage would require testing internal implementation details not accessible through the public interface.

## Testing Approach

### Principles

1. **Integration-First**: Test through public \`plot2d()\` API with realistic usage patterns
   - Validates actual user workflows
   - Each test exercises 100-500 statements
   - Higher value than isolated unit tests

2. **Realistic Scenarios**: Use production-like datasets and parameter combinations
   - Reflects actual library usage
   - Documents expected behavior
   - Validates documentation examples

3. **Systematic Parametrization**: Use \`pytest.mark.parametrize\` for parameter matrices
   - Efficient parameter space coverage
   - Catches interaction bugs
   - Maintainable test code

4. **Minimal Mocking**: Test real functionality over mocked behavior
   - Validates actual integration points
   - More reliable results

5. **Visual Safety**: All tests use Agg backend (headless) with proper cleanup
   - Prevents window popups
   - Ensures clean test environment

## Contributor Guidelines

### Adding New Features
1. Create integration test for primary usage path
2. Add parametrized tests for parameter variations
3. Ensure test covers documentation examples
4. Update coverage metrics in this document

### Bug Fixes
1. Add regression test reproducing the issue
2. Verify fix resolves the test
3. Retain test to prevent regression
4. Document bug scenario in test docstring

### Test Standards
- **Naming**: \`test_<category>_<specific_feature>.py\`
- **Approach**: Integration tests for API-level functionality
- **Parametrization**: Use for parameter space coverage
- **Documentation**: Docstrings describing validation scope
- **Cleanup**: Always call \`plt.close('all')\` in teardown
- **Markers**: Apply appropriate pytest markers

### Maintenance Checklist
- Analyze coverage gaps quarterly
- Identify high-value test additions
- Remove obsolete/redundant tests
- Update documentation
- Monitor execution time trends
- Address any flaky tests

## Continuous Integration

Automated testing runs on:
- Every commit to main branch
- Every pull request
- Python versions: 3.10, 3.11, 3.12
- Platforms: Linux, macOS, Windows
- Latest matplotlib releases

### Coverage Targets

| Level | Threshold | Description |
|-------|-----------|-------------|
| Minimum | 40% | Core functionality covered |
| Current | 51% | All public API and realistic workflows |
| Aspirational | 70% | Includes specialized features |
| Impractical | 90% | Requires testing internal implementation |

**Focus**: Quality over quantity - comprehensive coverage of realistic usage patterns rather than arbitrary percentage targets.
