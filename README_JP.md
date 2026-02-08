# 🏫 GSC WEB : スマート学科管理ソリューション

> **教室環境モニタリングから公平な掃除当番管理まで** 永進専門大学グローバルシステム融合科(GSC)学生のための **All-in-One Webサービス**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7.0-DC382D?style=flat-square&logo=redis&logoColor=white)

<br>

**언어 선택 (Language):**
[🇰🇷 한국어](./README.md) | **🇯🇵 日本語**

---

## 💡 プロジェクト紹介

毎日繰り返される学科生活の不便さを解消するために開発された、**IoTベースのスマート統合管理システム**です。

---

## 🚀 主な機能 (Core Features)

### 1. リアルタイム教室環境ダッシュボード
- **Zero-Refresh:** IoTセンサーデータを**リロードなしでリアルタイム**にグラフへ反映
- **Data Archive:** 過去1年間の月別平均温湿度データを蓄積し、季節ごとの環境変化を可視化

### 2. 公平性100% 掃除当番マッチング
- **Fair Algorithm:** 「最近担当した人を除外」「性別バランス(女子を含む)」などの公平なロジックを適用
- **History Tracking:** 当番遂行履歴をDBで管理し、重複当選による不満を根本から遮断

### 3. スマートカリキュラム管理
- **Dynamic Timetable:** 1~3学年の全時間割をWebで即時照会および管理者による修正機能

---

## 🛠️ 技術スタック (Tech Stack)

| 領域 | 技術スタック | 備考 |
|:---:|---|---|
| **Backend** | **Python, Flask** | RESTful APIサーバー構築 |
| **Database** | **MySQL (SQLAlchemy)** | データの整合性を保証 |
| **Real-time** | **Redis + SSE** | 超高速リアルタイムストリーミング実装 |
| **Frontend** | **HTML/CSS/JS (Jinja2)** | 直感的なUI/UX |
| **Batch** | **APScheduler** | 大容量データの統計自動化 |

---

## 👨‍💻 技術的挑戦 (Technical Challenges)

### 1. HTTP Pollingの限界克服 → SSE導入
- **課題:** 頻繁なPollingリクエストによるトラフィック過多および遅延の発生
- **解決:** **Server-Sent Events(SSE)** の導入により、単方向リアルタイム通信を実装
- **結果:** ネットワークリソースを削減しつつ、**遅延のないリアルタイムグラフ**を実現

### 2. 当番選定アルゴリズムの高度化
- **課題:** 単純なランダム抽選による性別の不均衡や連続当選の問題
- **解決:** **未経験者優先 + 性別クォータ制 + 直前担当者の除外** ロジックを実装
- **結果:** システム導入後、当番選定プロセスの利便性が向上

### 3. 大容量データ処理の最適化
- **課題:** 分単位で蓄積されるセンサーデータによる統計照会速度の低下
- **解決:** **APScheduler**を活用し、月別データの自動集計・移管バッチ処理を構築
- **結果:** 統計照会速度を**0.1秒未満**に維持

---

## 👤 Project Member

| 名前 | 役割 | Github |
|:---:|:---:|:---:|
| **ミン・スヒョン** | Full-Stack Developer | [@min-shy03](https://github.com/min-shy03) |
