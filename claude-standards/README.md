# Claude Development Standards Plugin

[![Plugin Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/wqaetly/ai_agent_for_skill)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Category](https://img.shields.io/badge/category-Code%20Quality-orange.svg)](https://claude.ai)

A streamlined Claude Code plugin that installs unified development standards globally across all your projects.

## 🌟 What It Does

This plugin installs a comprehensive set of development standards to your user-level `~/.claude/CLAUDE.md` file, making them automatically available in **all** your Claude Code sessions across **all** projects.

### 📋 Included Standards

- **Language & Expression**: English-first communication, direct sharp style, zero fluff
- **Core Work Principles**: Context priority, quality-oriented, architecture awareness
- **Socratic Dialogue**: Smart activation for deep technical discussions
- **Technical Analysis**: Systematic data structure and architecture analysis framework

## 🚀 Quick Start

### Installation

1. **Clone or copy the plugin to your Claude Code plugins directory:**

```bash
# Option 1: Clone repository
git clone https://github.com/wqaetly/ai_agent_for_skill.git ~/.claude/plugins/claude-standards

# Option 2: Manual copy
cp -r claude-standards ~/.claude/plugins/
```

2. **Install standards (one-time setup):**

```bash
/standards-load
```

That's it! The standards are now active in all your projects.

## 📖 Usage

### Install Standards

```bash
# First-time installation (interactive if file exists)
/standards-load

# Force overwrite existing file
/standards-load --force

# Merge with existing content
/standards-load --merge

# Backup before overwriting
/standards-load --backup

# Preview without installing
/standards-load --dry-run
```

### Uninstall Standards

```bash
# Remove plugin content (preserves original content)
/standards-uninstall

# Restore from backup
/standards-uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## 🔧 How It Works

### User-Level Installation

The plugin installs to `~/.claude/CLAUDE.md` instead of project-level `.claude/CLAUDE.md`:

- **Global scope**: Standards apply to ALL projects automatically
- **Session persistence**: Once installed, works across all future sessions
- **No per-project setup**: Install once, use everywhere
- **Respects project configs**: Project-level CLAUDE.md still takes precedence if present

### File Handling Options

When `~/.claude/CLAUDE.md` already exists, you can:

1. **Overwrite**: Replace entire file (loses original content)
2. **Merge**: Append plugin standards, preserve original content
3. **Backup**: Save original to `.backup_TIMESTAMP`, then overwrite
4. **Cancel**: Abort installation

### Merge Strategy

When merging, the plugin adds a separator to mark its content:

```markdown
# Your existing CLAUDE.md content
...

---
<!-- Claude Standards Plugin - DO NOT EDIT BELOW THIS LINE -->

# CLAUDE.md
Claude Code Development Standards
...
```

This makes it easy to identify and remove plugin content later.

## 📋 Commands

### `/standards-load`

Install development standards to user-level CLAUDE.md.

**Options:**
- `-f, --force`: Force overwrite without prompting
- `-m, --merge`: Merge with existing content
- `-b, --backup`: Backup before overwriting
- `-d, --dry-run`: Preview without making changes
- `-u, --uninstall`: Remove plugin content
- `--restore-backup <file>`: Restore from specific backup

**Examples:**
```bash
/standards-load              # Interactive installation
/standards-load --merge      # Preserve existing content
/standards-load --backup     # Safe overwrite with backup
/standards-load --dry-run    # Preview first
```

### `/standards-uninstall`

Remove Claude Standards Plugin content from CLAUDE.md.

**Options:**
- `--restore-backup <file>`: Restore from specific backup

**Examples:**
```bash
/standards-uninstall                  # Remove plugin content
/standards-uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## 💡 Best Practices

### When to Use Merge

Use `--merge` if you:
- Have existing custom standards in `~/.claude/CLAUDE.md`
- Want to combine personal preferences with plugin standards
- Need to preserve existing configuration

### When to Use Backup

Use `--backup` if you:
- Want a safety net before overwriting
- Plan to experiment with plugin standards
- May need to roll back to previous configuration

### When to Force Overwrite

Use `--force` if you:
- Want only plugin standards (no custom additions)
- Are reinstalling after uninstallation
- Want to reset to plugin defaults

## 🔍 Troubleshooting

### Plugin not working

```bash
# Verify installation
cat ~/.claude/CLAUDE.md

# Reinstall
/standards-load --force
```

### Want to customize standards

```bash
# Option 1: Edit user-level file directly
vim ~/.claude/CLAUDE.md

# Option 2: Use merge strategy
/standards-load --merge
# Then edit ~/.claude/CLAUDE.md to modify plugin section
```

### Multiple backups

```bash
# List backups
ls -la ~/.claude/CLAUDE.md.backup_*

# Restore specific backup
/standards-uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## 📁 Plugin Structure

```
claude-standards/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── commands/
│   ├── standards-load.md        # Installation command
│   └── standards-uninstall.md   # Uninstallation command
├── hooks/
│   └── hooks.json               # (Empty - not used)
├── prompts/
│   └── prompts.md               # Complete standards content
├── scripts/
│   └── apply-standards.py       # Installation script
└── README.md                    # This file
```

## 🎯 Design Philosophy

This plugin follows a "simple is better" philosophy:

- **One-time setup**: Install once, use everywhere
- **No complexity**: No modules, scenarios, or configurations
- **Safe defaults**: Interactive prompts prevent data loss
- **Easy rollback**: Backup and uninstall support
- **Global consistency**: Same standards across all projects

## 🔄 Version History

### v2.0.0 (Current)
- **Simplified**: Removed complex module system
- **User-level**: Install to `~/.claude/CLAUDE.md` globally
- **Interactive**: Smart file handling with user prompts
- **Safe**: Backup and merge strategies
- **Clean**: Removed non-functional hooks

### v1.0.0
- Initial release with modular system
- Project-level installation
- Complex configuration options

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update documentation
5. Submit a pull request

### Development Setup

```bash
git clone https://github.com/wqaetly/ai_agent_for_skill.git
cd claude-standards

# Edit standards
vim prompts/prompts.md

# Test locally
cp -r . ~/.claude/plugins/claude-standards
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 📞 Contact

- **Project Homepage**: https://github.com/wqaetly/ai_agent_for_skill
- **Issues**: https://github.com/wqaetly/ai_agent_for_skill/issues
- **Email**: wqaetly@example.com

---

**Simple, Effective Development Standards for Claude Code** 🚀
