#!/bin/bash

# 龙虾体检诊断脚本
# 用于采集 OpenClaw 配置信息，生成体检报告所需的数据

WORKSPACE="${WORKSPACE:-/root/.openclaw/workspace}"
CONFIG_FILE="$WORKSPACE/../openclaw.json"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🦞 龙虾体检诊断开始...${NC}"
echo ""

# 1. 基础信息
echo -e "${YELLOW}📋 基础信息采集${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 读取龙虾姓名（从 IDENTITY.md）
if [ -f "$WORKSPACE/IDENTITY.md" ]; then
    SOUL_NAME=$(grep "\*\*Name:\*\*" "$WORKSPACE/IDENTITY.md" | sed 's/.*\*\*Name:\*\*[[:space:]]*//' | sed 's/[[:space:]]*$//' || echo "")
    if [ -z "$SOUL_NAME" ]; then
        SOUL_NAME="未命名龙虾"
    fi
    echo -e "  🦞 姓名: ${GREEN}$SOUL_NAME${NC}"
else
    SOUL_NAME="未命名龙虾"
    echo -e "  🦞 姓名: ${YELLOW}$SOUL_NAME${NC}"
fi

# 检查 SOUL.md 是否存在（用于后续评分）
if [ -f "$WORKSPACE/SOUL.md" ]; then
    SOUL_EXISTS=true
else
    SOUL_EXISTS=false
fi

# 读取主人姓名（从 USER.md 第一个团队成员）
if [ -f "$WORKSPACE/USER.md" ]; then
    USER_NAME=$(grep "^### [0-9]" "$WORKSPACE/USER.md" | head -1 | sed 's/### [0-9]*\. //' | sed 's/(.*)//' | tr -d '[:space:]')
    if [ -z "$USER_NAME" ]; then
        USER_NAME="未知主人"
    fi
    echo -e "  👤 主人: ${GREEN}$USER_NAME${NC}"
    USER_EXISTS=true
else
    USER_NAME="未知主人"
    echo -e "  👤 主人: ${YELLOW}$USER_NAME${NC}"
    USER_EXISTS=false
fi

# 计算运行天数
if [ -d "$WORKSPACE/.git" ]; then
    FIRST_COMMIT=$(git -C "$WORKSPACE" log --reverse --format=%ci 2>/dev/null | head -1 | cut -d' ' -f1)
    if [ -n "$FIRST_COMMIT" ]; then
        DAYS=$(( ($(date +%s) - $(date -d "$FIRST_COMMIT" +%s)) / 86400 ))
        echo -e "  📅 创建日期: ${GREEN}$FIRST_COMMIT${NC}"
        echo -e "  ⏱️ 运行天数: ${GREEN}${DAYS}天${NC}"
    fi
else
    # 如果没有 git，使用文件修改时间
    OLDEST_FILE=$(find "$WORKSPACE" -name "*.md" -type f -printf '%T+ %p\n' 2>/dev/null | sort | head -1 | cut -d' ' -f1)
    if [ -n "$OLDEST_FILE" ]; then
        echo -e "  📅 最早文件: ${GREEN}$OLDEST_FILE${NC}"
    fi
fi

# 部署位置
HOSTNAME=$(hostname)
echo -e "  🖥️ 部署位置: ${GREEN}$HOSTNAME${NC}"
echo -e "  📍 工作目录: ${GREEN}$WORKSPACE${NC}"

echo ""

# 2. 人格完整度评估
echo -e "${YELLOW}🧠 人格完整度评估${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

PERSONALITY_SCORE=0

# SOUL.md 检查
if [ "$SOUL_EXISTS" = true ]; then
    SOUL_LINES=$(wc -l < "$WORKSPACE/SOUL.md")
    if [ "$SOUL_LINES" -gt 20 ]; then
        echo -e "  ✅ SOUL.md 存在且内容丰富 (${SOUL_LINES}行)"
        PERSONALITY_SCORE=$((PERSONALITY_SCORE + 10))
    else
        echo -e "  ⚠️ SOUL.md 存在但内容较少 (${SOUL_LINES}行)"
        PERSONALITY_SCORE=$((PERSONALITY_SCORE + 5))
    fi
else
    echo -e "  ❌ SOUL.md 不存在"
fi

# USER.md 检查
if [ "$USER_EXISTS" = true ]; then
    USER_LINES=$(wc -l < "$WORKSPACE/USER.md")
    if [ "$USER_LINES" -gt 20 ]; then
        echo -e "  ✅ USER.md 存在且内容丰富 (${USER_LINES}行)"
        PERSONALITY_SCORE=$((PERSONALITY_SCORE + 10))
    else
        echo -e "  ⚠️ USER.md 存在但内容较少 (${USER_LINES}行)"
        PERSONALITY_SCORE=$((PERSONALITY_SCORE + 5))
    fi
else
    echo -e "  ❌ USER.md 不存在"
fi

