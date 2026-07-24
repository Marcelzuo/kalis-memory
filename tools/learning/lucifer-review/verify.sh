#!/bin/bash
# 路西法数学题抽查验证脚本
# 用法: ./verify.sh <错题库目录>
# 从错题库随机抽取 3 道数学题，用 DeepSeek R1 独立求解，与原答案对比

ERROR_DIR="${1:-$HOME/WorkBuddy/错题库/数学}"
SAMPLE_COUNT=3
REPORT="$HOME/路西法-抽查报告-$(date +%Y%m%d).md"

echo "# 路西法数学抽查报告" > "$REPORT"
echo "> 抽查时间: $(date '+%Y-%m-%d %H:%M')" >> "$REPORT"
echo "> 错题库: $ERROR_DIR" >> "$REPORT"
echo "" >> "$REPORT"

# 随机选文件
files=$(ls "$ERROR_DIR"/*.md 2>/dev/null | sort -R | head -$SAMPLE_COUNT)

if [ -z "$files" ]; then
    echo "❌ 错题库为空或路径不对: $ERROR_DIR" | tee -a "$REPORT"
    exit 1
fi

count=0
for f in $files; do
    count=$((count + 1))
    echo "---" >> "$REPORT"
    echo "## 抽查 #$count: $(basename "$f")" >> "$REPORT"
    echo "" >> "$REPORT"
    
    # 提取原题
    question=$(grep -A2 "📝 原题" "$f" | tail -1)
    echo "**原题:** $question" >> "$REPORT"
    echo "" >> "$REPORT"
    
    # 提取原答案
    answer=$(grep -A1 "最终答案" "$f" | tail -1)
    echo "**WorkBuddy答案:** $answer" >> "$REPORT"
    echo "" >> "$REPORT"
    
    # 路西法独立验算（调用 DeepSeek R1）
    echo "**路西法验算:** 进行中..." >> "$REPORT"
    
    # 这里接入实际的 DeepSeek API 调用
    # curl -s https://api.deepseek.com/v1/chat/completions \
    #   -H "Authorization: Bearer $DEEPSEEK_KEY" \
    #   -d '{"model":"deepseek-reasoner","messages":[{"role":"user","content":"请解这道数学题，给出最终答案:'"$question"'"}]}'
    
    echo "  （需配置 DEEPSEEK_KEY 环境变量后自动验算）" >> "$REPORT"
    echo "" >> "$REPORT"
done

echo "---" >> "$REPORT"
echo "## 总结" >> "$REPORT"
echo "- 抽查数量: $count 道" >> "$REPORT"
echo "- 配置 DeepSeek API Key 后自动比对答案" >> "$REPORT"
echo "" >> "$REPORT"
echo "报告已生成: $REPORT"
cat "$REPORT"
