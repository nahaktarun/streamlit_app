import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyzer

    Shown are the stock prices of Apple
    """
)

ticker_symbol =  st.text_input(
    "Enter the Stock Symbol","AAPL", key="placeholder"
)
# ticker_symbol = "AAPL"

# $caleraws123$


col1 , col2 = st.columns(2)
with col1:
    start_date = st.date_input("Input the starting date", datetime.date(2023,1,1))
with col2:
    end_date = st.date_input("Input the Ending date", datetime.date(2023,2,11))


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start=f"{start_date}" , end=f"{end_date}")

st.write(f"""### {ticker_symbol}'s EOD price """)

st.dataframe(ticker_df)


st.write("""
    ## Daily closing price Chart

""")
## Show casing the charts
st.line_chart(ticker_df.Close)


st.write("""
    ## Volumes of shares traded each day

""")
## Show casing the charts
st.line_chart(ticker_df.Volume)