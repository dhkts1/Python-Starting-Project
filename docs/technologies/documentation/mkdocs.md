# MkDocs - Documentation Generator

MkDocs is a fast, simple, and beautiful static site generator designed for building project documentation. It uses Markdown files to create a professional documentation website with minimal configuration.

## Overview

MkDocs provides the following features:

- Simple and intuitive project structure
- Markdown-based content creation
- Live preview development server
- Multiple themes including Material for MkDocs
- Customizable navigation
- Full-text search capability
- Easy deployment to GitHub Pages or other hosting
- Plugin system for extended functionality
- Code highlighting
- Table of contents generation

## Installation

MkDocs is included as a development dependency:

```bash linenums="1"
# Install with other development dependencies
uv sync --dev
```

To install it directly:

```bash linenums="1"
uv pip install mkdocs
```

## How It's Used in This Project

In this project, MkDocs is used to:

1. Generate the project documentation website
2. Provide a searchable interface for documentation
3. Organize documentation in a logical structure
4. Enable easy navigation between documentation sections
5. Facilitate documentation updates alongside code changes

## Configuration in This Project

MkDocs is configured in the `mkdocs.yml` file at the root of the project:

```yaml linenums="1"
site_name: Python Starting Project
site_description: A modern Python project template with best practices
site_author: Your Name
site_url: https://example.com/

theme:
  name: material  # (1)
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.indexes
    - navigation.top
    - search.highlight
    - search.share
    - content.code.copy  # (2)

plugins:
  - search
  - mkdocstrings:  # (3)
      handlers:
        python:
          options:
            show_source: true

markdown_extensions:  # (4)
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.inlinehilite
  - pymdownx.tabbed
  - pymdownx.critic
  - admonition
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - Overview: overview.md
  - Development:
      - Workflow: development/workflow.md
      - Pre-commit Hooks: development/pre-commit-hooks.md
  - Technologies:
      - Package Management:
          - UV: technologies/package-management/uv.md
      - Code Quality:
          - Ruff: technologies/code-quality/ruff.md
  - API Reference: api/
```

1. Material theme provides a modern, responsive design
2. Adds copy buttons to all code blocks
3. MkDocstrings plugin generates API documentation from docstrings
4. Markdown extensions enhance the basic Markdown syntax

## Basic Usage

### Project Structure

A typical MkDocs project structure:

```text linenums="1"
my-project/
├── docs/
│   ├── index.md
│   └── getting-started.md
└── mkdocs.yml
```

### Running the Documentation Server

To preview the documentation locally:

=== "Using poe tasks"

\`\`\`bash linenums="1"
\# Start the development server
uv run poe docs-serve

````
# Build the static site
uv run poe docs-build

# Deploy to GitHub Pages
uv run poe docs-deploy
```
````

=== "Using direct commands"

\`\`\`bash linenums="1"
\# Start the development server
uv run mkdocs serve

````
# Build the static site
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy
```
````

## Creating Documentation

### Basic Markdown

MkDocs uses standard Markdown syntax:

```markdown linenums="1"
# Page Title

## Section

This is a paragraph with **bold** and *italic* text.

- List item 1
- List item 2

1. Numbered item 1
2. Numbered item 2

[Link text](https://example.com)

![Image alt text](image.png)
```

### Code Blocks

=== "Basic Code Block"

```` markdown linenums="1"     ```python     def hello_world():         print("Hello, world!")     ```      ````

=== "With Line Numbers"

```` markdown linenums="1"     ```python linenums="1"     def hello_world():         print("Hello, world!")     ```      ````

=== "With Annotations"

\`\`\`\`markdown linenums="1"
`python     def hello_world():  # (1)         print("Hello, world!")  # (2)     `

`````
1. Function definition
2. Print statement that outputs "Hello, world!"
````
`````

### Admonitions

```markdown linenums="1"
!!! note "Custom Title"
    This is a note admonition with a custom title.

!!! warning
    This is a warning admonition.

!!! tip
    This is a tip admonition.
```

## Best Practices

1. **Organize documentation logically**: Structure your documentation in a way that makes sense for users.
2. **Keep documentation up-to-date**: Update documentation when code changes.
3. **Use descriptive page titles**: Make it easy for users to find what they're looking for.
4. **Include examples**: Provide code examples and use cases.
5. **Use admonitions for important information**: Highlight warnings, notes, and tips.
6. **Add screenshots when helpful**: Visual aids can improve understanding.
7. **Maintain a consistent style**: Use a consistent writing style throughout.
8. **Link related content**: Cross-reference related documentation.
9. **Test documentation**: Ensure code examples work and instructions are accurate.
10. **Get feedback**: Ask users for feedback on documentation clarity.

## Advanced Features

### Custom Themes

Create a custom theme:

```text linenums="1"
mkdocs/
├── custom_theme/
│   ├── main.html
│   └── css/
│       └── style.css
```

Configure in `mkdocs.yml`:

```yaml linenums="1"
theme:
  name:
  custom_dir: mkdocs/custom_theme/
```

### Plugins

Add plugins to extend functionality:

```yaml linenums="1"
plugins:
  - search
  - minify:  # (1)
      minify_html: true
  - git-revision-date-localized:  # (2)
      type: date
```

1. Minifies HTML output for faster loading
2. Adds last updated dates to pages based on git history

## Troubleshooting

### Common Issues

#### Navigation Not Updating

If navigation isn't updating:

1. Check the `nav` section in `mkdocs.yml`
2. Ensure file paths are correct
3. Restart the development server

#### Build Errors

If you encounter build errors:

1. Check for syntax errors in Markdown files
2. Verify that all linked files exist
3. Check for configuration errors in `mkdocs.yml`

#### Search Not Working

If search isn't working:

1. Ensure the search plugin is enabled
2. Rebuild the documentation
3. Check for JavaScript errors in the browser console

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [MkDocs Plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins)
- [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
