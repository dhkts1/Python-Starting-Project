# Pytest-cov - Code Coverage for Pytest

Pytest-cov is a plugin for pytest that provides code coverage reporting, helping you identify which parts of your code are being tested and which are not.

## Overview

Pytest-cov helps improve test quality by:

- Measuring how much of your code is executed during tests
- Generating detailed reports on code coverage
- Identifying untested code paths
- Supporting branch coverage analysis
- Integrating seamlessly with pytest
- Providing various output formats (terminal, HTML, XML)

## Installation

Pytest-cov is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install pytest-cov
```

## How It's Used in This Project

In this project, Pytest-cov is used to:

1. Measure test coverage across the codebase
2. Generate coverage reports as part of the CI/CD pipeline
3. Identify areas of the code that need more testing
4. Enforce minimum coverage thresholds

## Configuration in This Project

Pytest-cov is configured in the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term --cov-report=html"
```

This configuration:

- Measures coverage for code in the `src` directory
- Outputs coverage reports to the terminal
- Generates HTML reports for detailed analysis

## Basic Usage

### Running Tests with Coverage

To run tests with coverage:

```bash
# Run tests with coverage
uv run pytest --cov=src

# Run tests with coverage and generate HTML report
uv run pytest --cov=src --cov-report=html

# Run tests with coverage for specific modules
uv run pytest --cov=src.module1 --cov=src.module2
```

### Common Command-Line Options

```bash
# Specify source directories to measure
uv run pytest --cov=src --cov=lib

# Generate different report formats
uv run pytest --cov=src --cov-report=term --cov-report=html --cov-report=xml

# Set minimum coverage threshold
uv run pytest --cov=src --cov-fail-under=90

# Show line numbers of missing coverage
uv run pytest --cov=src --cov-report=term-missing
```

## Examples

### Terminal Coverage Report

```
----------- coverage: platform linux, python 3.11.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
src/__init__.py             4      0   100%
src/module1.py             26      3    88%
src/module2.py             42      7    83%
src/utils.py               18      2    89%
-------------------------------------------
TOTAL                      90     12    87%
```

### HTML Report

The HTML report provides a detailed view of coverage, including:

- File-by-file breakdown
- Line-by-line highlighting of covered and uncovered code
- Branch coverage information
- Summary statistics

## Coverage Types

Pytest-cov supports different types of coverage measurement:

1. **Statement Coverage**: Measures which statements in your code have been executed
2. **Branch Coverage**: Measures which possible branches (if/else paths) have been taken
3. **Function Coverage**: Measures which functions have been called
4. **Line Coverage**: Measures which executable lines have been run

## Best Practices

1. **Aim for high coverage**: Strive for at least 80-90% code coverage.
2. **Focus on critical paths**: Ensure business-critical code has near 100% coverage.
3. **Don't just chase numbers**: High coverage doesn't guarantee good tests; focus on test quality too.
4. **Use branch coverage**: Enable branch coverage to catch untested conditional paths.
5. **Set minimum thresholds**: Use `--cov-fail-under` to enforce minimum coverage requirements.
6. **Review coverage reports regularly**: Identify and address areas with low coverage.
7. **Include coverage in CI**: Make coverage checks part of your continuous integration pipeline.

## Resources

- [Pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Code Coverage Best Practices](https://martinfowler.com/bliki/TestCoverage.html)
