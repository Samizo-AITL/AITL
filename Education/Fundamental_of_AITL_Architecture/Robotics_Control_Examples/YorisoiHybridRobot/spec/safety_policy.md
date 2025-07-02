# セーフティポリシー仕様（safety_policy.yaml）

---

## 📄 ファイル名

`safety_policy.yaml`

---

## 🔐 目的

このファイルは、人型ロボットが高齢者や周囲の人々に安全に動作するための  
「行動制限」「異常判定」「緊急停止」などのセーフティルールを定義します。

---

## 🧾 構造例

```yaml
emergency_stop:
  triggers:
    - condition: pose == "falling"
    - condition: no_response == true
    - condition: force_sensor > 30
  actions:
    - type: sound
      content: "emergency_alarm"
    - type: stop_motion
      content: "all"

safe_zone:
  boundaries:
    x_range: [-1.0, 1.0]
    y_range: [-1.0, 1.0]
    z_range: [0.0, 2.0]
  fallback_state: IDLE

overheat_protection:
  temperature_limit_degC: 70
  shutdown_after_sec: 10
```

## 📝 各フィールド説明

| セクション名 / フィールド名          | 型      | 必須 | 説明                                                                 |
|--------------------------------------|---------|------|----------------------------------------------------------------------|
| `emergency_stop.triggers`           | list    | 任意 | 緊急停止をトリガーする条件のリスト。複数条件を設定可能。             |
| ├ `condition`                        | string  | 必須 | 判定条件（例：`pose == "falling"`、`force_sensor > 30`）            |
| `emergency_stop.actions`            | list    | 任意 | トリガー条件成立時に実行されるアクションの定義。                     |
| ├ `type`                             | string  | 必須 | アクションの種類（例：`sound`, `stop_motion`）                        |
| ├ `content`                          | string  | 必須 | アクション内容（例：`emergency_alarm`, `all`）                       |
| `safe_zone.boundaries`              | object  | 任意 | ロボットが動作できる空間範囲（x, y, z 各軸の最小〜最大値）           |
| ├ `x_range`, `y_range`, `z_range`   | array   | 必須 | 各軸の安全範囲（例：`[-1.0, 1.0]`）                                  |
| `safe_zone.fallback_state`          | string  | 任意 | 領域逸脱時に強制的に遷移させるFSM状態（例：`IDLE`）                 |
| `overheat_protection.temperature_limit_degC` | int | 任意 | 許容温度上限（℃）。これを超えるとシャットダウン待機に入る           |
| `overheat_protection.shutdown_after_sec`     | int | 任意 | 上限超過後、何秒で停止するかの猶予時間                              |

---

## 💡 活用例

- `"pose == 'falling'"` → 緊急停止＋警報音＋動作中断  
- `z_range: [0.0, 2.0]` → 2m超のアーム上昇を防ぐ安全境界  
- `temperature_limit_degC: 70` → モーター温度70℃で自動停止カウント開始

---

## 📎 備考

- `triggers` の条件式はFSM条件と同様に `fsm_engine.py` 側で評価される  
- この設定は常時監視され、FSMに優先して動作抑制をかけるセーフティ層に属する  
- 本設定により「人への安心・社会実装時の安全基準への対応」が明文化される
