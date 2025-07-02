# 📑 LLMプロンプト設計テンプレート

本ドキュメントでは、LLMがユーザーの感情・音声・表情を受け取り、状態提案と応答文を出力するためのプロンプトテンプレートを定義する。

---

## 🧩 入力情報（JSON）

```json
{
  "emotion": "sad",
  "voice_text": "今日はなんだか寂しいな",
  "face_expression": "frown",
  "pose": "sitting"
}
```

---

## 💬 プロンプトテンプレート（英語例）

```text
You are a caring assistant robot for elderly people.  
Given the user's emotion, voice input, facial expression, and pose,  
suggest an appropriate system state and generate a gentle and empathetic response.  

Respond in the following JSON format:  
{
  "suggested_state": "...",
  "response_text": "..."
}

# Input
Emotion: sad  
Voice Input: "今日はなんだか寂しいな"  
Facial Expression: frown  
Pose: sitting
```

---

## 🧠 推論方針

| 要素            | 解釈・考慮点                                          |
|-----------------|-------------------------------------------------------|
| emotion         | ユーザーの心理状態（例：sad → CARE_MODE推奨）         |
| voice_text      | 感情的含意、疲労・孤独・安心などのワードを検出         |
| face_expression | 顔の動きに応じた感情裏付け（例：smile/frown）         |
| pose            | 身体的疲労やアクティブ度（例：lying → REST）           |

---

## ✅ 出力形式の制約

- JSON形式で返す（`suggested_state`, `response_text`）
- 状態名はFSMに存在する定義に一致する必要あり
- 応答文は自然で、感情に寄り添う内容とすること

---

## 🧪 評価観点

- 出力された状態がFSMロジックに矛盾しないか
- 応答文がユーザーの状況に共感的か
- 異常時（例：angry, confusion）の出力対応

---

このテンプレートは、プロンプトベースの軽量LLMまたはAPIに入力され、  
対話的な状態判断と応答生成を可能にする設計の土台である。
