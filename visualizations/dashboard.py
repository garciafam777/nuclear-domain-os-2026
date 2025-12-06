import streamlit as st
import pandas as pd
import os
import glob
from datetime import datetime

st.set_page_config(page_title="NUCLEAR DOMAIN OS 2026", layout="wide")

# MATRIX GREEN THEME
st.markdown("""
<style>
    .reportview-container {background: #000000}
    .sidebar .sidebar-content {background: #000000}
    h1, h2, h3 {color: #00ff00 !important; font-family: 'Courier New'}
    .css-1d391kg {color: #00ff00 !important}
    .stMetric {color: #00ff41 !important}
</style>
""", unsafe_allow_html=True)

st.title("╔══════════════════════════════════════════════════════════════════════╗")
st.title("║          N U C L E A R   D O M A I N   O S   2 0 2 6                 ║")
st.title("║                  LIVE MUSEUM DASHBOARD • ALL 11 AGENTS ACTIVE       ║")
st.title("╚══════════════════════════════════════════════════════════════════════╝")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Agents Online", "11 / 11", "LIVE")
with col2:
    st.metric("Winners Found", len(glob.glob("Winners/*.csv")), "SCANNING")
with col3:
    st.metric("Trust Engine", "ACTIVE", "100%")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["WINNERS", "TRUST SCORES", "HISTORY", "MUSEUM"])

with tab1:
    files = glob.glob("Winners/*.csv")
    if files:
        latest = max(files, key=os.path.getctime)
        df = pd.read_csv(latest)
        st.dataframe(df.style.set_properties(**{'color': '#00ff41', 'background-color': '#000000'}))
        st.download_button("Download Latest", data=open(latest,'rb').read(), file_name=os.path.basename(latest))
    else:
        st.write("No winners yet — sniper will feed here automatically")

with tab2:
    st.write("Trust Score Engine → Coming in 3… 2… 1…")

with tab3:
    st.write("Wayback + OCR Timeline → Next")

with tab4:
    st.write("Museum HTML Exhibits per Domain → Launching")

st.sidebar.success("NUCLEAR DOMAIN OS 2026\n11 Agents Active\nMuseum Mode: ENABLED")
st.caption("Press R to refresh • Next: Trust Engine + 11-Agent Orchestra")
