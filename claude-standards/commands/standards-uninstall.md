# Uninstall Claude Development Standards

Remove Claude Standards Plugin content from user-level `~/.claude/CLAUDE.md`. This command safely removes plugin-added content while preserving your original configuration.

## Usage

```bash
/standards-uninstall [options]
```

## Options

- `--restore-backup <file>`: Restore from a specific backup file instead of just removing plugin content

## Examples

```bash
# Remove plugin content (preserves original content if merged)
/standards-uninstall

# Restore from a specific backup
/standards-uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_120000
```

## What Happens

### If Content Was Merged
```
✅ 已移除Claude Standards Plugin内容
ℹ️  原有内容已保留
```

The plugin content (everything after the `<!-- Claude Standards Plugin -->` separator) is removed, and your original content is preserved.

### If Only Plugin Content Existed
```
✅ 已删除 /home/user/.claude/CLAUDE.md
```

The entire file is removed since it only contained plugin content.

### If No Plugin Content Found
```
ℹ️  未检测到Claude Standards Plugin内容
```

The file exists but doesn't contain plugin-added content. No changes are made.

### If File Doesn't Exist
```
ℹ️  ~/.claude/CLAUDE.md 不存在，无需卸载
```

Nothing to uninstall.

## Restoring from Backup

If you created a backup during installation (using `--backup` option), you can restore it:

```bash
# List available backups
ls ~/.claude/CLAUDE.md.backup_*

# Restore a specific backup
/standards-uninstall --restore-backup ~/.claude/CLAUDE.md.backup_20250104_153022
```

Output:
```
✅ 已从备份恢复: /home/user/.claude/CLAUDE.md.backup_20250104_153022
```

## Important Notes

- **Safe operation**: Only removes content added by Claude Standards Plugin
- **Preserves original**: Your original CLAUDE.md content is kept intact (if merged)
- **Separator detection**: Uses `<!-- Claude Standards Plugin -->` separator to identify plugin content
- **Backup recommended**: Always create a backup before uninstalling if you're unsure
- **Global scope**: Affects user-level configuration (all projects)

## Alternative Method

You can also use the install command with `--uninstall` flag:

```bash
/standards-load --uninstall
```

Both commands do the same thing - this dedicated uninstall command is provided for clarity.

## Re-installing

After uninstalling, you can re-install at any time:

```bash
/standards-load
```

Or with a different strategy:

```bash
/standards-load --merge  # Merge with any remaining content
```