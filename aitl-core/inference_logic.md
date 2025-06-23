# Inference Logic - AITL Core Layer 1
論理推論層：仮説生成・予測・因果関係理解

---

## 🎯 目的と役割

Inference Logic層は、AITLモデルの最下層に位置し、外界観測や内部知識から仮説を生成し、推論・予測・意思決定に必要な論理的枠組みを提供する。

---

## 🧠 コア機能

| 機能カテゴリ | 説明 |
|--------------|------|
| 仮説生成 | 状況理解と可能性推論に基づく「現実仮説」の構成 |
| 確率的予測 | 状態変化や行動の影響を予測（ベイズ推論・信念更新） |
| 因果推論 | 介入（do-operator）と結果の関係性を論理的に推定 |
| 意思決定 | 複数選択肢の中から最適行動を選ぶ推論メカニズム |
| マルチエージェント推論 | 他エージェントの意図や行動を仮定し協調・競合を予測 |

---

## 🏗 モデル構成と設計方針

### ◉ 論理構造の3階層

1. **知識記述層**  
 - 状態記述、前提知識、事象の定義（ファクトベース）  
 - 知識ベース構成：例）RDF/OWL, JSON-LD 等も選択可能

2. **推論エンジン層**  
 - 論理演算（命題論理・述語論理）、確率的推論（ベイズネット）  
 - 介入・反事実推論（Causal Graph, Pearlモデル 等）

3. **決定戦略層**  
 - 状況判断、仮説ランキング、意思決定（MDP/非確定型DP）  
 - 強化学習ロジックと連携可（Q推論／モデルベースRL等）

---

## 📦 推奨実装形式（PoC／教育用）

| 要素 | 内容 | 実装例 |
|------|------|--------|
| 知識ベース | 状態・事象・関係の定義 | JSON／YAMLベースDB |
| 推論器 | ベイズネット、ルールベース | Python: `pgmpy`, `pomegranate` |
| 仮説生成器 | 状況から仮説候補を生成 | GPT非依存／軽量NN（offline） |
| 意思決定器 | 状況選択と戦略判断 | Python: `MDPtoolbox`, `RLlib` |

---

## 🔄 他層との連携

- **Control Logic層**：
 予測結果に基づく制御ルールの選択・適用
- **Physical Model層**：
 観測値と仮説の整合性チェック（物理検証）
- **Self-Repair層**：
 異常検出と修復判断のための因果逆推論支援

---

## 📘 参考資料・理論基盤

- Judea Pearl：Causal Inference／do-calculus／Bayesian Networks
- Russell & Norvig：AI: A Modern Approach（第3〜4章）
- PGM for AI：Koller et al. - Probabilistic Graphical Models

---

## ✍ 著者

- 作成：Shinichi Samizo  
- モデル：AITL v1.0 論理推論層  
- GitHub：[@samizo-aitl](https://github.com/samizo-aitl)
