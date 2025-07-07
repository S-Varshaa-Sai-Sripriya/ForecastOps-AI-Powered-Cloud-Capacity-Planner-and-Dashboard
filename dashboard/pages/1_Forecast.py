import streamlit as st
from src.utils import load_region_data
from src.forecast import forecast_with_prophet

st.title("Forecasting")

region = st.selectbox("Choose a region", ['us-east', 'us-west', 'eu-central', 'ap-south'])
df = load_region_data("data/capacity_usage_simulated.csv", region)
forecast_df = forecast_with_prophet(df)

st.line_chart(forecast_df.set_index("ds")[["yhat", "yhat_lower", "yhat_upper"]])
