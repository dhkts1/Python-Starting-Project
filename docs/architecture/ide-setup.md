# IDE Setup

This project is optimized for development with [Visual Studio Code](https://code.visualstudio.com/), providing a powerful and flexible environment for Python development. Cursor is built on VSCode but adds AI-powered features that can enhance productivity.

## Editor Configuration

The project includes pre-configured settings that work with both VSCode and Cursor:

### 1. Code Quality Tools Integration

The `.vscode/settings.json` file configures the editor to work seamlessly with the project's code quality tools:

```json
{
  "editor.formatOnSave": true,
  "python.analysis.typeCheckingMode": "strict",
  "files.exclude": {
    "**/.git": true,
    "**/node_modules": true,
    "**/.ruff_cache": true,
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/.venv": true,
    "**/dist": true,
    "**/.history": true,
    "**/*.pyi": true,
    "**/coverage.xml": true,
    "**/.coverage": true
  },
  "ruff.enable": true,
  "ruff.organizeImports": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.ruff": "explicit",
    "source.organizeImports.ruff": "explicit"
  },
  "python.testing.pytestEnabled": true,
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.autoImportCompletions": true
}
```

These settings provide:

- Automatic formatting on save
- Strict type checking
- File exclusion patterns for cleaner workspace
- Ruff linting and formatting configuration
- Pytest integration
- Visual guide for line length

### 2. Recommended Extensions

The `.vscode/extensions.json` file recommends several extensions that enhance the development experience:

```json
{
  "recommendations": [
    "njpwerner.autodocstring",
    "usernamehw.errorlens",
    "tamasfe.even-better-toml",
    "visualstudioexptteam.vscodeintellicode",
    "visualstudioexptteam.intellicode-api-usage-examples",
    "yzhang.markdown-all-in-one",
    "bierner.markdown-mermaid",
    "ms-python.vscode-pylance",
    "ninoseki.vscode-pylens",
    "ms-python.python",
    "ms-python.debugpy",
    "kevinrose.vsc-python-indent",
    "mgesbert.python-path",
    "charliermarsh.ruff",
    "redhat.vscode-yaml",
    "eamodio.gitlens",
    "anysphere.pyright"
  ]
}
```

### 3. Debugging Configuration

The `.vscode/launch.json` file provides a pre-configured debugging setup for the application:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Main",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/main.py",
      "envFile": "${workspaceFolder}/.env",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  ]
}
```

This configuration allows you to:

- Debug the main application with F5
- Load environment variables from .env file
- Use the integrated terminal for input/output
- Set the Python path to include the project root

## VSCode Setup

### Getting Started with VSCode

1. Install [Visual Studio Code](https://code.visualstudio.com/)
1. Open the project folder in VSCode
1. When prompted, install the recommended extensions
1. VSCode will automatically use the project's settings

### Key VSCode Features

- **Integrated Terminal**: Run commands directly from the editor
- **Debugging**: Set breakpoints and step through code
- **Extensions**: Customize your environment with extensions

### Source Control with VSCode

VSCode's built-in source control features make it easy to track changes, review code, and manage your Git repository. This is especially valuable when working with AI-generated code changes, as it provides a clear view of what has been modified.

#### Accessing Source Control

The Source Control view can be accessed by:

- Clicking the Source Control icon in the Activity Bar (looks like a branch)
- Using the keyboard shortcut `Ctrl+Shift+G` (Windows/Linux) or `Cmd+Shift+G` (Mac)

#### Key Source Control Features

1. **Changes View**:

   - Shows all modified, added, and deleted files
   - Provides a clear overview of what has changed in your project
   - Allows you to stage individual files or all changes at once

1. **Diff Viewer**:

   - Click on any modified file to see a side-by-side comparison
   - Clearly highlights what has been added, changed, or removed
   - Makes reviewing AI-generated code changes much easier
   - Allows you to accept or reject changes at a granular level

1. **Commit Management**:

   - Write commit messages and commit changes directly from the editor
   - View commit history and browse previous versions
   - Create and switch between branches

1. **Integration with GitHub**:

   - Push and pull changes to/from remote repositories
   - Create and review pull requests
   - Manage issues

#### Best Practices for Source Control

- **Review Changes Frequently**: Get in the habit of checking the Source Control panel after making changes or running AI tools
- **Use Meaningful Commit Messages**: Write clear, descriptive commit messages that explain what changed and why
- **Commit Small, Related Changes**: Make small, focused commits rather than large, sweeping changes
- **Review Diffs Before Committing**: Always review the diff view before committing to ensure you understand all changes

#### Using Source Control with AI-Generated Code

When working with AI-generated code:

1. After the AI makes changes, open the Source Control panel to see all modified files
1. Click on each file to review the changes in the diff viewer
1. Verify that the changes match your expectations and make any necessary adjustments
1. Stage and commit the changes with a descriptive message

This workflow ensures you maintain full control over your codebase while benefiting from AI assistance.

## Common Features

The project is configured to provide:

### Automatic Formatting

The project is configured to automatically format code on save using Ruff, ensuring consistent code style throughout the project.

### Type Checking

Pyright is configured for strict type checking, helping to catch type-related errors early in the development process.

### Linting

Ruff is configured to lint the code, identifying potential issues and enforcing coding standards.

### Debugging

The project includes a launch configuration for debugging Python code, making it easy to set breakpoints and step through code.

### Code-Aware Documentation

This project uses MkDocs with several extensions that make documentation code-aware, providing rich features for displaying and interacting with code:

#### 1. Syntax Highlighting

Code blocks are automatically syntax-highlighted using Pygments, supporting a wide range of programming languages:

```python
def main() -> None:
    """Entry point for the application."""
    # Initialize logging
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("Starting %s v%s", settings.APP_NAME, settings.APP_VERSION)
    logger.debug("Debug mode is %s", "enabled" if settings.DEBUG else "disabled")

    # Application logic goes here
    logger.info("Application finished")
    logger.debug("Debug mode is %s", "enabled" if settings.DEBUG else "disabled")
