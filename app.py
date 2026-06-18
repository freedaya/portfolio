import streamlit as st
import streamlit.components.v1 as components
import base64
import pandas as pd
import plotly.express as px
import pickle
import requests

# ======================
# CONFIG
# ======================
st.set_page_config(page_title="Portfolio – Fayzan Rizky Hidayat", layout="wide", page_icon="📊")

# ======================
# GLOBAL CSS – Dark Professional Theme
# ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background-color: #0f1117;
    color: #e0e0e0;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ── Streamlit container padding reset ── */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}

/* ═══════════════════════════════════════
   TOP NAVIGATION BAR
═══════════════════════════════════════ */
.top-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 48px;
    background: #13151f;
    border-bottom: 1px solid #1e2030;
    
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    z-index: 999999;
}
.nav-logo {
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
}
.nav-logo span {
    color: #4f8ef7;
}
.nav-links {
    display: flex;
    gap: 32px;
    list-style: none;
    margin: 0;
    padding: 0;
}
.nav-links a {
    color: #a0a8be;
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: 0.3px;
    transition: color 0.2s;
}
.nav-links a:hover { color: #ffffff; }
.nav-links a.active {
    color: #ffffff;
    border-bottom: 2px solid #4f8ef7;
    padding-bottom: 2px;
}
.nav-social {
    display: flex;
    gap: 16px;
    align-items: center;
}
.nav-social a {
    color: #a0a8be;
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.2s;
}
.nav-social a:hover { color: #ffffff; }

/* ═══════════════════════════════════════
   HERO SECTION
═══════════════════════════════════════ */
.hero-section {
    display: flex;
    align-items: center;
    gap: 48px;
    padding: 64px 48px 48px;
    min-height: 520px;
    background: linear-gradient(135deg, #13151f 0%, #0f1117 60%, #1a1f35 100%);
    border-bottom: 1px solid #1e2030;
}
.hero-left {
    flex: 1.2;
}
.hero-greeting {
    font-size: 0.78rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #a0a8be;
    margin-bottom: 12px;
}
.hero-name {
    font-size: 3.8rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 8px;
}
.hero-name span {
    color: #4f8ef7;
}
.hero-title {
    font-size: 1.05rem;
    color: #6b7fa3;
    font-weight: 500;
    margin-bottom: 20px;
    letter-spacing: 0.3px;
}
.hero-description {
    font-size: 0.92rem;
    color: #8891a8;
    line-height: 1.75;
    max-width: 480px;
    margin-bottom: 32px;
}
.hero-cta-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 36px;
}
.hero-btn-primary {
    display: inline-block;
    padding: 11px 26px;
    background: #4f8ef7;
    color: #fff !important;
    border-radius: 6px;
    text-decoration: none !important;
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: 0.3px;
    transition: background 0.2s, transform 0.15s;
}
.hero-btn-primary:hover {
    background: #3a78e8;
    transform: translateY(-1px);
}
.hero-btn-outline {
    display: inline-block;
    padding: 11px 26px;
    border: 1.5px solid #2a3150;
    color: #a0a8be !important;
    border-radius: 6px;
    text-decoration: none !important;
    font-size: 0.88rem;
    font-weight: 500;
    transition: border-color 0.2s, color 0.2s;
}
.hero-btn-outline:hover {
    border-color: #4f8ef7;
    color: #ffffff !important;
}
.hero-social-row {
    display: flex;
    gap: 14px;
    align-items: center;
}
.hero-social-link {
    display: flex;
    align-items: center;
    gap: 6px;
    color: #6b7fa3 !important;
    text-decoration: none !important;
    font-size: 0.82rem;
    font-weight: 500;
    transition: color 0.2s;
}
.hero-social-link:hover { color: #4f8ef7 !important; }
.hero-right {
    flex: 0.8;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
}
.hero-avatar-wrap {
    position: relative;
}
.hero-avatar-wrap img {
    width: 240px;
    height: 240px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #1e2030;
    box-shadow: 0 8px 32px rgba(79,142,247,0.15);
}
.hero-badge {
    display: inline-block;
    background: #1a1f35;
    border: 1px solid #2a3150;
    color: #8891a8;
    font-size: 0.78rem;
    padding: 5px 14px;
    border-radius: 20px;
    letter-spacing: 0.5px;
}

/* ═══════════════════════════════════════
   ABOUT SECTIONS (Education, Skills, etc.)
═══════════════════════════════════════ */
.about-section {
    padding: 48px 48px 0;
    border-bottom: 1px solid #1e2030;
}
.about-section-title {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    color: #4f8ef7;
    margin-bottom: 6px;
}
.about-section-heading {
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 28px;
}

/* Education grid */
.edu-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding-bottom: 40px;
}
.edu-card {
    background: #13151f;
    border: 1px solid #1e2030;
    border-radius: 10px;
    padding: 20px 24px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.edu-card-inst {
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
}
.edu-card-degree {
    font-size: 0.88rem;
    color: #4f8ef7;
    font-weight: 500;
}
.edu-card-period {
    font-size: 0.78rem;
    color: #6b7fa3;
}
.edu-card-detail {
    font-size: 0.82rem;
    color: #8891a8;
    margin-top: 4px;
    line-height: 1.5;
}

/* Skills grid */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    padding-bottom: 40px;
}
.skill-card {
    background: #13151f;
    border: 1px solid #1e2030;
    border-radius: 10px;
    padding: 16px 20px;
}
.skill-name {
    font-size: 0.9rem;
    font-weight: 600;
    color: #e0e0e0;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.skill-score {
    font-size: 0.78rem;
    color: #4f8ef7;
    font-weight: 500;
}
.skill-bar-track {
    display: flex;
    gap: 4px;
}
.skill-pip {
    flex: 1;
    height: 8px;
    border-radius: 3px;
}
.skill-pip.filled { background: #4f8ef7; }
.skill-pip.empty  { background: #1e2030; }

/* Certification grid */
.cert-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding-bottom: 40px;
}
.cert-row {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 20px;
    background: #13151f;
    border: 1px solid #1e2030;
    border-radius: 10px;
    overflow: hidden;
    align-items: center;
}
.cert-info {
    padding: 24px 28px;
}
.cert-title {
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 4px;
}
.cert-issuer {
    font-size: 0.85rem;
    color: #4f8ef7;
    font-weight: 500;
    margin-bottom: 6px;
}
.cert-detail {
    font-size: 0.82rem;
    color: #8891a8;
    line-height: 1.5;
}
.cert-image {
    padding: 16px 20px 16px 0;
}
.cert-image img {
    width: 100%;
    border-radius: 6px;
    object-fit: contain;
    height: 400px;
}

/* ═══════════════════════════════════════
   SECTION HEADERS
═══════════════════════════════════════ */
.section-header {
    padding: 48px 48px 8px;
}
.section-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 2.5px;
    color: #4f8ef7;
    margin-bottom: 8px;
}
.section-title {
    font-size: 1.9rem;
    font-weight: 700;
    color: #ffffff;
}

/* ═══════════════════════════════════════
   PROJECT CARDS
═══════════════════════════════════════ */
.project-container {
    padding: 0 32px 16px;
}
/* override Streamlit's container border */
[data-testid="stVerticalBlock"] > [data-testid="element-container"] > div > div {
    background: #13151f;
}

/* ═══════════════════════════════════════
   PDF VIEWER
═══════════════════════════════════════ */
.pdf-viewer-wrap {
    background: #0a0c14;
    border: 1px solid #1e2030;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 12px;
}

/* ═══════════════════════════════════════
   FOOTER
═══════════════════════════════════════ */
.footer-section {
    background: #13151f;
    border-top: 1px solid #1e2030;
    padding: 56px 48px 0;
}
.footer-cta-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    max-width: 520px;
    line-height: 1.2;
    margin-bottom: 24px;
}
.footer-cta-desc {
    font-size: 0.93rem;
    color: #8891a8;
    max-width: 520px;
    line-height: 1.75;
    margin-bottom: 24px;
}
.footer-divider {
    width: 40px;
    height: 2px;
    background: #4f8ef7;
    margin: 20px 0;
}
.footer-contact-item {
    color: #a0a8be;
    font-size: 0.92rem;
    margin-bottom: 6px;
}
.footer-contact-item a {
    color: #a0a8be;
    text-decoration: none;
    transition: color 0.2s;
}
.footer-contact-item a:hover { color: #ffffff; }
.footer-links-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
    margin-top: 48px;
    padding-top: 36px;
    border-top: 1px solid #1e2030;
}
.footer-link-col-title {
    font-size: 0.85rem;
    font-weight: 600;
    color: #4f8ef7;
    margin-bottom: 8px;
    letter-spacing: 0.3px;
}
.footer-link-col-sub {
    font-size: 0.8rem;
    color: #6b7fa3;
}
.footer-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 0;
    margin-top: 36px;
    border-top: 1px solid #1e2030;
}
.footer-bottom-text {
    font-size: 0.78rem;
    color: #4a5170;
}
.footer-social-bar {
    display: flex;
    align-items: center;
    gap: 16px;
}
.footer-social-bar a {
    color: #6b7fa3;
    text-decoration: none;
    font-size: 0.82rem;
    transition: color 0.2s;
}
.footer-social-bar a:hover { color: #ffffff; }

/* ═══════════════════════════════════════
   MISC TWEAKS
═══════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: #13151f;
    border-bottom: 1px solid #1e2030;
    padding: 0 32px;
}
.stTabs [data-baseweb="tab"] {
    color: #a0a8be !important;
    font-weight: 500;
    font-size: 0.88rem;
}
.stTabs [aria-selected="true"] {
    color: #ffffff !important;
    border-bottom: 2px solid #4f8ef7 !important;
}

div[data-testid="stButton"] > button {
    background: #1a1f35;
    color: #c0c8e0;
    border: 1px solid #2a3150;
    border-radius: 6px;
    font-size: 0.84rem;
    font-weight: 500;
    padding: 8px 18px;
    transition: background 0.2s, border-color 0.2s;
}
div[data-testid="stButton"] > button:hover {
    background: #222840;
    border-color: #4f8ef7;
    color: #ffffff;
}

div[data-testid="stLinkButton"] > a {
    background: #1a2540 !important;
    color: #4f8ef7 !important;
    border: 1px solid #2a3d6a !important;
    border-radius: 6px !important;
    font-size: 0.84rem !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
    transition: background 0.2s !important;
}
div[data-testid="stLinkButton"] > a:hover {
    background: #203060 !important;
}


</style>
""", unsafe_allow_html=True)

# ======================
# HELPER – PDF VIEWER
# ======================
def pdf_viewer(url):
    st.markdown(f"""
    <iframe src="{url}" width="100%" height="600"></iframe>
    """, unsafe_allow_html=True)

# ======================
# HELPER – Dark styled dataframe
# ======================
_dark_table_styles = [
    {"selector": "thead th", "props": [
        ("background-color", "#1a1f35"), ("color", "#a0a8be"),
        ("font-weight", "600"), ("border-bottom", "1px solid #2a3150"),
    ]},
    {"selector": "tbody tr", "props": [("background-color", "#13151f")]},
    {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#16192a")]},
    {"selector": "tbody td", "props": [("color", "#e0e0e0"), ("border-color", "#1e2030")]},
]

def dark_df(styler):
    return (styler
            .set_properties(**{"background-color": "#13151f", "color": "#e0e0e0", "border-color": "#1e2030"})
            .set_table_styles(_dark_table_styles))

# ======================
# HELPER – Load image as base64
# ======================
def img_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ======================
# NAV BAR
# ======================
st.markdown("""
<div class="top-nav">
    <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
    <div class="nav-social">
        <a href="https://linkedin.com/in/fayzan-rizky-hidayat/" target="_blank">LinkedIn</a>
        <a href="https://github.com/freedaya" target="_blank">GitHub</a>
        <a href="https://www.instagram.com/fayzan.rizky" target="_blank">Instagram</a>
        <a href="https://wa.me/6287776604718" target="_blank">WhatsApp</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# HERO SECTION
# ======================
avatar_b64 = img_b64("assets/img_001.png")

st.markdown(f"""
<div class="hero-section" id="about">
    <div class="hero-left">
        <p class="hero-greeting">Hello there, nice to meet you &nbsp;👋&nbsp; I am</p>
        <h1 class="hero-name">Fayzan Rizky<br><span>Hidayat</span></h1>
        <p class="hero-title">Data Analyst &nbsp;·&nbsp; Data Scientist</p>
        <p class="hero-description" style="text-align: justify; text-justify: inter-word;">
            A physics graduate who transitioned into Data Analytics & Data Science,
            with a strong passion for data-driven decision making. Experienced in
            statistical analysis, machine learning, and data visualization using
            Python and Power BI.
        </p>
        <div class="hero-cta-row">
            <a href="mailto:fayzan.rh@gmail.com" class="hero-btn-primary">📩 Get in Touch</a>
            <a href="https://linkedin.com/in/fayzan-rizky-hidayat/" target="_blank" class="hero-btn-outline">View LinkedIn</a>
        </div>
        <div class="hero-social-row">
            <a href="https://github.com/freedaya" target="_blank" class="hero-social-link">GitHub</a>
            <a href="https://www.instagram.com/fayzan.rizky" target="_blank" class="hero-social-link">Instagram</a>
            <a href="https://wa.me/6287776604718" class="hero-social-link">WhatsApp</a>
        </div>
    </div>
    <div class="hero-right">
        <div class="hero-avatar-wrap">
            <img src="data:image/png;base64,{avatar_b64}" alt="Fayzan Rizky Hidayat">
        </div>
        <span class="hero-badge">📍 Jakarta, Indonesia</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# SECTION 1 – EDUCATION
# ======================
st.markdown("""
<div class="about-section" id="about-detail">
    <div class="about-section-title">Background</div>
    <div class="about-section-heading">Education</div>
    <div class="edu-grid">
        <div class="edu-card">
            <div class="edu-card-inst">Universitas Padjadjaran</div>
            <div class="edu-card-degree">Bachelor of Physics</div>
            <div class="edu-card-period">August 2021 – August 2025</div>
            <div class="edu-card-detail">Computational Physics, Instrumentation, Renewable Energy. Final Project: Hydrogen atom polarizability under Stark Effect using Python (80.6% accuracy).</div>
        </div>
        <div class="edu-card">
            <div class="edu-card-inst">Dibimbing.id</div>
            <div class="edu-card-degree">Data Analyst & Data Science Bootcamp</div>
            <div class="edu-card-period">September 2025 – April 2026</div>
            <div class="edu-card-detail">Python (Pandas, NumPy, Matplotlib, Seaborn), SQL, EDA, interactive dashboards, regression and classification with supervised & unsupervised learning.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# SECTION 2 – SKILLS
# ======================

skills = [
    ("Python",              '<i class="fa-brands fa-python" style="font-size: 1.4rem; color: #3776AB;"></i>'),
    ("SQL (PostgreSQL)",    '<i class="fa-solid fa-database" style="font-size: 1.3rem; color: #336791;"></i>'),
    ("Power BI",            '<i class="fa-solid fa-chart-bar" style="font-size: 1.3rem; color: #F2C811;"></i>'),
    ("Tableau",             '<i class="fa-solid fa-chart-pie" style="font-size: 1.3rem; color: #E97627;"></i>'),
    ("Excel",               '<i class="fa-regular fa-file-excel" style="font-size: 1.4rem; color: #10798F;"></i>'),
    ("Google Looker",       '<i class="fa-solid fa-chart-line" style="font-size: 1.3rem; color: #4285F4;"></i>'),
    ("Machine Learning",    '<i class="fa-solid fa-brain" style="font-size: 1.3rem; color: #A855F7;"></i>'),
    ("Data Cleaning",       '<i class="fa-solid fa-broom" style="font-size: 1.3rem; color: #EAB308;"></i>'),
    ("EDA",                 '<i class="fa-solid fa-magnifying-glass-chart" style="font-size: 1.3rem; color: #06b6d4;"></i>'),
]

font_awesome_cdn = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'

skill_cards = "".join([
    f"""<div class="skill-card" style="display: flex; align-items: center; gap: 14px; padding: 12px 16px;">
        <div class="skill-icon" style="display: flex; align-items: center; justify-content: center; width: 28px;">
            {icon_html}
        </div>
        <div class="skill-name" style="margin: 0; font-weight: 500;">{name}</div>
    </div>"""
    for name, icon_html in skills
])

st.markdown(f"""
{font_awesome_cdn}
<div class="about-section">
    <div class="about-section-title">Expertise</div>
    <div class="about-section-heading">Skills</div>
    <div class="skills-grid">
        {skill_cards}
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# SECTION 3 – CERTIFICATION
# ======================
dibimbing_b64 = img_b64("assets/sertidibimbing.jpg")
english_b64   = img_b64("assets/sertienglish.jpg")

st.markdown(f"""
<div class="about-section">
    <div class="about-section-title">Credentials</div>
    <div class="about-section-heading">Certifications</div>
    <div class="cert-grid">
        <div class="cert-row">
            <div class="cert-info">
                <div class="cert-title">Data Analyst & Data Science</div>
                <div class="cert-issuer">Dibimbing.id · 2025 – 2026</div>
                <div class="cert-detail">Grade A · Completed bootcamp covering Python, SQL, EDA, Machine Learning, and dashboard development.</div>
            </div>
            <div class="cert-image">
                <img src="data:image/png;base64,{dibimbing_b64}" alt="Dibimbing Certificate">
            </div>
        </div>
        <div class="cert-row">
            <div class="cert-info">
                <div class="cert-title">EF SET English Certificate</div>
                <div class="cert-issuer">EF Standard English Test · September 2025</div>
                <div class="cert-detail">C1 Advanced.</div>
            </div>
            <div class="cert-image">
                <img src="data:image/png;base64,{english_b64}" alt="EF English Certificate">
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# PROJECTS SECTION
# ======================
st.markdown("""
<div class="section-header" id="projects">
    <div class="section-label">My Work</div>
    <div class="section-title">🚀 Projects</div>
</div>
""", unsafe_allow_html=True)

# ─── Session state for PDF viewers ───────────────────
for key in ["project1","project2","project3","project4","project5","project5b","project6","project7",
            "pdf1","pdf2","pdf3","pdf4","pdf5","pdf5b","pdf6","pdf7"]:
    if key not in st.session_state:
        st.session_state[key] = False

# ─── Tabs ────────────────────────────────────────────
tab1, tab2 = st.tabs(["📊 Data Analyst", "📈 Data Science"])

# ══════════════════════════════════════════════════════
#  TAB 1 – DATA ANALYST
# ══════════════════════════════════════════════════════
with tab1:

    # ── Project 1: Surge Pricing ──────────────────────
    with st.container(border=True):
        st.subheader("🚕 Surge Pricing Analysis – Sigma Cabs")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/surgepricing.jpg")
        with col2:
            st.markdown("""
            Analysis of factors influencing dynamic surge pricing on the Sigma Cabs taxi aggregator
            platform in India, using a dataset of 131,662 trips across 8 deep analytical questions.
            """)
            st.write("**Tools:** Python (Pandas, Seaborn, Plotly, SciPy), Jupyter Notebook, Streamlit")
            btn_row1 = st.columns([1, 1, 1])
            with btn_row1[0]:
                if st.button("📄 View Slides", key="pdf_btn1"):
                    st.session_state.pdf1 = not st.session_state.pdf1
            with btn_row1[1]:
                st.link_button("🚀 Live Dashboard", "https://surge-pricing-analysis.streamlit.app/")
            with btn_row1[2]:
                if st.button("🔍 View Details", key="btn1"):
                    st.session_state.project1 = not st.session_state.project1

        if st.session_state.pdf1:
            pdf_viewer("https://drive.google.com/file/d/1A0mWoOcFSinUxcd-1uIyhwl2Q3kjRc7h/preview")

        if st.session_state.project1:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Feature Correlation vs Surge Pricing")
                corr_data = pd.DataFrame({
                    "Factor": ["Type_of_Cab","Cancellation_Last_1Month","Customer_Rating",
                               "Trip_Distance","Confidence_LSI","Destination_Type","Gender"],
                    "Correlation": [0.50, 0.19, -0.16, 0.14, 0.12, 0.08, 0.01],
                })
                corr_sorted = corr_data.sort_values("Correlation")
                fig_corr = px.bar(corr_sorted, x="Correlation", y="Factor", orientation="h",
                                  color="Correlation",
                                  color_continuous_scale=["#EF553B","#2a3150","#4f8ef7"],
                                  range_color=[-0.55, 0.55],
                                  text=corr_sorted["Correlation"].apply(lambda x: f"{x:+.2f}"))
                fig_corr.update_coloraxes(showscale=False)
                fig_corr.update_traces(textposition="outside")
                fig_corr.update_layout(height=320, margin=dict(t=10,b=0),
                                       paper_bgcolor="#13151f", plot_bgcolor="#13151f",
                                       font_color="#ffffff")
                st.plotly_chart(fig_corr, use_container_width=True)

                st.subheader("Cab Type vs Surge Level (%)")
                cab_data = pd.DataFrame({
                    "Cab Type": ["A","B","C","D","E"]*3,
                    "Surge Type": ["Type 1"]*5+["Type 2"]*5+["Type 3"]*5,
                    "Percentage": [69.2,17.8,3.7,5.0,9.2,10.5,63.3,61.5,13.2,18.7,20.4,18.9,34.8,81.2,72.1],
                })
                fig_cab = px.bar(cab_data, x="Cab Type", y="Percentage", color="Surge Type",
                                 barmode="relative",
                                 color_discrete_map={"Type 1":"#636EFA","Type 2":"#EF553B","Type 3":"#00CC96"},
                                 text="Percentage")
                fig_cab.update_traces(texttemplate="%{text:.1f}%", textposition="inside")
                fig_cab.update_layout(height=320, margin=dict(t=10,b=0),
                                      paper_bgcolor="#13151f", plot_bgcolor="#13151f",
                                      font_color="#ffffff",legend_font_color="#ffffff")
                st.plotly_chart(fig_cab, use_container_width=True)

            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                Sigma Cabs is a taxi aggregator platform in India connecting users with various
                transportation service providers. After nearly a year of operation, the company
                collected data from 131,662 trips but struggled to map the dominant factors
                triggering surge pricing increases (scale 1–3).

                **Goal:** Identify the key factors influencing surge pricing to support optimization
                of pricing strategy, supply-demand, and customer experience.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Analysis conducted through Univariate, Bivariate, and Multivariate Analysis
                using distribution visualizations (violin plot, box plot, stacked bar) and
                Chi-Squared statistical tests for categorical features.

                **5 significant factors:**
                - Type_of_Cab (r=0.50): Strongest predictor. Types D/E → 72–81% Type 3 surge
                - Cancellation_Last_1Month (r=0.19): ≥3 cancellations → Type 3 dominance
                - Customer_Rating (r=-0.16): Higher rating → lower surge
                - Trip_Distance (r=0.14): Type 3 median 45 km vs 36 km in Types 1 & 2
                - Destination_Type: p-value < 0.05 despite weak correlation

                **3 non-significant factors:** Customer_Since_Months, Life_Style_Index, Gender
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                Type of Cab is the most decisive variable with a clear linear pattern.

                **Recommendations:**
                - Use Type_of_Cab as the primary segmentation factor in the pricing algorithm
                - Implement early warning system for customers with high cancellation history
                - Provide surge discounts for high-rated customers as a loyalty reward
                - Focus retention on service quality, not subscription duration
                """)

    # ── Project 2: A/B Testing ───────────────────────
    with st.container(border=True):
        st.subheader("📈 A/B Testing – Landing Page Conversion Rate")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/abtesting.jpg")
        with col2:
            st.markdown("""
            A/B Testing analysis to evaluate the performance of a new landing page
            compared to the old version in improving conversion rate.
            """)
            st.write("**Tools:** Python (Statistical Analysis), Power BI")
            btn_row2 = st.columns([1, 1, 1])
            with btn_row2[0]:
                if st.button("📄 View Slides", key="pdf_btn2"):
                    st.session_state.pdf2 = not st.session_state.pdf2
            with btn_row2[1]:
                with open("docs/abtesting.pbix", "rb") as file:
                    st.download_button("📥 Power BI (.pbix)", data=file, file_name="abtesting_dashboard.pbix")
            with btn_row2[2]:
                if st.button("🔍 View Details", key="btn2"):
                    st.session_state.project2 = not st.session_state.project2

        if st.session_state.pdf2:
            pdf_viewer("https://drive.google.com/file/d/178vj2uIyOtUyvqhsubNUyzQarCbTHzF_/preview")

        if st.session_state.project2:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Power BI Dashboard")
                st.image("assets/abtestingdb.jpg")
            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                The company wants to improve conversion rate on its landing page through
                A/B Testing between the old version (control) and the new version (treatment).

                **Goal:** Determine whether the new landing page performs better than the old version.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Analysis conducted by calculating conversion rates and statistical testing
                using Two-Proportion Z-Test.

                **Results:**
                - Control group had a slightly higher conversion rate
                - p-value = 0.1897 (> 0.05)

                **Conclusion:** No statistically significant difference between the two groups;
                we fail to reject H₀.
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                The new landing page has not been proven more effective than the old version.
                Any difference observed is likely due to random variation, not design impact.

                **Recommendations:**
                - Iterate on design (CTA, layout, copy)
                - Increase sample size or experiment duration
                - Conduct further A/B testing for stronger results
                """)

    # ── Project 3: Customer Satisfaction ─────────────
    with st.container(border=True):
        st.subheader("📊 Customer Satisfaction & Sentiment Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/customersatisfaction.jpg")
        with col2:
            st.markdown("""
            Customer satisfaction and sentiment analysis to understand customer experience
            and the factors influencing satisfaction and loyalty.
            """)
            st.write("**Tools:** Python (NLP – RoBERTa), Power BI")
            btn_row3 = st.columns([1, 1])
            with btn_row3[0]:
                if st.button("📄 View Slides", key="pdf_btn3"):
                    st.session_state.pdf3 = not st.session_state.pdf3
            with btn_row3[1]:
                if st.button("🔍 View Details", key="btn3"):
                    st.session_state.project3 = not st.session_state.project3

        if st.session_state.pdf3:
            pdf_viewer("https://drive.google.com/file/d/1kmsQss_-QPlHZr-FEmVFkqvqmYHETOSM/preview")

        if st.session_state.project3:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Key Visualization")
                st.image("assets/customersatisfactiondb.jpg")
            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                Analysis conducted to understand customer satisfaction levels from surveys
                and to identify sentiment from customer reviews.

                **Goal:** Identify the main factors affecting customer satisfaction and loyalty.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Analysis using CSAT, CES, and NPS metrics, and sentiment analysis
                using the RoBERTa model.

                **Results:**
                - NPS score: 11.94% (average category)
                - 84.75% of customers gave positive reviews
                - Positive correlation between rating and sentiment
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                Most customers are satisfied, but there is still improvement opportunity
                from non-positive feedback.

                **Recommendations:**
                - Improve customer service quality
                - Fix product features and usability
                - Enhance value for money perception
                - Monitor sentiment regularly
                """)

    # ── Project 4: Customer Segmentation ─────────────
    with st.container(border=True):
        st.subheader("🧩 Customer Segmentation – RFM Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/customeranalysis.jpg")
        with col2:
            st.markdown("""
            Customer segmentation analysis using RFM (Recency, Frequency, Monetary) method
            to identify high-value customers and purchasing behavior.
            """)
            st.write("**Tools:** Power BI (DAX Feature Engineering)")
            btn_row4 = st.columns([1, 1, 1])
            with btn_row4[0]:
                if st.button("📄 View Slides", key="pdf_btn4"):
                    st.session_state.pdf4 = not st.session_state.pdf4
            with btn_row4[1]:
                with open("docs/customeranalysis.pbix", "rb") as f:
                    st.download_button("📥 Power BI (.pbix)", data=f, file_name="customeranalysis_dashboard.pbix")
            with btn_row4[2]:
                if st.button("🔍 View Details", key="btn4"):
                    st.session_state.project4 = not st.session_state.project4

        if st.session_state.pdf4:
            pdf_viewer("https://drive.google.com/file/d/1NrYtPw_MSOwZ_86QDOfMcUnQwpD_vYm0/preview")

        if st.session_state.project4:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Dashboard")
                st.image("assets/customeranalysisdb.jpg")
            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                Analysis conducted to group customers based on transaction behavior
                using the RFM (Recency, Frequency, Monetary) method.

                **Goal:** Identify high-value customer segments and determine the right business strategy.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Segmentation performed by calculating RFM scores:
                - Recency: time since last transaction
                - Frequency: number of transactions
                - Monetary: total profit

                **Results:**
                - Customers with high frequency (up to 37 transactions) identified
                - High-profit customers (> $3000) identified
                - Some customers with perfect RFM score (555)
                - Segments: Champions, Loyal, Potential, and At Risk
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                Not all customers with high recency have high business value;
                the full RFM combination must be considered.

                **Recommendations:**
                - Focus retention on Champions and Loyal segments
                - Re-engage At Risk customers with promos or campaigns
                - Increase Potential customers' value through upselling
                - Use segmentation for marketing personalization
                """)

# ══════════════════════════════════════════════════════
#  TAB 2 – DATA SCIENCE
# ══════════════════════════════════════════════════════
with tab2:

    # ── Project 5b: Sigma Cabs DS ─────────────────────
    with st.container(border=True):
        st.subheader("🚖 Surge Pricing Prediction – Sigma Cabs")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/surgepredict.jpg")
        with col2:
            st.markdown("""
            Machine Learning project to classify surge pricing type (1, 2, or 3) on the Sigma Cabs
            taxi aggregator platform based on trip characteristics and customer behavior.
            Built with a Random Forest Classifier pipeline with hyperparameter tuning via GridSearchCV
            and SHAP-based feature importance analysis.
            """)
            st.write("**Tools:** Python (Pandas, Scikit-learn, SHAP, Plotly), Jupyter Notebook, Streamlit")
            btn_row5b = st.columns([1, 1, 1])
            with btn_row5b[0]:
                if st.button("📄 View Slides", key="pdf_btn5b"):
                    st.session_state.pdf5b = not st.session_state.pdf5b
            with btn_row5b[1]:
                st.link_button("🚀 Live Dashboard", "https://surge-pricing-analysis.streamlit.app/")
            with btn_row5b[2]:
                if st.button("🔍 View Details", key="btn5b"):
                    st.session_state.project5b = not st.session_state.project5b

        if st.session_state.pdf5b:
            pdf_viewer("https://drive.google.com/file/d/1KWaTSj9JT8tuBiLLfhY5iLxEuCHufg8o/preview")

        if st.session_state.project5b:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("SHAP Feature Importance")
                shap_data = pd.DataFrame({
                    "Feature": [
                        "Type_of_Cab", "Trip_Distance", "Cancellation_Last_1Month",
                        "Customer_Rating", "Destination_Type", "Life_Style_Index",
                        "Confidence_LSI", "Var3", "Var2", "Customer_Since_Months",
                        "Gender_Female", "Gender_Male"
                    ],
                    "Type 1": [0.12, 0.14, 0.06, 0.10, 0.04, 0.03, 0.03, 0.02, 0.01, 0.01, 0.00, 0.00],
                    "Type 2": [0.15, 0.04, 0.03, 0.04, 0.05, 0.03, 0.03, 0.02, 0.01, 0.01, 0.00, 0.00],
                    "Type 3": [0.25, 0.16, 0.10, 0.10, 0.06, 0.05, 0.04, 0.03, 0.01, 0.01, 0.00, 0.00],
                })
                shap_data["Total"] = shap_data[["Type 1","Type 2","Type 3"]].sum(axis=1)
                shap_sorted = shap_data.sort_values("Total", ascending=False)
                shap_melt = shap_sorted.melt(
                    id_vars="Feature", value_vars=["Type 1","Type 2","Type 3"],
                    var_name="Surge_Type", value_name="SHAP_Value"
                )
                fig_shap = px.bar(
                    shap_melt, x="SHAP_Value", y="Feature", color="Surge_Type",
                    orientation="h", barmode="group",
                    color_discrete_map={"Type 1":"#636EFA","Type 2":"#EF553B","Type 3":"#00CC96"},
                    category_orders={"Feature": shap_sorted["Feature"].tolist()}
                )
                fig_shap.update_layout(
                    height=420, margin=dict(t=10, b=0),
                    paper_bgcolor="#13151f", plot_bgcolor="#13151f", font_color="#ffffff",
                    legend_font_color="#ffffff"
                )
                st.plotly_chart(fig_shap, use_container_width=True)

                st.subheader("Model Performance")
                perf_df = pd.DataFrame({
                    "Surge Type": ["Type 1", "Type 2", "Type 3", "Weighted Avg"],
                    "Precision": ["74.31%", "65.95%", "78.16%", "72.11%"],
                    "Recall":    ["60.10%", "83.99%", "61.37%", "70.83%"],
                    "F1-Score":  ["66.45%", "73.88%", "68.76%", "70.48%"],
                    "Support":   [6809, 14150, 11957, 32916],
                })
                st.dataframe(dark_df(perf_df.style), use_container_width=True, hide_index=True)

            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                Sigma Cabs is a taxi aggregator platform in India connecting customers to various
                service providers. Surge pricing is categorized into three types (1, 2, 3) based
                on dynamic conditions. The company needed a reliable system to predict which
                surge type an incoming order would fall into.

                **Goal:** Build a classification model to predict surge pricing type from trip
                characteristics and customer behavior, enabling faster and more efficient
                service matching.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Pipeline: ColumnTransformer (Yeo-Johnson on Var2/Var3) → StandardScaler →
                Random Forest Classifier, tuned with GridSearchCV (F1-Weighted scoring).

                **Best Model Parameters:**
                - n_estimators: 200, max_depth: 12
                - criterion: entropy, class_weight: balanced_subsample
                - min_samples_split: 10, min_samples_leaf: 2

                **Final Results (test set, n=32,916):**
                - Accuracy: 70.87%  |  F1-Weighted: 70.48%
                - Type 3 has the highest precision (78%), Type 2 has the highest recall (84%)
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                **Key SHAP findings:**
                - **Type_of_Cab** is the dominant predictor (SHAP ~0.52 total) — confirming the DA finding of r=0.50
                - **Trip_Distance** strongly influences Type 1 and Type 3
                - **Cancellation_Last_1Month** is the most behavioral signal for Type 3
                - **Customer_Rating** shows a consistent negative effect on surge level

                **Recommendations:**
                - Deploy model for real-time surge classification on incoming orders
                - Use cancellation patterns and destination insights for driver pre-positioning
                - Implement loyalty rewards for high-rated customers to reduce Type 3 exposure
                - Monitor and retrain periodically to prevent model drift
                """)

    # ── Project 5: Airbnb Superhost ───────────────────
    with st.container(border=True):
        st.subheader("🏨 Airbnb Superhost Classification Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/superhostclassification.jpg")
        with col2:
            st.markdown("""
            Machine Learning project to classify Superhost status on Airbnb listings based
            on host performance factors, service quality, and listing characteristics.
            The model identifies key factors influencing Superhost achievement and helps hosts
            optimize their performance.
            """)
            st.write("**Tools:** Python (Pandas, NumPy), Scikit-learn, Streamlit")
            btn_row5 = st.columns([1, 1, 1])
            with btn_row5[0]:
                if st.button("📄 View Slides", key="pdf_btn5"):
                    st.session_state.pdf5 = not st.session_state.pdf5
            with btn_row5[1]:
                st.link_button("🚀 Live Dashboard", "https://airbnb-superhost-classification.streamlit.app/")
            with btn_row5[2]:
                if st.button("🔍 View Details", key="btn5"):
                    st.session_state.project5 = not st.session_state.project5

        if st.session_state.pdf5:
            pdf_viewer("https://drive.google.com/file/d/1GzGorBgr3NcPHjO5m-Ri3WgO1xJmRh-3/preview")

        # ── Load feature importance data (always needed for chart)
        comparison_all = pd.read_csv("data/feature_importance_comparison.csv")
        comparison_long = comparison_all.melt(
            id_vars="Feature",
            value_vars=["Permutation_RF_Norm","SHAP_RF_Norm","LogReg_Norm"],
            var_name="Model", value_name="Importance")
        comparison_long["Model"] = comparison_long["Model"].replace({
            "Permutation_RF_Norm": "Permutation RF",
            "SHAP_RF_Norm": "SHAP RF",
            "LogReg_Norm": "Logistic Regression"
        })
        feature_order = comparison_all.sort_values("SHAP_RF_Norm", ascending=True)["Feature"].tolist()
        fig_comp = px.bar(comparison_long, x="Importance", y="Feature", color="Model",
                          orientation="h", barmode="group",
                          category_orders={"Feature": feature_order})
        fig_comp.update_layout(yaxis=dict(autorange="reversed"), yaxis_title="", height=600,
                               margin=dict(t=30,b=0),
                               paper_bgcolor="#13151f", plot_bgcolor="#13151f", font_color="#ffffff",legend_font_color="#ffffff")

        if st.session_state.project5:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Model Performance Comparison")
                model_results = pd.DataFrame({
                    "Model": ["Dummy Baseline","Logistic Regression","Random Forest",
                              "Logistic Regression (Tuned)","Random Forest (Tuned)"],
                    "Accuracy": [0.82, 0.79, 0.86, 0.79, 0.88],
                    "Precision": [0.00, 0.46, 0.57, 0.46, 0.61],
                    "Recall":    [0.00, 0.87, 0.89, 0.87, 0.86],
                    "F1 Score":  [0.00, 0.60, 0.70, 0.60, 0.71],
                    "ROC-AUC":   [0.50, 0.892, 0.942, 0.892, 0.949],
                })
                st.dataframe(dark_df(model_results.style
                             .format("{:.3f}", subset=["Accuracy","Precision","Recall","F1 Score","ROC-AUC"])
                             .highlight_max(subset=["F1 Score","ROC-AUC"], color="#1a3a5c")),
                             use_container_width=True, hide_index=True)
                st.subheader("📊 Feature Importance Comparison (Normalized)")
                st.plotly_chart(fig_comp, use_container_width=True)
            with col2:
                st.subheader("📌 Project Overview")
                st.write("""
                This project focuses on the short-term rental industry, specifically Airbnb listings
                in New York City. Superhost status is awarded to hosts who consistently deliver
                high-quality service and maintain high customer satisfaction.

                **Goal:** Build a machine learning model to classify whether a host is likely to
                become a Superhost based on listing characteristics, host behavior, and location factors.
                """)
                st.subheader("📊 Method & Result")
                st.write("""
                Analysis conducted through EDA, feature engineering, and modeling using
                Logistic Regression and Random Forest Classifier.

                **Results:**
                - Random Forest achieved best performance with ROC-AUC of 0.949
                - Most influential features: host response rate, review scores rating,
                  number of reviews, amenities count
                """)
                st.subheader("💡 Insight & Recommendation")
                st.write("""
                Behavioral factors have a stronger influence than structural or location factors
                in determining Superhost status.

                **Recommendations:**
                - Increase speed and consistency of customer responses
                - Focus on service quality improvements to maintain high ratings
                - Add amenities to increase listing appeal
                - Encourage customers to leave reviews for higher credibility
                """)

    # ── Project 6: Flight Clustering ─────────────────
    with st.container(border=True):
        st.subheader("✈️ Flight Customer Segmentation – K-Means Clustering")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/clustering.jpg")
        with col2:
            st.markdown("""
            Machine Learning project for airline customer segmentation based on travel patterns,
            loyalty, and transaction behavior using K-Means Clustering. Identifies customer groups
            with similar characteristics to support more effective marketing and retention strategies.
            """)
            st.write("**Tools:** Python (Pandas, NumPy), Jupyter Notebook, Scikit-learn, Plotly")
            btn_row6 = st.columns([1, 1])
            with btn_row6[0]:
                if st.button("📄 View Slides", key="pdf_btn6"):
                    st.session_state.pdf6 = not st.session_state.pdf6
            with btn_row6[1]:
                if st.button("🔍 View Details", key="btn6"):
                    st.session_state.project6 = not st.session_state.project6

        if st.session_state.pdf6:
            pdf_viewer("https://drive.google.com/file/d/1EL5MEYlmGAYgs6YayQt6NqVlygyLo_hd/preview")

    # ── Load clustering data (always prepared) ───────
    new_df = pd.read_csv("data/new_df_cluster.csv")
    with open("models/kmeans_model.pkl", "rb") as f:
        kmeans = pickle.load(f)
    with open("models/pca_model.pkl", "rb") as f:
        pca = pickle.load(f)
    X_pca  = pca.transform(new_df)
    clusters = kmeans.predict(new_df)
    df_plot = pd.DataFrame({"PC1": X_pca[:,0], "PC2": X_pca[:,1], "Cluster": clusters.astype(str)})
    fig_pca = px.scatter(df_plot, x="PC1", y="PC2", color="Cluster")
    fig_pca.update_layout(height=500, paper_bgcolor="#13151f", plot_bgcolor="#13151f",
                          font_color="#ffffff",legend_font_color="#ffffff")

    if st.session_state.project6:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Clustering Insight (PCA Projection)")
            st.plotly_chart(fig_pca, use_container_width=True)
        with col2:
            st.subheader("📌 Project Overview")
            st.write("""
            This project focuses on airline customer segmentation based on transaction and
            loyalty data using an unsupervised learning approach.

            **Goal:** Identify customer groups with different behavioral characteristics to
            understand the business value of each segment and support more effective marketing.
            """)
            st.subheader("📊 Method & Result")
            st.write("""
            Analysis through data preprocessing, EDA, feature engineering, and K-Means Clustering.
            PCA used for dimensionality reduction and 2D visualization.

            **4 Segments:**
            - **Cluster 0 – Core Loyal Customers:** High activity, high frequency, large total distance
            - **Cluster 1 – Dormant/Low Value Users:** Low activity, rarely flies, long inactive
            - **Cluster 2 – Active Price-Sensitive Users:** Fairly active but deal-driven
            - **Cluster 3 – New/Growing Users:** New customers with early growing activity
            """)
            st.subheader("💡 Insight & Recommendation")
            st.write("""
            Customer distribution is uneven; most business value comes from specific segments.

            **Recommendations:**
            - **Core Loyal:** Exclusive loyalty programs and enhanced service experience
            - **Dormant Users:** Low-cost re-engagement campaigns (email, limited promos)
            - **Price-Sensitive:** Dynamic pricing and bundling strategies
            - **New Users:** Strong onboarding with early incentives for repeat orders
            """)

    # ── Project 7: House Price Regression ────────────
    with st.container(border=True):
        st.subheader("🏠 House Price Prediction – Regularized Regression")
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/regression.jpg")
        with col2:
            st.markdown("""
            Machine Learning project to predict house prices using Ridge and Lasso Regression
            to address multicollinearity and improve model stability.
            The main focus is model performance evaluation and feature influence interpretation.
            """)
            st.write("**Tools:** Python (Pandas, NumPy, Scikit-learn), Plotly, Streamlit")
            btn_row7 = st.columns([1, 1])
            with btn_row7[0]:
                if st.button("📄 View Slides", key="pdf_btn7"):
                    st.session_state.pdf7 = not st.session_state.pdf7
            with btn_row7[1]:
                if st.button("🔍 View Details", key="btn7"):
                    st.session_state.project7 = not st.session_state.project7

        if st.session_state.pdf7:
            pdf_viewer("https://drive.google.com/file/d/1O3JA4hDTSZfTmEJra5EupFjyu1ubJHdI/preview")

    # ── Load regression data ──────────────────────
    df_metrics = pd.read_csv("data/metrics.csv")
    df_coef    = pd.read_csv("data/coef.csv")
    df_coef_melt = df_coef.melt(id_vars="Feature", var_name="Model", value_name="Coefficient")
    fig_coef = px.bar(df_coef_melt, x="Feature", y="Coefficient", color="Model",
                      barmode="group")
    fig_coef.update_layout(height=450, paper_bgcolor="#13151f", plot_bgcolor="#13151f",
                           font_color="#ffffff",legend_font_color="#ffffff")

    if st.session_state.project7:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Model Evaluation")
            st.dataframe(dark_df(df_metrics.style), use_container_width=True, hide_index=True)
            st.subheader("Feature Importance")
            st.plotly_chart(fig_coef, use_container_width=True)
        with col2:
            st.subheader("📌 Project Overview")
            st.write("""
            This project predicts house prices using the Boston Housing Dataset with a
            Regularized Regression approach. Models used: Ridge Regression and Lasso
            Regression to address multicollinearity and improve stability.
            """)
            st.subheader("📊 Method & Result")
            st.write("""
            Analysis through data preprocessing, EDA, and modeling with Ridge and Lasso Regression.

            Evaluation metrics: MAE, RMSE, MAPE

            **Results:**
            - Ridge: MAE ~3.04, RMSE ~4.67, MAPE ~15.29%
            - Lasso: MAE ~3.08, RMSE ~4.67, MAPE ~15.47%
            - Ridge slightly outperforms in accuracy; Lasso simplifies features
            """)
            st.subheader("💡 Insight & Recommendation")
            st.write("""
            Feature influence on house prices is uneven and affected by multicollinearity.

            **Insights:**
            - **rm** (rooms) consistently has a strong positive effect on price
            - **lstat** shows a significant negative effect
            - Some features like **nox** are retained in Ridge but eliminated by Lasso

            **Recommendations:**
            - Use Ridge for more accurate and stable price predictions
            - Use Lasso to understand the main factors affecting price
            - Focus on key features like room count and socioeconomic conditions
            """)

# ======================
# FOOTER
# ======================
st.markdown("""
<div class="footer-section" id="contact">
    <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:40px;">
        <div style="max-width:520px;">
            <div class="footer-cta-title">Let's Connect & Collaborate</div>
            <p class="footer-cta-desc" style="text-align: justify; text-justify: inter-word;">
                Open to new opportunities, collaborations, or just a conversation about data.
                Whether you have a project in mind or want to discuss insights, I'd love to hear from you.
            </p>
            <div class="footer-divider"></div>
            <div class="footer-contact-item"><a href="mailto:fayzan.rh@gmail.com">📧 fayzan.rh@gmail.com</a></div>
            <div class="footer-contact-item"><a href="https://wa.me/6287776604718">📞 +62-877-7660-4718</a></div>
        </div>
        <div style="font-size:0.85rem; color:#6b7fa3; min-width:180px;">
            <div style="font-weight:600; color:#a0a8be; margin-bottom:8px;">Connect</div>
            <div style="margin-bottom:6px;"><a href="https://linkedin.com/in/fayzan-rizky-hidayat/" target="_blank" style="color:#6b7fa3; text-decoration:none;">LinkedIn</a></div>
            <div style="margin-bottom:6px;"><a href="https://github.com/freedaya" target="_blank" style="color:#6b7fa3; text-decoration:none;">GitHub</a></div>
            <div style="margin-bottom:6px;"><a href="https://www.instagram.com/fayzan.rizky" target="_blank" style="color:#6b7fa3; text-decoration:none;">Instagram</a></div>
            <div><a href="mailto:fayzan.rh@gmail.com" style="color:#6b7fa3; text-decoration:none;">Email</a></div>
        </div>
    </div>
    <div class="footer-bottom" style="display: flex; align-items: center; justify-content: space-between; padding: 20px 0; margin-top: 36px; border-top: 1px solid #1e2030;">
        <div class="footer-bottom-text" style="font-size: 0.78rem; color: #4a5170;">
            © 2025 Fayzan Rizky Hidayat · Data Analyst & Data Scientist
        </div>
    </div>
""", unsafe_allow_html=True)
