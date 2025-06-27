# 🌱 Sky-HyEV AgriEdge Model v1.0  
## モジュール構成と設計ガイド（README）

---

## 🔰 概要

Sky-HyEV AgriEdge Model v1.0 は、農業分野向けに最適化された次世代知能制御プラットフォームです。AITL理論をベースに、センサ／AI／通信／電源／外部制御／教育用評価系を統合した、PoCおよび教育活用可能な構成です。

---

## 📦 ディレクトリ構成

| ディレクトリ名         | モジュール名                      | 説明                             |
|------------------------|----------------------------------|----------------------------------|
| `01_AIControlImage/`   | AI制御SoC + 画像処理             | センサ・画像の統合判断を行う中核 |
| `02_CMOSCamera/`       | CMOSカメラモジュール             | MIPI経由で画像入力を提供         |
| `03_SensorArray/`      | 環境・土壌センサ群               | 温度・水分・CO₂などを取得         |
| `04_CommModule/`       | 通信（LoRa/Wi-Fi/5G）            | モード自動切替・省電制御を含む   |
| `05_PowerControl/`     | 電源制御（EcoAgriPower連携）     | 自家発電・蓄電・消費管理          |
| `06_ExtIO/`            | 拡張I/O（灌水・ドローン制御）     | GPIO/PWMによる機器制御           |
| `07_EduInterface/`     | 教育用PoCDK連携・GUI対応         | 学習・可視化・評価支援           |

---

## 📘 統合仕様書

📄 [`AgriEdgeModel_v1.0_Integrated_Specification.md`](./AgriEdgeModel_v1.0_Integrated_Specification.md)

- 各モジュールの関係とAITLの統合位置を明示
- 教育・評価・現場展開への展開性を網羅

---

## 🧠 AITLとの関係

- 各センサ・カメラ・通信のデータはすべて AITLルール判断エンジンに統合されます
- AITLルールはGUIやPoCDK経由で変更・学習可能
- 教育活用時には**GUIによる因果可視化**も提供されます

---

## 🎓 教育・PoC活用例

- AITLルールの書き換え実験（GUI）
- センサ入力 vs 行動出力の関係性の可視化
- 通信切替シナリオ／灌水タイミング判断の検証
- GUIとCSVによるログ解析と評価レポート化

---

## 📌 今後の展望

- 他派生モデル（Military / DisasterResponse）との構造共通化
- GUIツールやAITLルールエディタの開発連携
- 教育カリキュラム（edusemi-plus）との連動教材展開

---

© 2025 Samizo-AITL Project  
This project is part of the EcoPowerPlatform Initiative.
