# Xenon - Code Maintainability Checker

Xenon is a Python tool that monitors code complexity using Radon, enforcing thresholds to ensure your codebase remains maintainable.

## Overview

Xenon helps maintain code quality by:

- Enforcing complexity thresholds for your codebase
- Preventing overly complex code from being merged
- Monitoring code maintainability over time
- Integrating with CI/CD pipelines and pre-commit hooks
- Building on Radon's complexity metrics
- Providing a simple pass/fail result for automated checks

## Installation

Xenon is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install xenon
```

## How It's Used in This Project

In this project, Xenon is used to:

1. Enforce maximum complexity thresholds
2. Prevent code quality degradation over time
3. Run as part of the pre-commit hooks and CI/CD pipeline
4. Ensure maintainable code across the codebase

## Configuration in This Project

Xenon is configured as a poethepoet task:

```toml linenums="1"
[tool.poe.tasks]
xenon = "xenon --max-absolute B --max-modules B --max-average A src"
```

This configuration:

- Sets maximum absolute complexity to rank B (6-10)
- Sets maximum module complexity to rank B (6-10)
- Sets maximum average complexity to rank A (1-5)
- Analyzes code in the src directory

## Basic Usage

### Running Xenon

To run Xenon on the project:

=== "Using poe tasks"

`bash linenums="1"     # Run via poethepoet     uv run poe xenon     `

=== "Using direct commands"

`bash linenums="1"     # Run directly with thresholds     uv run xenon --max-absolute B --max-modules B --max-average A src/     `

### Common Command-Line Options

```bash linenums="1"
# Set maximum absolute complexity (A-F)
uv run xenon --max-absolute C src/

# Set maximum module complexity (A-F)
uv run xenon --max-modules C src/

# Set maximum average complexity (A-F)
uv run xenon --max-average B src/

# Exclude specific files or directories
uv run xenon --exclude "tests/*,docs/*" src/

# Increase verbosity
uv run xenon -v src/
```

## Examples

### Passing Check

```text linenums="1"
$ uv run xenon --max-absolute B --max-modules B --max-average A src/
Absolute: B (6.0)
Modules: A (3.42)
Average: A (3.42)

No thresholds exceeded
```

### Failing Check

```text linenums="1"
$ uv run xenon --max-absolute B --max-modules B --max-average A src/
Absolute: C (12.0)
Modules: B (7.5)
Average: A (4.2)

The following thresholds were exceeded:
  Absolute complexity: C > B
```

## Complexity Thresholds

Xenon uses Radon's letter grades to rank complexity:

| Rank | Complexity | Risk                              |
| ---- | ---------- | --------------------------------- |
| A    | 1-5        | Low - simple block                |
| B    | 6-10       | Low - well structured and stable  |
| C    | 11-20      | Moderate - slightly complex       |
| D    | 21-30      | More than moderate - more complex |
| E    | 31-40      | High - complex, alarming          |
| F    | 41+        | Very high - error-prone, unstable |

## Metrics Explained

Xenon checks three different complexity metrics:

1. **Absolute Complexity**: The highest complexity of any single function or method in the codebase
2. **Module Complexity**: The highest average complexity of any module in the codebase
3. **Average Complexity**: The average complexity across all functions and methods in the codebase

## Best Practices

1. **Start with reasonable thresholds**: Begin with moderate thresholds (C or D) and gradually tighten them.
2. **Focus on absolute complexity first**: Prioritize fixing the most complex functions.
3. **Use with Radon**: Use Radon to identify specific complex functions that Xenon flags.
4. **Include in CI pipeline**: Make Xenon part of your continuous integration checks.
5. **Gradually improve thresholds**: As you refactor, gradually lower thresholds to prevent regression.
6. **Document exceptions**: If certain complex functions can't be simplified, document why.
7. **Balance strictness with practicality**: Very strict thresholds (all A's) might be impractical for some codebases.

## Integration with CI/CD

### GitHub Actions Example

```yaml linenums="1"
  - name: Check code complexity
    run: |
      uv pip install xenon
      xenon --max-absolute B --max-modules B --max-average A src/
```

### Pre-commit Hook Example

```yaml linenums="1"
  - repo: local
    hooks:
      - id: xenon
        name: xenon
        entry: xenon --max-absolute B --max-modules B --max-average A
        language: python
        types: [python]
        additional_dependencies: [xenon]
```

## Troubleshooting

### Common Issues

#### Too Strict Thresholds

If Xenon consistently fails with your current thresholds:

1. Use Radon to identify the most complex parts of your code
2. Refactor those parts to reduce complexity
3. If refactoring isn't feasible, consider slightly relaxing thresholds

#### False Positives

Some complex code might be unavoidably complex due to the problem domain:

1. Consider excluding specific files from analysis
2. Document why the complexity is necessary
3. Ensure complex code is well-tested and documented

## Resources

- [Xenon Documentation](https://xenon.readthedocs.io/)
- [Radon Documentation](https://radon.readthedocs.io/)
- [Cyclomatic Complexity Explained](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- [Refactoring Techniques](https://refactoring.guru/refactoring/techniques)
