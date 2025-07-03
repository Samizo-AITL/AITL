# AITL-HX: Hybrid Intelligence Control Example for Space Robotics

このディレクトリは、Samizoアーキテクチャに基づく **FSM × LLM × H∞制御** を組み合わせた、宇宙対応ロボット制御のPoC（Proof of Concept）です。AITL-HXは、過酷環境でのロバスト性と適応性を兼ね備えた、次世代知能制御フレームの一例として設計されています。

---

## 📌 概要

- **名称**: AITL-HX（Hybrid eXample）
- **構成**: FSM（本能）＋ LLM（理性）＋ H∞（制御の骨格）
- **目的**: 宇宙・災害・介護など、予測不能な環境における知的ロボット制御の実現
- **理論背景**: [Samizoアーキテクチャ](../../Fundamental_of_AITL_Architecture/)（AITL構想）
- **応用対象**: 多関節アーム、冷却ファン、介護支援ロボット（Yorisoi構想）

---

## 🧠 機能構造（Samizoアーキテクチャ準拠）

```
          +----------------------+
          |   LLM Interface      | ← 状況判断・例外推論（理性）
          +----------------------+
                   ↑
                   ↓
+------------------+------------------+
|       FSM Engine（状態遷移）        | ← 本能的制御（決まった反応）
+------------------+------------------+
                   ↓
          +----------------------+
          |  H∞ Controller       | ← ロバスト制御（安定性・安全性）
          +----------------------+
                   ↓
          +----------------------+
          |  Physical Actuator   |
          +----------------------+
```

---

## 📂 ディレクトリ構成

```
AITL-HX/
├── fsm_engine.py               # FSM制御エンジン
├── fsm_state_def.yaml          # 状態定義と遷移ルール
├── llm_interface.py            # LLMとの接続・意図解釈
├── data/
│   └── test_scenarios/
│       └── interaction_scenario.md  # テスト用インタラクションシナリオ
├── docs/
│   ├── specification/
│   │   ├── fsm_llm_structure.md       # FSM×LLM仕様書
│   │   ├── h_infinity_control_spec.md# H∞制御仕様
│   │   └── yorisoi_robot_outline.md  # 介護ロボット構想
│   └── reference/
│       └── keywords_and_architecture.md # 技術用語とIF構造メモ
└── README.md
```

---

## 🚀 実行方法（PoCテスト）

```bash
# 状態遷移エンジンの起動
python fsm_engine.py

# 状態定義（fsm_state_def.yaml）と連携し、LLM（llm_interface.py）を介して
# 状況推論と制御出力を繰り返します。
```

---

## 🧩 技術キーワード

- FSM（有限状態機械）による形式的制御
- LLMによる対話的フィードバックと例外対応
- 多変数H∞制御によるロバストな動的応答
- 宇宙環境を想定したFDSOI（25nm）×LDMOS（0.35um）デバイス設計
- 対応センサ：加速度・姿勢・温度など

---

## 📚 関連プロジェクト

- [`AITL-H`: 人型ロボット構想（介護支援）](../../../../AITL-H_Robot_Project/)
- [`Fundamental_of_AITL_Architecture`](../../Fundamental_of_AITL_Architecture/): Samizoアーキテクチャ理論
- [`Application_Expansions/`](../../../../Application_Expansions/): 宇宙、防衛、災害対応などへの応用展開

---

## 📄 ライセンス

MIT License（詳細は上位階層のLICENSEを参照）

---

## 📬 連絡先

AITL開発チーム（代表：三溝 真一）  
ご意見・連携のご提案は Issues または Discussions からお寄せください。

---
