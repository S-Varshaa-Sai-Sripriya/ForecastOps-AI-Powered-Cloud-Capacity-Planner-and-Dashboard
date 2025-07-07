import streamlit as st
from src.utils import load_region_data

st.title("Region Drilldown")

region = st.selectbox("Select region", ['us-east', 'us-west', 'eu-central', 'ap-south'])
df = load_region_data("data/capacity_usage_simulated.csv", region)

st.line_chart(df.set_index("timestamp")[["cpu_usage", "memory_usage", "demand_forecast"]])
st.dataframe(df.head(100))
