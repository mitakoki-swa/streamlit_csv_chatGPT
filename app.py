import streamlit as st

"""
streamlitアプリの構築基本
1. コンストラクタ（if __name__ == "__main__": ←これ）を用意し、各機能をそれぞれ関数で分離する。
    - 保守・追加開発がしやすいため。
    - notebookフォルダを用意し、その中でアルゴリズム検証するのはOK。私もよくやります。

2. 1ができたら次書きます

アプリの実行方法
- ターミナル（venv作るところ）で `streamlit run [実行ファイル名: 今回はapp.py]` を実行。
- 今回は app.py ファイルとしているが、home.py にしてもよい
"""

def init_page():
    """ streamlitの初期化 """
    st.set_page_config(
        page_title="xxx" # ページタイトル
        page_icon="📚" # ページアイコン
    )
    st.title("title")

def main():
    """ここに基本処理を書く"""
    st.write("body")

if __name__ == "__main__":
    init_page()
    main()