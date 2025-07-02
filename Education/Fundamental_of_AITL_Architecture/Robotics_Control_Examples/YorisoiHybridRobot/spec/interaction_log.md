# 対話履歴ログ仕様（interaction_log.json）

---

## 📄 ファイル名

`interaction_log.json`

---

## 📥 形式と内容

このJSONは、ユーザーとロボット間の対話イベントを時系列で記録するログファイルです。  
感情入力、LLM応答、FSM遷移、実行アクションをすべて紐付けて記録します。

```json
{
  "timestamp": "2025-07-02T15:32:05+09:00",
  "user_id": "elder_01",
  "voice_input": "今日は少し不安なんだ",
  "emotion": "fear",
  "fsm_state_before": "CHECK",
  "suggested_state": "ALERT",
  "fsm_state_after": "ALERT",
  "llm_message": "不安が続いているようなので、警戒状態に移行します",
  "action_output": "voice:落ち着いてください。そばにいます。"
}
```

## 📝 各フィールド説明

| フィールド名        | 型      | 必須 | 説明                                                                  |
|---------------------|---------|------|-----------------------------------------------------------------------|
| `timestamp`         | string  | 必須 | ログ記録の日時（ISO 8601形式）。すべての時系列解析の基準になる。     |
| `user_id`           | string  | 任意 | 発話者（または対象ユーザー）の識別子。個別ログ追跡に活用。           |
| `voice_input`       | string  | 任意 | 音声認識から取得されたユーザーの発話内容。                            |
| `emotion`           | string  | 任意 | 感情推定の分類結果（例：`happy`, `sad`, `fear`, `neutral`）。         |
| `fsm_state_before`  | string  | 必須 | 対話開始直前のFSMの状態。                                             |
| `suggested_state`   | string  | 任意 | LLMが提案した状態（FSM側が必ずしも採用するとは限らない）。            |
| `fsm_state_after`   | string  | 必須 | 実際にFSMが遷移した後の状態。                                         |
| `llm_message`       | string  | 任意 | LLMによる応答や判断根拠の説明テキスト。                              |
| `action_output`     | string  | 任意 | 実行されたアクション（例：`voice:大丈夫ですか？`、`motion:turn_left`）。|

---

## 💡 補足

- `fsm_state_before` と `fsm_state_after` を比較することで、遷移の有無がわかる  
- `suggested_state` は LLMの推論性能を評価する指標になる  
- `action_output` は実行ログ・シナリオ確認に不可欠なフィールド
