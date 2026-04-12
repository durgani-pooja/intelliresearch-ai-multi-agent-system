# 🧬 IntelliResearch Pro

> **Multi-Agent Academic Intelligence & Code Analysis Platform**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)](https://langchain.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

---

## 📋 Table of Contents

1. [Business Problem](#-business-problem)
2. [Possible Solution](#-possible-solution)
3. [Implemented Solution](#-implemented-solution)
4. [Tech Stack](#-tech-stack-used)
5. [Architecture Diagram](#-architecture-diagram)
6. [How to Run Locally](#-how-to-run-locally)
7. [Screenshots](#-screenshots)
8. [Demo Recording](#-demo-recording)
9. [Problems Faced & Solutions](#-problems-faced--solutions)
10. [References & Resources](#-references--resources)

---

## 🔴 Business Problem

Academic researchers, students, and developers face significant challenges when dealing with large volumes of research PDFs, technical documents, and code-heavy academic material:

- **Information Overload** — Reading and digesting hundreds of pages of academic content is time-consuming and cognitively exhausting.
- **Lack of Deep Query Support** — Ctrl+F keyword search is not enough; users need contextual and intelligent answers from documents.
- **Code Comprehension Gap** — Academic papers with embedded code logic or pseudoalgorithms are hard to understand without expert-level explanation.
- **No Unified Intelligence Layer** — There is no single tool that combines document summarization, technical insight extraction, and code logic explanation in one interface.

---

## 💡 Possible Solution

A Multi-Agent AI system that:

- **Ingests research PDFs** and extracts both text and code logic automatically.
- Uses **multiple specialized agents** — one for summarization, one for technical insights, one for deep queries, and one for code explanation.
- Provides an **interactive query interface** to ask domain-specific questions about the document.
- Generates a **comprehensive final report** combining all agent outputs into one structured document.

---

## ✅ Implemented Solution

**IntelliResearch Pro** is a Streamlit-based multi-agent application that enables:

| Feature | Description |
|---|---|
| 📄 PDF Ingestion | Upload any research PDF up to 200MB via drag-and-drop |
| 📝 Executive Summary | 3-paragraph AI-generated overview of the document |
| 💡 Technical Insights | 5 high-level technical findings extracted from the document |
| 🔍 Deep Query | Ask any natural language question about the paper |
| 💻 Code Logic Explainer | Explains embedded code snippets and algorithms in plain English |
| 🏆 Final Comprehensive Report | Unified structured report combining all agent outputs |
| ❤️ System Health Monitor | Real-time status indicator showing core module health |

### How It Works

1. User uploads a research PDF via the **Command Module** sidebar
2. The system ingests, chunks, and indexes the document using vector embeddings
3. Multiple AI agents are triggered simultaneously:
   - **Summary Agent** → Generates Executive Summary
   - **Insight Agent** → Extracts Technical Insights
   - **Code Agent** → Explains Code Logic
4. User types a specific question in the **Deep Query** panel
5. Clicking **Initiate Analysis** triggers all agents and produces the **Final Comprehensive Report**

---

## 🛠 Tech Stack Used

| Layer | Technology |
|---|---|
| **Frontend / UI** | Streamlit |
| **AI / LLM Backend** | Google Gemini API |
| **PDF Processing** | PyMuPDF `fitz` / pdfplumber |
| **Vector Store** | FAISS / ChromaDB |
| **Embeddings** | Google Generative AI Embeddings |
| **Multi-Agent Framework** | LangChain Agents |
| **Language** | Python 3.10+ |
| **Config Management** | python-dotenv + config.py |
| **Deployment** | Streamlit Community Cloud / Localhost |
| **Dev Environment** | DevContainer `.devcontainer` |

---

## 🏗 Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     IntelliResearch Pro                      │
│                   (Streamlit Frontend UI)                    │
└─────────────────────────┬────────────────────────────────────┘
                          │
           ┌──────────────▼──────────────┐
           │        Command Module        │
           │   (PDF Upload & Ingestion)   │
           └──────────────┬──────────────┘
                          │
           ┌──────────────▼──────────────┐
           │      Document Processor      │
           │  (PyMuPDF / pdfplumber)      │
           │    Chunk → Embed → Index     │
           └──────────────┬──────────────┘
                          │
           ┌──────────────▼──────────────┐
           │         Vector Store         │
           │      (FAISS / ChromaDB)      │
           └──────────────┬──────────────┘
                          │
      ┌───────────────────┼────────────────────────┐
      │                   │                        │
 ┌────▼────┐        ┌─────▼─────┐          ┌───────▼──────┐
 │ Summary │        │ Technical │          │     Code     │
 │  Agent  │        │  Insight  │          │  Explainer   │
 │         │        │   Agent   │          │    Agent     │
 └────┬────┘        └─────┬─────┘          └───────┬──────┘
      │                   │                        │
      └───────────────────▼────────────────────────┘
                          │
           ┌──────────────▼──────────────┐
           │       Deep Query Engine      │
           │    (User Q&A + RAG Chain)    │
           └──────────────┬──────────────┘
                          │
           ┌──────────────▼──────────────┐
           │  Final Comprehensive Report  │
           │  (Unified Structured Output) │
           └──────────────────────────────┘
```

---

## 🚀 How to Run Locally

### Prerequisites

- Python 3.10 or above
- pip package manager
- Google Gemini API key — [Get one here](https://ai.google.dev)
- Git installed on your machine

### Step 1 — Clone the Repository

```bash
git clone https://github.com/durgani-pooja/intelliresearch-ai-multi-agent-system.git
cd intelliresearch-ai-multi-agent-system
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up Environment Variables

Create a `.env` file in the root folder and add:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

### Step 5 — Run the Application

```bash
streamlit run app.py
```

The app will launch at `http://localhost:8501` in your browser.

### Step 6 — Use the App

1. Upload a PDF using the drag-and-drop panel in the **Command Module** sidebar
2. Type a specific question in the **Deep Query** text field (optional)
3. Click **Initiate Analysis** to trigger all agents
4. View the Executive Summary, Technical Insights, Code Explainer, and Final Report

---

## 📸 Screenshots

### 1. Main Interface — PDF Upload and Executive Summary

![Main Interface](screenshots/screenshot1.png)

> The AI generates a 3-paragraph Executive Summary and 5 Technical Insights immediately after PDF upload.

---

### 2. Deep Query and Code Logic Explainer

![Deep Query](screenshots/screenshot2.png)

> User types a natural language question and the AI responds with structured, context-aware answers from the document.

---

### 3. Final Comprehensive Report

![Final Report](screenshots/screenshot3.png)

> A fully structured markdown report covering all sections — auto-generated from the uploaded PDF.

---

## 🎥 Demo Recording

> 📹 **Watch the full demo here:** *(Add your Loom or YouTube link here)*

The demo covers:
- Uploading a research PDF
- Initiating multi-agent analysis
- Using the Deep Query feature
- Viewing the Final Comprehensive Report

---

## 🐛 Problems Faced & Solutions

| # | Problem | Solution |
|---|---|---|
| 1 | Streamlit app.py not found on Streamlit Cloud | Ensured app.py is in root directory with all dependencies listed in requirements.txt |
| 2 | PDF text extraction failing for scanned PDFs | Switched from PyPDF2 to PyMuPDF (fitz) for reliable text and image PDF handling |
| 3 | LLM hallucinating answers on deep queries | Implemented RAG using FAISS so the model answers only from document context |
| 4 | Slow response time for large PDFs | Added chunking strategy with 1000 token size and parallel agent execution |
| 5 | Gemini API rate limits during multi-agent calls | Added exponential backoff retry logic using the tenacity library |
| 6 | Typo handling in Deep Query input | Gemini naturally interprets and corrects typos in context with no extra preprocessing |
| 7 | Session state lost on page refresh | Used st.session_state to persist uploaded documents and agent results |
| 8 | venv folder accidentally pushed to GitHub | Added venv/ to .gitignore and ran git rm -r --cached venv/ to untrack it |

---

## 📚 References & Resources

| Resource | Link |
|---|---|
| Streamlit Documentation | https://docs.streamlit.io |
| LangChain Documentation | https://docs.langchain.com |
| Google Gemini API | https://ai.google.dev/docs |
| PyMuPDF Documentation | https://pymupdf.readthedocs.io |
| FAISS Vector Store | https://faiss.ai |
| ChromaDB Documentation | https://docs.trychroma.com |
| Streamlit Community Cloud | https://streamlit.io/cloud |
| Python dotenv | https://pypi.org/project/python-dotenv |
| GitHub Docs | https://docs.github.com |

---

## 👩‍💻 Author

**Durgani Pooja**

- GitHub: [@durgani-pooja](https://github.com/durgani-pooja)
- Project Repository: [intelliresearch-ai-multi-agent-system](https://github.com/durgani-pooja/intelliresearch-ai-multi-agent-system)