```

#### 2. Code Annotations

You can add annotations to your code blocks to explain specific parts:

```python
class Settings(BaseSettings):  # (1)!
    """Application settings."""

    APP_NAME: str = Field(  # (2)!
        default="Python Starting Project",
        description="The name of the application.",
    )
    APP_VERSION: str = Field(
        default="0.1.0",
        description="The version of the application.",
    )
    DEBUG: bool = Field(
        default=False,
        description="Enable or disable debug mode.",
    )
    LOG_LEVEL: str = Field(  # (3)!
        default="INFO",
        description="The logging level.",
    )
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="The log message format.",
    )
    LOG_FILE: str = Field(
        default="logs/app.log",
        description="Path to the log file.",
    )

    # Paths
    BASE_DIR: Path = Field(
        default_factory=lambda: Path(__file__),
        description="Base directory of the application.",
    )
    LOG_DIR: Path = Field(  # (4)!
        default_factory=lambda: Path("logs"),
        description="Directory for log files.",
    )

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")  # (5)!
```

1. Uses Pydantic's BaseSettings for environment variable loading and validation
1. Default application name that can be overridden via environment variables
1. Default log level is INFO, can be changed to DEBUG for more verbose logging
1. Uses a factory function to create the logs directory path
1. Configuration for loading settings from .env file with UTF-8 encoding

#### 3. Advanced Code Block Features

The documentation supports several advanced code block features:

- **Copy Button**: Each code block has a copy button for easy copying
- **Line Numbers**: Add line numbers to code blocks for reference
- **Line Highlighting**: Highlight specific lines to draw attention
- **Code Block Titles**: Add titles to code blocks for context
- **External File Embedding**: Include code from external files

Example with line numbers and highlighting:

```python linenums="1" hl_lines="3 4 5"
def setup_logging() -> None:
    """Set up logging configuration."""
    # Create log directory if it doesn't exist
    log_file = Path(settings.LOG_FILE)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)

    # Clear existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create formatter
    formatter = logging.Formatter(settings.LOG_FORMAT)
```

#### 4. API Documentation with mkdocstrings

The project uses mkdocstrings to automatically generate API documentation from Python docstrings. Here's how it's used in our API documentation:

```markdown
### Utils

::: src.utils.settings
    options:
      show_root_heading: true
      show_source: true

::: src.utils.logging
    options:
      show_root_heading: true
      show_source: true
