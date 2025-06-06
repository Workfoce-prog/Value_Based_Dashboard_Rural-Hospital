
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Value-Based Care Readiness Dashboard", layout="wide")
st.title("🏥 Value-Based Care Readiness Dashboard for Rural Hospitals")

st.sidebar.header("📂 Data Upload or Browse")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
use_sample = st.sidebar.checkbox("Use Sample Data Instead", value=True)

# Load data safely
df = None
if uploaded_file and not use_sample:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully.")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
elif use_sample:
    try:
        sample_path = "value_based_sample_data.csv"
        if os.path.exists(sample_path):
            df = pd.read_csv(sample_path)
            st.info("ℹ️ Using built-in sample data.")
        else:
            st.warning("⚠️ Sample data file not found.")
    except Exception as e:
        st.error(f"❌ Error loading sample data: {e}")

# Show table and visualizations
if df is not None:
    st.subheader("📊 Hospital Scorecard Table")
    st.dataframe(df)

    st.subheader("📈 RAG Indicator Visualizations")
    metrics = [col for col in df.columns if col != "Hospital"]
    selected_metric = st.selectbox("Choose a metric to visualize", metrics)

    fig, ax = plt.subplots()
    ax.bar(df["Hospital"], df[selected_metric], edgecolor='black')
    ax.set_ylabel(selected_metric)
    ax.set_title(f"{selected_metric} by Hospital")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.download_button("📥 Download Data as CSV", df.to_csv(index=False), "hospital_scorecard.csv")
else:
    st.warning("Upload a file or enable sample data to continue.")
