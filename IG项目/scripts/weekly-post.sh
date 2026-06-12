#!/bin/bash
# KALIS TORIK IG 周发帖脚本
# 用法：bash weekly-post.sh <本周素材目录>
# 例：bash weekly-post.sh weekly/2026-W25

WEEK_DIR="${1:-weekly/$(date +%Y-W%V)}"
echo "📅 本周素材目录：$WEEK_DIR"

# 检查素材
if [ ! -f "$WEEK_DIR/scripts.md" ]; then
    echo "❌ 缺少脚本文件：$WEEK_DIR/scripts.md"
    exit 1
fi

echo "✅ 脚本文件已就绪"
echo "📋 请确认以下内容后手动执行 opencli 命令："
echo ""
echo "  # Feed 帖"
echo "  opencli instagram post \"caption\" --media $WEEK_DIR/assets/mon-1.jpg,$WEEK_DIR/assets/mon-2.jpg"
echo "  opencli instagram post \"caption\" --media $WEEK_DIR/assets/wed-1.jpg"
echo ""
echo "  # Reels"
echo "  opencli instagram reel \"caption\" --video $WEEK_DIR/assets/fri-reel.mp4"
echo ""
echo "  # Story"
echo "  opencli instagram story --media $WEEK_DIR/assets/story.jpg"
