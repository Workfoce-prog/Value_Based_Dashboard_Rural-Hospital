
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Value-Based Care Readiness Dashboard", layout="wide")

st.title("🏥 Value-Based Care Readiness Dashboard for Rural Hospitals")

# Sidebar
st.sidebar.header("📂 Data Upload or Browse")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
use_sample = st.sidebar.checkbox("Use Sample Data Instead", value=True)

# Load data
if uploaded_file and not use_sample:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
elif use_sample:
    df = pd.read_csv("value_based_sample_data.csv")
    st.info("ℹ️ Using built-in sample data.")

if 'df' in locals():
    st.subheader("📊 Hospital Scorecard Table")
    st.dataframe(df)

    # Visualizations
    st.subheader("📈 RAG Indicator Visualizations")
    metrics = [
        "Readmission Rate (%)",
        "Chronic Disease Score",
        "Patient Engagement Rate (%)",
        "Population Health Index",
        "Timely Follow-Up Rate (%)",
        "Social Determinants Screening (%)",
        "Preventive Care Utilization (%)"
    ]

    selected_metric = st.selectbox("Choose a metric to visualize", metrics)

    fig, ax = plt.subplots()
    ax.bar(df["Hospital"], df[selected_metric], edgecolor='black')
    ax.set_ylabel(selected_metric)
    ax.set_title(f"{selected_metric} by Hospital")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.markdown("---")
    st.download_button("📥 Download Data as CSV", df.to_csv(index=False), "hospital_scorecard.csv")
