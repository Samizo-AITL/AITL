# Eco Power Platform 〜 AITL理論実装による持続可能なエコシステム〜

本プラットフォームは、最新のAITL（All-in-Theory Logic）理論を実装し、ハードウェアとソフトウェア両面からの最適制御を実現することで、省エネルギーかつ持続可能なシステムを目指しています。  
「Eco」は単なる自己発電や低消費電力だけでなく、AITL理論による自己修復や効率化を含む、次世代の環境配慮設計理念を示しています。

---

## 🔁 モデル一覧（用途・形態別分類）

| モデル名         | 主な用途                         | 形態（タイプ）              | 主な構成技術                                      | リンク |
|------------------|----------------------------------|-----------------------------|---------------------------------------------------|--------|
| **Standard**      | 教育用ドローン制御               | 🛩️ ドローン基板              | 65nm CMOS, USB/Wi-Fi                             | [Standard](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/Standard/) |
| **Professional**  | 産業用ドローン制御               | 🛩️ ドローン基板              | 28nm FD-SOI, LTE                                 | [Professional](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/Professional/) |
| **SkyEdge**       | 次世代スマートドローン           | 🛩️ 高性能ドローン制御基板      | 3nm GAA, AI SoC, MIPI-4K, BLE/LTE/GNSS            | [SkyEdge](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/SkyEdge/) |
| **AgriEdge**      | 農業用ドローン                   | 🛩️ ドローン（農業特化）        | 65nm CMOS + LoRa + MIPIカメラ                     | [AgriEdge](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/AgriEdge/) |
| **EcoAgriPower**  | 畑の環境センシング端末           | 🏡 地上センサノード           | LoRa, ソーラー給電, 温湿度・土壌センサ            | [EcoAgriPower](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/EcoAgriPower/) |
| **Military**      | 防災監視／軍用／公共インフラ      | 🛡️ 耐環境型ドローン＋センサ     | 28nm FD-SOI, GNSS, IMU, 自律制御, 耐環境仕様       | [Military](https://samizo-aitl.github.io/AITL/docs/EcoPowerPlatform/Military/) |
| **Robotics**      | 教育・研究用ロボット制御         | 🤖 ロボット                   | RISC-V + AI + センサ群 + GUI                      | [Robotics](https://samizo-aitl.github.io/AITL/docs/Robotics/) |

---

## 🚀 プロジェクト構想別ガイド

### 1. **EcoSmartEdge Project**
- **用途**：産業DX、スマートファクトリー、次世代IoT
- **中心モデル**：SkyEdge
- **構成特徴**：
  - 3nm GAA / 28nm FD-SOI
  - AI制御、マルチ通信、SystemDK展開
- **リンク**： [EcoSmartEdge](https://samizo-aitl.github.io/AITL/docs/Projects/EcoSmartEdge/)

---

### 2. **EcoAgriSky Project**
- **用途**：スマート農業、教育PoC、地域環境センシング
- **中心モデル**：AgriEdge（ドローン）＋ EcoAgriPower（畑センサ）
- **構成特徴**：
  - 空（ドローン）＋地（センシング端末）の連携
  - LoRa通信、ソーラー駆動、GUI教材付き
- **リンク**： [EcoAgriSky](https://samizo-aitl.github.io/AITL/docs/Projects/EcoAgriSky/)

---

### 3. **SkyShield Project**
- **用途**：防災・軍用・公共インフラ保守
- **中心モデル**：Military
- **構成特徴**：
  - 高耐環境設計（EMI/温度/振動）
  - GNSS＋リアルタイムAI制御、セキュア通信
- **リンク**： [SkyShield](https://samizo-aitl.github.io/AITL/docs/Projects/SkyShield/)

---

## 📘 PoC / 教育対応状況

| モデル           | PoCDK | SystemDK | 教育GUI | 備考                                |
|------------------|--------|-----------|----------|-------------------------------------|
| **Standard**      | ✅     | ✅        | ✅       | 教育PoCテンプレートあり             |
| **Professional**  | ✅     | ✅        | ⚪︎       | 商用PoCテンプレート構築中           |
| **SkyEdge**       | ✅     | ✅        | ✅       | DX向けSDK対応、最重要モデル         |
| **AgriEdge**      | ✅     | ✅        | ✅       | ドローン制御PoC対応                 |
| **EcoAgriPower**  | ✅     | ✅        | ✅       | 教育PoC＋GUI付き教材展開             |
| **Military**      | ✅     | ✅        | ―        | 高信頼PoC、教育GUI非対象             |
| **Robotics**      | ✅     | ✅        | ✅       | 教育用PoC＋SystemDKテンプレあり       |

---

## 📁 ディレクトリ構成（GitHub展開想定）

```
AITL/docs/
├── EcoPowerPlatform/
│   ├── Standard/
│   ├── Professional/
│   ├── AgriEdge/
│   ├── EcoAgriPower/
│   ├── Military/
│   └── SkyEdge/
├── Robotics/
│   ├── modules/
│   ├── PoCDK/
│   ├── SystemDK/
│   └── README.md
├── Projects/
│   ├── EcoSmartEdge/
│   ├── EcoAgriSky/
│   └── SkyShield/
└── projects.md ← 本ドキュメント
```

---

## 🔚 補足

- 本ドキュメントは `projects.md` としてリポジトリのルートまたは `docs/` に配置可能です。
- モデル名ごとに `README.md` や `*_Specification.md` を用意済み。
- GUI・PoCDK・SystemDKとの連携も各ディレクトリに構成されています。
