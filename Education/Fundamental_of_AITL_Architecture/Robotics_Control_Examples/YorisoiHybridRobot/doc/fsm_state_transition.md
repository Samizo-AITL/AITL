# 🔄 FSM 状態遷移設計書

本ドキュメントでは、YorisoiHybridRobotにおけるFSM（有限状態機械）の設計方針、状態定義、および遷移条件を明記する。

---

## 🧠 設計方針

- 状態はユーザーの感情・発話内容に対応し、安全な振る舞いを制御
- 遷移条件はセンサ入力およびLLM提案により柔軟に制御
- 状態数を限定し、分かりやすくトレース可能にする（5〜7状態）

---

## 📋 状態一覧

| 状態名       | 説明                                     |
|--------------|------------------------------------------|
| `IDLE`       | 初期待機状態（入力待ち）                 |
| `CARE_MODE`  | 感情的ケアを提供する応答状態             |
| `TALK_MODE`  | 日常会話を行うフレンドリーな状態         |
| `REST_MODE`  | 休憩・リラックスを促す状態               |
| `ALERT_MODE` | 異常検知時に安全誘導する警戒状態         |
| `SAFE_MODE`  | 動作停止または支援者呼出などセーフ動作   |

---

## 🔁 状態遷移ルール概要

```text
IDLE
  ├─(emotion: sad)────────┐
  │                       ▼
  └────────────→ CARE_MODE
                           ├─(emotion: neutral)──→ TALK_MODE
                           └─(emotion: tired)────→ REST_MODE

TALK_MODE
  └─(emotion: tired)──────→ REST_MODE

ANY_STATE
  └─(abnormal_flag=True)─→ ALERT_MODE
ALERT_MODE
  └─(recovery)────────────→ IDLE or SAFE_MODE
```

---

## 📝 実装形式

- `fsm_state_def.yaml` に状態定義と遷移条件をYAMLで記述
- `fsm_engine.py` にて定義を読み取り、条件判定・状態更新を実行

---

## ✅ 安全性対策

- `ALERT_MODE` では動作を制限し、TTSによる通知を実施
- `SAFE_MODE` は外部との連携による安全処理専用
- 不明な入力・異常な状態は `IDLE` にフォールバック

---

このFSM設計により、LLMによる柔軟性とFSMによる安全性が両立された信頼性の高いロボット制御が実現できる。
