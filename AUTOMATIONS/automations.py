import streamlit as st
from fcl_drive_input import fcl_drive_for_input
from fcl_drive_input2 import fcl_2nd_drive_for_input
from pif_legal_mapping import pif_legal_mapping
from pif_legal_web_import_file import pif_legal_website_import_file
from autostat_for_fcl import autostat_fcl

# Sidebar Campaign Selection
st.sidebar.title("CAMPAIGN AUTOMATIONS")
selected_campaign = st.sidebar.selectbox(
    "SELECT CAMPAIGN",
    ["FCL", "SBC HOMELOAN", "SBC INSURANCE", "SBF HOMELOAN"]
)

# Only show tabs when the campaign is FCL
if selected_campaign == "FCL":
    tab1, tab2, tab3 = st.tabs(["ENDORSEMENT", "PULLOUTS", "PTP"])

    # Endorsements Tab
    with tab1:
        if selected_campaign == "FCL":
            st.title("ENDORSEMENT")
            fcl_page = st.sidebar.selectbox(
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

    # Pullouts Tab
    with tab2:
        st.title("PULLOUTS")
        fcl_page = st.selectbox(
            "SELECT AUTOMATION",
            ["AUTOSTAT FOR FCL"]
        )
        if fcl_page == "AUTOSTAT FOR FCL":
            autostat_fcl()

    # PTP Tab
    with tab3:
        st.write("COMING SOON")

# SBC HOMELOAN
elif selected_campaign == "SBC HOMELOAN":
    tab4, tab5, tab6 = st.tabs(["ENDORSEMENT", "PULLOUTS", "PTP"])

    with tab4:
        if selected_campaign == "SBC HOMELOAN":
            st.title("ENDORSEMENT")
            sbc_homeloan = st.selectbox("SELECT AUTOMATION",
                                        ["SBC ENDORSEMENT"])
    with tab5:
        st.title("COMING SOON")
    with tab6:
        st.title("COMING SOON")

# SBC INSURANCE
elif selected_campaign == "SBC INSURANCE":
    tab7, tab8, tab9 = st.tabs(["ENDORSEMENT", "PULLOUTS", "PTP"])

    with tab7:
        if selected_campaign == "SBC INSURANCE":
            st.title("COMING SOON")
    with tab8:
        st.title("PULLOUTS")
    with tab9:
        st.title("PTP")

# SBF HOMELOAN
elif selected_campaign == "SBF HOMELOAN":
    tab10, tab11, tab12 = st.tabs(["ENDORSEMENTS","PULLOUTS","PTP"])
    st.title("SBF HOMELOAN AUTOMATIONS")
    st.write("COMING SOON")

