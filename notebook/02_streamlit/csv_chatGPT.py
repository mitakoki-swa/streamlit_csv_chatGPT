import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from openai import OpenAI
import os


# Open AIキー
#openai.api_key = st.secrets['OPENAI_API_KEY']

st.title('データ分析 × ChatGPT レポート自動生成')

#ファイルアップロード
uploaded_file = st.file_uploader('csvファイルをアップロードしてください', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('データプレビュー')
    st.dataframe(df.head())

    # 基本統計量
    st.subheader('基本統計情報')
    st.write(df.describe())

    # グラフ化
    st.subheader('ヒストグラム')
    numeric_cols = df.select_dtypes(include='number').columns
    selected_col = st.selectbox('数値列を選んでください。', numeric_cols)
    fig, ax = plt.subplots()
    df[selected_col].hist(ax=ax, bins='auto')
    st.pyplot(fig)

    # ChatGPTに要約を依頼
    st.subheader('ChatGPTによるレポート生成')
    if st.button('レポート生成'):
        prompt = f"""
        以下はデータ分析の結果です。統計的に意味のある特徴や気付きを日本語でレポートしてください
        
        データ概要：
        {df.describe().to_string()}
        """

        with st.spinner('ChatGPTが分析しています...'):
            # .env読み込み
            load_dotenv()
            client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': 'あなたは優秀なデータアナリストです'},
                    {'role': 'user', 'content': prompt}
                ]
            )
            
            report = response.choices[0].message.content