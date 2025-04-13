import streamlit as st
from fcl_drive_input import fcl_drive_for_input
from fcl_drive_input2 import fcl_2nd_drive_for_input
from pif_legal_mapping import pif_legal_mapping
from pif_legal_web_import_file import pif_legal_website_import_file
from autostat_for_fcl import autostat_fcl

st.sidebar.title("CAMPAIGN AUTOMATIONS")
selected_campaign = st.sidebar.selectbox(
    "SELECT CAMPAIGN",
    ["FCL", "SBC HOMELOAN", "SBC INSURANCE", "SBF HOMELOAN"]
)

if selected_campaign == "FCL":
    st.title("FCL AUTOMATIONS")
    fcl_page = st.selectbox(
        "SELECT AUTOMATION",
        ["FOR INPUT DATA IN FCL DRIVE",
         "FOR INPUT DATA IN 2ND FCL DRIVE",
         "PIF LEGAL MAPPING",
         "PIF LEGAL WEBSITE IMPORT FILE",
         "AUTOSTAT FOR FCL"]
    )
    if fcl_page == "FOR INPUT DATA IN FCL DRIVE":
        fcl_drive_for_input()
    elif fcl_page == "FOR INPUT DATA IN 2ND FCL DRIVE":
        fcl_2nd_drive_for_input()
    elif fcl_page == "PIF LEGAL MAPPING":
        pif_legal_mapping()
    elif fcl_page == "PIF LEGAL WEBSITE IMPORT FILE":
        pif_legal_website_import_file()
    elif fcl_page == "AUTOSTAT FOR FCL":
        autostat_fcl()

elif selected_campaign == "SBC HOMELOAN":
    st.title("SBC HOMELOAN AUTOMATIONS")
    st.write("Content for SBC Home Loan campaign coming soon...")

elif selected_campaign == "SBC INSURANCE":
    st.title("SBC INSURANCE AUTOMATIONS")
    st.write("Content for SBC Insurance campaign coming soon...")

elif selected_campaign == "SBF HOMELOAN":
    st.title("SBF HOMELOAN AUTOMATIONS")
    st.write("Content for SBF Home Loan campaign coming soon...")
