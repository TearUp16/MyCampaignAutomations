import streamlit as st

# Download this first:
# pip install streamlit openpyxl xlsxwriter 

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