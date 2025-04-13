import streamlit as st

st.set_page_config(
    page_title="Campaign Automations",
    layout="wide",
    initial_sidebar_state="expanded"
)
pages = {"PAGES": [
        st.Page("dashboard.py", icon="📊", title="DASHBOARD"),
        st.Page("automations.py", icon ="🤖", title="AUTOMATIONS"),
    ],}

pg = st.navigation(pages)
pg.run()