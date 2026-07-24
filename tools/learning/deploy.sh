#!/bin/bash
# ============================================
# WorkBuddy 初中学习方案 · 一键部署
# 米迦勒团队出品 · 2026.07
# ============================================
set -e

WB_SKILLS="$HOME/.workbuddy/skills"
WB_CONFIG="$HOME/.workbuddy"
ERROR_DIR="$HOME/WorkBuddy/错题库"

echo "🚀 部署 WorkBuddy 初中学习方案..."
echo ""

# 1. 创建目录
echo "📁 创建目录..."
mkdir -p "$WB_SKILLS"
mkdir -p "$ERROR_DIR"/{数学,语文,英语}
echo "   ✅ Skills 目录: $WB_SKILLS"
echo "   ✅ 错题库: $ERROR_DIR"

# 2. 复制 Skills
echo ""
echo "📋 部署 Skills..."
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
for skill in math-tutor chinese-tutor english-tutor study-planner; do
    if [ -d "$SCRIPT_DIR/skills/$skill" ]; then
        cp -r "$SCRIPT_DIR/skills/$skill" "$WB_SKILLS/"
        echo "   ✅ $skill"
    else
        echo "   ⚠️  $skill 未找到，跳过"
    fi
done

# 3. 配置模型
echo ""
echo "🔧 配置模型..."
if [ ! -f "$WB_CONFIG/models.json" ]; then
    cp "$SCRIPT_DIR/config/models.json" "$WB_CONFIG/models.json"
    echo "   ✅ models.json 已创建"
    echo "   ⚠️  请编辑 $WB_CONFIG/models.json 填入你的 API Key"
else
    echo "   ⚠️  models.json 已存在，跳过"
    echo "   如需更新请手动合并 $SCRIPT_DIR/config/models.json"
fi

# 4. 验证
echo ""
echo "🔍 验证部署..."
skill_count=$(ls "$WB_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
echo "   已部署 $skill_count 个 Skills"

echo ""
echo "========================================"
echo "  ✅ 部署完成！"
echo "========================================"
echo ""
echo "📋 下一步："
echo "  1. 编辑 ~/.workbuddy/models.json → 填入 API Key"
echo "     DeepSeek: https://platform.deepseek.com"
echo "     Kimi:     https://platform.moonshot.cn"
echo "     通义千问:  https://dashscope.aliyun.com"
echo ""
echo "  2. 重启 WorkBuddy"
echo ""
echo "  3. 试试说："
echo "     '帮我分析这道数学错题：xxx'"
echo "     '帮我批改这篇作文'"
echo "     '制定本周复习计划'"
echo ""
echo "  4. 路西法抽查（在爸爸电脑上）："
echo "     bash lucifer-review/verify.sh"
echo ""
echo "💰 费用估算（按月）："
echo "     初中生每天10道题 ≈ 5万token"
echo "     DeepSeek R1: ¥0.05/天 ≈ ¥1.5/月"
echo "     已付费，不产生额外费用"
echo ""
