import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("📈 Time Series Forecasting App")

# Upload file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])

    monthly_data = (
        df.groupby(pd.Grouper(key='Date', freq='M'))['Close']
        .mean()
        .reset_index()
    )
    monthly_data.columns = ['ds', 'y']

    st.subheader("Monthly Time Series")
    st.line_chart(monthly_data.set_index('ds'))

    # Forecast horizon
    periods = st.slider("Forecast months", 3, 24, 12)

    model = Prophet()
    model.fit(monthly_data)

    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)

    st.subheader("Forecast")
    fig = model.plot(forecast)
    st.pyplot(fig)
