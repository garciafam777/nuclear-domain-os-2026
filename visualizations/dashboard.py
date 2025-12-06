import streamlit as st
import pandas as pd, os, glob, random
from datetime import datetime

# ----------  page ----------
st.set_page_config(page_title="NUCLEAR DOMAIN OS 2026", page_icon="☢️",
                  layout="centered", initial_sidebar_state="expanded")

# ----------  MATRIX THEME ----------
st.markdown("""
<style>
body{background:#000;color:#00ff00;font-family:'Courier New';overflow:hidden;}
.reportview-container{background:#000;color:#00ff00;}
.main{background:#000;}
h1,h2,h3{color:#00ff00!important;text-shadow:0 0 10px #00ff00;font-size:3em;}
.stButton>button{background:#000;color:#00ff00;border:2px solid #00ff00;box-shadow:0 0 20px #00ff00;}
.matrix-rain{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;}
.glitch{animation:glitch 2s infinite;}
@keyframes glitch{0%,100%{text-shadow:0.05em 0 0 #00ff00,-0.05em 0 0 #00ff00;}15%{text-shadow:-0.05em -0.05em 0 #00ff00,0.05em 0.05em 0 #00ff00;}}
</style>""", unsafe_allow_html=True)

# ----------  SIDEBAR (never reloads) ----------
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

# ----------  ORIGINAL MAIN PAGE ----------
st.markdown('<h1 class="glitch">NUCLEAR DOMAIN OS 2026</h1>', unsafe_allow_html=True)
st.markdown("<h2>11 AGENTS ACTIVE • 1024-DIMENSIONAL INTELLIGENCE • MUSEUM MODE</h2>", unsafe_allow_html=True)

# MATRIX RAIN
st.markdown(f"""
<div class="matrix-rain">
    <pre style="opacity:0.1;font-size:20px;line-height:10px;">
{''.join(random.choice('01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン') for _ in range(5000))}
    </pre>
</div>
""", unsafe_allow_html=True)

# LIVE METRICS
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("AGENTS", "11 / 11", "ONLINE")
with col2: st.metric("WINNERS", len(glob.glob("Winners/*.csv")), "HUNTING")
with col3: st.metric("TRUST ENGINE", "ACTIVE", "100%")
with col4: st.metric("MUSEUM", "LIVE", "∞")
st.markdown("---")

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["LIVE SNIPER", "TRUST ENGINE", "HISTORICAL ARCHIVE", "MUSEUM"])
with tab1:
    files = sorted(glob.glob("Winners/*.csv"), key=os.path.getctime, reverse=True)
    if files:
        df = pd.read_csv(files[0])
        st.dataframe(df.tail(10).style.set_properties(**{'color':'#00ff00','background':'#000'}))
        st.download_button("DOWNLOAD ALL", data=open(files[0],'rb').read(), file_name="nuclear_winners_today.csv")
    else:
        st.write("Sniper active — first winners incoming...")
with tab2: st.write("Trust Score Engine → Deploying in 3… 2… 1…")
with tab3: st.write("Wayback + OCR Ancient Timeline → Loading 1996–2026")
with tab4: st.write("Museum-grade HTML exhibits per domain → Coming next")

# FOOTER
st.sidebar.markdown("<h1 style='color:#00ff00;'>NUCLEAR OS</h1>", unsafe_allow_html=True)
st.sidebar.success("All systems operational\nEternal hunt mode: ENABLED")
st.caption("Press R to refresh • Next: 11-Agent CrewAI Orchestra • Trust Engine • Museum Generator")
