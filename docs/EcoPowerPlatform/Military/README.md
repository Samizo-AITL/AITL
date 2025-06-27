# 🛡️ Sky-HyEV Military Model v1.0  
## モジュール構成と設計ガイド（README）

---

## 🧭 概要

本モデルは、Sky-HyEVプラットフォームを防衛・セキュリティ用途に特化して展開した「Military Model v1.0」です。AITLロジックによるリアルタイム状況判断と、自己電力供給、セキュア通信、外部I/F制御を統合し、教育から実証評価まで活用可能な構成を提供します。

---

## 📦 ディレクトリ構成

| ディレクトリ名             | モジュール名                | 概要                               |
|----------------------------|-----------------------------|------------------------------------|
| `01_SelfPowerSystem/`      | 自己発電モジュール          | 太陽光・蓄電併用の電力供給          |
| `02_SensorControlChip/`    | センサ制御チップ            | 人体・振動・環境センサの信号処理    |
| `03_AIControlChip/`        | AI判断モジュール            | AITLにより敵味方識別・状況判断      |
| `04_LDMOSControlChip/`     | 出力制御（高電圧対応）      | アクチュエータや兵装制御            |
| `05_SecureCommModule/`     | セキュア通信モジュール      | 暗号通信・妨害耐性の高い伝送設計    |
| `06_SecurityMonitoring/`   | 状態監視・異常検知          | ハートビート監視・異常時ログ記録    |
| `07_ExternalInterface/`    | 外部I/F制御（出力・受信）   | GPIO/PWM制御・外部機器接続          |
| `SystemDK/`                | ハード統合仕様              | モジュールの接続・筐体設計           |
| `PoCDK/`                   | 教育PoC開発キット           | 評価・GUI連携対応                   |
| `ProjectPlan/`             | 開発計画書                  | Militaryモデルの開発背景と方針      |

---

## 📘 統合仕様書

📄 [`SkyHyEV_MilitaryModel_v1.0_Integrated_Specification.md`](./SkyHyEV_MilitaryModel_v1.0_Integrated_Specification.md)

- AITL判断・センサ制御・出力動作の全体構成を明記
- 教育PoCDKとの連動性・拡張I/Fにも対応

---

## 🔐 セキュリティ設計の特徴

- 通信はAES/TLS対応、低帯域モード切替機能あり
- センサ信号は前処理＋正規化＋検証経路を通過
- 状態異常はSecurityMonitoringモジュールにより自動ログ化

---

## 🎓 教育・評価用機能

- GUI＋PoCDKにより状況判断ロジックの可視化可能
- センサ模擬信号、通信遮断試験、バッテリ切替評価などが可能
- 評価ログはCSV出力、AI判断過程と照合可能

---

## 🌐 将来拡張構想

- 衛星通信（Starlink/Iridium）接続の準備中
- 災害支援モデル（DisasterResponse）との連携設計あり
- 国防×市民教育の橋渡し教材としての活用を想定

---

© 2025 Samizo-AITL Project  
This project is part of the EcoPowerPlatform - Military Initiative.
