# FSM状態定義仕様（fsm_state_def.yaml）

---

## 📄 ファイル名

`fsm_state_def.yaml`

---

## 🧭 目的

このファイルは、FSM（有限状態機械）の状態と状態遷移ルールを定義するために使用します。  
YAML形式により、状態追加・条件変更が柔軟に行えます。

---

## 🏷 構造例

```yaml
states:
  - name: IDLE
    transitions:
      - to: CHECK
        condition: input_received

  - name: CHECK
    transitions:
      - to: SAFE
        condition: emotion in ["happy", "neutral"]
      - to: ALERT
        condition: emotion in ["fear", "sad"]

  - name: SAFE
    transitions:
      - to: IDLE
        condition: timeout

  - name: ALERT
    transitions:
      - to: EMERGENCY
        condition: no_response
      - to: SAFE
        condition: emotion == "happy"

  - name: EMERGENCY
    transitions:
      - to: IDLE
        condition: manual_reset
```

## 📝 各フィールド説明

| フィールド名     | 型      | 必須 | 説明                                                               |
|------------------|---------|------|----------------------------------------------------------------------|
| `states`         | list    | 必須 | 状態オブジェクトのリスト。各状態に対する遷移条件を定義する。       |
| `name`           | string  | 必須 | 状態名。FSM内で一意である必要がある。                               |
| `transitions`    | list    | 任意 | 状態遷移の定義リスト。空の場合は遷移なし。                          |
| `to`             | string  | 必須 | 遷移先の状態名。FSM内で定義されている状態と一致している必要あり。   |
| `condition`      | string  | 必須 | 遷移を発生させる条件。入力値やセンサ状態などをもとに記述。         |

---

## 💡 条件式に使用可能な入力例

| キー名           | 意味例                             |
|------------------|------------------------------------|
| `emotion`        | 感情分類（例：`sad`, `happy`）     |
| `pose`           | 姿勢分類（例：`falling`, `sitting`）|
| `no_response`    | 応答がない状態（true/false）       |
| `timeout`        | 一定時間反応がない                 |
| `manual_reset`   | 人による手動初期化                |

---

## 🧪 例：SAFE → IDLE へ遷移

```yaml
- name: SAFE
  transitions:
    - to: IDLE
      condition: timeout
```

## 📎 備考
	•	条件式には簡易論理記述（emotion in [...] や pose == "falling"）が使用可能です
	•	複雑な条件は fsm_engine.py 側で判定ロジックにマッピングして実装されます
	•	状態名はLLM出力の suggested_state にも対応する必要があります

