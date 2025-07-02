## 🔁 データフロー（処理の流れ）

本PoCにおける実行処理は、センサ入力からアクション出力までを一連のステップとして構成し、各ステップが明確な責務を持っている。

---

### 1. センサ入力（JSON）

```text
🟦 SensorManager  
↓  
📄 data/emotion_input.json  
```

- 音声テキスト・感情分類・表情・姿勢などをJSONで受け取る  
- 入力ファイルを読み取り、統合的な辞書型オブジェクトとして返却  

---

### 2. FSM制御（状態遷移）

```text
🟨 FSMEngine  
↓  
状態定義：fsm_state_def.yaml  
```

- 現在のFSM状態と、入力条件に応じて次の状態を決定  
- LLMによる「suggested_state」があれば反映を判断  

---

### 3. 推論層の判断（LLM連携）

```text
🟩 LLMInterface  
↓  
OpenAI API / 事前定義LLMモック  
```

- 感情・テキスト・表情をもとに状態提案と自然言語応答を生成  
- FSMへ提案し、アクションとしての応答文を返す  

---

### 4. アクション出力（物理層）

```text
🟥 ActionExecutor  
↓  
TTS / 表示 / PWM駆動など  
```

- 応答文を音声化（TTS）、または振る舞いに変換（モータ駆動など）  
- `action` オブジェクトに応じた出力を実行  

---

### 5. ログ保存（1ステップごと）

```text
📝 interaction_log.jsonl  
```

- 1ステップごとに、以下の要素をJSONLとして保存：  
  - timestamp  
  - user_id  
  - emotion / voice_input  
  - fsm_state_before / after  
  - llm提案内容 / 出力アクション  

---

この明確な処理フローにより、FSMとLLMが**協調的に動作するAIロボット**の構造と挙動を可視化・再現・評価できる。
