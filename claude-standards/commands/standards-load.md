# Load Claude Development Standards

Install Claude development standards to the project by creating a `.claude/CLAUDE.md` file. This is a one-time setup that persists across all sessions for the current project.

## Usage

```bash
/standards-load [options]
```

## Options

### Standard Types
- `--all`: Install all standard modules (default)
- `--language`: Install only language expression standards
- `--principles`: Install only core work principles
- `--socratic`: Install only Socratic dialogue standards
- `--analysis`: Install only technical analysis framework

### Application Scenarios
- `--code-review`: Code review scenario optimized configuration
- `--architecture`: Architecture design scenario optimized configuration
- `--planning`: Technical planning scenario optimized configuration
- `--debugging`: Problem debugging scenario optimized configuration

### Configuration Options
- `--interactive`: Interactive selection of standard configuration
- `--force`: Force overwrite existing CLAUDE.md file
- `--dry-run`: Preview standards to be installed without actually applying

## Examples

```bash
# Install all standards (recommended)
/standards-load

# Install standards specifically for code review scenario
/standards-load --code-review

# Interactive selection of standards
/standards-load --interactive

# Install only language and technical analysis standards
/standards-load --language --analysis

# Force overwrite existing configuration
/standards-load --force
```

## Features

### One-Time Installation
- Creates `.claude/CLAUDE.md` in your project root
- Standards persist across all sessions
- No need to reload standards for each new session

### Modular Selection
- Choose which standard modules to install
- Scenario-specific configurations available
- Interactive selection for custom combinations

### File Management
- Automatically creates `.claude` directory if needed
- Overwrites existing CLAUDE.md when using `--force`
- Preserves existing configuration without `--force`

## Output Format

### Successful Installation
```
✅ Claude development standards installed successfully
✅ Development standards written to: /path/to/project/.claude/CLAUDE.md

📋 Installed standard modules:
├── Language Expression Standards (中文交流，直接犀利风格)
├── Core Work Principles (质量导向，架构感知)
├── Socratic Dialogue (深度质疑，智能激活)
└── Technical Analysis Framework (系统性分析框架)

⚙️ Configuration details:
- Primary language: 中文
- Expression style: 直接、零废话
- Quality gates: 严格模式
- Dialogue mode: 智能激活

💡 Usage tips:
- Standards are now persistent across all sessions
- Use '为什么'等关键词触发深度讨论
- Code reviews will automatically apply quality gate checks
- Technical analysis will use systematic framework
```

### Interactive Selection
```
🎯 请选择要安装的规范模块:

1. language-standards - 中文交流，直接犀利风格
2. work-principles - 质量导向，架构感知
3. socratic-dialogue - 深度质疑，智能激活
4. technical-analysis - 系统性分析框架

请输入数字选择 (多选用逗号分隔，或选择0安装全部):
```

## Important Notes

- **One-time setup**: This command only needs to be run once per project
- **File location**: Standards are installed to `.claude/CLAUDE.md` in your project root
- **Overwrite protection**: Existing files are not overwritten unless `--force` is used
- **Session persistence**: Once installed, standards automatically apply to all future sessions
- **Project-specific**: Each project can have its own standards configuration