import streamlit as st
st.set_page_config(page_title="NUCLEAR DOMAIN OS 2026", page_icon="☢️",
                  layout="centered", initial_sidebar_state="expanded")

# ----  MATRIX THEME (shared) ----
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{background:#000;color:#00ff00;}
[data-testid="stSidebar"]{background:#000;border-right:1px solid #00ff00;}
a.streamlit-page-link{background:#000;color:#00ff00;border:1px solid #00ff00;}
.glitch{animation:glitch 2s infinite}@keyframes glitch{0%,100%{text-shadow:0.05em 0 0 #00ff00,-0.05em 0 0 #00ff00}15%{text-shadow:-0.05em -0.05em 0 #00ff00,0.05em 0.05em 0 #00ff00}}
</style>""", unsafe_allow_html=True)

# ----  SIDEBAR NAV ----
with st.sidebar:
    st.markdown("# ☢️  AGENT CONSOLE")
    st.page_link("pages/01_🔍_Extractor.py",        label="Extractor",       icon="🔍")
    st.page_link("pages/02_✅_Verifier.py",         label="Verifier",        icon="✅")
    st.page_link("pages/03_🌐_Translator.py",      label="Translator",      icon="🌐")
    st.page_link("pages/04_📜_Historian.py",       label="Historian",       icon="📜")
    st.page_link("pages/05_📊_Analyst.py",         label="Analyst",         icon="📊")
    st.page_link("pages/06_🧠_Orchestrator.py",    label="Orchestrator",    icon="🧠")
    st.page_link("pages/07_📈_Visualization.py",   label="Visualization",   icon="📈")
    st.page_link("pages/08_💾_Storage.py",         label="Storage",         icon="💾")
    st.page_link("pages/09_🔐_Trust_Engine.py",    label="Trust Engine",    icon="🔐")
    st.page_link("pages/10_🏛️_Museum_Curator.py", label="Museum Curator",  icon="🏛️")
    st.page_link("pages/11_🌍_Internationalization.py", label="I18n", icon="🌍")
    st.markdown("---")
    st.success("All 11 agents ONLINE")

# ----  HOME PAGE ----
st.markdown('<h1 class="glitch">NUCLEAR DOMAIN OS 2026</h1>', unsafe_allow_html=True)
st.markdown("### 1024-Dimensional Intelligence System")
st.markdown("Select an agent from the sidebar to begin the eternal hunt.")
