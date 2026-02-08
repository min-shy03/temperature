# 🏫 GSC WEB : スマート学科管理ソリューション

> **教室環境のモニタリングから公平な当番管理まで**
> 永進専門大学 グローバルシステム融合科(GSC) 生徒のための **All-in-One ウェブサービス**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7.0-DC382D?style=flat-square&logo=redis&logoColor=white)

---

**言語選択 (Language):**
[🇰🇷 한국어](./README.md) | **🇯🇵 日本語**

---

## 💡 プロジェクト紹介

日々の学科生活における不便さを解決するために開発された **IoTベースのスマート統合管理システム**です。

---

## 🚀 主要機能

### 1. リアルタイム教室環境ダッシュボード
- **Zero-Refresh:** IoTセンサーデータを**リロードなしでリアルタイム**にグラフへ反映
- **Data Archive:** 過去1年間の月別平均温・湿度の統計データを可視化

### 2. 循環型掃除当番選出エンジン
- **Rolling Deck:** 全員が一度ずつ遂行するまで重複なしで循環する公平なアルゴリズム
- **Auto-Fill:** 候補者が不足する場合、即座にデータをリセットし、当番(4名)を強制補充
- **デモ:**
  <p align="center">
    <img src="https://github.com/user-attachments/assets/98cd551c-a8f8-4e1b-8e2f-7a79a3e50f36" width="600" alt="当番選出デモ">
  </p>

### 3. スマートカリキュラム管理
- **Dynamic Timetable:** 1〜3年生全クラスの時間表照会および管理者修正機能
- **デモ:**
  <p align="center">
    <img src="https://github.com/user-attachments/assets/e7697289-02e4-4557-aa66-7fb964e49d3a" width="600" >
  </p>

---

## 🛠️ 技術的チャレンジ (Highlights)

### 1. HTTP Polling の限界克服 → SSE 導入
- **課題:** 頻繁なPollingリクエストによるトラフィック過負荷とデータ遅延の発生
- **解決:** **Server-Sent Events(SSE)** の導入によりサーバー負荷を軽減し、単方向リアルタイム通信を実現
- **結果:** ネットワークリソースの削減および遅延のないリアルタイムグラフを実現

### 2. 当番選出ロジックの高度化とDB同期
- **課題:** 候補者不足時の選出中断およびPythonオブジェクトとDB間の状態不一致(Stale Data)による更新漏れの発生
- **解決:** 1. **残りの人員を優先選出 + 即時リセット** ロジックによる無限循環構造の構築
  2. SQLの `update` 命令の代わりに **オブジェクト直接修正および明示的なcommit** 方式を採用し、完璧なDB同期を保証
- **結果:** 例外のない安定した自動選出システムを構築

### 3. 大容量データ処理の最適化 (Batch Task)
- **課題:** 分単位で蓄積される膨大なセンサーデータにより、統計照会速度が徐々に低下
- **解決:** **APScheduler** を活用し、毎月1日にデータを自動集計・統計テーブルへ移管するバッチ処理を構築
- **結果:** 統計照会時の大量演算を防止し、レスポンス速度を **0.1秒未満** に維持

---

## 👤 Project Member

| 名前 | 役割 | Github |
|:---:|:---:|:---:|
| **ミン・スヒョン** | Full-Stack Developer | [@min-shy03](https://github.com/min-shy03) |
