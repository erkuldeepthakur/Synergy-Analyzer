import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Synergy Analyzer", layout="wide")

st.title("📁 Synergy Analyzer – CSV File Uploader")

# CSV upload box
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Preview of Uploaded Data")
    st.dataframe(df)

    st.subheader("📊 Statistical Summary")
    st.write(df.describe())

    # Find numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_cols:
        st.subheader("📈 Visualization")
        selected_col = st.selectbox("Select a numeric column to plot:", numeric_cols)

        fig, ax = plt.subplots()
        ax.plot(df[selected_col])
        ax.set_title(f"Line Chart of {selected_col}")
        ax.set_xlabel("Index")
        ax.set_ylabel(selected_col)

        st.pyplot(fig)
    else:
        st.info("No numeric columns available for plotting.")
else:
    st.warning("Please upload a CSV file to proceed.")
