\# 🤖 Intelligent Data Analyst Agent (基于 RAG 与微调的垂直领域智能助手)



\## 📖 项目介绍

针对金融与统计分析场景中，通用大模型存在“知识幻觉”且无法处理私有非结构化数据（PDF）及结构化数据（CSV）的问题，本项目构建了一套集 \*\*文档检索 (RAG)\*\*、\*\*自动化分析 (Agent)\*\*、\*\*专业问答 (Fine-tuning)\*\* 于一体的智能系统。



\## 🚀 核心功能

\*   \*\*🧠 领域模型微调 (Fine-tuning):\*\* 基于 \*\*Qwen2-1.5B\*\* 模型，使用 \*\*LLaMA-Factory\*\* 进行 \*\*LoRA\*\* 指令微调，显著提升模型对统计学术语的理解能力。

\*   \*\*📚 高级 RAG 检索:\*\* 实现了 "PDF解析 -> Chunking -> 向量召回 (FAISS) -> \*\*重排序 (Rerank)\*\*" 的完整链路，解决长尾语义匹配问题。

\*   \*\*📊 数据分析 Agent:\*\* 基于 \*\*LangChain\*\* 开发代码解释器，支持通过自然语言指令（Text-to-Code）自动清洗数据并生成 Matplotlib 图表。



\## 🛠️ 技术栈

\*   \*\*LLM Framework:\*\* LangChain, LLaMA-Factory

\*   \*\*Model:\*\* Qwen2-1.5B-Instruct, BGE-Small-Zh (Embedding), BGE-Reranker

\*   \*\*Database:\*\* FAISS (Vector DB)

\*   \*\*Tools:\*\* Pandas, PyPDFLoader, Matplotlib



\## 📂 项目结构

```text

├── data/               # 原始数据 (PDF/JSON)

├── src/

│   ├── rag\_engine.py   # RAG 检索核心逻辑 (含 Rerank)

│   ├── agent\_tool.py   # Pandas Agent 实现

│   └── train\_lora.sh   # 微调启动脚本

├── notebooks/          # 实验与测试 Notebook

├── requirements.txt    # 依赖包

└── README.md

