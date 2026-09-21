# daily-notifier

GitHub Actionsを利用して、翌日の生活情報を毎日夕方に自動通知するシステムです。

GitHub Actionsから毎日自動実行され、気象庁の翌日の天気予報と暦情報をメール通知できる状態です。

今後は、追加機能の実装を進める予定です。

---

## このプロジェクトが解決すること

夕方は、家事や子どもの世話などで忙しく、翌日の生活に必要な情報を複数のWebサイトやアプリで確認するのが負担でした。

daily-notifierは、翌日の天気や降水確率、暦などの生活情報をまとめて通知することで、必要な情報を短時間で確認できるようにすることを目的としています。

また、SNSやアプリを開く機会を減らし、広告やショート動画などに時間を奪われないデジタルデトックス環境を目指しています。

---

## 現在通知される情報

- 明日の日付
- 明日の天気予報
- ６時間ごとの降水確率
- 最高気温
- 最低気温
- 予報取得時刻
- 明日の暦イベント

<img width="448" height="569" alt="通知メールのスクリーンショット" src="https://github.com/user-attachments/assets/278a5690-822c-4390-a5b0-46668b5e7805" />


---


## 現在の開発状況


- プロジェクト基盤
    - プロジェクトの作成
    - Gitリポジトリの作成
    - 開発方針・設計ドキュメントの整備
- GitHub Actionsによる自動実行
    - GitHub ActionsによるPython実行
    - GitHub Actionsの定期実行
- 天気情報の取得・加工
    - 気象庁JSONの取得
    - JSONから必要な情報の抽出
    - dataclassによる天気情報の型付きデータ構造
    - JSON抽出処理の整理
    - エリア検索の共通化
    - 取得情報を人間に読みやすい形式に変換
- メール通知
    - メール送信
    - 暦情報のメール通知
- 暦情報の取得
    - 暦情報APIの取得
- 設定・機密情報管理
    - GitHub Secretsによる機密情報管理
    - Settingsによるメール関連環境変数の管理
    - 環境変数の存在・空文字チェック
    - Local / GitHub Actionsの環境差を吸収
- コード品質・保守性
    - Pythonモジュール分割
    - 型注釈
    - Ruffによるコード整形
    - ログの実装
- テスト・CI
    - pytestの実装
    - CIの導入（pytest、Ruffによるコードチェックとフォーマットチェック）
    - GitHubのブランチ保護にRequired Status Checkを設定


---

## 開発環境

| 項目      | 内容                 |
| ------- | ------------------ |
| OS      | Windows 11         |
| 言語      |  Python 3.14     |
| 利用ライブラリ |  requests, python-dotenv, pytest|
| 開発ツール |  Ruff |
| エディタ    | Visual Studio Code |
| バージョン管理 | Git / GitHub       |
| CI/CD   | GitHub Actions     |


---


## ディレクトリ構成

.env はプロジェクト外で管理しています。

```text
daily-notifier/
├── .github/workflows/
│   ├── daily-notifier.yml  # 本番用：定期実行・メール通知
│   └── ci.yml              # CI用：Pull Request時のテスト・コード検証
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── mailer.py
│   ├── formatters/
│   │   ├── message.py
│   │   ├── weather_formatter.py
│   │   └── koyomi_formatter.py
│   └── providers/
│       ├── weather_json_models.py
│       ├── weather_json.py
│       ├── koyomi_models.py
│       └── koyomi.py
├── tests/
│   ├── test_config.py
│   ├── test_mailer.py
│   ├── test_weather_formatter.py
│   ├── test_weather_json.py
│   ├── test_koyomi_formatter.py
│   └── test_koyomi.py
├── main.py
├── .venv/（Git管理外）
├── .vscode/（Git管理外）
├── .env.example
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ライセンス

未定

---

## セットアップ方法


### Python仮想環境

本プロジェクトでは、Pythonの仮想環境（`.venv`）を使用しています。

初回セットアップ

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
仮想環境有効化後は、
```bash
python --version
```
でPython 3.14.6となることを確認してください。

### 依存ライブラリ

ライブラリをインストールする場合は、

```bash
pip install -r requirements.txt
```

### 天気予報データの取得

気象庁ホームページで公開されている予報JSONを利用しています。

採用理由

- APIキー不要
- 日本語の天気予報をそのまま利用できる
- 降水確率・最高気温・最低気温等必要な情報を取得できる

### 地域設定

現在は名古屋市（気象庁 名古屋地方気象台）の予報を取得するよう設定しています。

他の地域で利用する場合は、`src/config.py`で設定している気象庁の予報JSONの「URL」「取得地域」「取得地点」を変更してください。

気象庁の予報区一覧：
https://www.jma.go.jp/bosai/common/const/area.json


### GitHub Secrets

本プロジェクトでは、メールアドレスやパスワードなどの機密情報はGitHub Secretsで管理しています。
必要なSecretsは、以下の通りです。

- MAIL_ADDRESS：送信元のGmailアドレス
- MAIL_PASSWORD：送信元GmailアドレスのAppパスワード
- MAIL_TO：送信先のメールアドレス

ローカル開発では プロジェクト外に配置した`.env` を利用し、GitHub Actionsでは Secrets を環境変数として渡しています。

ローカル実行時は、`.env.example` を参考に、プロジェクト外の任意の場所（例：`C:\Secrets\daily-notifier.env`）へ `.env` ファイルを作成してください。
その後、config.pyの「ENV_PATH」に.envファイルのパスを記載してください。

### テストの実行

プロジェクトのルートディレクトリで以下のコマンドを実行すると、テストを実行できます。

```bash
pytest
```

テストカバレッジを確認する場合は、以下を実行します。

```bash
pytest --cov=src
```

`pytest --cov=src` では、`src` 配下のソースコードについて、テストによる実行状況を確認できます。


