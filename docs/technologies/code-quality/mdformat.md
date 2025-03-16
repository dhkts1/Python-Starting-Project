# MDFormat - Markdown Formatter

MDFormat is an opinionated Markdown formatter that automatically formats Markdown files to a consistent style, improving readability and maintainability.

## Overview

MDFormat helps maintain consistent Markdown formatting by:

- Enforcing a consistent style across all Markdown files
- Automatically fixing formatting issues
- Supporting various Markdown extensions and flavors
- Integrating with pre-commit hooks and CI/CD pipelines
- Providing plugins for additional formatting rules

## Installation

MDFormat is included as a development dependency:

```bash
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash
uv pip install mdformat
```

## How It's Used in This Project

In this project, MDFormat is used to:

1. Ensure consistent formatting across all Markdown documentation
2. Automatically fix formatting issues in documentation files
3. Run as part of the pre-commit hooks and CI/CD pipeline
4. Maintain professional and readable documentation

## Configuration in This Project

MDFormat is configured in the `pyproject.toml` file:

```toml
[tool.mdformat]
number = true
```

This configuration enables automatic numbering of ordered lists.

## Basic Usage

### Running MDFormat

To run MDFormat on the project:

```bash
# Format a single file
uv run mdformat docs/README.md

# Format multiple files
uv run mdformat docs/*.md

# Format and check if files would be changed
uv run mdformat --check docs/*.md
```

### Common Command-Line Options

```bash
# Check files without modifying them
uv run mdformat --check docs/*.md

# Enable specific plugins
uv run mdformat --wrap=80 --number docs/README.md

# Format with specific extensions
uv run mdformat --enable-extensions=tables,footnotes docs/README.md
```

## Examples

### Before Formatting

```markdown
# My Document

This is a paragraph with  extra  spaces.

* Unordered list item 1
* Unordered list item 2
  * Nested item

1. First item
1. Second item
1. Third item

```

### After Formatting

```markdown
# My Document

This is a paragraph with extra spaces.

- Unordered list item 1
- Unordered list item 2
  - Nested item

1. First item
2. Second item
3. Third item
```

## Formatting Rules

MDFormat applies several formatting rules:

1. **Consistent headings**: Uses ATX-style headings (`#` syntax)
2. **List formatting**: Standardizes list markers (`-` for unordered lists)
3. **Whitespace**: Removes trailing whitespace and ensures consistent spacing
4. **Line breaks**: Normalizes line breaks
5. **List numbering**: Correctly numbers ordered lists (when enabled)
6. **Table formatting**: Aligns table columns (with extensions)
7. **Code blocks**: Ensures proper fencing for code blocks

## Best Practices

1. **Run MDFormat regularly**: Include it in your pre-commit hooks to maintain consistent formatting.
2. **Format before committing**: Run MDFormat on documentation files before committing changes.
3. **Use with other Markdown tools**: Combine with Markdown linters for comprehensive documentation quality.
4. **Enable relevant extensions**: Use extensions that match your Markdown flavor (e.g., GitHub Flavored Markdown).
5. **Check formatting in CI**: Verify Markdown formatting as part of your CI pipeline.

## Resources

- [MDFormat Documentation](https://github.com/executablebooks/mdformat)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [CommonMark Spec](https://spec.commonmark.org/)
