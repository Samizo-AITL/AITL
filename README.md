# AITL - All-in-Theory Logic

## 🌐 English Overview

**AITL (All-in-Theory Logic)** is a next-generation theoretical framework for Artificial Intelligence  
that integrates logical inference, control systems, physics-informed modeling, and self-repair mechanisms.  
Unlike LLM-based models, AITL functions as an independent core architecture applicable to robotics, edge AI, disaster-response systems, and autonomous control.  
This repository contains the full model specification, robotics implementation (AITL-R), and related policy proposals (e.g., for METI, NEDO, and OpenAI).  
For questions, collaborations, or discussions, feel free to reach out via GitHub or email (see below).

---

## 🧠 概要

AITL（All-in-Theory Logic）は、人工知能技術の高度な**理論統合モデル**です。  
推論、制御、物理統合、自己修復の4層構造を持ち、AIの多様な機能を一体化して実装・応用できるフレームワークを提供します。

---

## はじめに

AITL（All-in-Theory Logic）は、  
「見る・考える・動く・直す」を一体化した、現実世界で動く頭脳つきAIのフレームワークです。

詳しくは、初心者向けのやさしい解説を以下でご覧いただけます：  

➡️ [AITLとは？〜やさしい解説〜 (日本語)](docs/intro_presentation.md)

---

## 🔧 特徴

- **多層構造**  
  推論層（Inference Logic）、制御層（Control Logic）、物理統合層（Physical Integration）、自己修復層（Self-Repair Logic）を統合。

- **高信頼性と自己修復**  
  異常検知から制御の再構成、強化学習による適応までを包括。

- **応用分野**  
  自律ロボティクス、災害対応モビリティ、エッジAIなどの高度制御システムに適用。

---

## 🧱 4層構造

| 層名                 | 機能概要                          |
|----------------------|----------------------------------|
| Inference Logic      | 仮説生成、因果推論、意思決定     |
| Control Logic        | PID制御、MPC、強化学習制御       |
| Physical Integration | 物理信号整合、センサ処理         |
| Self-Repair Logic    | 異常検知、再構成、適応学習       |

---

## 📁 フォルダ構成（v1.0）

```plaintext
AITL/
├── README.md                      # ← このファイル
├── docs/                          # モデル構成・提言書
│   ├── AITL_Model_v1.0.md         # AITL全体モデル構成解説
│   ├── AITL_Policy_Proposal_v1.0.md # 政策提言書（経済産業省・NEDO・OpenAI向け）
│   └── AITL_Robotics_Structure.md # ロボット向け構成・SoC設計
│   └── intro_presentation.md      # 初心者向けやさしい解説
├── aitl-core/                     # 理論構成（中核モデル）
│   ├── inference_logic.md         # 論理推論層詳細
│   ├── control_design.md          # 制御設計論理
│   └── physics_integration.md     # 物理統合設計
├── aitl-r/                        # ロボット向け実装（SoC設計等）
│   ├── robotics_soc_config.md     # SoC構成仕様
│   ├── self_repair_control.md     # 自己修復ロジック設計
│   └── skyhyev_poc.md             # PoC設計例（SkyHyEV）
└── LICENSE                        # ライセンス（必要に応じて）

```

## 参考資料

- [`docs/AITL_Model_v1.0.md`](docs/AITL_Model_v1.0.md) — AITL全体構成と理論階層の解説  
- [`docs/AITL_Policy_Proposal_v1.0.md`](docs/AITL_Policy_Proposal_v1.0.md) — 政策提言書（経済産業省・NEDO・OpenAI向け）  
- [`docs/AITL_Robotics_Structure.md`](docs/AITL_Robotics_Structure.md) — AITL-Rのロボット向け構成案  
- [`aitl-core/inference_logic.md`](aitl-core/inference_logic.md) — 論理推論層の定式化と応用設計  
- [`aitl-core/control_design.md`](aitl-core/control_design.md) — 制御設計（PID/MPC/RL）の統合理論  
- [`aitl-core/physics_integration.md`](aitl-core/physics_integration.md) — PIML構成・物理知識の内在化設計  
- [`aitl-r/robotics_soc_config.md`](aitl-r/robotics_soc_config.md) — SoC構成（3nm〜0.18µm）の分担設計  
- [`aitl-r/self_repair_control.md`](aitl-r/self_repair_control.md) — 自己修復ロジック（異常検知・再構成）  
- [`aitl-r/skyhyev_poc.md`](aitl-r/skyhyev_poc.md) — SkyHyEV PoC例（災害対応AI機構）  

---

## 著者情報

- 作成者：Shinichi Samizo   (専門　半導体デバイス技術)
- GitHub：[@samizo-aitl](https://github.com/samizo-aitl)  
- Email：shin3t72@gmail.com  

---

## お問い合わせ

ご質問やご提案、協力のご希望は下記までご連絡ください。

- GitHub Discussions: [AITL Discussions](https://github.com/samizo-aitl/AITL/discussions)  
- Email: shin3t72@gmail.com  

---
