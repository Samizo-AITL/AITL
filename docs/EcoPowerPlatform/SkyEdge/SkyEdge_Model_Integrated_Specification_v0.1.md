# SkyEdgeモデル - 統合仕様書 v0.1

## 概要

本書はSkyEdgeモデルに含まれる各モジュールの仕様を統合したドキュメントです。  
3nm GAA / FinFET技術を用い、産業DX・スマートシティ向けに高性能かつ多機能なエッジAIプラットフォームを提供します。

---

## モジュール一覧

| 番号 | モジュール名          | 概要                                    | 仕様書ファイルパス                          |
|-------|---------------------|-----------------------------------------|---------------------------------------------|
| 01    | AIControlChip        | 高性能AI推論コア、マルチコア構成       | SkyEdge/01_AIControlChip/specification.md   |
| 02    | PowerManagement      | バッテリ管理、太陽光MPPT制御           | SkyEdge/02_PowerManagement/specification.md |
| 03    | MultiCommModule      | Wi-Fi, LTE, GNSS, BLE統合通信モジュール| SkyEdge/03_MultiCommModule/specification.md |
| 04    | CameraInterface      | 4K MIPI CSIカメラおよびIRカメラ制御     | SkyEdge/04_CameraInterface/specification.md |
| 05    | SensorHub            | 複合IMU・環境センサー管理               | SkyEdge/05_SensorHub/specification.md       |
| 06    | SecureCommModule     | 通信のハードウェア暗号化・認証         | SkyEdge/06_SecureCommModule/specification.md|
| 07    | ExternalInterface    | 外部機器接続用高速インターフェース     | SkyEdge/07_ExternalInterface/specification.md|

---

## 共通仕様

- **プロセス技術**: 3nm GAA / FinFET  
- **動作電圧**: Core 0.7V〜1.2V、I/O 3.3V  
- **動作温度範囲**: -40℃〜+85℃（環境依存）  
- **通信機能**: Wi-Fi 6E, LTE Cat.18, GNSS, BLE 5.2  
- **電源**: 高効率バッテリ＋太陽光システム対応  
- **SDK・開発環境**: PoCDK v1.1、SystemDK v1.1、GUI設計支援ツール

---

## 開発・運用管理

- 各モジュール仕様書は個別管理し、統合仕様書は概要・相互接続の整合を担保  
- 仕様変更時は個別仕様書の更新を優先し、統合仕様書は定期的に同期更新  
- モジュール間インターフェース仕様は共通規格を基準とし、バージョン管理を徹底

---

## 参考資料

- 各モジュール個別仕様書（上記一覧参照）  
- PoCDK v1.1仕様書  
- SystemDK v1.1仕様書  
- Eco Power Platform v2.0モデル仕様詳細
