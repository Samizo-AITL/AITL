# システムアーキテクチャ設計書（YorisoiHybridRobot）

---

## 🏗 全体構成図（AITL × LLM）

```text
[Sensor Input]
     │
     ▼
[Emotion Recognition (LLM)]
     │
     ▼
[Suggested State] ───► [FSM Engine (AITL)]
                                │
                                ▼
                          [Action Execution]
```
---

## 🔧 モジュール構成

| モジュール         | 内容                                         | 実装言語           |
|--------------------|----------------------------------------------|--------------------|
| emotion_input.json | 音声・表情・姿勢などの感情入力ログ           | JSONログ           |
| llm_interface.py   | 感情認識・状態推論からFSM制御への連携        | Python             |
| fsm_engine.py      | AITLベースの状態遷移制御                     | Python             |
| fsm_state_def.yaml | FSM状態・遷移条件定義ファイル                | YAML               |
| actuator_driver    | モータ／音声出力制御                         | Verilog／C         |

---

## 📡 データフロー定義（センサ→制御→応答）

1. `emotion_input.json` にセンサから感情情報を記録  
2. `llm_interface.py` がLLM推論から `suggested_state` を抽出  
3. `fsm_engine.py` がFSM遷移を実行  
4. 出力動作（音声・動作など）へ反映

---

## 🔐 安全設計とフェイルセーフ

- FSM状態 `ALERT`／`EMERGENCY` で安全停止処理を強制  
- アクチュエータ制御には LDMOSベースのハード保護機能を併用  
- LLM推論エラー時には FSMが `CHECK` 状態で保留待機

---

## 🧪 拡張可能性

- FSM状態は `fsm_state_def.yaml` により柔軟に追加可能  
- LLMモデルはAPI差し替えで多言語・高精度に対応  
- センサIFはROS2／MQTTなどにも今後対応予定
