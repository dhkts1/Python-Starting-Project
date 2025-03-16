# Simplified Workflow

This project is designed to have a minimal learning curve. You only need to know **4 commands** for the entire development cycle.

## Complete Workflow Example

```bash
# Initial setup (only once)
uv sync
uv run pre-commit install

# Development cycle (repeat as needed)
poe pre

# Commit your changes
git add .
git commit -m "Your message"
git push
```

## What Happens Behind the Scenes

When you run `git commit`, the pre-commit hooks automatically:

1. **Format your code** using Ruff
2. **Lint your code** to check for errors and style issues
3. **Check types** using Pyright
4. **Detect security issues** using Bandit
5. **Find dead code** using Vulture
6. **Verify docstring coverage** using Interrogate
7. **Measure code complexity** using Radon and Xenon

If any of these checks fail, the commit is aborted, and you'll see error messages explaining what needs to be fixed.

## Benefits of This Workflow

- **Minimal learning curve** - just 4 commands to remember
- **Consistent code quality** - automated checks ensure high standards
- **Fast feedback loop** - issues are caught before they're committed
- **Reduced review cycles** - fewer issues to fix during code review
- **Better collaboration** - everyone follows the same standards

## Troubleshooting

### Pre-commit Hooks Failing

If your commit fails due to pre-commit hooks:

1. Read the error messages to understand what failed
2. Fix the issues in your code
3. Run `git add .` to stage the fixes
4. Try committing again with `git commit -m "Your message"`

### Skipping Pre-commit Hooks (Not Recommended)

In rare cases, you might need to bypass the pre-commit hooks:

```bash
git commit -m "Your message" --no-verify
```

**Warning:** This should only be used in exceptional circumstances, as it bypasses all quality checks.

### Updating Pre-commit Hooks

To update your pre-commit hooks to the latest versions:

```bash
uv run pre-commit autoupdate
```

## Next Steps

For more detailed information about the pre-commit hooks and what they check for, see [Pre-commit Hooks](pre-commit-hooks.md).
