# Antigravity (AGY) Essential Plugins

**The definitive performance and orchestration suite for Google Antigravity.**

*Drastically reduce latency, slash token expenditure, and enforce kernel-level security across your autonomous agent swarms.*

---

## 📖 Overview

The **Antigravity Essential Plugins** repository is a production-grade monorepo containing the 5 critical open-source extensions required to run [Google Antigravity (AGY)](https://github.com/google/antigravity) at scale. 

As identified by the 2026 Deep Research initiative, standard multi-agent orchestration often suffers from exponential token degradation, "lost in the middle" context saturation, and unoptimized execution bottlenecks. This toolkit solves these systemic issues by introducing heterogeneous routing, Model Context Protocol (MCP) semantic caching, and persistent ChromaDB architectural memory.

## 🏗 Architecture Workflow

1. **AGY Orchestrator Engine** routes tasks to ->
2. **agy-swarm-router**: Triages task complexity (High -> Gemini 1.5 Pro, Med -> Gemini 1.5 Flash, Low -> Gemma 7B Local)
3. **agy-perf-toolkit**: Prunes context and batches requests.
4. **mcp-semantic-cache**: Uses cosine similarity (>0.95) to bypass redundant tool calls.
5. **agy-chroma-memory**: Saves and retrieves architectural knowledge.
6. **agy-secure-sandbox**: Enforces eBPF kernel-level monitoring for all external interactions.

## 📦 The 5 Essential Plugins

### 1. `agy-perf-toolkit` ⚡️
**Native AGY Key-Value (KV) cache management.**
*   **Dynamic Context Pruning:** Automatically excises semantically redundant conversational turns to preserve the active context window.
*   **Request Batching:** Aggregates parallel subagent queries into consolidated batches for optimized cloud API transport.

### 2. `mcp-semantic-cache` 🧠
**Intelligent caching for the Model Context Protocol.**
*   **Vector-Based Retrieval:** Uses the locally executed `all-MiniLM-L6-v2` embedding model to calculate cosine similarity on incoming tool requests.
*   **Zero-Latency Bypassing:** Returns cached tool execution results for non-deterministic requests scoring >0.95 similarity.

### 3. `agy-swarm-router` 🔀
**Dynamic heterogeneous model routing.**
*   **Complexity Triage:** Evaluates the semantic density and tool dependencies of an incoming subtask.
*   **Cost Reduction:** Routes trivial formatting tasks to local SLMs (Gemma) while reserving frontier models (Gemini Pro) for profound logical deduction.

### 4. `agy-chroma-memory` 💾
**Persistent state and architectural memory.**
*   **Knowledge Graphing:** Automatically vectors and indexes every significant conclusion reached by your agents.
*   **Proactive Retrieval:** Allows agents to query implications of past structural changes without needing to traverse the codebase repeatedly.

### 5. `agy-secure-sandbox` 🛡
**Kernel-level security for 3rd-party MCP servers.**
*   **eBPF Isolation:** Monitors and intercepts system calls from isolated MCP extensions.
*   **Strict Egress:** Enforces network policies ensuring zero unauthorized external communication.

## 🚀 Quick Start

To install all plugins into your local AGY daemon environment, run the provided installation script (Requires AGY SDK v2.0+):

```bash
git clone https://github.com/danieljamesdrinkwater/Antigravity.git
cd Antigravity/Antigravity-Essential-plugins
chmod +x install.sh
./install.sh
```

## 📚 Deep Research Textbook
The theoretical and academic foundations for these architectures are extensively documented. We have included the synthesized 10-chapter academic textbook derived from our deep research runs. 
👉 **[Read the Full Textbook Here](./research/AGY_Textbook_Compiled.md)**
