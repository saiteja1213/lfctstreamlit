import streamlit as st

st.set_page_config(page_title="LFxCT Season 2", layout="wide", page_icon="🏏")

# Global CSS — cricket pitch dark theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --green:   #1a7a4a;
    --lime:    #b5e550;
    --dark:    #0d1f14;
    --card:    #132a1c;
    --border:  #1e3d28;
    --text:    #e8f5ee;
    --muted:   #7aab8a;
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
}

.stButton > button {
    background: var(--lime) !important;
    color: #0d1f14 !important;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }

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

.stMetric {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
}

.hero-banner {
    background: linear-gradient(135deg, #0d2b18 0%, #1a5c35 50%, #0d2b18 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 3rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(ellipse at center, rgba(181,229,80,0.06) 0%, transparent 70%);
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4rem;
    letter-spacing: 6px;
    color: var(--lime);
    margin: 0;
    line-height: 1;
}
.hero-sub {
    font-size: 1rem;
    color: var(--muted);
    margin-top: 0.5rem;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.nav-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    transition: border-color 0.2s;
}
.nav-card:hover { border-color: var(--lime); }
.nav-card .icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.nav-card .label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.2rem;
    letter-spacing: 2px;
    color: var(--lime);
}
.nav-card .desc { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero-banner">
    <p class="hero-title">🏏 LFxCT</p>
    <p class="hero-sub">Season 2 &nbsp;·&nbsp; Prediction League</p>
</div>
""", unsafe_allow_html=True)

# Quick-nav cards
cols = st.columns(4)
pages = [
    ("📝", "Submit Prediction", "Pick your winner & go bold", "1_User"),
    ("📅", "Match Schedule",    "Upcoming fixtures",          "4_Schedule"),
    ("🏆", "Leaderboard",       "See who's leading",          "5_Leaderboard"),
    ("📊", "My Stats",          "Your personal breakdown",    "6_My_Stats"),
]
for col, (icon, label, desc, _) in zip(cols, pages):
    col.markdown(f"""
    <div class="nav-card">
        <div class="icon">{icon}</div>
        <div class="label">{label}</div>
        <div class="desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p style='color:#7aab8a; font-size:0.85rem; text-align:center;'>Use the sidebar to navigate · Manager & Admin access via their respective pages</p>", unsafe_allow_html=True)
