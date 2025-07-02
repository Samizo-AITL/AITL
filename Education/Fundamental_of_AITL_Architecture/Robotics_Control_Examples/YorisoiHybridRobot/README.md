# 🤖 YorisoiHybridRobot

AITL × LLM ハイブリッドによる「寄り添い型人型ロボット」制御システム  
人間の“本能”と“理性”を模した構造で、安心・共感・対話を実現するPoC

---

## 🎯 プロジェクトの目的

- 本能（FSM制御）と理性（LLM応答）のハイブリッド構造をPoCで実証
- 高齢者との自然な感情インタラクションを支援する人型ロボット制御を実現
- 教育・災害支援・福祉ケアなど多様な応用を見据えた設計

---

## 🧠 システム構成（3層構造）

| 層         | 概要                                   | 実装言語・ツール           |
|------------|----------------------------------------|----------------------------|
| 物理層     | センサ取得、PWM駆動、出力制御         | Verilog, C                |
| 制御層     | FSM管理、H∞制御、状態遷移             | Python, YAML              |
| 推論層     | LLMによる感情応答・状態提案            | Python + LLM API          |

---

## 📁 ディレクトリ構成

```
YorisoiHybridRobot/
├── spec/               # JSON仕様書・API定義
│   ├── emotion_input.md
│   ├── llm_response.md
│   ├── fsm_state_def.yaml
│   └── interaction_log.md
├── code/               # 実装コード（FSM, LLM連携）
│   ├── fsm_engine.py
│   ├── llm_interface.py
│   └── action_executor.py
├── data/               # シナリオログ・入力データ
│   └── emotion_input.json
├── doc/                # 提案書・設計資料・スライド
│   ├── design_philosophy.md
│   ├── test_plan.md
│   ├── module_interface.md
│   ├── state_behavior_matrix.md
│   ├── interaction_scenario.md
│   ├── llm_failover_policy.md
│   └── vision_extension_plan.md
└── README.md           # この概要ファイル
```

---

## 📚 主要ドキュメント

- 🧭 [設計思想と理念](./doc/design_philosophy.md)
- 🧪 [テスト計画と評価方針](./doc/test_plan.md)
- 🔧 [モジュールインタフェース仕様](./doc/module_interface.md)
- 📊 [状態別動作マトリクス](./doc/state_behavior_matrix.md)
- 💬 [対話シナリオテンプレート](./doc/interaction_scenario.md)
- 🔁 [LLMフェイルオーバー設計](./doc/llm_failover_policy.md)
- 👁️ [画像認識拡張構想](./doc/vision_extension_plan.md)

---

## 🛠️ 開発環境・使用技術

- Python 3.11 / YAML / JSON / LLM API (OpenAI or others)
- pytest, pandas, matplotlib
- Verilog HDL（PWM制御など物理層実装想定）

---

## 🧩 応用想定分野

- 👵 高齢者福祉（会話・感情支援）
- 🚨 災害避難誘導・状況説明
- 🎓 教育ロボット・思考支援
- 🏥 医療・メンタルヘルス領域

---

## ⚖️ ライセンス

MIT License

---

このプロジェクトは、AITL構造理論をもとにした  
**「本能と理性を併せ持つAIロボット制御」**の研究開発・教育活用を目指します。
