import streamlit as st
from src.utils import load_region_data
from src.detect_anomalies import detect_isolation_forest

st.title("Anomaly Detection")

region = st.selectbox("Select region", ['us-east', 'us-west', 'eu-central', 'ap-south'])
df = load_region_data("data/capacity_usage_simulated.csv", region)
anomaly_df = detect_isolation_forest(df, "cpu_usage")

st.dataframe(anomaly_df[anomaly_df["anomaly"] == -1])
