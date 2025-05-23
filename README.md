# アプリ説明
## 概要
* 機能
  - CSV読み込み
  - CSV先頭５行表示
  - ヒストグラム作成
  - chatGPTがデータの要約を生成

## 使い方
* 通常
  - ターミナルにおいて`streamlit run app.py`でアプリ起動
  - 任意のCSV投入で自動分析
* chatGPTが動かなかった場合
  - 02_streamlit内に「.env」ファイル作成
  - .envファイル内に「OPENAI_API_KEY」という変数名でOPENAIのAPIキーを入力
  - 上記の手順で実行