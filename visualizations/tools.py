import streamlit as st, pandas as pd, glob, os, time, random

@st.cache_data(ttl=20)   # refresh every 20 s
def last_winners():
    files = sorted(glob.glob("Winners/*.csv"), key=os.path.getctime, reverse=True)
    return pd.read_csv(files[0]) if files else pd.DataFrame()

def matrix_rain_placeholder(height=200):
    rain = ''.join(random.choice('01アイウエオ') for _ in range(height*4))
    return f'<div style="opacity:0.08;font-size:18px;line-height:10px;">{rain}</div>'
