# 感情入力仕様（emotion_input.json）

---

## 📄 ファイル名

`emotion_input.json`

---

## 📥 形式と内容

ユーザーからの入力（音声、表情、姿勢）を時刻付きで記録する感情入力ログです。

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
## 📝 各フィールド説明

| フィールド名         | 型      | 必須 | 説明                                                      |
|----------------------|---------|------|-----------------------------------------------------------|
| `timestamp`          | string  | 必須 | ISO 8601形式のタイムスタンプ                              |
| `user_id`            | string  | 任意 | ユーザーの識別子。省略可能（ログ用途）                   |
| `emotion`            | string  | 必須 | 認識された感情（例：`happy`, `sad`, `fear`, `neutral`）   |
| `emotion_confidence` | float   | 任意 | 感情分類の信頼度（0.0〜1.0）                              |
| `voice_text`         | string  | 任意 | 音声認識結果のテキスト                                    |
| `face_expression`    | string  | 任意 | 表情推定結果（例：`smile`, `frown`, `neutral`）           |
| `pose`               | string  | 任意 | 姿勢（例：`sitting`, `standing`, `falling`, `lying`）     |

---

## 🧪 利用場面の例

| 状況                             | emotion  | face_expression | pose     |
|----------------------------------|----------|------------------|----------|
| 「今日は寂しい」とつぶやく       | `sad`    | `frown`          | `sitting`|
| 転倒検出                         | `fear`   | `neutral`        | `falling`|
| 明るく会話している              | `happy`  | `smile`          | `standing`|
| 応答がなく無表情で座り続ける    | `neutral`| `neutral`        | `sitting`|

---

## 📎 備考

- このデータは、**LLMによる状態提案**のインプットとして直接使用されます。  
- `emotion` のラベル分類は独自モデル or 外部APIで事前定義が必要です。  
- 高精度実装では、リアルタイムで連続記録しFSMに逐次反映可能です。