```

This renders the complete documentation for the settings and logging modules, including all functions, classes, and their docstrings.

## Custom Tasks

The project includes several custom tasks that can be run from either editor:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
1. Type "Tasks: Run Task"
1. Select one of the available tasks:
   - Run Tests
   - Build Documentation
   - Lint Code
   - Format Code

## Keyboard Shortcuts

Here are some useful keyboard shortcuts for working with Python in both editors:

- `F5`: Start debugging
- `Ctrl+Shift+B` or `Cmd+Shift+B`: Run build task
- `Ctrl+Shift+P` or `Cmd+Shift+P`: Open Command Palette
- `Ctrl+Space` or `Cmd+Space`: Trigger suggestions
- `F12`: Go to definition
- `Alt+F12` or `Option+F12`: Peek definition
- `Shift+F12`: Find all references

## Best Practices

### Using AI Features (Cursor)

1. **Use AI Suggestions Wisely**

   - Review AI-generated code for correctness
   - Understand suggested changes before applying
   - Use AI as a tool, not a replacement for understanding

1. **Documentation**

   - Let AI help generate initial documentation
   - Review and enhance AI-generated content
   - Keep documentation up-to-date with code changes

1. **Code Quality**

   - Use AI to maintain consistent code style
   - Leverage AI for complex refactoring
   - Run automated tests after AI-suggested changes

## Additional Resources

- [VSCode Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python in VSCode](https://code.visualstudio.com/docs/languages/python)
- [Debugging Python](https://code.visualstudio.com/docs/python/debugging)
- [Cursor Documentation](https://cursor.sh/docs)

## Model Context Protocol (MCP) Configuration

This project supports the Model Context Protocol (MCP), which enhances AI-assisted development by providing specialized tools for complex tasks. MCPs allow AI models to break down problems into steps, maintain context, and perform specialized operations.

### What is MCP?

Model Context Protocol (MCP) is a framework that enables AI models to:

- Process complex tasks through structured thinking
- Maintain context across multiple steps
- Access specialized tools and capabilities
- Provide more accurate and reliable results

### MCP Configuration

The project includes MCP configuration in the `.cursor/mcp.json` file:

```json
{
    "mcpServers": {
        "sequential-thinking": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-sequential-thinking"
            ]
        },
        "fetch": {
            "command": "uvx",
            "args": [
                "mcp-server-fetch"
            ]
        }
    }
}
```

This configuration enables two MCP servers:

1. **sequential-thinking**: Helps break down complex problems into manageable steps
1. **fetch**: Allows the AI to retrieve information from the internet

### Using MCPs

When working with AI tools that support MCP:

1. The AI will automatically use the appropriate MCP when needed
1. For long-running operations or multi-step processes, you may see the AI thinking through steps
1. When the AI is using an MCP and needs your input to continue, simply respond with "continue"
1. For fetch operations, the AI may retrieve information from the internet to provide more accurate responses

### Global MCP Rules

You can define global MCP rules using the `@global.mdc` directive in your prompts. This allows you to:

- Specify how the AI should approach problems
- Define constraints or requirements for the AI's responses
- Set preferences for how MCPs should be used

For example:

```
@global.mdc Use sequential thinking for complex problems and fetch for retrieving up-to-date information
```

### Enabling MCPs

To ensure MCPs are enabled:

1. Make sure the `.cursor/mcp.json` file exists in your project
1. Install the required dependencies:
   ```bash
   npm install -g @modelcontextprotocol/server-sequential-thinking
   pip install mcp-server-fetch
   ```
1. When working with AI tools, verify they have access to the MCP configuration

## AI-Enhanced Development with Cursor

For developers interested in AI-assisted development, [Cursor](https://cursor.sh) provides an enhanced coding experience built on top of VSCode.

### Getting Started with Cursor

1. Install [Cursor](https://cursor.sh)
1. Open the project folder in Cursor:
   ```bash
   cursor .
   ```
1. Cursor will automatically use the same settings and extensions as VSCode
1. Let Cursor's AI agent analyze your codebase

### AI-Assisted Development Features

Cursor provides several AI-powered features that significantly improve the development experience:

#### 1. Real-Time Code Quality Improvements

- **Automatic Error Detection and Fixing**: Cursor's AI agent identifies and suggests fixes for code issues in real-time
- **Smart Linting**: Beyond traditional linting, the AI understands context and suggests semantic improvements
- **Type Inference**: Assists with type annotations and catches type-related issues early

#### 2. Code Generation and Completion

- **Contextual Code Generation**: Suggests complete functions and classes based on your codebase
- **Intelligent Autocomplete**: Provides context-aware code completions
- **Docstring Generation**: Automatically generates comprehensive docstrings

#### 3. Refactoring Assistance

- **Smart Refactoring**: Suggests code improvements and refactoring opportunities
- **Code Organization**: Helps maintain clean code structure
- **Import Management**: Automatically organizes and optimizes imports

### MCP Integration in Cursor

Cursor has built-in support for Model Context Protocol (MCP), making it particularly powerful for complex development tasks. When using Cursor:

1. The AI automatically leverages MCPs when appropriate
1. You can see the AI's thought process through sequential thinking
1. For long-running operations, simply type "continue" when prompted
1. The fetch MCP allows the AI to retrieve up-to-date information from the internet

This integration makes Cursor especially valuable for tackling complex development challenges and staying current with the latest programming practices.
