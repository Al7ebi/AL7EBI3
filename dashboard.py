import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
from datetime import datetime

# 1. إعدادات الواجهة (Dark Professional Theme)
st.set_page_config(page_title="QUANTUM TERMINAL // LIVE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #8b9bb4; font-family: 'Consolas', monospace; }
    .neon-yellow { color: #f5d300; text-shadow: 0 0 5px #f5d300; }
    .card { background-color: #151a22; border: 1px solid #1f2937; border-radius: 8px; padding: 20px; margin-bottom: 15px; }
    .big-val { font-size: 2.5rem; font-weight: bold; color: #f5d300; }
    h5 { color: #ffffff; border-bottom: 1px solid #1f2937; padding-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 2. محرك البيانات الحية
def get_live_market_data(ticker):
    data = yf.download(ticker, period="1d", interval="5m")
    return data

# --- الهيدر (Header) ---
h1, h2, h3 = st.columns([2, 3, 2])
with h1:
    st.markdown("### MARKET PULSE <br><span class='neon-yellow'>// G R I D</span>", unsafe_allow_html=True)
with h2:
    st.markdown(f"<div style='text-align:center; padding-top:15px;'><span style='color:#00ffaa'>SESSION: ACTIVE</span> | SCANNER: 1.2K/HR | PNL: <span class='neon-yellow'>+$12,184</span></div>", unsafe_allow_html=True)
with h3:
    st.markdown(f"<h3 style='text-align:right;'>{datetime.now().strftime('%H:%M:%S')} <span class='neon-yellow'>LIVE</span></h3>", unsafe_allow_html=True)

st.divider()

# --- توزيع المربعات (Grid Layout) ---
col_left, col_main, col_right = st.columns([1, 2.5, 1])

# العمود الأيسر (الرادار)
with col_left:
    st.markdown("##### 📡 SIGNAL RADAR")
    st.info("🟡 **GOLD**: Potential Liquidity Sweep")
    st.success("🟢 **EURUSD**: Bullish FVG Detected")
    st.warning("🔴 **BTC**: High Volatility Zone")
    
    st.markdown("<br>##### 📊 DESK METRICS", unsafe_allow_html=True)
    st.markdown("<p class='big-val'>51x</p><small>CAPITAL VELOCITY</small>", unsafe_allow_html=True)

# العمود الأوسط (الشارت الحي)
with col_main:
    st.markdown("##### 📈 LIVE CHART: GOLD (XAU/USD)")
    try:
        df = get_live_market_data("GC=F") # بيانات الذهب الحقيقية
        current_price = df['Close'].iloc[-1]
        
        # رسم الشارت الاحترافي
        fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
                                            increasing_line_color='#00ffaa', decreasing_line_color='#ff3366')])
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          margin=dict(l=0, r=0, t=0, b=0), height=450, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.error("جاري انتظار بيانات السوق المفتوحة...")

# العمود الأيمن (الحيتان والتنفيذ)
with col_right:
    st.markdown("##### 🐋 WHALE WATCH")
    st.markdown("🐳 0xe41... <span style='color:#00ffaa'>$40.3K (BUY)</span>", unsafe_allow_html=True)
    st.markdown("🐳 0xa22... <span style='color:#ff3366'>$11.2K (SELL)</span>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("##### 🏹 EXECUTE SIGNAL")
    entry = st.number_input("Entry Price", format="%.2f")
    if st.button("EXECUTE QUANTUM ORDER"):
        st.toast("Order sent to Global Pool")
        st.balloons()

st.markdown("<br><center><small>Mohammad's Private Terminal v3.0 // Powered by ICT Methodology</small></center>", unsafe_allow_html=True)
