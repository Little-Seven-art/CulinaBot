<div align="center">
  <h1>CulinaBot —— AI 私厨管家智能体</h1>
  <p>
    <img src="https://img.shields.io/badge/LangChain-1.2.0-FF6B6B" alt="LangChain">
    <img src="https://img.shields.io/badge/多模态模型-v1.0-4B8BBE" alt="多模态模型">
    <img src="https://img.shields.io/badge/Python-3.13-3776AB" alt="Python">
    <img src="https://img.shields.io/badge/SQLite-3.44-003B57" alt="SQLite">
    <img src="https://img.shields.io/badge/AI智能体-v1.0-4CAF50" alt="AI智能体">
  </p>
</div>

## 项目简介
AI 私厨管家（CulinaBot）是一个基于 LangChain 和多模态模型的食谱推荐应用。用户可以拍摄自家冰箱或厨房的食物照片，管家会自动识别图片中的食材，根据食材搜索相关食谱推荐给用户。

## ✨ 核心亮点
- 基于多模态模型实现食材图像自动识别
- 结合 LangChain 构建食谱检索与推荐智能体
- 支持食材搭配禁忌、烹饪难度适配等个性化推荐
- 本地 SQLite 存储用户偏好与历史对话，支持对话回滚
- 可扩展对接城市生活服务平台，联动线下商家资源

## 🛠️ 技术栈
- **核心框架**：LangChain
- **多模态能力**：多模态大模型（图像识别 + 文本生成）
- **开发语言**：Python 3.10+
- **数据存储**：SQLite（用户偏好、对话历史、食材记录）
- **外部工具**：Tavily / 通用搜索引擎（食谱信息检索）

## 🚀 功能模块
1. **食材图像识别**
   上传厨房/冰箱食材照片，自动识别并提取食材列表。

2. **智能食谱推荐**
   根据现有食材匹配最优食谱，支持按难度、时长、口味排序。

3. **个性化适配**
   支持素食、减脂、过敏忌口、烹饪水平等偏好设置。

4. **对话记忆与历史**
   本地持久化对话记录，支持上下文延续、历史回顾与对话回滚。

5. **扩展能力**
   可接入外卖、生鲜配送、线下餐饮等生活服务接口。

## 🧩 快速开始
1. 克隆项目并安装依赖
```bash
pip install -r requirements.txt

