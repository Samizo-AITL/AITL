# YorisoiHybridRobot: JSON仕様設計書 & API定義書

---

## 1. JSONデータ仕様（モジュール間インタフェース）

### `emotion_input.json`

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