echo -e "  📊 得分: ${GREEN}${PERSONALITY_SCORE}/20${NC}"
echo ""

# 3. 功能完备度评估
echo -e "${YELLOW}🔧 功能完备度评估${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

FUNCTION_SCORE=0

# 检查 channels
if [ -f "$CONFIG_FILE" ]; then
    CHANNEL_COUNT=$(grep -c '"type"' "$CONFIG_FILE" 2>/dev/null | tr -d '\n' || echo "0")
    CHANNEL_COUNT=$(echo "$CHANNEL_COUNT" | head -1 | tr -d '[:space:]')
    if [ "$CHANNEL_COUNT" -ge 2 ] 2>/dev/null; then
        echo -e "  ✅ 配置了 ${CHANNEL_COUNT} 个 Channel"
        FUNCTION_SCORE=$((FUNCTION_SCORE + 10))
    elif [ "$CHANNEL_COUNT" -ge 1 ] 2>/dev/null; then
        echo -e "  ✅ 配置了 ${CHANNEL_COUNT} 个 Channel"
        FUNCTION_SCORE=$((FUNCTION_SCORE + 5))
    else
        echo -e "  ❌ 未配置 Channel"
    fi
else
    echo -e "  ⚠️ openclaw.json 不存在"
    CHANNEL_COUNT=0
fi

# 检查 cron 任务
CRON_COUNT=0
if command -v openclaw &> /dev/null; then
    CRON_COUNT=$(openclaw cron list 2>/dev/null | grep -c "enabled" | tr -d '\n' || echo "0")
    CRON_COUNT=$(echo "$CRON_COUNT" | head -1 | tr -d '[:space:]')
    if [ "$CRON_COUNT" -gt 0 ] 2>/dev/null; then
        echo -e "  ✅ 配置了 ${CRON_COUNT} 个 Cron 任务"
        FUNCTION_SCORE=$((FUNCTION_SCORE + 5))
    else
        echo -e "  ⚠️ 未配置 Cron 任务"
    fi
fi

# 检查 skills 数量
SKILLS_DIR="$WORKSPACE/skills"
if [ -d "$SKILLS_DIR" ]; then
    SKILLS_COUNT=$(find "$SKILLS_DIR" -name "SKILL.md" -type f 2>/dev/null | wc -l)
    if [ "$SKILLS_COUNT" -ge 5 ]; then
        echo -e "  ✅ 安装了 ${SKILLS_COUNT} 个 Skills"
        FUNCTION_SCORE=$((FUNCTION_SCORE + 5))
    elif [ "$SKILLS_COUNT" -gt 0 ]; then
        echo -e "  ⚠️ 安装了 ${SKILLS_COUNT} 个 Skills"
        FUNCTION_SCORE=$((FUNCTION_SCORE + 2))
    else
        echo -e "  ❌ 未安装 Skills"
    fi
fi

echo -e "  📊 得分: ${GREEN}${FUNCTION_SCORE}/20${NC}"
echo ""

# 4. 记忆系统评估
echo -e "${YELLOW}📝 记忆系统评估${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

MEMORY_SCORE=0

# MEMORY.md 检查
if [ -f "$WORKSPACE/MEMORY.md" ]; then
    MEMORY_LINES=$(wc -l < "$WORKSPACE/MEMORY.md")
    if [ "$MEMORY_LINES" -gt 100 ]; then
        echo -e "  ✅ MEMORY.md 内容丰富 (${MEMORY_LINES}行)"
        MEMORY_SCORE=$((MEMORY_SCORE + 10))
    elif [ "$MEMORY_LINES" -gt 20 ]; then
        echo -e "  ⚠️ MEMORY.md 有一定内容 (${MEMORY_LINES}行)"
        MEMORY_SCORE=$((MEMORY_SCORE + 5))
    else
        echo -e "  ⚠️ MEMORY.md 内容较少 (${MEMORY_LINES}行)"
        MEMORY_SCORE=$((MEMORY_SCORE + 2))
    fi
else
    echo -e "  ❌ MEMORY.md 不存在"
fi

# 日常笔记检查
MEMORY_DIR="$WORKSPACE/memory"
if [ -d "$MEMORY_DIR" ]; then
    NOTES_COUNT=$(find "$MEMORY_DIR" -name "*.md" -type f 2>/dev/null | wc -l)
    if [ "$NOTES_COUNT" -ge 7 ]; then
        echo -e "  ✅ 有 ${NOTES_COUNT} 个日常笔记文件"
        MEMORY_SCORE=$((MEMORY_SCORE + 10))
    elif [ "$NOTES_COUNT" -gt 0 ]; then
        echo -e "  ⚠️ 有 ${NOTES_COUNT} 个日常笔记文件"
        MEMORY_SCORE=$((MEMORY_SCORE + 5))
    else
        echo -e "  ❌ 没有日常笔记"
    fi
else
    echo -e "  ❌ memory/ 目录不存在"
