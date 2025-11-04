#!/usr/bin/env python3
"""
Claude 开发规范安装脚本
将开发规范复制到项目的 .claude/CLAUDE.md 文件
"""

import os
import sys
import argparse
from pathlib import Path

def install_standards(plugin_root: str, force: bool = False, dry_run: bool = False) -> bool:
    """安装开发规范到项目"""

    # 获取源文件和目标文件路径
    prompts_md_file = Path(plugin_root) / "prompts" / "prompts.md"
    current_dir = Path.cwd()
    claude_dir = current_dir / ".claude"
    claude_md_file = claude_dir / "CLAUDE.md"

    # 检查源文件是否存在
    if not prompts_md_file.exists():
        print(f"❌ 源文件不存在: {prompts_md_file}")
        return False

    # 检查目标文件是否已存在
    if claude_md_file.exists() and not force:
        print(f"⚠️  CLAUDE.md 已存在: {claude_md_file}")
        print("使用 --force 参数强制覆盖")
        return False

    if dry_run:
        print(f"🔍 预览: 将复制 {prompts_md_file} 到 {claude_md_file}")
        if claude_md_file.exists():
            print("⚠️  目标文件已存在，将覆盖")
        return True

    try:
        # 确保.claude目录存在
        claude_dir.mkdir(exist_ok=True)

        # 复制文件内容
        with open(prompts_md_file, 'r', encoding='utf-8') as src:
            content = src.read()

        with open(claude_md_file, 'w', encoding='utf-8') as dst:
            dst.write(content)

        print(f"✅ 开发规范已安装到: {claude_md_file}")
        print("💡 现在所有session都会自动应用这些标准")
        return True

    except Exception as e:
        print(f"❌ 安装失败: {e}")
        return False

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="Claude 开发规范安装工具")

    parser.add_argument("--force", "-f", action="store_true",
                       help="强制覆盖已存在的 CLAUDE.md 文件")
    parser.add_argument("--dry-run", "-d", action="store_true",
                       help="预览模式，不实际执行")
    parser.add_argument("--plugin-root",
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       help="插件根目录路径")

    args = parser.parse_args()

    success = install_standards(
        plugin_root=args.plugin_root,
        force=args.force,
        dry_run=args.dry_run
    )

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()