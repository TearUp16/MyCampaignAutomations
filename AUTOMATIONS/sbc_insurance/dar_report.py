import pandas as pd
import streamlit as st
from io import BytesIO
from datetime import datetime

def dar_sbc_insurance(file):
    df = pd.read_excel(file)

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%d/%Y')
    else:
        st.warning("Column 'Date' is missing or misnamed.")
    
    df_cleaned = pd.DataFrame()
    df_cleaned['Action Date'] = df['Date']
    df_cleaned['Campaign'] = 'ACA'
    df_cleaned['Agency'] = 'SP MADRID'
    df_cleaned['Account'] = df['Account No.']
    df_cleaned['Action'] = df['Remark Type']
    df_cleaned['Result'] = df['Status']
    df_cleaned['Contact'] = ''  
    df_cleaned['Payment_Date'] = ''  
    df_cleaned['Payment_Amount'] = ''  
    df_cleaned['RFD'] = '' 

    if 'Product Type' in df.columns and 'Remark' in df.columns:
        df_cleaned['Comments'] = df['Product Type'].astype(str) + " | " + df['Remark'].astype(str)
    else:
        df_cleaned['Comments'] = ''
        st.warning("Columns 'Product Type' or 'Remark' are missing or misnamed.")


    if 'Remark' in df.columns:
        df_cleaned['COUNTER'] = df['Remark'].str.len()
    else:
        df_cleaned['COUNTER'] = pd.NA 
        st.warning("Column 'Remark' is missing or misnamed.")

    df_cleaned['Product'] = df['Product Type']
    df_cleaned['Level'] = ''
    df_cleaned['Remarks'] = df['Remark']
    
    return df_cleaned
container = st.container(border=True)
container.title("DAR REPORT")
container.subheader("Upload your Daily Remark Report")

uploaded_file = container.file_uploader("Upload your file", type=["xlsx"])

if uploaded_file is not None:
    try:
        cleaned_df = dar_sbc_insurance(uploaded_file)
        
        container.dataframe(cleaned_df)
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            cleaned_df.to_excel(writer, index=False)
        output.seek(0)

        current_date = datetime.today().strftime('%Y-%m-%d')
        file_name = f"EFS DAR {current_date}.xlsx"

        container.download_button(
            label="Download File",
            data=output,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        container.error(f"An error occurred: {e}")