fi

echo -e "  📊 得分: ${GREEN}${MEMORY_SCORE}/20${NC}"
echo ""

# 5. 活跃度评估
echo -e "${YELLOW}⚡ 活跃度评估${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

ACTIVITY_SCORE=0

# Heartbeat 检查
if [ -f "$WORKSPACE/HEARTBEAT.md" ]; then
    HEARTBEAT_LINES=$(wc -l < "$WORKSPACE/HEARTBEAT.md")
    if [ "$HEARTBEAT_LINES" -gt 5 ]; then
        echo -e "  ✅ HEARTBEAT.md 有配置任务"
        ACTIVITY_SCORE=$((ACTIVITY_SCORE + 10))
    else
        echo -e "  ✅ HEARTBEAT.md 存在（空或默认）"
        ACTIVITY_SCORE=$((ACTIVITY_SCORE + 5))
    fi
else
    echo -e "  ❌ HEARTBEAT.md 不存在"
fi

# Cron 任务检查
if [ "$CRON_COUNT" -gt 0 ]; then
    echo -e "  ✅ 有 ${CRON_COUNT} 个定时任务在运行"
    ACTIVITY_SCORE=$((ACTIVITY_SCORE + 10))
else
    echo -e "  ⚠️ 没有定时任务"
fi

echo -e "  📊 得分: ${GREEN}${ACTIVITY_SCORE}/20${NC}"
echo ""

# 6. 安全配置评估
echo -e "${YELLOW}🛡️ 安全配置评估${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

SECURITY_SCORE=0

# AGENTS.md 安全规则检查
if [ -f "$WORKSPACE/AGENTS.md" ]; then
    if grep -qi "安全\|safety\|confirm\|询问" "$WORKSPACE/AGENTS.md"; then
        echo -e "  ✅ AGENTS.md 有安全相关规则"
        SECURITY_SCORE=$((SECURITY_SCORE + 10))
    else
        echo -e "  ⚠️ AGENTS.md 无明确安全规则"
        SECURITY_SCORE=$((SECURITY_SCORE + 5))
    fi
else
    echo -e "  ❌ AGENTS.md 不存在"
fi

# SOUL.md 边界检查
if [ "$SOUL_EXISTS" = true ]; then
    if grep -qi "边界\|boundary\|private\|隐私" "$WORKSPACE/SOUL.md"; then
        echo -e "  ✅ SOUL.md 有边界设置"
        SECURITY_SCORE=$((SECURITY_SCORE + 10))
    else
        echo -e "  ⚠️ SOUL.md 无明确边界"
        SECURITY_SCORE=$((SECURITY_SCORE + 5))
    fi
fi

echo -e "  📊 得分: ${GREEN}${SECURITY_SCORE}/20${NC}"
echo ""

# 7. 总分计算
TOTAL_SCORE=$((PERSONALITY_SCORE + FUNCTION_SCORE + MEMORY_SCORE + ACTIVITY_SCORE + SECURITY_SCORE))

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 总分: ${TOTAL_SCORE}/100${NC}"

if [ "$TOTAL_SCORE" -ge 80 ]; then
    echo -e "${GREEN}💪 健康龙虾${NC}"
elif [ "$TOTAL_SCORE" -ge 60 ]; then
    echo -e "${YELLOW}🔧 需要调优${NC}"
else
    echo -e "${RED}🚑 需要治疗${NC}"
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 8. 生成 JSON 输出（供 AI 使用）
echo -e "${YELLOW}📄 JSON 数据（供 AI 处理）${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat <<EOF
{
  "basic_info": {
    "name": "$SOUL_NAME",
    "owner": "$USER_NAME",
    "hostname": "$HOSTNAME",
    "workspace": "$WORKSPACE"
  },
  "scores": {
    "personality": $PERSONALITY_SCORE,
    "function": $FUNCTION_SCORE,
    "memory": $MEMORY_SCORE,
    "activity": $ACTIVITY_SCORE,
    "security": $SECURITY_SCORE,
    "total": $TOTAL_SCORE
  },
  "grade": "$([ "$TOTAL_SCORE" -ge 80 ] && echo "healthy" || ([ "$TOTAL_SCORE" -ge 60 ] && echo "needs_tuning" || echo "needs_treatment"))",
  "details": {
    "soul_lines": ${SOUL_LINES:-0},
    "user_lines": ${USER_LINES:-0},
    "memory_lines": ${MEMORY_LINES:-0},
    "channels": ${CHANNEL_COUNT:-0},
    "cron_tasks": ${CRON_COUNT:-0},
    "skills": ${SKILLS_COUNT:-0},
    "notes_files": ${NOTES_COUNT:-0}
  }
}
EOF

echo ""
echo -e "${GREEN}✅ 诊断完成！${NC}"
echo -e "${YELLOW}💡 将以上信息提供给 AI，生成完整的体检报告${NC}"
