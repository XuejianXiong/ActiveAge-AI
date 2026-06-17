# ActiveAge AI

[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](https://github.com/XuejianXiong/ActiveAge-AI/releases)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Orchestration-orange)](https://www.langchain.com/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-LLM%20Framework-green)](https://www.langchain.com/)
[![LangSmith](https://img.shields.io/badge/LangSmith-LLM%20Observability-111827)](https://www.langchain.com/langsmith)
[![OpenAI](https://img.shields.io/badge/OpenAI-LLM-412991?logo=openai&logoColor=white)](https://openai.com/)
[![Gemma](https://img.shields.io/badge/Gemma-Local%20LLM-4285F4)](https://ai.google.dev/gemma)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-purple)](https://www.trychroma.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/)
[![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-red)]()
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-darkgreen)]()
[![Semantic Search](https://img.shields.io/badge/Semantic-Search-purple)]()
[![Guardrails](https://img.shields.io/badge/Safety-Guardrails-red)]()
[![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-FF6F00?logo=gradio&logoColor=white)](https://www.gradio.app/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


## Production-Ready Agentic AI Platform for Personalized Wellness Guidance

ActiveAge AI is a modular, production-oriented agentic AI application that delivers personalized physical wellness activities, cognitive training exercises, and evidence-informed health information through a conversational interface.

Built with LangGraph, LangChain, Retrieval-Augmented Generation (RAG), vector databases, and tool orchestration, the platform demonstrates modern AI engineering patterns including multi-tool agents, semantic retrieval, guardrails, configurable model backends, and scalable service-oriented architecture.

The project serves as a reference implementation for building production-grade AI assistants that combine structured APIs, vector search, and real-time information retrieval within a unified agent framework.

---

# Features

## Physical Wellness Guidance

Provides structured exercise recommendations through integration with external fitness knowledge sources.

Capabilities:

* Exercise discovery
* Mobility and stretching routines
* Strength and balance activities
* Step-by-step exercise instructions
* Structured activity recommendations

---

## Cognitive Training and Mental Fitness

Uses Retrieval-Augmented Generation (RAG) to retrieve cognitive training activities from a semantic knowledge base.

Capabilities:

* Brain exercises
* Memory training activities
* Attention and focus exercises
* Problem-solving activities
* Cognitive wellness recommendations

---

## Real-Time Knowledge Retrieval

Provides access to current information when local knowledge sources are insufficient.

Capabilities:

* Health and wellness news
* Nutrition information
* Recent research updates
* Current fitness trends
* Time-sensitive information retrieval

---

## Agentic AI Workflow

The application uses LangGraph to orchestrate reasoning and tool execution.

Features:

* Dynamic tool selection
* Multi-step workflows
* Retrieval-aware responses
* Stateful conversations
* Configurable routing logic
* Tool execution tracking

---

# System Architecture

```
User
 │
 ▼
Gradio Interface
 │
 ▼
LangGraph Agent
 │
 ├── Guardrails Layer
 │
 ├── Physical Exercise Tool
 │      └── Wger API
 │
 ├── Mental Fitness Tool
 │      └── ChromaDB + Embeddings
 │
 └── Web Search Tool
        └── Tavily Search
```

---

# Project Structure

```
ActiveAge-AI/
│
├── agents/
│   ├── activeage_agent.py
│   └── state.py
│
├── core/
│   ├── config.py
│   ├── prompts.py
│   ├── prompt_builder.py
│   ├── output_schema.py
│   ├── guardrails.py
│   ├── models.py
│   ├── tool_registry.py
│   ├── embedding.py
│   └── chat.py
│
├── services/
│   ├── exercise_service.py
│   └── search_service.py
│
├── tools/
│   ├── exercise.py
│   ├── mental.py
│   └── search.py
│
├── rag/
│   ├── build_vector_db_hf.py
│   ├── build_vector_db_openai.py
│   └── vector_db_builder.py
│
├── data/
│
├── utils/
│
├── app.py
├── .secrets
├── .gitignore
├── pyproject.toml
├── SETUP.md
├── README.md
└── LICENSE
```

---

# Technology Stack

## AI Frameworks

* LangGraph
* LangChain
* OpenAI Compatible APIs
* LM Studio

## Retrieval Technologies

* ChromaDB
* Vector Embeddings
* Semantic Search
* Retrieval-Augmented Generation (RAG)

## Data Sources

* Wger Exercise API
* Local Knowledge Base
* Tavily Search

## Application Layer

* Python
* Gradio
* Environment-Based Configuration
* Modular Service Architecture

---

# Production Engineering Features

## Modular Architecture

The application follows clear separation of responsibilities:

* Agent orchestration
* Tool definitions
* Service layer integrations
* Prompt management
* Guardrails and safety controls
* Configuration management

---

## Configurable Model Backends

Supports multiple model providers through centralized configuration.

Examples:

* OpenAI-compatible endpoints
* Local LLMs via LM Studio
* Future cloud-hosted model deployments

---

## Guardrails and Safety Layer

Built-in safety mechanisms help ensure controlled behavior.

Features:

* Pre-LLM request validation
* Restricted topic detection
* Safe response routing
* Out-of-scope handling
* Emergency escalation responses

---

## Retrieval-Augmented Generation

Mental fitness recommendations are grounded using semantic retrieval.

Pipeline:

1. Data ingestion
2. Embedding generation
3. Vector indexing
4. Similarity search
5. Context retrieval
6. Response generation

Benefits:

* Reduced hallucinations
* Improved consistency
* Domain-specific knowledge grounding

---

## Tool-Oriented Agent Design

The system separates reasoning from execution.

Available tools:

| Tool                   | Purpose                         |
| ---------------------- | ------------------------------- |
| Physical Exercise Tool | Exercise recommendations        |
| Mental Fitness Tool    | Cognitive activity retrieval    |
| Web Search Tool        | Real-time information retrieval |

This architecture enables easy expansion with additional tools and services.

---

# Running the Application

## Install Dependencies

```
uv sync
```

## Configure Environment

Create a `.secrets` file using `.secrest.template`

## Build Local ChromaDB

```
uv run python -m rag.build_vector_db_hf
```

## Launch Application

```
uv run app.py
```

The application will be available locally through the Gradio web interface.

---

# Future Enhancements

Planned improvements include:

* Long-term memory support
* User personalization
* Multi-agent collaboration
* Health document ingestion
* Clinical knowledge retrieval
* Cloud deployment
* Authentication and user management
* Monitoring and observability dashboards

---

# Purpose

This project demonstrates practical implementation of modern AI engineering concepts including:

* Agentic AI systems
* LangGraph workflows
* Retrieval-Augmented Generation
* Vector databases
* Semantic search
* Tool orchestration
* Guardrails and safety systems
* Production-oriented software architecture

The goal is to showcase how modular AI applications can be designed, deployed, and extended using industry-standard engineering practices.
