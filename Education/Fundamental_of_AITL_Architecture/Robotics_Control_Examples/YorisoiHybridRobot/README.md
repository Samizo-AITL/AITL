# YorisoiHybridRobot

寄り添い型ハイブリッドAIロボットのPoC実装。

---

## 🔧 構成

- AITL（FSM制御）＝本能  
- LLM（感情・対話理解）＝理性  
- 感情センシング＋LLM＋FSM連携で、人間的かつ安全な対応を実現

---

## 📂 ディレクトリ構成

YorisoiHybridRobot/
├── spec/               # JSON仕様書・API定義
├── code/               # 実装コード（FSM, LLM連携）
├── data/               # シナリオログ・入力データ
├── doc/                # 提案書・スライドなど
└── README.md           # この概要ファイル

---

## 🚀 実行手順（例）

1. `spec/llm_response.json` を用意  
2. `code/fsm_engine.py` と `llm_interface.py` を実行  
3. FSMが状態遷移 → 動作出力（音声など）

---

## 💡 主な用途

- 高齢者との寄り添い対話  
- 災害時・異常時の安全行動  
- AI×感情×ロボット教育教材

---

## 👤 企画・設計

三溝 真一（AITL構想）＋ ChatGPT支援  
MITライセンス／教材・PoC公開予定
