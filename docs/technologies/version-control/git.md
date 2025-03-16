# Git - Distributed Version Control System

Git is a distributed version control system that tracks changes in source code during software development, enabling collaboration among multiple developers.

## Overview

Git helps manage code changes by:

- Tracking file changes over time
- Supporting branching and merging
- Enabling distributed development
- Providing a complete history of changes
- Facilitating collaboration among team members
- Supporting workflows for code review and quality control
- Integrating with CI/CD pipelines and other development tools

## Installation

Git is a core tool that should be installed globally on your system:

```bash
# macOS (using Homebrew)
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Windows
# Download from https://git-scm.com/download/win
```

Verify your installation:

```bash
git --version
```

## How It's Used in This Project

In this project, Git is used to:

1. Track changes to source code and documentation
1. Manage feature development through branches
1. Facilitate code reviews through pull requests
1. Integrate with pre-commit hooks for quality control
1. Support the CI/CD pipeline
1. Maintain a complete history of project development

## Configuration in This Project

Git is configured with standard settings and integrates with pre-commit hooks:

```bash
# View current configuration
git config --list

# Set up user information (if not already configured)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Basic Usage

### Common Git Commands

```bash
# Initialize a repository
git init

# Clone a repository
git clone https://github.com/username/repository.git

# Check status
git status

# Stage changes
git add filename
git add .  # Stage all changes

# Commit changes
git commit -m "Descriptive commit message"

# Push changes to remote
git push origin branch-name

# Pull changes from remote
git pull origin branch-name
```

### Branching and Merging

```bash
# Create a new branch
git branch feature-branch

# Switch to a branch
git checkout feature-branch

# Create and switch to a new branch
git checkout -b feature-branch

# Merge a branch
git checkout main
git merge feature-branch

# Delete a branch
git branch -d feature-branch
```

## Examples

### Typical Workflow

```bash
# Start a new feature
git checkout -b new-feature

# Make changes and commit them
git add .
git commit -m "feat: add new feature"

# Push the branch to remote
git push origin new-feature

# Create a pull request (via GitHub/GitLab/etc.)

# After review and approval, merge the pull request

# Update local main branch
git checkout main
git pull origin main

# Delete the feature branch
git branch -d new-feature
```

### Working with Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Make changes
# ...

# Stage changes
git add .

# Commit (pre-commit hooks will run automatically)
git commit -m "feat: add new feature"

# If hooks fail, fix issues and try again
git add .
git commit -m "feat: add new feature"
```

## Git Workflow in This Project

This project follows a feature branch workflow:

1. **Main Branch**: The `main` branch contains stable, production-ready code
1. **Feature Branches**: New features are developed in dedicated branches
1. **Pull Requests**: Changes are reviewed through pull requests
1. **Merge Strategy**: Feature branches are merged into `main` after review
1. **Commit Messages**: Follows the Conventional Commits specification

## Best Practices

1. **Write meaningful commit messages**: Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
1. **Keep commits focused**: Each commit should represent a single logical change.
1. **Pull before pushing**: Always pull the latest changes before pushing to avoid conflicts.
1. **Use branches for features**: Develop new features in dedicated branches.
1. **Review code before merging**: Use pull requests for code review.
1. **Don't commit sensitive information**: Keep secrets, credentials, and personal data out of the repository.
1. **Use .gitignore**: Properly configure `.gitignore` to exclude unnecessary files.

## Common Git Patterns

### Feature Branch Workflow

1. Create a feature branch from `main`
1. Develop the feature in the branch
1. Create a pull request for review
1. Merge the feature branch into `main` after approval

### Gitflow Workflow

1. `main` branch for production releases
1. `develop` branch for development
1. Feature branches for new features
1. Release branches for preparing releases
1. Hotfix branches for urgent fixes

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
