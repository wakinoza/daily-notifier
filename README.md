# daily-notifier

GitHub Actionsを利用して、翌日の生活情報を毎晩自動通知するシステムです。

現在はMVP（Minimum Viable Product：最小限の実用機能）の開発を進めています。

---

# プロジェクト概要

本プロジェクトでは、GitHub Actionsによる定期実行を利用し、天気などの生活情報を取得して通知するシステムを構築します。

主な目的は以下のとおりです。

* GitHub Actionsを利用した自動化システムの構築
* Pythonによる外部API連携
* 通知機能を拡張しやすい設計の実践
* AIエージェント（Codex CLI）を活用した開発手法の習得

---

# 現在の開発状況

現在はプロジェクトの初期構築を進めています。

## 実装済み

* プロジェクトの作成
* Gitリポジトリの作成
* 開発方針・設計ドキュメントの整備

## 未実装

以下は今後実装予定です。

* GitHub ActionsによるPython実行
* 天気APIとの連携
* メール通知
* LINE通知
* その他生活情報の通知機能

---

# 開発環境

| 項目      | 内容                 |
| ------- | ------------------ |
| OS      | Windows 11         |
| 言語      |  Python 3.14.6     |
| エディタ    | Visual Studio Code |
| バージョン管理 | Git / GitHub       |
| CI/CD   | GitHub Actions     |

※Pythonのバージョンや利用ライブラリは今後決定予定です。

---

# ディレクトリ構成

現在は開発初期のため、ディレクトリ構成は変更される可能性があります。

```text
daily-notifier/
├── .venv/（Git管理外）
├── src/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 今後の予定

MVPでは、以下の流れを実現することを目標としています。

```text
GitHub Actions
        │
        ▼
Python
        │
        ▼
天気API
        │
        ▼
メール通知
```

MVP完成後は、通知先や取得する情報を拡張する予定です。

---

# 開発方針

本プロジェクトでは、以下の方針で開発を進めています。

* 学習目的を重視する
* 保守性・可読性を優先する
* 実務で避けられるアンチパターンは採用しない
* 設計理由を理解しながら実装を進める
* AIエージェントを積極的に活用する

---

# ライセンス

未定

---

## Python仮想環境

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

## 依存ライブラリ

ライブラリをインストールする場合は、

```bash
pip install -r requirements.txt
```