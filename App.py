import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('''# **Binance Price**
A cryptocurrency app that pulls data from *Binance API*.
''')

st.header('**Selected Crypto Price**')


df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

crpytoList = {
    'Crypto 1': 'BTCBUSD',
    'Crypto 2': 'ETHBUSD',
    'Crypto 3': 'BNBBUSD',

}

col1, col2, col3 = st.columns(3)

for i in range(len(crpytoList.keys())):
    selected_crypto_label = list(crpytoList.keys())[i]
    selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
    selected_crypto = st.sidebar.selectbox(selected_crypto_label, df.symbol, selected_crypto_index, key=str(i))
    col_df = df[df.symbol == selected_crypto]
    col_price = round_value(col_df.weightedAvgPrice)
    col_percent = f'{float(col_df.priceChangePercent)}%'

    if i == 0:
        with col1:
            st.metric(selected_crypto, col_price, col_percent)
            selected_crypto_df = df[df.symbol == selected_crypto]
            fig, ax = plt.subplots()
            ax.bar(selected_crypto_df.symbol, col_price)
            ax.set_xlabel('Cryptocurrency')
            ax.set_ylabel('Price')
            ax.set_title(f'Price of {selected_crypto}')
            st.pyplot(fig)

    if i== 1:
        with col2:
            st.metric(selected_crypto, col_price, col_percent)
            selected_crypto_df = df[df.symbol == selected_crypto]
            fig, ax = plt.subplots()
            ax.bar(selected_crypto_df.symbol,col_price)
            ax.set_xlabel('Cryptocurrency')
            ax.set_ylabel('Price')
            ax.set_title(f'Price of {selected_crypto}')
            st.pyplot(fig)

    if i == 2:
        with col3:
            st.metric(selected_crypto, col_price, col_percent)
            selected_crypto_df = df[df.symbol == selected_crypto]
            fig, ax = plt.subplots()
            ax.bar(selected_crypto_df.symbol, col_price)
            ax.set_xlabel('Cryptocurrency')
            ax.set_ylabel('Price')
            ax.set_title(f'Price of {selected_crypto}')
            st.pyplot(fig)

st.header('**All Price**')
st.dataframe(df)
