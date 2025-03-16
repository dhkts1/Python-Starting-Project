# Radon - Code Complexity Analyzer

Radon is a Python tool that computes various metrics from source code, helping you identify complex, hard-to-maintain code that might need refactoring.

## Overview

Radon helps improve code quality by:

- Calculating cyclomatic complexity of functions and methods
- Computing raw metrics (LOC, SLOC, comments, etc.)
- Analyzing Halstead metrics for cognitive complexity
- Measuring maintainability index
- Identifying code that might be difficult to understand or test
- Integrating with CI/CD pipelines and pre-commit hooks

## Installation

Radon is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install radon
```

## How It's Used in This Project

In this project, Radon is used to:

1. Identify overly complex functions and methods
1. Maintain reasonable complexity levels across the codebase
1. Run as part of the pre-commit hooks and CI/CD pipeline
1. Guide refactoring efforts to improve code maintainability

## Configuration in This Project

Radon is configured in the `pyproject.toml` file:

```toml linenums="1"
[tool.radon]
exclude = ["tests/*", "docs/*", "build/*", "dist/*"]
```

And as a poethepoet task:

```toml linenums="1"
[tool.poe.tasks]
radon = "radon cc src/ -a -nc"
```

This configuration:

- Excludes test files, documentation, and build artifacts
- Analyzes cyclomatic complexity in the src directory
- Shows complexity for all functions (-a)
- Uses no color output (-nc) for CI compatibility

## Basic Usage

### Running Radon

To run Radon on the project:

=== "Using poe tasks"
`bash linenums="1"     # Run via poethepoet     uv run poe radon     `

=== "Using direct commands"
\`\`\`bash linenums="1"
\# Run cyclomatic complexity analysis directly
uv run radon cc src/

````
# Run raw metrics analysis
uv run radon raw src/

# Run maintainability index analysis
uv run radon mi src/

# Run Halstead metrics analysis
uv run radon hal src/
```
````

### Common Command-Line Options

```bash linenums="1"
# Show complexity for all functions (not just those exceeding threshold)
uv run radon cc -a src/

# Set complexity threshold (A-F)
uv run radon cc -nc --min=B src/

# Sort by complexity
uv run radon cc -s src/

# Show average complexity
uv run radon cc --average src/

# Exclude specific files or directories
uv run radon cc --exclude "tests/*,docs/*" src/
```

## Examples

### Cyclomatic Complexity Output

```text linenums="1"
src/your_package/module.py
    F 24:0 complex_function - F (15)
    C 10:0 ComplexClass - A (5)
        M 12:4 simple_method - A (1)
        M 18:4 complex_method - C (7)
```

### Maintainability Index Output

```text linenums="1"
src/your_package/module.py - A (100.00)
src/your_package/complex.py - C (65.32)
```

## Complexity Ranks

Radon uses letter grades to rank complexity:

| Rank | Complexity | Risk |
|------|------------|-------------------------------------|
| A | 1-5 | Low - simple block |
| B | 6-10 | Low - well structured and stable |
| C | 11-20 | Moderate - slightly complex |
| D | 21-30 | More than moderate - more complex |
| E | 31-40 | High - complex, alarming |
| F | 41+ | Very high - error-prone, unstable |

## Metrics Explained

### Cyclomatic Complexity (CC)

Measures the number of linearly independent paths through a program's source code. Higher values indicate more complex code that is harder to test and maintain.

### Maintainability Index (MI)

A composite metric based on cyclomatic complexity, lines of code, and Halstead volume. Higher values (0-100) indicate more maintainable code.

### Raw Metrics

- **LOC**: Lines of Code (total)
- **SLOC**: Source Lines of Code (excluding comments and blank lines)
- **LLOC**: Logical Lines of Code
- **COMMENTS**: Comment Lines
- **MULTI**: Multi-line strings
- **BLANK**: Blank lines

### Halstead Metrics

- **h1**: Number of distinct operators
- **h2**: Number of distinct operands
- **N1**: Total number of operators
- **N2**: Total number of operands
- **vocabulary**: h1 + h2
- **length**: N1 + N2
- **volume**: length * log2(vocabulary)
- **difficulty**: (h1/2) * (N2/h2)
- **effort**: difficulty * volume

## Best Practices

1. **Keep functions simple**: Aim for cyclomatic complexity below 10 (A-B rank).
1. **Refactor complex code**: Break down functions with high complexity.
1. **Write unit tests**: Complex functions need thorough testing.
1. **Set thresholds in CI**: Fail builds if complexity exceeds acceptable levels.
1. **Monitor trends**: Track complexity metrics over time to prevent degradation.
1. **Use with other tools**: Combine with tools like Ruff and Xenon for comprehensive quality checks.
1. **Focus on hotspots**: Prioritize refactoring the most complex parts of your codebase.

## Refactoring Strategies

When Radon identifies complex code, consider these refactoring strategies:

=== "Extract Method"
\`\`\`python linenums="1"
\# Before refactoring
def complex_function(data):
\# Process data
processed = []
for item in data:
\# Complex processing logic (10+ lines)
processed.append(result)

````
    # More complex logic (10+ lines)
    return final_result

# After refactoring
def complex_function(data):
    processed = process_data(data)
    return calculate_result(processed)

def process_data(data):
    processed = []
    for item in data:
        # Complex processing logic (10+ lines)
        processed.append(result)
    return processed

def calculate_result(processed):
    # More complex logic (10+ lines)
    return final_result
```
````

=== "Replace Conditionals"
\`\`\`python linenums="1"
\# Before refactoring (complex if/else chain)
def get_discount(customer_type, order_total):
if customer_type == 'regular':
if order_total < 100:
return 0
elif order_total < 500:
return 0.05
else:
return 0.1
elif customer_type == 'premium':
if order_total < 100:
return 0.1
elif order_total < 500:
return 0.15
else:
return 0.2
else: # new customer
if order_total < 100:
return 0
elif order_total < 500:
return 0.02
else:
return 0.05

````
# After refactoring (strategy pattern)
discount_rules = {
    'regular': {
        'base': 0,
        'mid': 0.05,
        'high': 0.1,
    },
    'premium': {
        'base': 0.1,
        'mid': 0.15,
        'high': 0.2,
    },
    'new': {
        'base': 0,
        'mid': 0.02,
        'high': 0.05,
    }
}

def get_discount(customer_type, order_total):
    if customer_type not in discount_rules:
        customer_type = 'new'

    if order_total < 100:
        tier = 'base'
    elif order_total < 500:
        tier = 'mid'
    else:
        tier = 'high'

    return discount_rules[customer_type][tier]
```
````

## Resources

- [Radon Documentation](https://radon.readthedocs.io/)
- [Cyclomatic Complexity Explained](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- [Halstead Complexity Measures](https://en.wikipedia.org/wiki/Halstead_complexity_measures)
- [Maintainability Index](https://docs.microsoft.com/en-us/visualstudio/code-quality/code-metrics-maintainability-index)
