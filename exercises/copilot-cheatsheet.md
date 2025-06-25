# GitHub Copilot Cheatsheet - Advanced Features

*Quick reference for advanced Copilot features in VS Code*

## 🎯 Essential Context Variables

| Variable | Purpose | Example Use |
|----------|---------|-------------|
| `#codebase` | Project-wide understanding | `How is authentication handled? #codebase` |
| `#selection` | Current editor selection | `Optimize this function #selection` |
| `#problems` | Issues from Problems panel | `Fix these errors #problems` |
| `#changes` | Source control changes | `Generate commit message #changes` |
| `#terminalLastCommand` | Last terminal command | `Explain this error #terminalLastCommand` |
| `#testFailure` | Test failure details | `Why is this test failing? #testFailure` |
| `#usages` | Symbol references/definitions | `Find all uses of this function #usages` |

## 🚀 Powerful Slash Commands

| Command | Purpose | Best For |
|---------|---------|----------|
| `/tests` | Generate test suites | Creating comprehensive tests |
| `/docs` | Generate documentation | Adding docstrings and comments |
| `/fix` | Fix code issues | Debugging and error resolution |
| `/explain` | Explain code/concepts | Understanding complex logic |
| `/new` | Scaffold projects/files | Creating new components |
| `/setupTests` | Configure testing | Setting up test frameworks |
| `/fixTestFailure` | Debug failing tests | Test troubleshooting |

## 🎛️ Advanced Features

**Keyboard Shortcuts:**
- `⌘I` - Inline Chat in editor/terminal
- `⇧⌥⌘L` - Quick Chat
- `⌃⌘I` - Open Chat view
- `F2` - AI-powered symbol renaming

**Chat Participants:**
- `@workspace` - Project-wide operations
- `@terminal` - Shell command help
- `@vscode` - VS Code features help
- `@github` - GitHub integration

**Custom Instructions:**
- `.github/copilot-instructions.md` - Project-wide guidance
- Language-specific settings in VS Code
- Reusable `.prompt.md` files (experimental)

## 💡 Pro Tips

1. **Combine context**: `#codebase #problems #selection` for comprehensive understanding
2. **Be specific**: Include framework/library names in requests
3. **Use drag & drop**: Drop files/folders into chat for instant context
4. **Chain commands**: Use multiple slash commands in sequence
5. **Custom instructions**: Create project-specific guidance for consistency

## 🏴‍☠️ Analytics Project Specifics

**For FastAPI endpoints:**
```
/new FastAPI endpoint for data analysis with Pydantic models #codebase
```

**For data processing:**
```
/tests generate tests for pandas data processing functions #selection
```

**For debugging:**
```
/fix optimize this query performance #problems #selection
```

**For documentation:**
```
/docs add comprehensive docstrings #selection
```
