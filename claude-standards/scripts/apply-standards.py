#!/usr/bin/env python3
"""
Claude 开发规范安装脚本
将开发规范安装到用户级 ~/.claude/CLAUDE.md 文件，全局生效
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# 分隔标记，用于标识plugin添加的内容
PLUGIN_SEPARATOR = "\n\n---\n<!-- Claude Standards Plugin - DO NOT EDIT BELOW THIS LINE -->\n\n"

def get_user_claude_dir():
    """获取用户级.claude目录"""
    return Path.home() / ".claude"

def get_user_claude_md():
    """获取用户级CLAUDE.md文件路径"""
    return get_user_claude_dir() / "CLAUDE.md"

def backup_file(file_path: Path) -> Path:
    """备份文件，添加时间戳"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = file_path.parent / f"{file_path.name}.backup_{timestamp}"

    if file_path.exists():
        import shutil
        shutil.copy2(file_path, backup_path)
        print(f"📦 已备份到: {backup_path}")
        return backup_path
    return None

def merge_content(existing_content: str, plugin_content: str) -> str:
    """合并内容，避免重复添加"""
    # 检查是否已经包含plugin内容
    if PLUGIN_SEPARATOR.strip() in existing_content:
        # 已存在，替换旧内容
        parts = existing_content.split(PLUGIN_SEPARATOR)
        return parts[0].rstrip() + PLUGIN_SEPARATOR + plugin_content
    else:
        # 新添加
        return existing_content.rstrip() + PLUGIN_SEPARATOR + plugin_content

