import pandas as pd
import streamlit as st
from datetime import datetime
import os

# Function to process and clean the data (without passing df)
def process_data(uploaded_file):
    # Read the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Select only the necessary columns and rename them
    df_cleaned = pd.DataFrame()

    df_cleaned['COLLECTOR NAME'] = df['Remark By']
    df_cleaned['ACA'] = 'SP MADRID'
    df_cleaned['Product ( AL/ SBL/ SHL)'] = df['Product Type']
    df_cleaned['Client Name'] = df['Debtor']
    df_cleaned['IS Ref No#'] = ''
    df_cleaned['BUCKET'] = ''
    df_cleaned['AGING'] = ''
    df_cleaned['Date Endorsed'] = ''
    df_cleaned['PN_Number'] = df['Account No.']
    df_cleaned['UNPAID INSURANCE'] = ''
    df_cleaned['PTP Amt'] = df['PTP Amount']
    df_cleaned['PTP Date Acquired'] = ''
    df_cleaned['PTP Date'] = df['PTP Date']
    df_cleaned['STATUS (PTP / BP / CURED)'] = df['Status']
    
    # Time condition for 'TIME (10AM/ 2PM and 4PM)'
    def set_time_category(time_str):
        try:
            time_obj = datetime.strptime(time_str, '%I:%M:%S %p')
            if time_obj <= datetime.strptime("10:00:00 AM", '%I:%M:%S %p') and time_obj < datetime.strptime("2:00:00 PM", '%I:%M:%S %p'):
                return '10AM'
            elif time_obj <= datetime.strptime("2:00:00 PM", '%I:%M:%S %p') and time_obj < datetime.strptime("4:00:00 PM", '%I:%M:%S %p'):
                return '2PM'
            elif time_obj <= datetime.strptime("10:00:00 PM", '%I:%M:%S %p'):
                return '4PM'
            else:
                return ''
        except:
            return ''
    
    # Apply time condition to 'TIME (10AM/ 2PM and 4PM)'
    df_cleaned['TIME (10AM/ 2PM and 4PM)'] = df['Time'].apply(set_time_category)

    # Add the additional blank column
    df_cleaned['TYPE OF BOM / NEW'] = ''
    
    # Filter rows where STATUS starts with 'PTP'
    df_cleaned = df_cleaned[df_cleaned['STATUS (PTP / BP / CURED)'].str.startswith('PTP', na=False)]

    # Convert the date columns to just show the date (removing time) and format as MM/DD/YYYY
    df_cleaned['Date Endorsed'] = pd.to_datetime(df_cleaned['Date Endorsed'], errors='coerce').dt.strftime('%m/%d/%Y')
    df_cleaned['PTP Date'] = pd.to_datetime(df_cleaned['PTP Date'], errors='coerce').dt.strftime('%m/%d/%Y')

    return df_cleaned

# Streamlit UI components
st.title('Data Cleaner Tool')

# Upload file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Process the data directly without passing a DataFrame
    cleaned_df = process_data(uploaded_file)  # <-- Pass the uploaded file here to the process_data function

    # Style the DataFrame: make only the columns yellow
    styled_df = cleaned_df.style.set_table_styles(
        [{
            'selector': 'th', 
            'props': [('background-color', 'yellow')]
        }]
    )

    # Display styled data
    st.dataframe(styled_df)

    cleaned_data = process_data(uploaded_file)

    # Save the cleaned file to a valid directory
    output_dir = os.path.join(os.getcwd(), "output_files")  # Save to a folder named 'output_files'
    os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist
    cleaned_file_path = os.path.join(output_dir, "cleaned_file_filtered_ptp.xlsx")

    # Save the cleaned DataFrame to the file
    cleaned_df.to_excel(cleaned_file_path, index=False)

    # Provide the option to download the cleaned file
    st.download_button(
        label="Download File",
        data=open(cleaned_file_path, "rb").read(),
        file_name="SBC_INSURANCE_PTP.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
