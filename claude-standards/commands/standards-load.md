# Load Claude Development Standards

Install Claude development standards to user-level `~/.claude/CLAUDE.md`. This setup applies globally to all projects and persists across all sessions.

## Usage

```bash
/standards-load [options]
```

## Installation Location

**User-level**: `~/.claude/CLAUDE.md` (Global - applies to ALL projects)

This is different from project-level `.claude/CLAUDE.md` which only affects a single project. User-level configuration provides a baseline for all your projects.

## Options

### Basic Options
- `--force`, `-f`: Force overwrite existing CLAUDE.md file
- `--merge`, `-m`: Merge with existing CLAUDE.md (preserves original content)
- `--backup`, `-b`: Backup before overwrite (saves to `.backup_TIMESTAMP`)
- `--dry-run`, `-d`: Preview what will happen without making changes
- `--uninstall`, `-u`: Remove Claude Standards Plugin content

### Advanced Options
- `--restore-backup <file>`: Restore from a specific backup file
- `--plugin-root <path>`: Specify plugin root directory (auto-detected by default)

## Interactive Mode

If `~/.claude/CLAUDE.md` already exists and no options are specified, you'll be prompted to choose:

```
⚠️  ~/.claude/CLAUDE.md 已存在
📄 当前文件大小: 1234 字符

请选择处理方式:
  [O] Overwrite - 直接覆盖（丢失原有内容）
  [M] Merge - 合并（保留原有内容，追加plugin标准）
  [B] Backup - 备份后覆盖（保存原文件到 .backup）
  [C] Cancel - 取消操作

选择 [O/M/B/C]:
```

## Examples

```bash
# Install (interactive if file exists)
/standards-load

# Force overwrite without prompting
/standards-load --force

# Merge with existing content
/standards-load --merge

# Backup before overwriting
/standards-load --backup

# Preview what will happen
/standards-load --dry-run

# Uninstall the plugin content
/standards-load --uninstall

# Restore from a specific backup
/standards-load --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## What Happens

### New Installation (file doesn't exist)
```
✅ 开发规范已创建: /home/user/.claude/CLAUDE.md
💡 全局生效 - 所有项目的session都会自动应用这些标准
```

### Merge Strategy
- Preserves your existing content
- Adds a separator: `<!-- Claude Standards Plugin - DO NOT EDIT BELOW THIS LINE -->`
- Appends plugin standards below the separator
- Subsequent merges will update plugin content without duplicating

### Backup Strategy
```
📦 已备份到: /home/user/.claude/CLAUDE.md.backup_20250104_153022
✅ 开发规范已备份并覆盖: /home/user/.claude/CLAUDE.md
💡 全局生效 - 所有项目的session都会自动应用这些标准
```

## Uninstalling

```bash
# Remove plugin content (preserves original content if merged)
/standards-load --uninstall

# Restore from backup
/standards-load --uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## Important Notes

- **Global scope**: Affects ALL projects, not just the current one
- **Session persistence**: Standards apply automatically to all future sessions
- **Priority**: Project-level `.claude/CLAUDE.md` takes precedence over user-level
- **Safe merging**: Multiple installs with `--merge` won't duplicate content
- **Backup naming**: Backups include timestamp for easy identification
- **One-time setup**: Run once to apply globally, no need to run per project

## File Structure After Merge

```markdown
# Your existing CLAUDE.md content
...

---
<!-- Claude Standards Plugin - DO NOT EDIT BELOW THIS LINE -->

# CLAUDE.md
Claude Code 个人配置文件
...
```

The separator makes it easy to identify and remove plugin content later.