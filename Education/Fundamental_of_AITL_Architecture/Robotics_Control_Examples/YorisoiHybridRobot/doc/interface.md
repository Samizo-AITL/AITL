# インタフェース定義書（YorisoiHybridRobot）

---

## 📁 ファイルベース連携

### emotion_input.json

感情センサ入力のログデータ。

```json
{
  "timestamp": "2025-07-02T15:30:00+09:00",
  "user_id": "elder_01",
  "emotion": "sad",
  "emotion_confidence": 0.87,
  "voice_text": "今日はなんだか寂しいな",
  "face_expression": "frown",
  "pose": "sitting"
}
```
# LLM出力仕様（llm_response.json）

---

## 📄 ファイル名

`llm_response.json`

---

## 📥 形式と内容

感情認識後、LLMがFSMに提案する状態遷移情報をJSON形式で提供します。

```json
{
  "suggested_state": "SAFE",
  "reason": "ユーザーが悲しそうな発話を繰り返しています。",
  "confidence": 0.91,
  "action_message": "やさしく声をかけましょう"
}
```

## 📝 各フィールド説明

| フィールド名       | 型      | 必須 | 説明                                                   |
|--------------------|---------|------|--------------------------------------------------------|
| `suggested_state`  | string  | 必須 | FSMに提案される状態（例：`SAFE`, `ALERT`, `EMERGENCY`）|
| `reason`           | string  | 任意 | LLMが状態を提案した自然言語による理由                  |
| `confidence`       | float   | 任意 | 状態提案の信頼度（0.0〜1.0）                           |
| `action_message`   | string  | 任意 | ロボットがユーザーに伝える推奨発話や行動メッセージ     |

---

## 🧪 利用場面の例

| 入力感情／状況               | 推論状態       | メッセージ例                             |
|------------------------------|----------------|------------------------------------------|
| "今日は寂しい"（emotion=sad）| `SAFE`         | "お話を聞きますよ、大丈夫ですか？"       |
| 転倒検知（pose=falling）     | `ALERT`        | "大丈夫ですか？すぐに助けを呼びます。"   |
| 応答なし（no_response=true） | `EMERGENCY`    | "応答がありません、緊急対応を開始します" |

---

## 📎 備考

- `suggested_state` はFSM側で定義済みの状態名と一致する必要があります  
- `action_message` は対話エンジンまたは音声出力に直接使用可能です  
- この仕様は今後、マルチターン対話履歴や画像入力対応にも拡張予定です
  
