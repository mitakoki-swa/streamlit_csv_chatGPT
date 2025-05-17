import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import os
load_dotenv()

def init_page():
    """ streamlitの初期化 """
    st.set_page_config(
        page_title="CSV読み込み", # ページタイトル
        page_icon="📚" # ページアイコン
        )
    st.title("CSV要約アプリ")


def upload_file():
    """ ファイルアップロード """
    try:
        uploaded_file = st.file_uploader('csvファイルをアップロードしてください', type='csv')
    except Exception:
        st.error('ファイル読み込みに失敗しました。正しいCSVファイルを指定してください。')
    return uploaded_file


def load_file(uploaded_file):
    """ ファイル読み込み、出力 """
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
    return df


def request_chatgpt(df):
    """ ChatGPTに要約を依頼 """
    st.subheader('ChatGPTによるレポート生成')
    if st.button('レポート生成'):
        prompt = f"""
        以下はデータ分析の結果です。統計的に意味のある特徴や気付きを日本語でレポートしてください

        データ概要：
        {df.describe().to_string()}
        """

        with st.spinner('ChatGPTが分析しています...'):
            # .env読み込み
            load_dotenv(find_dotenv())
            client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': 'あなたは優秀なデータアナリストです'},
                    {'role': 'user', 'content': prompt}
                ]
            )
            report = response.choices[0].message.content

            return report


def main():
    uploaded_file = upload_file()
    if uploaded_file:
        df = load_file(uploaded_file)
        request_chatgpt(df)


if __name__ == "__main__":
    init_page()
    main()