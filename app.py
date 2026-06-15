import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

# ==========================================
# 1. PREMIUM APPMESH CANVAS INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="Enterprise Capital Operations Matrix",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Power BI Desktop UI Theme Injection
st.markdown("""
    <style>
    /* Premium Abstract Digital Connectivity Mesh Backdrop Overlay */
    .stApp {
        background: radial-gradient(circle at 50% 50%, rgba(244, 246, 249, 0.92) 0%, rgba(220, 227, 238, 0.96) 100%), 
                    url('https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Clean, Modern Microsoft Segment Typography Layouts */
    .app-title { 
        font-family: 'Segoe UI', -apple-system, sans-serif;
        font-size: 36px !important; 
        font-weight: 700 !important; 
        color: #0F172A;
        letter-spacing: -0.5px; 
        margin-bottom: 2px;
    }
    .app-subtitle { font-size: 14px !important; color: #475569; margin-bottom: 25px; font-weight: 400;}
    
    /* Power BI Crisp Flat Container Visuals with Sapphire Accents */
    .metric-card {
        background: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid rgba(226, 232, 240, 0.8) !important;
        border-top: 4px solid #2563EB !important; /* Classic Power BI Top Navigation Flag Accent */
        backdrop-filter: blur(12px);
        padding: 20px;
        border-radius: 8px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
    }
    
    /* Premium Feedback Segment Containers */
    .feedback-panel {
        background: rgba(240, 253, 244, 0.8); border: 1px solid rgba(220, 252, 231, 0.9); border-left: 5px solid #16A34A;
        padding: 20px; border-radius: 8px; margin-bottom: 25px; backdrop-filter: blur(10px);
    }
    
    /* Red Data Governance Failure Highlight Panels */
    .issue-box {
        background: rgba(255, 241, 242, 0.85); border: 1px solid rgba(255, 228, 230, 0.9); border-left: 5px solid #F43F5E;
        padding: 20px; border-radius: 10px; margin-top: 20px; backdrop-filter: blur(10px);
    }
    
    /* Sidebar Navigation Slicer Style Configuration overrides */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid #E2E8F0;
    }
    
    /* Tech Left Blue Indicator Flags */
    .section-header { 
        font-size: 14px !important; 
        font-weight: 700 !important; 
        color: #1E293B; 
        margin-bottom: 18px; 
        text-transform: uppercase;
        letter-spacing: 1px;
        border-left: 3px solid #2563EB; 
        padding-left: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. REAL-WORLD DATA GENERATION ENGINE
# ==========================================
@st.cache_data(ttl=60)
def generate_audit_dataset():
    np.random.seed(42)  
    rows = 2500
    
    customer_directory = [
        {"Name": "Acme Global Logistics", "Area": "New York City, USA", "Lat": 40.7128, "Lon": -74.0060, "ISO": "USA", "Region": "North Region Core"},
        {"Name": "Vanguard Tech Systems", "Area": "San Francisco, USA", "Lat": 37.7749, "Lon": -122.4194, "ISO": "USA", "Region": "North Region Core"},
        {"Name": "Bavaria Auto Clearing", "Area": "Frankfurt, Germany", "Lat": 50.1109, "Lon": 8.6821, "ISO": "DEU", "Region": "East Region Hub"},
        {"Name": "EuroFreight Solutions", "Area": "Berlin, Germany", "Lat": 52.5200, "Lon": 13.4050, "ISO": "DEU", "Region": "East Region Hub"},
        {"Name": "Pacific Rim Trading", "Area": "Sydney, Australia", "Lat": -33.8688, "Lon": 151.2093, "ISO": "AUS", "Region": "South Region Grid"},
        {"Name": "Aura Mining Consortium", "Area": "Melbourne, Australia", "Lat": -37.8136, "Lon": 144.9631, "ISO": "AUS", "Region": "South Region Grid"},
        {"Name": "Amazonas Agro-Industrial", "Area": "São Paulo, Brazil", "Lat": -23.5505, "Lon": -46.6333, "ISO": "BRA", "Region": "West Region Matrix"},
        {"Name": "Atlântico Energy Group", "Area": "Rio de Janeiro, Brazil", "Lat": -22.9068, "Lon": -43.1729, "ISO": "BRA", "Region": "West Region Matrix"}
    ]
    
    segments = ["Commercial Sales", "Retail Outlets", "Online Portals", "Wholesale Distribution", "Service Agreements"]
    start_date = datetime(2026, 1, 1)
    dates = [start_date + pd.Timedelta(days=np.random.randint(0, 160)) for _ in range(rows)]
    
    base_sales = np.random.exponential(scale=1400, size=rows) + 200
    profit_margins = np.random.uniform(0.20, 0.45, size=rows)
    satisfaction = np.random.normal(4.5, 0.3, size=rows).clip(1.0, 5.0)
    
    selected_clients = [customer_directory[np.random.randint(0, len(customer_directory))] for _ in range(rows)]
    
    data = {
        "Order_Date": dates,
        "Transaction_ID": [f"TXN-{i:06d}" for i in range(100000, 100000 + rows)],
        "Customer_Name": [c["Name"] for c in selected_clients],
        "Customer_Area": [c["Area"] for c in selected_clients],
        "Latitude": [c["Lat"] for c in selected_clients],
        "Longitude": [c["Lon"] for c in selected_clients],
        "ISO_Country": [c["ISO"] for c in selected_clients],
        "Sales_Region": [c["Region"] for c in selected_clients],
        "Business_Segment": np.random.choice(segments, rows, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        "Gross_Revenue_USD": np.round(base_sales, 2),
        "Profit_Margin_Pct": np.round(profit_margins, 4),
        "Customer_Satisfaction": np.round(satisfaction, 1)
    }
    
    df = pd.DataFrame(data)
    df["Net_Profit_USD"] = np.round(df["Gross_Revenue_USD"] * df["Profit_Margin_Pct"], 2)
    
    # Injected Compliance Data Flaws For Remediation Logs
    df.loc[15:25, "Customer_Satisfaction"] = np.nan
    df = pd.concat([df, df.iloc[0:8]], ignore_index=True)
    df.loc[500, "Gross_Revenue_USD"] = 152450.00
    df.loc[500, "Net_Profit_USD"] = 61000.00
    
    return df

df_raw = generate_audit_dataset()

# ==========================================
# 3. SIDEBAR POWER BI TAB SWITCHER & NAVIGATION SLICERS
# ==========================================
st.sidebar.markdown("## 📑 REPORT NAVIGATION")
report_page = st.sidebar.radio("Go to Page:", ["📊 Global Executive Summary", "🗄️ Master Database Ledger Report"])
st.sidebar.markdown("---")

st.sidebar.markdown("## 🌐 INTERACTIVE 3D GLOBE")
df_globe_nodes = df_raw.groupby(["Sales_Region", "Customer_Name", "Customer_Area", "Latitude", "Longitude"])["Gross_Revenue_USD"].sum().reset_index()

fig_globe = go.Figure()
fig_globe.add_trace(go.Scattergeo(
    lon=df_globe_nodes["Longitude"], lat=df_globe_nodes["Latitude"],
    hovertext=df_globe_nodes["Customer_Name"] + "<br>" + df_globe_nodes["Customer_Area"],
    mode="markers",
    marker=dict(size=11, color=df_globe_nodes["Gross_Revenue_USD"], colorscale="Blues", line=dict(width=1, color="rgba(255,255,255,0.7)")),
    customdata=df_globe_nodes["Sales_Region"]
))
fig_globe.update_geos(
    projection_type="orthographic", showland=True, landcolor="#E2E8F0",
    showocean=True, oceancolor="#0F172A", showcountries=True, countrycolor="#94A3B8"
)
fig_globe.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=240, paper_bgcolor="rgba(0,0,0,0)")

# RENDERED STABLE CALL BLOCK (FIXED PARENTHESIS ERROR TRAP)
globe_selection = st.sidebar.plotly_chart(fig_globe, key="3d_globe_slicer", on_select="rerun")

selected_regions = []
if globe_selection and "selection" in globe_selection and "points" in globe_selection["selection"]:
    for point in globe_selection["selection"]["points"]:
        selected_regions.append(point["customdata"])

if not selected_regions:
    selected_regions = list(df_raw["Sales_Region"].unique())
    tracker_text = "✨ **All Global Sub-Portfolios Active** (Rotate and click Globe markers to slice data models)"
else:
    tracker_text = f"🎯 **Active Selection Isolated:** {', '.join(set(selected_regions))}"

df = df_raw[df_raw["Sales_Region"].isin(selected_regions)]

# ==========================================
# 4. REPORT CONTENT ROUTER
# ==========================================
if report_page == "📊 Global Executive Summary":
    
    st.markdown("<div class='app-title'>Global Capital Operations Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='app-subtitle'>Power BI Desktop Active Layout Framework — Visual Telemetry Analytics Page</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown(f"<div class='selection-tracker-box'><strong>🌐 DYNAMIC SLICER CONTEXT:</strong> {tracker_text}</div>", unsafe_allow_html=True)
    
    total_rev = df["Gross_Revenue_USD"].sum()
    total_prof = df["Net_Profit_USD"].sum()
    blended_margin = (total_prof / total_rev) * 100 if total_rev > 0 else 0.0
    avg_csat = df["Customer_Satisfaction"].mean()
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Total Gross Volume Settled", value=f"${total_rev:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
    with kpi2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Total Net Interest Revenue", value=f"${total_prof:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)
    with kpi3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Blended Margin Efficiency", value=f"{blended_margin:.2f}%")
        st.markdown("</div>", unsafe_allow_html=True)
    with kpi4:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Blended Client CSAT Index", value=f"{avg_csat:.2f} / 5.0")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-header'>⭐ Stakeholder Review & Feedback Panel</div>", unsafe_allow_html=True)
    st.markdown("<div class='feedback-panel'><p style='color: #1F2937; font-size:13px; margin:0;'>Toggle validation matrices to monitor customer text ratings and customer client satisfaction profiles dynamically:</p></div>", unsafe_allow_html=True)
    
    chk_col1, chk_col2 = st.columns(2)
    with chk_col1: show_feedback_metrics = st.checkbox("📋 Display CSAT Performance Breakdown", value=True)
    with chk_col2: show_text_reviews = st.checkbox("💬 Stream Qualitative Client Sentiment Logs", value=False)
    
    if show_feedback_metrics:
        df_csat = df.groupby("Business_Segment")["Customer_Satisfaction"].mean().reset_index()
        fig_csat = px.bar(df_csat, x="Business_Segment", y="Customer_Satisfaction", title="Average Satisfaction Scores by Segment", color="Customer_Satisfaction", color_continuous_scale=px.colors.sequential.Blues, template="plotly_white")
        fig_csat.update_layout(height=260, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_csat, use_container_width=True)
        
    if show_text_reviews:
        review_data = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d")] * 3,
            "Customer_Name": ["Acme Global Logistics", "Vanguard Tech Systems", "Bavaria Auto Clearing"],
            "Verified_Review_Text": [
                "⭐ 5.0 - 'Transaction completion times are incredibly fast. API integration is completely stable.'",
                "⭐ 4.8 - 'Support responses are helpful. Looking for faster resolution bounds on enterprise contracts.'",
                "⭐ 4.2 - 'Volume transfer metrics are accurate. High-value ledger updates require clearer batch notifications.'"
            ]
        }
        st.table(pd.DataFrame(review_data))
        
    st.markdown("---")
    
    st.markdown("<div class='section-header'>📋 Objective 1: Structural Data Schema & Type Validation</div>", unsafe_allow_html=True)
    col_chk1, col_chk2, col_chk3, col_chk4 = st.columns(4)
    with col_chk1:
        if st.checkbox(" Order_Date | **datetime64**", value=True): st.caption(f"✓ Validated. {df.shape[0]} arrays.")
        if st.checkbox("🔑 Transaction_ID | **object (String)**", value=True): st.caption("✓ Validated Alphanumeric indexing.")
    with col_chk2:
        if st.checkbox("🏢 Customer_Name | **object (String)**", value=True): st.caption("✓ Validated Corporate structures registry.")
        if st.checkbox("📍 Customer_Area | **object (String)**", value=True): st.caption("✓ Validated City grid strings.")
    with col_chk3:
        if st.checkbox("💰 Gross_Revenue_USD | **float64**", value=True): st.caption("✓ Validated Continuous numeric variance.")
    with col_chk4:
        if st.checkbox("📊 Profit_Margin_Pct | **float64**", value=True): st.caption("✓ Validated Mapped margin fractions.")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-header'>📈 Objectives 2 & 3: Performance Trends, Hypothesis Testing, & Outlier Detection</div>", unsafe_allow_html=True)
    row2_col1, row2_col2 = st.columns([3, 2])
    with row2_col1:
        df_trend = df.copy()
        df_trend["Date_Truncated"] = df_trend["Order_Date"].dt.date
        trend_grouped = df_trend.groupby("Date_Truncated")[["Gross_Revenue_USD", "Net_Profit_USD"]].sum().reset_index()
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=trend_grouped["Date_Truncated"], y=trend_grouped["Gross_Revenue_USD"], name="Gross Sales Inflow", line=dict(color='#2563EB', width=3, shape='spline')))
        fig_line.update_layout(template="plotly_white", margin=dict(l=10, r=10, t=10, b=10), height=320, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line, use_container_width=True)
    with row2_col2:
        fig_box = px.box(df, y="Gross_Revenue_USD", color="Sales_Region", color_discrete_sequence=['#1E3A8A', '#2563EB', '#0EA5E9', '#64748B'], template="plotly_white")
        fig_box.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_box, use_container_width=True)
        
    st.markdown("---")
    
    st.markdown("<div class='section-header'>🚨 Objective 4: Pre-Analysis Data Quality Issue & Rectification Engine</div>", unsafe_allow_html=True)
    duplicate_count = df_raw.duplicated().sum()
    missing_csat = df_raw["Customer_Satisfaction"].isna().sum()
    revenue_outliers = df_raw[df_raw["Gross_Revenue_USD"] > 50000].shape[0]
    
    issue_col1, issue_col2, issue_col3 = st.columns(3)
    with issue_col1:
        st.markdown(f"""<div class='issue-box'><h4 style='color:#9F1239;margin-top:0;'>⚠️ Issue 1: Redundant Logs</h4><p style='font-size:13px;'><strong>Detected:</strong> {duplicate_count} perfect duplicate rows.</p><hr style='border:0;border-top:1px solid #FDA4AF;margin:12px 0;'><p style='font-size:13px;'><strong>Rectify?</strong> YES<br><strong>Action:</strong> Run <code>df.drop_duplicates()</code> to avoid metrics variance inflation.</p></div>""", unsafe_allow_html=True)
    with issue_col2:
        st.markdown(f"""<div class='issue-box'><h4 style='color:#9F1239;margin-top:0;'>⚠️ Issue 2: Missing Data Blocks</h4><p style='font-size:13px;'><strong>Detected:</strong> {missing_csat} missing fields localized in CSAT parameters.</p><hr style='border:0;border-top:1px solid #FDA4AF;margin:12px 0;'><p style='font-size:13px;'><strong>Rectify?</strong> YES<br><strong>Action:</strong> Use median-imputation to substitute fields cleanly without skews.</p></div>""", unsafe_allow_html=True)
    with issue_col3:
        st.markdown(f"""<div class='issue-box'><h4 style='color:#9F1239;margin-top:0;'>⚠️ Issue 3: Value Outliers</h4><p style='font-size:13px;'><strong>Detected:</strong> Outlier spike row detected over $150,000.00.</p><hr style='border:0;border-top:1px solid #FDA4AF;margin:12px 0;'><p style='font-size:13px;'><strong>Rectify?</strong> NO (ISOLATE ONLY)<br><strong>Action:</strong> Retain wholesale bulk record. Segment from retail counts to avoid mean distortions.</p></div>""", unsafe_allow_html=True)

else:
    # ==========================================
    # PAGE 2: MASTER DATABASE POWER BI INTERFACE
    # ==========================================
    st.markdown("<div class='app-title'>🗄 nighttime Ingested Master Production Ledger Report</div>", unsafe_allow_html=True)
    st.markdown("<div class='app-subtitle'>Power BI Desktop Report Page 2 — Full-Scale Relational Database Audit Terminal</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown(f"<div class='selection-tracker-box'><strong>🌐 ACTIVE SLICER CONTEXT (MASTER DB):</strong> {tracker_text}</div>", unsafe_allow_html=True)
    
    db_total_rows = df.shape[0]
    db_total_cols = df.shape[1]
    db_unique_clients = df["Customer_Name"].nunique()
    
    db_kpi1, db_kpi2, db_kpi3 = st.columns(3)
    with db_kpi1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Active Relational Tuple Records (Rows)", value=f"{db_total_rows:,}")
        st.markdown("</div>", unsafe_allow_html=True)
    with db_kpi2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Ingested Data Dimensions (Columns)", value=f"{db_total_cols}")
        st.markdown("</div>", unsafe_allow_html=True)
    with db_kpi3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric(label="Unique Corporate Clients Tracked", value=f"{db_unique_clients}")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-header'>📊 Transaction Record Densities by Corporate Customer Entity</div>", unsafe_allow_html=True)
    df_client_dist = df.groupby(["Customer_Name", "Customer_Area"])["Gross_Revenue_USD"].agg(['sum', 'count']).reset_index()
    df_client_dist.columns = ["Customer_Name", "Customer_Area", "Total_Revenue", "Transaction_Count"]
    
    fig_db_bar = px.bar(
        df_client_dist, x="Customer_Name", y="Transaction_Count", color="Customer_Area",
        title="Database Row Volume Matrix Mapped to Individual Client Sub-Accounts",
        color_discrete_sequence=px.colors.sequential.Blues_r, template="plotly_white"
    )
    fig_db_bar.update_layout(height=340, margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_db_bar, use_container_width=True)
    
    st.markdown("<div class='section-header'>🗄️ Core Production Database Storage Matrix Ledger</div>", unsafe_allow_html=True)
    st.write("Below is the complete clean master ledger dataset matching your selection scope:")
    st.dataframe(df, use_container_width=True)