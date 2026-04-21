import os
import sqlite3

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver

# 加载环境变量
load_dotenv()

# 创建多模态模型
model = init_chat_model(
    model="qwen3.6-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

# 定义工具
web_search = TavilySearch(
    max_results=5,
    topic="general",
    search_depth="basic",  # 如果需要指定搜索深度
    time_range=None,  # 如果需要指定时间范围，可以是 "day", "week", "month", "year" 或 None
    include_domains=[],
    exclude_domains=[]
)

# 连接sqlite
connection = sqlite3.connect("resources/personal_chief.db", check_same_thread=False)
# 初始化checkpointer
checkpointer = SqliteSaver(connection)
# 自动建表
checkpointer.setup()

# 系统提示词
system_prompt = """
你是一名私人厨师。收到用户提供的食材照片或清单后，请按以下流程操作:
1.识别和评估食材:若用户提供照片，首先辨识所有可见食材。基于食材的外观状态，评估其新鲜度与可用量，整理出一份“当前可用食材清单”
2.智能食谱检索:优先调用 web_search 工具，以“可用食材清单”为核心关键词，查找可行菜谱。
3.多维度评估与排序:从营养价值和制作难度两个维度对检索到的候选食谱进行量化打分，并根据得分排序，制作简单且营养丰富的排名靠前。
4.结构化方案输出:把排序后的食谱整理为一份结构清晰的建议报告，要包含食谱信息、得分、推荐理由、食谱的参考图片，帮助用户快速做出决策。

请严格按照流程，优先调用 web_search 工具搜索食谱，搜索不到的情况下才能自己发挥。
"""

# 创建智能体
agent = create_agent(
    model=model,
    tools=[web_search],
    checkpointer=checkpointer,
    system_prompt=system_prompt
)

# 多模态消息
multimodel_messages = HumanMessage([
    {"type": "text", "text": "帮我看看能做什么？"},
    {"type": "image", "url": "https://aisearch.cdn.bcebos.com/pic_create/2026-04-10/10/74d52055e4947f8c.jpg"}
])

# 配置会话标识
config = {"configurable": {"thread_id": "thread_1"}}

# 测试智能体效果
response = agent.invoke({"messages": [multimodel_messages]}, config)

for message in response['messages']:
    message.pretty_print()
