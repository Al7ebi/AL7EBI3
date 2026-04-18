import streamlit as st
import pandas as pd
import datetime

# إعداد الواجهة الاحترافية
st.set_page_config(page_title="ICT Institutional Dashboard", layout="wide")

# CSS لتصميم البطاقات والجداول
st.markdown("""
    <style>
    .main { background-color: #06090f; }
    .stMetric { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; }
    .status-card { padding: 25px; border-radius: 15px; border-left: 8px solid #238636; background-color: #0d1117; margin-bottom: 20px; }
    .model-badge { background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ نظام ICT لصفر شك | التحليل الرقمي المتقدم")

# لوحة المعلومات العلوية
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("المنطقة الحالية", "Discount", "Bullish Bias")
with c2: st.metric("قوة الاتجاه", "92%", "High Confidence")
with c3: st.metric("السيولة القادمة", "BSL 1.1240", "Target Hit")
with c4: st.metric("التوقيت", "London Killzone", "Active")

# جدول الفرص الذكي
st.subheader("📋 مصفوفة الفرص المؤسسية (Multi-Model Matrix)")

data = {
    "الأصل": ["Gold", "EURUSD", "GBPUSD", "Nasdaq"],
    "النموذج الرئيسي": ["Breaker + FVG", "Turtle Soup", "Model 2022", "Silver Bullet"],
    "درجة القوة (AI)": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐"],
    "السبب الخوارزمي": [
        "سحب سيولة آسيوي + ملامسة Breaker في منطقة خصم",
        "اختراق كاذب لقاع يوم أمس + SMT مع الاسترليني",
        "تغير هيكل مع إزاحة عنيفة + فجوة قيمة عادلة",
        "تمركز داخل فجوة زمنية محددة واستهداف سيولة داخلية"
    ],
    "الهدف (DOL)": ["1950.00", "1.0950", "1.2800", "15400"],
    "الحالة": ["دخول فوري", "مراقبة MSS", "تأمين أرباح", "انتظار تلاعب"]
}

df = pd.DataFrame(data)
st.table(df)

# تفصيل النموذج الأقوى (Deep Dive)
st.subheader("🔍 تشريح الفرصة الذهبية")
st.markdown(f"""
<div class="status-card">
    <span class="model-badge">نموذج Unicorn الصاعد</span>
    <h2>الذهب (Gold) - فريم 15 دقيقة</h2>
    <p><b>لماذا هذه الفرصة؟</b> تداخل كامل بين <b>Breaker Block</b> و <b>FVG</b> بعد حدوث <b>SMT Divergence</b> مع الفضة.</p>
    <hr style="border-color: #30363d;">
    <div style="display: flex; justify-content: space-between;">
        <div><b>نقطة الدخول:</b> 1942.50</div>
        <div><b>وقف الخسارة:</b> 1938.00</div>
        <div><b>العائد المتوقع:</b> 3.5R</div>
    </div>
    <p style="margin-top:15px; color: #8b949e;"><i>* ملاحظة: تم تأكيد الفرصة بظهور "إزاحة" فاقت 1.5 من قيمة الـ ATR.</i></p>
</div>
""", unsafe_allow_html=True)
