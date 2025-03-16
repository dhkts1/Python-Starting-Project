# Codespell - Spell Checker

Codespell is a tool that checks for common misspellings in text files. It's designed to catch spelling errors that might be missed by traditional spell checkers, especially in code and documentation.

## Overview

Codespell helps improve the quality of your codebase by:

- Finding and fixing common spelling mistakes
- Checking multiple file types (Python, Markdown, text, etc.)
- Supporting custom dictionaries for project-specific terms
- Integrating with pre-commit hooks for automated checks

## Installation

Codespell is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install codespell
```

## How It's Used in This Project

In this project, Codespell is used to:

1. Check for spelling errors in all project files
1. Run automatically as a pre-commit hook
1. Ensure consistent spelling in documentation and code comments

## Configuration in This Project

Codespell is configured in the `pyproject.toml` file:

```toml linenums="1"
[tool.codespell]
skip = "*.json,*.csv,*.pyc,*.min.js,node_modules/*,build/*,dist/*"
ignore-words-list = "crate,hist,ro,while"
```

This configuration:

- Skips checking certain file types and directories
- Ignores specific words that might be flagged incorrectly
- Runs on all other files in the project

## Basic Usage

To run Codespell on the project:

```bash linenums="1"
# Run on the entire project
uv run codespell

# Run on specific files or directories
uv run codespell src/ docs/ README.md
```

### Common Command-Line Options

```bash linenums="1"
# Check with a custom dictionary
uv run codespell --dictionary=./custom_dictionary.txt

# Write corrections directly to files
uv run codespell --write-changes

# Show only certain types of errors
uv run codespell --quiet-level=2

# Ignore specific words
uv run codespell --ignore-words-list="crate,hist,ro"
```

### Detecting Spelling Errors

Here's an example of what codespell output might look like:

```text linenums="1"
$ uv run codespell src/
src/module.py:10: definitely -> definitely
src/utils.py:25: receive -> receive
docs/README.md:15: occurred -> occurred
```

### Correcting Spelling Errors

Example of checking and correcting:

```text linenums="1"
# Check and show suggestions without making changes
$ uv run codespell src/module.py
src/module.py:10: definitely -> definitely

# Apply corrections automatically
$ uv run codespell --write-changes src/module.py
src/module.py:10: definitely -> definitely
```

## Common Misspellings

Here are some common misspellings that Codespell catches:

| Common Typo | Correct Spelling |
|---------------|---------------|
| accommodate | accommodate |
| achieve | achieve |
| address | address |
| argument | argument |
| believe | believe |
| consensus | consensus |
| definitely | definitely |
| dependency | dependency |
| existence | existence |
| occurred | occurred |
| receive | receive |
| separate | separate |
| successful | successful |

## Best Practices

1. **Run regularly**: Include Codespell in your pre-commit hooks
1. **Customize for your project**: Add project-specific terms to the ignore list
1. **Fix spelling errors promptly**: Correct spelling errors as soon as they're detected
1. **Use with other tools**: Combine with other linting tools for comprehensive code quality
1. **Update dictionaries**: Keep custom dictionaries updated with domain-specific terminology

## Troubleshooting

### False Positives

If Codespell flags words that are actually correct:

1. Add them to the `ignore-words-list` in your configuration
1. Create a custom dictionary file with words to ignore

### Performance Issues

For large codebases:

1. Use the `skip` option to exclude large generated files or binary files
1. Run Codespell only on changed files during development

## Resources

- [Codespell GitHub Repository](https://github.com/codespell-project/codespell)
- [Pre-commit Hook Configuration](https://pre-commit.com/hooks.html)
