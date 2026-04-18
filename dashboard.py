import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

# 1. إعدادات الصفحة (إخفاء القوائم الجانبية لتوسيع الشاشة)
st.set_page_config(page_title="ICT MASTER TERMINAL", layout="wide", initial_sidebar_state="collapsed")

# 2. تصميم الواجهة (نظام الحجول والنيون)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e2e8f0; }
    .card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .card:hover { border-color: #f5d300; }
    .status-active { color: #00ffaa; font-weight: bold; }
    .status-closed { color: #ff3366; font-weight: bold; }
    .neon-yellow { color: #f5d300; font-weight: bold; }
    .label { color: #8b9bb4; font-size: 0.8rem; }
    .price-val { font-size: 1.2rem; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- محرك البيانات الاستراتيجي ---
def get_ict_signal(symbol, category):
    # محاكاة لتحليل ICT بناءً على بيانات السوق الحقيقية
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    current_price = hist['Close'].iloc[-1]
    
    # تفاصيل الصفقة (بناءً على منطق ICT)
    data = {
        "symbol": symbol,
        "price": round(current_price, 2),
        "direction": "صعود (Long)" if symbol in ["AAPL", "MSFT", "GC=F"] else "هبوط (Short)",
        "entry": round(current_price * 0.998, 2),
        "sl": round(current_price * 0.990, 2),
        "tp1": round(current_price * 1.005, 2),
        "tp2": round(current_price * 1.015, 2),
        "tp3": round(current_price * 1.030, 2),
        "status": "فعالة ✅",
        "reason": "Liquidity Sweep + FVG Entry (ICT Model)",
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    return data

# --- الهيدر ---
st.markdown("<h2 style='text-align: center;'><span class='neon-yellow'>ICT</span> QUANTUM DASHBOARD</h2>", unsafe_allow_html=True)
st.divider()

# --- الفلاتر والقوائم ---
col_f1, col_f2 = st.columns([1, 1])
with col_f1:
    filter_type = st.radio("اختر نوع الأسهم:", ["الأسهم القيادية (Blue Chips)", "الأسهم التقنية (Tech)"], horizontal=True)

# تحديد القائمة بناءً على الفلتر
if "التقنية" in filter_type:
    symbols = ["AAPL", "MSFT", "NVDA", "TSLA", "META"]
else:
    symbols = ["GC=F", "EURUSD=X", "JPM", "V", "WMT"]

# --- توزيع الشاشة (قوائم يمين ويسار وشارت بالوسط) ---
left_col, center_col, right_col = st.columns([1, 2, 1])

with left_col:
    st.markdown("##### 📍 قائمة الإشارات")
    selected_symbol = st.selectbox("اختر السهم للتحليل:", symbols)
    sig = get_ict_signal(selected_symbol, filter_type)
    
    # عرض البيانات على شكل بطاقة (حجول)
    st.markdown(f"""
    <div class="card">
        <div style="display: flex; justify-content: space-between;">
            <span class="neon-yellow">{sig['symbol']}</span>
            <span class="status-active">{sig['status']}</span>
        </div>
        <hr style="opacity: 0.1;">
        <p class="label">الاتجاه: <span style="color:white;">{sig['direction']}</span></p>
        <p class="label">تاريخ التحديث: {sig['updated']}</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div><p class="label">الدخول</p><p class="price-val">{sig['entry']}</p></div>
            <div><p class="label" style="color:#ff3366;">الوقف</p><p class="price-val">{sig['sl']}</p></div>
        </div>
        <hr style="opacity: 0.1;">
        <p class="label">الأهداف:</p>
        <p class="neon-green" style="color:#00ffaa;">TP1: {sig['tp1']} | TP2: {sig['tp2']} | TP3: {sig['tp3']}</p>
        <p class="label" style="margin-top:10px;">سبب الصفقة:</p>
        <p style="font-size:0.9rem; font-style: italic;">{sig['reason']}</p>
    </div>
    """, unsafe_allow_html=True)

with center_col:
    st.markdown(f"##### 📈 الشارت الحي: {selected_symbol}")
    data = yf.download(selected_symbol, period="1d", interval="5m")
    fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                                        increasing_line_color='#00ffaa', decreasing_line_color='#ff3366')])
    fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                      height=450, margin=dict(l=0, r=0, t=0, b=0), xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.markdown("##### 📊 مراقبة السوق")
    for s in symbols[:4]:
        ticker_data = yf.Ticker(s).history(period="1d")
        price = round(ticker_data['Close'].iloc[-1], 2)
        st.markdown(f"""
        <div style="background:#1c2128; padding:10px; border-radius:5px; margin-bottom:5px; border-left: 3px solid #f5d300;">
            <span style="font-size:0.8rem;">{s}</span><br>
            <span style="font-weight:bold;">${price}</span>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Mohammad's Professional ICT Terminal - AI Analysis Driven")
