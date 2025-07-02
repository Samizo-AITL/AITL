# 💬 対話シナリオ & 状態遷移実例（FSM × LLM）

---

## 🧑‍🦳 高齢者との自然対話セッション（感情中心）

### 🟩 初期状態：IDLE

```json
{
  "emotion": "sad",
  "voice_text": "今日はなんだか寂しいな"
}
```

### 🔁 LLM 推論

- 状態提案：`CARE_MODE`
- 応答提案：  
  > 「寂しい日もありますよね。今日はどんなことがありましたか？」

---

## 🤝 状態遷移：IDLE → CARE_MODE（LLM提案をFSMが許容）

### 🟦 次の入力：

```json
{
  "emotion": "neutral",
  "voice_text": "少し元気が出てきたよ"
}
```

### 🔁 LLM 推論

- 状態提案：`TALK_MODE`
- 応答提案：  
  > 「よかったです。今日は何をして過ごしますか？」

---

## 💬 状態遷移：CARE_MODE → TALK_MODE

### 🟨 次の入力：

```json
{
  "emotion": "tired",
  "voice_text": "ちょっと疲れたな"
}
```

### 🔁 LLM 推論

- 状態提案：`REST_MODE`
- 応答提案：  
  > 「少し休みましょうか。お茶でも飲みませんか？」

---

## 💤 状態遷移：TALK_MODE → REST_MODE

### 最終ログ出力（例）

```json
{
  "timestamp": "2025-07-02T15:35:00+09:00",
  "user_id": "elder_01",
  "fsm_state_before": "TALK_MODE",
  "fsm_state_after": "REST_MODE",
  "llm_suggested_state": "REST_MODE",
  "llm_response": "少し休みましょうか。お茶でも飲みませんか？"
}
```

---

## ✅ 検証ポイント

- 状態遷移が感情と対話に応じて自然に変化している
- LLMは文脈に応じた適切な状態を提案している
- FSMは過剰な遷移を防ぎ、安全な状態遷移を保証している
