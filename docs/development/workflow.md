# Development Workflow

This document outlines the recommended development workflow for contributing to this project. Following these guidelines ensures consistency and quality across the codebase.

## Overview

Our development workflow is designed to:

- Maintain high code quality
- Ensure consistent code style
- Prevent bugs and issues before they reach production
- Streamline the development process
- Facilitate collaboration between team members

## Setup

Before you begin development, ensure you have:

1. Forked and cloned the repository
1. Set up your development environment as described in [Getting Started](../getting-started.md)
1. Installed pre-commit hooks with `uv run pre-commit install`
1. Familiarized yourself with the [project structure](../getting-started.md)

## Development Workflow

When making changes:

1. Follow the project's code style guidelines
1. Write tests for new functionality
1. Update documentation as needed
1. Keep commits small and focused
1. Use meaningful commit messages

### 3. Run Tests Locally

Before submitting your changes, run tests locally:

```bash linenums="1"
# Run all tests
poe pre
```

## Continuous Integration

Our CI pipeline automatically:

1. Runs tests on all PRs
1. Checks code quality
1. Verifies documentation builds
1. Ensures all pre-commit hooks pass

## Release Process

Releases are managed by maintainers and follow these steps:

1. Version bump according to [Semantic Versioning](https://semver.org/)
1. Changelog update
1. Tag creation
1. Release build and deployment

## Best Practices

### Code Quality

- Write clean, readable code
- Follow the principle of least surprise
- Keep functions small and focused
- Use meaningful variable and function names
- Add comments for complex logic

### Testing

- Write tests for all new features
- Maintain high test coverage
- Test edge cases
- Use parameterized tests for similar test cases
- Mock external dependencies

### Documentation

- Update documentation for API changes
- Add examples for new features
- Keep README and other docs up to date
- Document complex algorithms and decisions

### Git Practices

- Keep commits atomic and focused
- Write descriptive commit messages
- Rebase feature branches on main regularly
- Squash commits before merging if needed

## Troubleshooting

### Pre-commit Hooks Failing

If pre-commit hooks fail:

1. Read the error message carefully
1. Fix the issues locally
1. Stage the changes
1. Try committing again

If you need to bypass hooks temporarily:

```bash linenums="1"
git commit -m "your message" --no-verify  # (1)
```

1. This bypasses pre-commit hooks, but should only be used in exceptional cases

### Merge Conflicts

When encountering merge conflicts:

```bash linenums="1"
git checkout main  # (1)
git pull  # (2)
git checkout your-branch  # (3)
git rebase main  # (4)
# Resolve conflicts
git add .  # (5)
git rebase --continue  # (6)
git push --force-with-lease origin your-branch  # (7)
```

1. Switch to the main branch
1. Pull the latest changes
1. Switch back to your feature branch
1. Rebase your branch on main
1. Stage resolved conflicts
1. Continue the rebase process
1. Force push with lease for safety

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
