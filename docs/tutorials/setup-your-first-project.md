# Tutorial: Setting Up Your First Project

**Est. time to complete:** 20 minutes

## Overview

This tutorial guides you through the process of setting up a new Python project using this template. By the end, you'll have a fully configured development environment with best-practice tools for code quality, testing, and documentation.

## Prerequisites

- Python 3.11+ installed on your system
- Git installed on your system
- Basic command-line knowledge
- Either Visual Studio Code or Cursor (recommended) installed

## Step 1: Install UV Package Manager

Let's start by installing UV, a blazing-fast Python package manager written in Rust. It's much faster than pip and provides better dependency resolution.

### For MacOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### For Windows:

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, verify that UV is properly installed:

```bash
uv --version
```

You should see the UV version number displayed, indicating that UV is ready to use.

## Step 2: Create a Virtual Environment

Before getting the project code, let's set up a virtual environment to keep our dependencies isolated:

```bash
# Create a directory for your project
mkdir my-python-project
cd my-python-project

# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

You should now see the virtual environment name in your terminal prompt, showing that it's active.

## Step 3: Get the Repository

Now that we have our environment ready, let's get the project template:

1. Go to the Python Starting Project GitHub: https://github.com/dhkts1/Python-Starting-Project
2. Click the green "Use this template" button
3. Choose "Create a new repository"
4. Fill in your repository details and click "Create repository"
5. Clone your new repository into your project directory:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git .
    ```

The dot at the end of the clone command ensures that the repository is cloned into your current directory.

## Step 4: Install Dependencies

With our repository set up and virtual environment active, we can now install all the project dependencies:

```bash
# Install all dependencies (including development tools)
uv sync
```

This command installs:

- All production dependencies
- Development tools (linters, formatters, testing tools)
- Documentation tools

You'll see a progress bar and eventually a success message when all packages are installed.

## Step 5: Set Up Pre-commit Hooks

Next, let's set up pre-commit hooks which will automatically check your code quality before each commit:

```bash
# Install pre-commit hooks
pre-commit install
```

These hooks are configured in the `.pre-commit-config.yaml` file and help maintain code quality by running checks before each commit.

## Step 6: Verify Your Setup

Let's make sure everything is working correctly by running the pre-commit checks manually:

```bash
# Run all pre-commit hooks
poe pre
```

You should see a series of checks running, all of which should pass. This confirms that your setup is working correctly and all tools are properly configured.

## Step 7: Open in Your IDE

Now that our project is set up, let's open it in an IDE for easier editing:

### For Visual Studio Code:

```bash
code .
```

### For Cursor:

```bash
cursor .
```

When you first open the project, your IDE should recommend installing some extensions. Install these for the best development experience, as they enhance code editing with features like syntax highlighting, code completion, and linting.

## Step 8: Run the Sample Application

The template includes a sample application you can run to verify everything works correctly:

```bash
# Run the main script
python -m src.main
```

You can also use the Run and Debug button in VSCode/Cursor to run the application. There's a pre-configured `launch.json` file in the `.vscode` folder that makes this process seamless.

You should see some log output, confirming that the application is working correctly.

## Step 9: Make Your First Change

Now that everything is running smoothly, let's make our first change to the project:

1. Open `src/main.py`
2. Modify the log message in the main function
3. Save the file
4. Run the application again to see your changes:
    ```bash
    python -m src.main
    ```

You should see your modified log message in the output, confirming that your changes were applied successfully.

## Step 10: Commit Your Changes

Finally, let's save our changes to the repository:

```bash
# Stage your changes
git add src/main.py
# You can also use "git add ." to stage all changes
# Or use "git status" to see what files were changed
```

If there are errors in the output or files were automatically formatted, you'll need to run `git add` again to stage the updated files.

Then, commit your changes:

```bash
# Commit your changes
git commit -m "Update log message in main function"
```

Notice how the pre-commit hooks run automatically before the commit is created. These checks ensure your code meets the project's quality standards.

## Troubleshooting

### Common Issues

**Problem**: Missing dependencies when running commands
**Solution**: Run `uv sync` again to ensure all dependencies are installed

**Problem**: Pre-commit hooks failing
**Solution**: Read the error messages carefully. Most issues can be fixed by running `poe lint` to lint format and fix errors.
**Problem**: IDE not showing proper code intelligence
**Solution**: Make sure you've installed the recommended extensions and configured your IDE to use the project's virtual environment.

## Next Steps

Congratulations on setting up your Python project! Here are some next steps you might want to take:

- Learn about the [code quality tools](../tools-guide/code-quality.md) to maintain high code standards
- Explore the [project structure](../architecture/configuration.md) to understand how everything fits together
- Check out the [development workflow](../development/workflow.md) for daily development practices
- Add your own code to the project and start building something amazing

## Check Your Understanding

1. What command installs all dependencies for the project?

    - `uv sync`

2. What command sets up pre-commit hooks?

    - `pre-commit install`

3. What command runs all pre-commit checks manually?

    - `poe pre`

4. What happens when you run `git commit` after setting up pre-commit hooks?

    - Pre-commit hooks run automatically to check code quality before creating the commit
