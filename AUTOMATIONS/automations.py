import streamlit as st
from fcl_drive_input import fcl_drive_for_input
from fcl_drive_input2 import fcl_2nd_drive_for_input
from pif_legal_mapping import pif_legal_mapping
from pif_legal_web_import_file import pif_legal_website_import_file
from autostat_for_fcl import autostat_fcl

# Sidebar Campaign Selection
st.sidebar.title("CAMPAIGN AUTOMATIONS")
selected_task = st.sidebar.selectbox(
    "SELECT TASK",
    ["ENDORSEMENT", "PULLOUTS", "PTP"]
)

# Only show tabs when the campaign is "ENDORSEMENT"
if selected_task == "ENDORSEMENT":
    tab1, tab2, tab3 = st.tabs(["FORECLOSURE", "SBC HOMELOAN", "SBC INSURANCE"])

    # FCL Tab
    with tab1:
        st.title("FORECLOSURE") 
        fcl_page = st.selectbox(
            "SELECT AUTOMATION",
            [
                "FOR INPUT DATA IN FCL DRIVE",
                "FOR INPUT DATA IN 2ND FCL DRIVE",
                "PIF LEGAL MAPPING",
                "PIF LEGAL WEBSITE IMPORT FILE"
            ]
        )
        if fcl_page == "FOR INPUT DATA IN FCL DRIVE":
            fcl_drive_for_input()
        elif fcl_page == "FOR INPUT DATA IN 2ND FCL DRIVE":
            fcl_2nd_drive_for_input()
        elif fcl_page == "PIF LEGAL MAPPING":
            pif_legal_mapping()
        elif fcl_page == "PIF LEGAL WEBSITE IMPORT FILE":
            pif_legal_website_import_file()

    # SBC HOMELOAN Tab
    with tab2:
        st.title("SBC HOMELOAN")
        sbc_homeloan = st.selectbox("SELECT AUTOMATION", ["SBC ENDORSEMENT"])

    # SBC INSURANCE Tab
    with tab3:
        st.title("SBC INSURANCE")
        st.write("COMING SOON")

# PULLOUTS
elif selected_task == "PULLOUTS":
    tab5, tab6, tab7 = st.tabs(["FORECLOSURE", "SBC HOMELOAN", "SBC INSURANCE"])

    # FCL Tab
    with tab5:
        st.title("FORECLOSURE")
        fcl_page = st.selectbox(
            "SELECT AUTOMATION",
            ["AUTOSTAT FOR FCL"]
        )
        if fcl_page == "AUTOSTAT FOR FCL":
            autostat_fcl()

    # SBC HOMELOAN Tab
    with tab6:
        st.title("SBC HOMELOAN")
        st.write("COMING SOON")

    # SBC INSURANCE Tab
    with tab7:
        st.title("SBC INSURANCE")
        st.write("COMING SOON")

# PTP
elif selected_task == "PTP":
    tab8, tab9, tab10 = st.tabs(["FORECLOSURE", "SBC HOMELOAN", "SBC INSURANCE",])

    # FCL Tab
    with tab8:
        st.title("FCL")
        st.write("COMING SOON")

    # SBC HOMELOAN Tab
    with tab9:
        st.title("SBC HOMELOAN")
        st.write("COMING SOON")

    # SBC INSURANCE Tab
    with tab10:
        st.title("SBC INSURANCE")

