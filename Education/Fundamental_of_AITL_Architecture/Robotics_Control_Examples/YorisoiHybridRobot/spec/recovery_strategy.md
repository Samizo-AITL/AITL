# 自己修復戦略仕様（recovery_strategy.yaml）

---

## 📄 ファイル名

`recovery_strategy.yaml`

---

## 🎯 目的

このファイルは、FSMが異常状態（`ALERT`, `EMERGENCY`）に遷移した際に適用される「自己修復」戦略を定義します。  
AITL層とLLM層の連携により、安全・確実な状態復帰プロセスを実行します。

---

## 🧾 構造例

```yaml
ALERT:
  max_duration_sec: 60
  recovery_conditions:
    - condition: emotion == "neutral"
      next_state: SAFE
    - condition: no_response == false
      next_state: SAFE
  fallback_action:
    type: voice
    content: "大丈夫ですか？安心してください。"

EMERGENCY:
  max_duration_sec: 120
  recovery_conditions:
    - condition: manual_reset == true
      next_state: IDLE
  fallback_action:
    type: sound
    content: "emergency_alarm"
```

## 📝 各フィールド説明

| フィールド名              | 型      | 必須 | 説明                                                                 |
|---------------------------|---------|------|----------------------------------------------------------------------|
| `<state>`                | object  | 必須 | 状態名（例：`ALERT`, `EMERGENCY`）をキーとした回復戦略定義         |
| `max_duration_sec`        | int     | 任意 | 指定状態を継続できる最大許容時間（秒）。時間超過時は強制復旧可能   |
| `recovery_conditions`     | list    | 任意 | 状態を復帰可能と判断する条件式と遷移先のセット                     |
| ├ `condition`             | string  | 必須 | 状態復帰の判定に使う条件式。FSM内の入力値や信号を評価対象にする   |
| ├ `next_state`            | string  | 必須 | 条件が満たされたときに遷移すべき状態名                             |
| `fallback_action`         | object  | 任意 | すべての回復条件が不成立だった場合に実行される補助アクション       |
| ├ `type`                  | string  | 任意 | アクションの種類（例：`voice`, `sound`, `motion`）                  |
| ├ `content`               | string  | 任意 | アクション内容（例：TTSテキスト、警報音名、モーションIDなど）      |

---

## 💡 状態ごとの運用イメージ

| 状態       | 回復条件                           | 補助アクション                           |
|------------|------------------------------------|------------------------------------------|
| `ALERT`    | `emotion == "neutral"`             | 「大丈夫ですか？」と声かけ               |
|            | `no_response == false`             |                                          |
| `EMERGENCY`| `manual_reset == true`             | 警告音を鳴らす                            |

---

## 📎 備考

- 条件式は `fsm_engine.py` 内で動的に評価される（Python式互換）  
- `fallback_action` は時間切れまたは無反応時に実行される安全策  
- 状態別に細やかな「回復フロー」を設定することで、安心かつ柔軟なインタラクションが可能になる