def install_standards(plugin_root: str,
                     force: bool = False,
                     merge: bool = False,
                     backup: bool = False,
                     dry_run: bool = False) -> bool:
    """安装开发规范到用户级目录"""

    # 获取源文件和目标文件路径
    prompts_md_file = Path(plugin_root) / "prompts" / "prompts.md"
    claude_dir = get_user_claude_dir()
    claude_md_file = get_user_claude_md()

    # 检查源文件是否存在
    if not prompts_md_file.exists():
        print(f"❌ 源文件不存在: {prompts_md_file}")
        return False

    # 读取plugin内容
    try:
        with open(prompts_md_file, 'r', encoding='utf-8') as f:
            plugin_content = f.read()
    except Exception as e:
        print(f"❌ 读取源文件失败: {e}")
        return False

    # 检查目标文件是否已存在
    existing_content = ""
    file_exists = claude_md_file.exists()

    if file_exists:
        try:
            with open(claude_md_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        except Exception as e:
            print(f"⚠️  读取现有文件失败: {e}")
            existing_content = ""

    # 决定处理策略
    strategy = None

    if not file_exists:
        strategy = 'create'
    elif force:
        strategy = 'overwrite'
    elif merge:
        strategy = 'merge'
    elif backup:
        strategy = 'backup'
    else:
        # 交互式选择
        print(f"⚠️  ~/.claude/CLAUDE.md 已存在")
        print(f"📄 当前文件大小: {len(existing_content)} 字符")
        print()
        print("请选择处理方式:")
        print("  [O] Overwrite - 直接覆盖（丢失原有内容）")
        print("  [M] Merge - 合并（保留原有内容，追加plugin标准）")
        print("  [B] Backup - 备份后覆盖（保存原文件到 .backup）")
        print("  [C] Cancel - 取消操作")
        print()

        while True:
            choice = input("选择 [O/M/B/C]: ").strip().upper()
            if choice == 'O':
                strategy = 'overwrite'
                break
            elif choice == 'M':
                strategy = 'merge'
                break
            elif choice == 'B':
                strategy = 'backup'
                break
            elif choice == 'C':
                print("❌ 操作已取消")
                return False
            else:
                print("⚠️  无效选择，请重新输入")

    # 根据策略生成最终内容
    if strategy == 'create':
        final_content = plugin_content
        action_msg = "创建"
    elif strategy == 'overwrite':
        final_content = plugin_content
        action_msg = "覆盖"
    elif strategy == 'merge':
        final_content = merge_content(existing_content, plugin_content)
        action_msg = "合并"
    elif strategy == 'backup':
        backup_file(claude_md_file)
        final_content = plugin_content
        action_msg = "备份并覆盖"
    else:
        print(f"❌ 未知策略: {strategy}")
        return False

    if dry_run:
        print(f"🔍 预览: 将{action_msg} {claude_md_file}")
        print(f"📊 最终内容大小: {len(final_content)} 字符")
        if strategy == 'merge':
            print(f"📈 原有内容: {len(existing_content)} 字符")
            print(f"➕ Plugin内容: {len(plugin_content)} 字符")
        return True

    try:
        # 确保.claude目录存在
        claude_dir.mkdir(exist_ok=True)

        # 写入文件
        with open(claude_md_file, 'w', encoding='utf-8') as dst:
            dst.write(final_content)

        print(f"✅ 开发规范已{action_msg}: {claude_md_file}")
        print(f"💡 全局生效 - 所有项目的session都会自动应用这些标准")

        if strategy == 'merge':
            print(f"ℹ️  已保留原有内容并追加plugin标准")

        return True

    except Exception as e:
        print(f"❌ 安装失败: {e}")
        return False

def uninstall_standards(restore_backup: bool = False, backup_file: str = None) -> bool:
    """卸载开发规范"""

    claude_md_file = get_user_claude_md()

    if not claude_md_file.exists():
        print("ℹ️  ~/.claude/CLAUDE.md 不存在，无需卸载")
        return True

    try:
        with open(claude_md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return False

    # 检查是否包含plugin内容
    if PLUGIN_SEPARATOR.strip() not in content:
        print("ℹ️  未检测到Claude Standards Plugin内容")

        if restore_backup and backup_file:
            # 尝试从备份恢复
            backup_path = Path(backup_file)
            if backup_path.exists():
                import shutil
                shutil.copy2(backup_path, claude_md_file)
                print(f"✅ 已从备份恢复: {backup_file}")
                return True
            else:
                print(f"❌ 备份文件不存在: {backup_file}")
                return False

        return True

    # 移除plugin内容
    parts = content.split(PLUGIN_SEPARATOR)
    original_content = parts[0].rstrip()

    if not original_content:
        # 整个文件都是plugin内容，直接删除
        claude_md_file.unlink()
        print(f"✅ 已删除 {claude_md_file}")
    else:
        # 保留原有内容
        with open(claude_md_file, 'w', encoding='utf-8') as f:
            f.write(original_content)
        print(f"✅ 已移除Claude Standards Plugin内容")
        print(f"ℹ️  原有内容已保留")

    return True

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Claude 开发规范管理工具 - 用户级安装",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 安装（如果已存在会提示选择）
  %(prog)s

  # 直接覆盖
  %(prog)s --force

  # 直接合并
  %(prog)s --merge

  # 备份后覆盖
  %(prog)s --backup

  # 预览
  %(prog)s --dry-run

  # 卸载
  %(prog)s --uninstall
        """
    )

    parser.add_argument("--force", "-f", action="store_true",
                       help="强制覆盖已存在的 CLAUDE.md 文件")
    parser.add_argument("--merge", "-m", action="store_true",
                       help="合并到已存在的 CLAUDE.md 文件")
    parser.add_argument("--backup", "-b", action="store_true",
                       help="备份后覆盖已存在的 CLAUDE.md 文件")
    parser.add_argument("--dry-run", "-d", action="store_true",
                       help="预览模式，不实际执行")
    parser.add_argument("--uninstall", "-u", action="store_true",
                       help="卸载Claude Standards Plugin")
    parser.add_argument("--restore-backup",
                       help="从指定备份文件恢复")
    parser.add_argument("--plugin-root",
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       help="插件根目录路径")

    args = parser.parse_args()

    # 卸载模式
    if args.uninstall:
        success = uninstall_standards(
            restore_backup=bool(args.restore_backup),
            backup_file=args.restore_backup
        )
        sys.exit(0 if success else 1)

    # 安装模式
    success = install_standards(
        plugin_root=args.plugin_root,
        force=args.force,
        merge=args.merge,
        backup=args.backup,
        dry_run=args.dry_run
    )

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
