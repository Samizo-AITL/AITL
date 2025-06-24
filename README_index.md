# AITL - All-in-Theory Logic  
## 📘 理論・実装・仕様・PoC 総合インデックス  
## 📘 Unified Index for Theory, Implementation, Spec, and PoC

---

🌐 **概要 / Overview**

AITL（All-in-Theory Logic）は、論理推論、制御理論、物理モデリングを統合した多層型AIアーキテクチャです。  
この構成は以下の2つのGitHubリポジトリで運用されています：

AITL is a multi-layered AI architecture integrating logical reasoning, control theory, and physics-based modeling.  
The project spans two coordinated repositories:

- **理論リポジトリ (v1.0)**： [Samizo-AITL/theory](https://github.com/Samizo-AITL/theory)  
- **実装リポジトリ (v2.0)**：本リポジトリ（Samizo-AITL/AITL）  

---

## 📂 構成一覧 / Repository Structure

| 区分 | パス | 説明 / Description |
|------|------|-------------------|
| **理論** / Theory | [Samizo-AITL/theory](https://github.com/Samizo-AITL/theory) | 論理・制御・物理層の理論（別リポジトリ） / Core logic, control, and physical models |
| **実装** / Implementation | `implementation/` | 実環境での理論適用（ロボット・ドローン）/ Real-world use |
| **仕様** / Specs | `spec/` (各機体ごと) | 制御信号・インターフェース定義 / Interfaces and protocols |
| **PoC** | `poc/` (各機体ごと) | 検証用実装例・応用 / Use-case validations |

---

## 🧠 理論構成 / Theory Layers

📘 理論は [Samizo-AITL/theory](https://github.com/Samizo-AITL/theory) に格納されています。  
📘 Core theory is maintained in [Samizo-AITL/theory](https://github.com/Samizo-AITL/theory).

| 層 / Layer | ディレクトリ | 内容 / Topics |
|------------|--------------|---------------|
| 推論層 / Reasoning Layer | `theory/reasoning/` | 状態推論、制約論理、因果関係 / Logic programming, belief inference |
| 制御層 / Control Layer | `theory/control/` | PID, MPC, デジタル制御、ロバスト制御 / PID, MPC, digital, robust |
| 物理層 / Physics Layer | `theory/physics/` | 動力学、センサ・外乱モデル / Physical dynamics, interfacing |

🔗 理論トップ / Entry: [`theory/README.md`](https://github.com/Samizo-AITL/theory/blob/main/README.md)

---

## 🤖 実装構成 / Implementation Projects

| プラットフォーム | パス | 内容 / Description |
|------------------|------|--------------------|
| AITL-R（ロボット） | `implementation/robot/` | 推論・制御・物理層統合の自律ロボット制御 / Full logic-to-physics robot AI |
| SkyEdge（ドローン） | `implementation/drone/` | 経路・姿勢・外乱対応を含む飛行AI / Flight control & dynamic planning |

各構成には以下が含まれます：  
Each platform contains:

- `poc/`: 検証用デモ / Proof-of-concepts  
- `spec/`: インターフェース仕様 / Actuator & logic interface

---

## 🛠 利用例 / Use Cases

| 対象 / Platform | 応用例 / Use | PoC |
|------------------|-------------|-----|
| AITL-R | 故障検知と自律復旧 / Self-repair logic | `robot/poc/diagnostics.md` |
| SkyEdge | 飛行ルート再計画 / Dynamic route replanning | `drone/poc/drone_path.md` |
| マルチエージェント | 協調型復旧制御 / Cooperative fault logic | `drone/poc/multiagent_recovery.md` |

---

## 📑 仕様定義 / Spec Documents

各機体配下の `spec/` に整理されています：  
Specs are defined under each `/spec/` folder:

- `control_interface.md`: 制御信号とフィードバック構造  
- `fault_handling.md`: 故障対応・異常伝播の制御論  
- `logic_runtime.md`: 推論エンジンの実行仕様

---

## 👤 著作・貢献 / Author & Contribution

- 開発者 / Author: **三溝 真一（Shinichi Samizo）**  
- ライセンス / License: [MIT License](./LICENSE)  
- 貢献歓迎 / Contributions welcome: Fork, improve, or open issues

---

## 🚀 はじめに / Getting Started

1. 理論を理解 → [Samizo-AITL/theory](https://github.com/Samizo-AITL/theory)  
2. 実装を参照 → `implementation/`（robot, drone）  
3. 仕様で接続確認 → `spec/`  
4. 応用PoCで動作確認 → `poc/`  

---
