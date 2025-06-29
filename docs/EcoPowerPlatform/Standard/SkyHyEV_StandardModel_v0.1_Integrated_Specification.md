# SkyHyEV Standard Model v0.1 - 統合仕様書

## 1. モデル概要

Standardモデルは、Eco Power Platform v2.0 における入門・教育用途向け構成です。  
基本的なセンシング、簡易AI推論、セキュア通信、USB給電によるシンプルな電源管理に対応し、低コストで高い拡張性を備えています。

---

## 2. システム構成

| モジュール名              | 概要                                         |
|---------------------------|----------------------------------------------|
| 01_SelfPowerSystem        | USB + バッテリ給電、過放電保護機能付き         |
| 02_SensorControlChip      | 温度・湿度・照度センサの制御および平滑出力     |
| 03_AIControlChip          | TinyMLベースの簡易推論コア                    |
| 04_LDMOSControlChip       | 小型モータ・アクチュエータ用LDMOSドライバ     |
| 05_SecureCommModule       | Wi-Fi＋TLS通信（MQTT/HTTP）対応               |
| 06_SecurityMonitoring     | 異常検知とアラート通知（センサ連携）          |
| 07_ExternalInterface      | USB/I2C/SPI/UART/GPIOなど外部I/F群            |

---

## 3. モジュール連携構成図（概念）

```
         +----------------------------+
         |     SkyHyEV Standard      |
         +----------------------------+
         |                            |
         | 01 SelfPowerSystem         |
         | 02 SensorControlChip       |
         | 03 AIControlChip           |
         | 04 LDMOSControlChip        |
         | 05 SecureCommModule        |
         | 06 SecurityMonitoring      |
         | 07 ExternalInterface       |
         +----------------------------+
                     |
             +---------------+
             | 外部I/F (USB, GPIO, etc.)
             +---------------+
```

---

## 4. 通信仕様

- 通信方式：Wi-Fi（IEEE 802.11b/g/n）
- プロトコル：MQTT v3.1.1 / HTTP / WebSocket
- セキュリティ：TLS1.2（AES-128）、証明書またはPSK認証
- 通信ログ出力／通信状態取得対応

---

## 5. AI推論仕様（簡易）

- 推論方式：8bit量子化NN
- 処理対象：画像分類（簡易）、温湿度傾向識別
- 推論時間：5〜10ms（128x128入力）
- 対応モデル：TFLite for Micro（TFLM）

---

## 6. 電源・電力仕様

| 項目               | 値                                  |
|--------------------|-------------------------------------|
| 電源構成           | USB給電 / Li-ionバッテリ（自動切替）|
| 電圧               | 3.3V システム電圧（500mA max）       |
| 消費電力（全体）    | 約100〜300mW（動作モードに依存）     |
| ソーラー対応       | オプション（5V入力換装）             |

---

## 7. 実装方針・運用メモ

- 教育／実験用途向けに、全インタフェースをヘッダ出力
- 筐体は樹脂ケース（半透明）＋USBポートアクセス設計
- AIモデル／しきい値はI2CまたはUSB経由で更新可能

---

## 8. 拡張可能性

- センサ追加：I2C拡張可（環境／ガス／音／距離 等）
- 通信追加：BLE/UWBモジュールへの交換対応
- LDMOS出力：5V対応アクチュエータの統合拡張あり

---

## 9. 関連仕様書リンク

- `01_SelfPowerSystem/specification.md`
- `02_SensorControlChip/specification.md`
- `03_AIControlChip/specification.md`
- `04_LDMOSControlChip/specification.md`
- `05_SecureCommModule/specification.md`
- `06_SecurityMonitoring/specification.md`
- `07_ExternalInterface/specification.md`

---

## 10. 付録・将来展開

- TFLite学習済みモデル提供テンプレート（準備中）
- GUI制御ツール連携（PoCDKへの展開予定）
- 簡易OSベース統合制御（AITL PoC Lite）
