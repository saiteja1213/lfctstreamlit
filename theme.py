import streamlit as st

def apply_theme():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --green:  #1a7a4a;
    --lime:   #b5e550;
    --dark:   #0d1f14;
    --card:   #132a1c;
    --border: #1e3d28;
    --text:   #e8f5ee;
    --muted:  #7aab8a;
}
html, body, [data-testid="stAppViewContainer"] {
    background: var(--dark) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stSidebar"] {
    background: #0a180f !important;
    border-right: 1px solid var(--border);
}
h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 2px;
    color: var(--lime) !important;
}
.stButton > button {
    background: var(--lime) !important;
    color: #0d1f14 !important;
    font-weight: 600;
    border: none !important;
    border-radius: 4px !important;
}
.stTextInput > div > input,
.stSelectbox > div > div {
    background: var(--card) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
}
[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
}
div[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
}
div[data-testid="stMetricValue"] { color: var(--lime) !important; }
.badge {
    display:inline-block; padding:2px 10px; border-radius:20px;
    font-size:0.75rem; font-weight:600; letter-spacing:1px;
}
.badge-bold   { background:#3d2e00; color:#f5c842; }
.badge-normal { background:#1a3d28; color:#b5e550; }
</style>
""", unsafe_allow_html=True)
