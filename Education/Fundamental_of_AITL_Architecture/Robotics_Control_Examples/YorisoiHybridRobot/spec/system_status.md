# システム状態ログ仕様（system_status.json）

---

## 📄 ファイル名

`system_status.json`

---

## 📥 形式と内容

このJSONは、ロボット全体の稼働状態を一定周期で記録するシステムモニタリングログです。

```json
{
  "timestamp": "2025-07-02T15:32:00+09:00",
  "fsm_state": "SAFE",
  "llm_status": "active",
  "sensor_status": {
    "temperature_sensor": "ok",
    "encoder": "ok",
    "load_sensor": "ok",
    "camera": "ok"
  },
  "last_emotion": "sad",
  "last_action": "voice:大丈夫ですか？"
}
```

## 📝 各フィールド説明

| フィールド名     | 型      | 必須 | 説明                                                                 |
|------------------|---------|------|----------------------------------------------------------------------|
| `timestamp`      | string  | 必須 | ログ記録時刻。ISO 8601形式（例：`2025-07-02T15:32:00+09:00`）       |
| `fsm_state`      | string  | 必須 | 現在のFSM状態（例：`IDLE`, `SAFE`, `ALERT`, `EMERGENCY`）            |
| `llm_status`     | string  | 任意 | LLMの状態（例：`active`, `standby`, `error`）                        |
| `sensor_status`  | object  | 任意 | センサごとの状態を記録するオブジェクト。キーはセンサ名、値は状態。 |
| `last_emotion`   | string  | 任意 | 直近で認識された感情（例：`happy`, `sad`, `fear`）                   |
| `last_action`    | string  | 任意 | 直前に実行されたアクションの簡易表現（例：`voice:大丈夫ですか？`）  |

---

## 🧪 sensor_status の例

```json
"sensor_status": {
  "temperature_sensor": "ok",
  "encoder": "ok",
  "load_sensor": "error",
  "camera": "timeout"
}
```
- `"ok"`：正常動作  
- `"error"`：センサ異常（例：値不正、通信断）  
- `"timeout"`：一定期間更新なし（応答待ち状態）  

---

## 📎 備考

- システム監視やWebUIのステータス表示に活用可能  
- `last_action` のログ蓄積により、ユーザーとの対話履歴が追跡できる  
- 定期的なバッチ保存 or イベント駆動で `/data/system_status/` に保存推奨  
- このファイルはロギングシステムとダッシュボードのインタフェース仕様にも対応可能
  
