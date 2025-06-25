# Eco Power Platform v2.0  
## SkyEdge主軸構成への移行案

---

## 1. プロジェクト分類

| プロジェクト名           | 用途・対象                | 特徴・技術構成の方向性                           |
|--------------------------|---------------------------|--------------------------------------------------|
| EcoSmartEdge Project      | 産業DX・スマートIoT       | SkyEdge主軸モデル、28nm FD-SOIから3nm GAAへ進化 |
| EcoAgriSky Project        | 地域・農業・教育           | AgriEdgeモデル中心、65nm SoC＋LoRa＋ソーラー     |
| SkyShield Project         | 防災・防衛・公共安全       | Militaryモデル強化、環境耐性設計＋自律性強化     |

---

## 2. モデル仕様比較（全モデル）

| 項目                   | Standardモデル         | Professionalモデル        | AgriEdgeモデル              | Militaryモデル             | SkyEdgeモデル（主軸）           |
|------------------------|-----------------------|--------------------------|----------------------------|----------------------------|--------------------------------|
| プロセス技術            | 65nm CMOS             | 28nm FD-SOI              | 65nm CMOS（AMS + LDMOS混載） | 28nm FD-SOI                | 3nm GAA / FinFET（予定）       |
| AI制御SoC               | 標準AIコア            | 高性能AIコア             | SoC＋AIコア（農業特化）     | AI制御＋高耐環境SoC         | 最先端AI SoC＋高性能制御        |
| 通信機能                | Wi-Fi（基本）          | Wi-Fi＋LTE               | LoRa                       | LTE＋GNSS                  | Wi-Fi／LTE／GNSS＋BLE          |
| カメラ                  | CMOS＋レンズ           | CMOS＋レンズ＋LVDS        | CMOS＋MIPI CSI             | CMOS＋自動露出調整          | 4K MIPI CSI＋IRカメラ対応       |
| センサー                | 環境センサー基本       | 複数環境センサー         | 土壌・光・環境センサー      | IMU・温湿度・GPS            | 複合IMU＋画像解析センサー群     |
| 電源構成                | USB／バッテリ          | バッテリ＋太陽光オプション | 2W級ソーラー＋バッテリ      | バッテリ＋太陽光             | 高効率バッテリ＋太陽光システム   |
| SDK・開発環境           | PoCDK v1.0             | PoCDK v1.0＋SystemDK v1.0 | PoCDK v1.0＋SystemDK v1.0  | PoCDK v1.0＋SystemDK v1.0  | PoCDK v1.1＋SystemDK v1.1＋GUI  |
| 主な用途                | 基本IoT・教育          | 産業用エッジAI           | スマート農業・地域支援      | 防災・防衛・公共安全        | 産業DX・高度エッジAI・スマートシティ |
| 特徴・強み              | コスト重視・教育向け   | 高性能AI・多通信対応     | 省電力長時間稼働           | 環境耐性・リアルタイム制御  | 最新ノード＋高性能AI・複合制御  |

---

## 3. PoCDK v1.1（SkyEdge統合）

- バージョン：v1.1  
- 対応モデル：SkyEdge, AgriEdge, Military, Standard, Professional  
- 特徴：モデル共通設計キット化、GUI設定支援、リモート更新／監視対応  
- 技術：PoCDベース構成管理、オンデマンドAI推論、PoC評価ツール群  
- 教育対応：Zenn連携教材、GitHub PoC例、評価DB付属  

---

## 4. SystemDK v1.1（SkyEdge対応版）

- 対象：SkyEdge / Professional / AgriEdge / Military  
- 新機能：GUI設計支援ツール、ノード別PoCテンプレート、評価データ収集機能  
- AI統合：オンデマンドAIノード構成、学習データとPoC同期  
- 学習教材連携：edusemi対応スクリプト、PoCDK例題、GUI実演ビデオ（予定）  
- 開発支援：ノードモジュール生成、自動コード展開（Python/C対応）  

---

## 5. SkyEdge先進ノードロードマップ（2025〜2028）

| 年度 | 技術ノード        | 概要                                               |
|------|-------------------|----------------------------------------------------|
| 2025 | 28nm FD-SOI       | 現行SkyEdge、低電力・広温度対応                     |
| 2026 | 14nm FinFET       | 中性能モデルへ展開、電力効率／演算強化              |
| 2027 | 3nm GAA準備       | GAA技術探索開始、AITL-Rとの統合試験PoC実施         |
| 2028 | 3nm GAA本格展開   | SkyEdge GAA正式投入、量産設計・PoC統合SDKへ昇格     |

---

## 6. 今後の移行ポイント（まとめ）

- PoCDKとSystemDKをSkyEdge標準仕様へ移行  
- SkyEdgeを全プロジェクトの主軸SoCへ昇格  
- GAA対応SDKとPoC準備を2026年以降開始  
- 教育・地域実証から、産業・商用PoCへスムーズに接続  

---

*本資料はEco Power Platform v2.0移行案の現時点まとめです。更新・拡張は適宜行います。*
