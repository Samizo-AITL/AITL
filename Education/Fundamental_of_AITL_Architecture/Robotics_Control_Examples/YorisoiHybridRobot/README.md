# 🤖 YorisoiHybridRobot

寄り添い型ハイブリッドAIロボット（FSM × LLM × AITL構造）

---

## 🧠 コンセプト

- **FSM（本能）× LLM（理性）** の役割分離に基づいた構造化AI  
- 感情・発話・表情を認識し、状況に応じた柔軟な応答と安全な状態遷移を実現  
- AITL三層モデル（物理層・制御層・推論層）に基づくPoC構成  

---

## 📐 システム構成（三層）

| 層        | 概要                           | 主な実装モジュール                         |
|-----------|--------------------------------|---------------------------------------------|
| 推論層    | 感情認識・対話生成             | `llm_interface.py`                           |
| 制御層    | FSM状態管理・セーフティ制御     | `fsm_engine.py`, `fsm_state_def.yaml`        |
| 物理層    | TTS出力・モータ制御            | `action_executor.py`, `sensor_manager.py`    |

---

## 📂 ディレクトリ構成

```text
YorisoiHybridRobot/
├── spec/               # JSON仕様書・API定義
├── code/               # 実装コード（FSM, LLM連携）
├── data/               # シナリオログ・入力データ
├── doc/                # 提案書・設計図・構成解説
└── README.md           # この概要ファイル
```

---

## 📄 主な仕様書・資料

| ファイル                              | 内容                                 |
|---------------------------------------|--------------------------------------|
| `spec/api_spec.md`                    | モジュール間JSON & API定義書        |
| `doc/interaction_scenario.md`         | 実行シナリオ（対話例と状態遷移）    |
| `doc/fsm_state_transition.md`         | FSM状態遷移構成と説明               |
| `doc/hybrid_architecture.md`          | FSM×LLMハイブリッド設計の意義       |
| `doc/architecture_dataflow.md`        | センサ〜応答までの処理フロー        |

---

## 🚀 実行例（シミュレーション）

1. `data/emotion_input.json` に入力  
2. `fsm_engine.py` で状態遷移処理  
3. `llm_interface.py` が応答文と提案状態を生成  
4. `action_executor.py` により出力（TTS想定）  
5. `data/interaction_log.jsonl` に1ステップずつ保存  

---

## 🔧 今後の展開

- 実センサ接続（音声・表情・姿勢）の統合  
- LLM API連携精度と高速化検討  
- 高齢者支援、医療・災害・教育など多領域への応用  

---

© 2025 三溝真一 + AITL開発チーム（MIT License）
