# FSM×LLM構造仕様書（Samizoアーキテクチャ準拠）

この文書は、AITL-HXプロジェクトにおける「本能としてのFSM」と「理性としてのLLM」を分離統合する**Samizoアーキテクチャ**に基づいた制御構造仕様を記述するものです。

---

## 🧭 目的

- **形式的制御（FSM）**による安定・即応性
- **言語モデル（LLM）**による状況理解と例外処理
- 両者を**疎結合**で統合し、動的環境に対応する適応制御を実現する

---

## 🧠 アーキテクチャ構造

```
[LLM Interface] ────┐
                    ▼
         +-------------------------+
         |     FSM Engine          |  ← 本能的状態遷移（高速・形式的）
         |   ────────────────      |
         |   状態: sensing, act... |
         +-------------------------+
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
[H∞ Controller]         [Fallback Command (e.g. stop)]
        ▼
[Actuator Command Output]
```

---

## 🧩 コンポーネント定義

### 1. FSM Engine（fsm_engine.py）

- `fsm_state_def.yaml` に定義された状態遷移表を参照
- センサ入力やLLMからのフラグを元に、現在の状態と次状態を決定
- 転送される制御命令は **H∞ Controller** へ渡される

### 2. LLM Interface（llm_interface.py）

- 対話履歴、センサ異常、外部コマンドなどを自然言語処理で解釈
- 「意図」または「異常推論」をFSMに渡す（フラグや補助情報として）
- 例：
  ```json
  {
    "llm_intent": "safe_shutdown",
    "reason": "temperature exceeds 80°C"
  }
  ```

### 3. 状態定義ファイル（fsm_state_def.yaml）

```yaml
initial_state: idle
states:
  idle:
    on_entry: log_idle
    transitions:
      - trigger: start
        condition: always
        target: sensing
  sensing:
    on_entry: acquire_data
    transitions:
      - trigger: high_temp
        condition: temp > 80
        target: emergency_stop
      - trigger: nominal
        condition: temp <= 80
        target: control_loop
...
```

---

## ⚙️ FSM↔LLM連携フロー

1. センサ異常をFSMが検知できない場合、LLMが意味的に解釈（例：「振動パターンが通常と異なる」）
2. LLMが補助フラグ（`llm_override`, `intent`, `risk_flag`）をFSMに送信
3. FSMは遷移ロジックを更新 or 安全状態へ移行
4. フィードバックは再びLLMへ返却（自己学習支援）

---

## 🛡️ 安全設計と分離性

- FSMの状態遷移は常に **決定論的** かつ **形式的検証**が可能な構造とする
- LLMは**アシスタント的推論支援**であり、最終制御はFSMが判断
- 非常時は常に FSM → `emergency_stop` or `shutdown` に即移行

---

## 🚀 今後の拡張

- LLMによる状態遷移テーブルの**自動更新提案**
- ログ解析による「状態遷移パターンの意味的検証」
- FSM→LLM→FSMという**対話的制御ループ**のPoC実装

---

## 📚 関連ファイル

- `fsm_engine.py`: 実装本体
- `fsm_state_def.yaml`: 状態と遷移定義
- `llm_interface.py`: LLM側推論インターフェース
- `interaction_scenario.md`: インタラクション例とPoCの想定状況

---

## 📝 ライセンス

MIT License  
(C) 2025 Shinichi Samizo & AITL Project Team
