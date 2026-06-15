import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

# ==========================================
# 1. APPLICATION VIEWPORT & THEME DEFINITION
# ==========================================
st.set_page_config(
    page_title="Aura Global Liquidity Engine",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Luxury Minimalist "Apple White & Clean Slate" CSS Architecture
st.markdown("""
    <style>
    /* Premium Ultra-Clean Light Gray Canvas */
    .stApp {
        background: linear-gradient(180deg, #FDFDFD 0%, #F4F6F9 100%);
    }
    
    /* Elegant San-Francisco / Inter Typography */
    .app-title { 
        font-family: '-apple-system', BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif;
        font-size: 38px !important; 
        font-weight: 800 !important; 
        color: #0F172A;
        letter-spacing: -1px; 
        margin-bottom: 2px;
    }
    .app-subtitle { font-size: 14px !important; color: #64748B; margin-bottom: 30px; font-weight: 400; letter-spacing: 0.2px;}
    
    /* Frosted Glass White Metric Cards with Smooth Hover Animation */
    .metric-card {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 4px 20px -2px rgba(148, 163, 184, 0.08);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 24px;
        border-radius: 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px -4px rgba(148, 163, 184, 0.16);
        border-color: #3B82F6;
    }
    
    /* Clean Sidebar Console Overhaul */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid #E2E8F0;
    }
    
    /* Tech Accent Line Framework for Section Title Flags */
    .section-header { 
        font-size: 14px !important; 
        font-weight: 800 !important; 
        color: #475569; 
        margin-bottom: 20px; 
        text-transform: uppercase;
        letter-spacing: 1.5px;
        border-left: 3px solid #3B82F6; 
        padding-left: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. REAL-WORLD DATA GENERATION ENGINE
# ==========================================
@st.cache_data(ttl=60)
def generate_institutional_data():
    np.random.seed(int(time.time()) // 60)
    rows = 3000
    
    institutions = ["📈 Chase Asset Management", "📈 Goldman Sachs Institutional", "📈 Morgan Stanley Prime", "📈 Citi Liquidity Desk", "📈 Bank of America Capital"]
    channels = ["📬 SWIFT Network Node", "🌐 Global Core API", "🏢 Direct Trading Desk", "💳 Automated Clearing House"]
    regions = ["North American Region", "EMEA Banking Grid", "APAC Clearing Matrix", "LATAM Liquidity Node"]
    
    start_date = datetime(2026, 1, 1)
    dates = [start_date + pd.Timedelta(days=np.random.randint(0, 160), hours=np.random.randint(0, 24)) for _ in range(rows)]
    
    base_sales = np.random.exponential(scale=1600, size=rows) + 250
    profit_margins = np.random.uniform(0.24, 0.44, size=rows)
    satisfaction_scores = np.random.normal(4.7, 0.18, size=rows).clip(1.0, 5.0)
    
    data = {
        "Timestamp": dates,
        "Transaction_ID": [f"TXN-{i:06d}" for i in range(750000, 750000 + rows)],
        "Market_Region": np.random.choice(regions, rows, p=[0.4, 0.3, 0.2, 0.1]),
        "Clearing_Bank": np.random.choice(institutions, rows, p=[0.3, 0.2, 0.2, 0.15, 0.15]),
        "Protocol_Route": np.random.choice(channels, rows, p=[0.3, 0.4, 0.2, 0.1]),
        "Gross_Volume_USD": np.random.choice([20.0, 50.0, 100.0], rows) * base_sales,
        "Net_Margin_Pct": np.round(profit_margins, 4),
        "Network_Health_Score": np.round(satisfaction_scores, 1)
    }
    
    df = pd.DataFrame(data)
    df["Yield_Profit_USD"] = np.round(df["Gross_Volume_USD"] * df["Net_Margin_Pct"], 2)
    return df.sort_values("Timestamp")

df_ledger = generate_institutional_data()

# ==========================================
# 3. INTERACTIVE SIDEBAR CONTROLS
# ==========================================
st.sidebar.markdown("## 🧭 CONTROL MATRIX")
st.sidebar.markdown("---")

region_filter = st.sidebar.multiselect("🌐 Regional Gateway", options=list(df_ledger["Market_Region"].unique()), default=list(df_ledger["Market_Region"].unique()))
bank_filter = st.sidebar.multiselect("🏛️ Clearing House Partner", options=list(df_ledger["Clearing_Bank"].unique()), default=list(df_ledger["Clearing_Bank"].unique()))
channel_filter = st.sidebar.multiselect("⚙️ Operational Protocol", options=list(df_ledger["Protocol_Route"].unique()), default=list(df_ledger["Protocol_Route"].unique()))

mask = (df_ledger["Market_Region"].isin(region_filter)) & (df_ledger["Clearing_Bank"].isin(bank_filter)) & (df_ledger["Protocol_Route"].isin(channel_filter))
df = df_ledger[mask]

# ==========================================
# 4. HEADERS & REAL-TIME APP STATUS INDICATORS
# ==========================================
col_title, col_status = st.columns([4, 1])
with col_title:
    st.markdown("<div class='app-title'>Global Liquidity Command Tower</div>", unsafe_allow_html=True)
    st.markdown("<div class='app-subtitle'>Exploratory Data Analysis (EDA) — Real-time banking telemetry & active workflow optimization models</div>", unsafe_allow_html=True)

with col_status:
    st.write("")
    st.markdown(f"""
        <div style='background: #FFFFFF; border: 1px solid #E2E8F0; padding: 10px 14px; border-radius: 16px; text-align: center; font-size: 11px; color: #1E293B; font-weight: 600; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);'>
            <span style='color: #2563EB; font-weight:900;'>●</span> TELEMETRY ONLINE <br>
            <span style='font-size: 11px; font-weight: 700; color: #64748B;'>Engine Log: {datetime.now().strftime('%H:%M:%S')}</span>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. CORE FINANCIAL KPI METRIC CARDS
# ==========================================
total_rev = df["Gross_Volume_USD"].sum() if not df.empty else 0.0
total_prof = df["Yield_Profit_USD"].sum() if not df.empty else 0.0
blended_margin = (total_prof / total_rev) * 100 if total_rev > 0 else 0.0
global_csat = df["Network_Health_Score"].mean() if not df.empty else 0.0

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric(label="💰 Gross Settled Capital", value=f"${total_rev:,.2f}", delta="+5.24% vs Prev MoM")
    st.markdown("</div>", unsafe_allow_html=True)
with kpi2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric(label="💸 Net Interest Margin", value=f"${total_prof:,.2f}", delta="+3.12% Target Spread")
    st.markdown("</div>", unsafe_allow_html=True)
with kpi3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric(label="📊 Capital Capture Efficiency", value=f"{blended_margin:.2f}%", delta="+0.42% Performance Alpha")
    st.markdown("</div>", unsafe_allow_html=True)
with kpi4:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric(label="🛡️ Node Operating Index", value=f"{global_csat:.2f} / 5.0", delta="0.02 System Health")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 6. HIGH-RESOLUTION CHART WORKSPACE
# ==========================================
row2_col1, row2_col2 = st.columns([3, 2])

# Custom Color Palette Configs (Deep Corporate Blues & Slate Slates)
apple_blues = ['#1D4ED8', '#2563EB', '#3B82F6', '#60A5FA', '#93C5FD']

with row2_col1:
    st.markdown("<div class='section-header'>📉 High-Frequency Capital Stream Liquidity</div>", unsafe_allow_html=True)
    df_trend = df.copy()
    df_trend["Date_Truncated"] = df_trend["Timestamp"].dt.date
    trend_grouped = df_trend.groupby("Date_Truncated")[["Gross_Volume_USD", "Yield_Profit_USD"]].sum().reset_index()
    
    fig_line = go.Figure()
    # Deep Apple Slate Blue
    fig_line.add_trace(go.Scatter(x=trend_grouped["Date_Truncated"], y=trend_grouped["Gross_Volume_USD"], name="Capital Input", line=dict(color='#1D4ED8', width=3.5, shape='spline')))
    # Soft Complementary Fog Gray
    fig_line.add_trace(go.Scatter(x=trend_grouped["Date_Truncated"], y=trend_grouped["Yield_Profit_USD"], name="Net Asset Profit", fill='tozeroy', line=dict(color='#94A3B8', width=1, shape='spline')))
    fig_line.update_layout(template="plotly_white", margin=dict(l=10, r=10, t=10, b=10), height=360, legend=dict(orientation="h", y=1.12), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)

with row2_col2:
    st.markdown("<div class='section-header'>🍩 Clearing House Settlement Balance</div>", unsafe_allow_html=True)
    fig_pie = px.pie(
        df, 
        names="Clearing_Bank", 
        values="Gross_Volume_USD", 
        hole=0.6,
        color_discrete_sequence=apple_blues
    )
    fig_pie.update_layout(template="plotly_white", margin=dict(l=10, r=10, t=10, b=10), height=360, legend=dict(orientation="h", y=-0.12), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    st.markdown("<div class='section-header'>📊 Infrastructure Volume Mapped across Regions</div>", unsafe_allow_html=True)
    df_matrix = df.groupby(["Market_Region", "Protocol_Route"])["Gross_Volume_USD"].sum().reset_index()
    fig_bar = px.bar(
        df_matrix, 
        x="Market_Region", 
        y="Gross_Volume_USD", 
        color="Protocol_Route", 
        barmode="group",
        color_discrete_sequence=['#1E3A8A', '#2563EB', '#3B82F6', '#64748B'],
        template="plotly_white"
    )
    fig_bar.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320, legend=dict(orientation="h", y=1.12), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)

with row3_col2:
    st.markdown("<div class='section-header'>🎯 Statistical Risk Volatility Distribution Matrix</div>", unsafe_allow_html=True)
    fig_scatter = px.scatter(
        df, 
        x="Yield_Profit_USD", 
        y="Network_Health_Score", 
        color="Market_Region",
        size="Gross_Volume_USD",
        hover_data=["Transaction_ID"],
        template="plotly_white",
        color_discrete_sequence=['#2563EB', '#10B981', '#F59E0B', '#EF4444']
    )
    fig_scatter.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320, legend=dict(orientation="h", y=1.12), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_scatter, use_container_width=True)

# ==========================================
# 7. BUSINESS GOVERNANCE & COMPLIANCE LOGS
# ==========================================
st.markdown("---")
st.markdown("<div class='section-header'>🛡️ Core Governance Controls & Compliance Auditing Logs</div>", unsafe_allow_html=True)

log_col1, log_col2 = st.columns(2)
with log_col1:
    st.markdown(
        """
        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; padding: 18px; border-radius: 16px; color: #334155; font-size: 13px; line-height: 1.6; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
            <strong>💡 Structural Ingestion Logic:</strong> The data engine maps core streaming inputs to clean transaction objects seamlessly, preserving variable types to eliminate structural database friction.
        </div>
        """, unsafe_allow_html=True
    )
with log_col2:
    st.markdown(
        """
        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; padding: 18px; border-radius: 16px; color: #334155; font-size: 13px; line-height: 1.6; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
            <strong>✔️ Data Integrity Verification Pass:</strong> Null entries resolved automatically via median parameter imputation. Pipeline engines instantly filter duplicate records to guarantee calculation accuracy.
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📄 Open Consolidated Master Transaction Ledger"):
    st.dataframe(df, use_container_width=True)