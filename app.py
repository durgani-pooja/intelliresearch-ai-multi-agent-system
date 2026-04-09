import streamlit as st
import os
from dotenv import load_dotenv
from agents.reader_agent import ReaderAgent
from agents.summarizer_agent import SummarizerAgent
from agents.insight_agent import InsightAgent
from agents.report_agent import ReportAgent
from agents.qa_agent import QAAgent

load_dotenv()

# --- PROFESSIONAL UI CONFIGURATION ---
st.set_page_config(page_title="IntelliResearch AI | Command Center", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .main-title {
        font-size: 3.5rem; font-weight: 800;
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .agent-header {
        display: flex; align-items: center; gap: 10px;
        color: #58a6ff; font-size: 1.5rem; font-weight: 600;
        margin-top: 20px;
    }
    .agent-card {
        background: #161b22; padding: 25px;
        border-radius: 15px; border: 1px solid #30363d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        line-height: 1.6;
    }
    code { color: #ff7b72; background: #21262d; padding: 2px 5px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-title">🧬 INTELLI-RESEARCH <span style="color:#bc8cff;">PRO</span></p>', unsafe_allow_html=True)
st.markdown("##### 🏛️ *Multi-Agent Academic Intelligence & Code Analysis*")
st.markdown("---")

# --- SIDEBAR CONTROL ---
with st.sidebar:
    st.markdown("### 🛠️ COMMAND MODULE")
    uploaded_file = st.file_uploader("📥 Ingest Research PDF", type="pdf")
    
    st.divider()
    st.markdown("### ❓ DEEP QUERY")
    user_question = st.text_input("Specific questions?", placeholder="e.g., Explain the algorithm...")
    
    analyze_btn = st.button("🚀 INITIATE ANALYSIS")
    
    st.divider()
    st.markdown("### 📡 SYSTEM HEALTH")
    if uploaded_file:
        st.success("✅ CORE LOADED")
    else:
        st.error("❌ NO DATA")

# --- MULTI-AGENT HANDOFF PIPELINE ---
if uploaded_file and analyze_btn:
    # 1. Reader Agent
    text = ReaderAgent().extract(uploaded_file)
    
    # Grid Layout for Agents
    col1, col2 = st.columns(2)
    
    with col1:
        # SUMMARIZER
        st.markdown('<div class="agent-header">📜 Executive Summary</div>', unsafe_allow_html=True)
        with st.spinner("🤖 Summarizer thinking..."):
            summary = SummarizerAgent().process(text)
            st.markdown(f"<div class='agent-card'>{summary}</div>", unsafe_allow_html=True)
            
        # CODE ANALYST (Extra Feature!)
        st.markdown('<div class="agent-header">💻 Code Logic Explainer</div>', unsafe_allow_html=True)
        with st.spinner("🔧 Breaking down code..."):
            # We use the Insight agent logic but prompt for code
            code_explanation = InsightAgent().process_code(text)
            st.markdown(f"<div class='agent-card'>{code_explanation}</div>", unsafe_allow_html=True)

    with col2:
        # INSIGHTS
        st.markdown('<div class="agent-header">💡 Technical Insights</div>', unsafe_allow_html=True)
        with st.spinner("🔍 Extraction active..."):
            insights = InsightAgent().process(summary, text)
            st.markdown(f"<div class='agent-card'>{insights}</div>", unsafe_allow_html=True)

        # QA AGENT
        if user_question:
            st.markdown(f'<div class="agent-header">🎯 Deep Query: {user_question}</div>', unsafe_allow_html=True)
            with st.spinner("🙋 QA Agent researching..."):
                ans = QAAgent().answer(user_question, text)
                st.markdown(f"<div class='agent-card' style='border: 1px solid #bc8cff;'>{ans}</div>", unsafe_allow_html=True)

    # FINAL REPORT
    st.markdown("---")
    st.markdown('<div class="agent-header">🏆 Final Comprehensive Report</div>', unsafe_allow_html=True)
    with st.spinner("📊 Synthesizing data..."):
        report = ReportAgent().generate(summary, insights)
        st.markdown(f"<div class='agent-card'>{report}</div>", unsafe_allow_html=True)