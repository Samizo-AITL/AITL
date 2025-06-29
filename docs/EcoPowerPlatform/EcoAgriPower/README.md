```markdown
# Eco Agri Power Model - README

## 概要

**Eco Agri Power Model** は、スマート農業向けに設計された超低消費電力の環境センシングシステムです。  
土壌・気候データをAI推論により解析し、LoRa通信で遠隔送信。  
独立電源としてソーラーとLFP電池を搭載し、農地に単独で設置可能な持続型IoTデバイスです。

---

## 主な特徴

- 🌱 **AI SoC内蔵**：65nm CMOSプロセス + 軽量推論AI + センサI/F（I²C/SPI/ADC）
- ☀️ **自律電源**：2Wソーラーパネル + MPPT制御 + LFPバッテリ（3.2V/1500mAh）
- 📡 **LoRa通信**：920MHz、最大5km、LoRaWAN Class A 対応予定
- 📊 **センサ接続**：温度、湿度、日射、CO₂などを柔軟に接続可能
- 🧠 **GUI連携**：Pythonベースの教育用GUIでデータ可視化・AI制御も可能
- 🧪 **PoC連携**：地域PoC（2025年7〜9月）に向けた評価キット展開予定

---

## モジュール構成

| No. | モジュール名         | 区分     | 概要                                          |
|-----|----------------------|----------|-----------------------------------------------|
| 1   | AI SoCモジュール      | コア     | RISC Core + 軽量AI、I²C/SPI/ADC内蔵              |
| 2   | 電源モジュール        | 基本     | 2Wソーラー + MPPT + LFP電池                    |
| 3   | 通信モジュール        | 通信     | LoRa 920MHz、最大5km                           |
| 4   | センサI/F            | I/O      | 温度・湿度・日射・CO₂などのセンサ対応          |
| 5   | GUIモジュール         | 教育     | Python対応、USB/UART接続、教育用GUI            |
| 6   | ファームウェア        | ソフト   | LoRa送信、センサ制御、AI推論、低電力動作       |
| 7   | 評価・教育キット      | 検証     | 教材付き評価ボード一式                         |
| 8   | 拡張インターフェース  | オプション| GNSS、土壌・圧力センサ等（将来拡張）           |
| 9   | PoCデータ連携        | 実証     | 通信ログ・AI判定記録・学習データ送信           |

---

## 開発ステータス

- 🔧 **PoC準備中**（2025年7月〜9月に長野県内で地域実証）
- 📦 **教育キット試作済み**（GUI＋教材＋電源付き評価ボード）
- 📁 **仕様書・PoCDK/SystemDK構築中**

---

## ディレクトリ構成

```
EcoAgriPower/
├── README.md
├── EcoAgriPower_ModuleList_v0.1.md
├── PoCDK/
│   └── specification.md（予定）
├── SystemDK/
│   └── specification.md（予定）
├── Model_Integrated_Specification.md（予定）
```

---

## ライセンス / お問い合わせ

- 本プロジェクトは教育・研究用途に限定して無償提供予定です。  
- ご意見・導入希望などは [Samizo-AITL GitHub](https://samizo-aitl.github.io/) まで。
```
