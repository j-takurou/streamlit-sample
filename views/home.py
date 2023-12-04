import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ダミーデータの生成
date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq='B')
data = {
    'Open': np.random.uniform(100, 200, len(date_range)),
    'High': np.random.uniform(100, 200, len(date_range)),
    'Low': np.random.uniform(100, 200, len(date_range)),
    'Close': np.random.uniform(100, 200, len(date_range))
}
df = pd.DataFrame(data, index=date_range)
df['High'] = df.apply(lambda row: max(row['Open'], row['Close'], row['High']), axis=1)
df['Low'] = df.apply(lambda row: min(row['Open'], row['Close'], row['Low']), axis=1)

# データをCSVファイルに保存
df.to_csv('stock_data.csv')


def load_view():
    # データの読み込み
    df = pd.read_csv('stock_data.csv', parse_dates=True, index_col=0)

    # ダッシュボードのタイトル
    st.title('株価データ可視化ダッシュボード')

    # データテーブルの表示
    st.write(df)

    # 折れ線グラフの作成
    plt.figure(figsize=(10, 4))
    plt.plot(df['Open'], label='Open')
    plt.plot(df['Close'], label='Close')
    plt.plot(df['High'], label='High')
    plt.plot(df['Low'], label='Low')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    st.pyplot(plt)
