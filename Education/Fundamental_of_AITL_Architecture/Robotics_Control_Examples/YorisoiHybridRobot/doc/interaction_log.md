# 📑 interaction_log.jsonl 仕様書

本ドキュメントは、各ステップごとに生成される対話ログ `interaction_log.jsonl` の構造と記録項目を定義する。

---

## 📄 ファイル形式

- 拡張子：`.jsonl`（JSON Lines）
- 各行が1ステップの対話・遷移・応答データを記録

---

## 🧾 サンプルログ（1行）

```json
{
  "timestamp": "2025-07-02T15:35:00+09:00",
  "user_id": "elder_01",
  "emotion": "sad",
  "voice_input": "今日はなんだか寂しいな",
  "fsm_state_before": "IDLE",
  "llm_suggested_state": "CARE_MODE",
  "fsm_state_after": "CARE_MODE",
  "response_text": "寂しい日もありますよね。今日は何があったのですか？",
  "action": {
    "voice_tone": "gentle",
    "expression": "soft",
    "motion": null
  }
}
```

---

## 📝 各フィールド説明

| フィールド名           | 型     | 内容                                             |
|------------------------|--------|--------------------------------------------------|
| `timestamp`            | string | 実行時刻（ISO8601）                              |
| `user_id`              | string | ユーザー識別子（高齢者ID等）                     |
| `emotion`              | string | 入力された感情分類（例：sad, happy, tired）      |
| `voice_input`          | string | 音声入力テキスト                                 |
| `fsm_state_before`     | string | 遷移前のFSM状態                                   |
| `llm_suggested_state`  | string | LLMが提案した状態名                              |
| `fsm_state_after`      | string | 実際に遷移した後のFSM状態                        |
| `response_text`        | string | LLMが生成した応答文                              |
| `action.voice_tone`    | string | 出力音声のトーン（例：gentle, firm）             |
| `action.expression`    | string | 表情アニメーション（例：soft, smile, frown）     |
| `action.motion`        | string | 身体動作（例：nod, wave、またはnull）            |

---

## ✅ 利用目的

- 実行履歴の検証・再現・評価
- LLM/FSMの整合性チェック
- 安全動作記録の保存

---

このログ仕様により、PoCの実行過程を全て機械可読な形式で記録・分析可能となる。
