# AITL-Core Module Overview

**📁 aitl-core/** は、AITL（All-in-Theory Logic）モデルの中核を構成する**3つの理論層**を格納したディレクトリです。  
本モジュールは、AIの論理推論・制御設計・物理統合をそれぞれのレイヤーで定義し、相互接続可能な階層構造を形成します。

---

## 🔧 構成ファイル一覧（Core 3-Layer）

| ファイル名 | 層名 | 主な役割 |
|------------|------|-----------|
| [`inference_logic.md`](./inference_logic.md) | 論理推論層（Layer 1） | 仮説生成・因果推論・意思決定 |
| [`control_design.md`](./control_design.md) | 制御設計層（Layer 2） | 安定化制御・最適化・予測設計 |
| [`physics_integration.md`](./physics_integration.md) | 物理統合層（Layer 3） | 物理法則との整合・PIML実装 |

---

## 🔍 概要：AITL中核3層の機能と連携

### 1️⃣ Inference Logic（論理推論層）

- 外界観測と知識ベースに基づいて「仮説」を生成
- ベイズ推論・因果グラフ・マルチエージェント推論に対応
- 意思決定のための**論理エンジンと戦略選択**を提供

🔗 **連携**：
- → Control層：予測・状況判断に基づく制御切替
- ← Physical層：観測との整合確認（物理検証）

---

### 2️⃣ Control Logic（制御設計層）

- PID／MPC／LQR等による**安定化・最適化制御の設計**
- meta-controlにより複数制御器を動的選択
- 強化学習とも連携可能（DQN, MDPベース設計）

🔗 **連携**：
- ← Inference層：目標・方策決定の入力
- → Physical層：制御対象へのフィードバック制御

---

### 3️⃣ Physical Model Integration（PIML）

- ニュートン力学、熱伝導、電磁気などの**物理法則を学習に内在化**
- Physics-Informed ML（PINNs）を用いた現実反映
- センサデータ欠損補間、仮説の物理整合性チェックにも使用

🔗 **連携**：
- → Inference層：推論との整合性確認（仮説検証）
- ← Control層：物理ダイナミクスに沿った制御設計を支援

---

## 🧩 AITLにおける位置付け

本 `aitl-core/` モジュールは、AITLの4層構成のうち**Layer 1〜3**をカバーし、  
**GPT非依存かつSoC実装にも適応可能な「理論核」**として設計されています。

> 第4層：Self-Repair Logic は `/aitl-r/` 側に格納・定義されます（ロボットSoC用途に特化）。

---

## 📘 関連資料

- 📄 [AITL_Model_v1.0.md](../docs/AITL_Model_v1.0.md)：AITL全体モデル構成
- 🛠 各レイヤーの詳細仕様：`*.md` ファイルをご参照ください

---

## ✍ 著者情報

- 作成：**Shinichi Samizo**
- モデル：**AITL-Core v1.0**
- GitHub：[@samizo-aitl](https://github.com/samizo-aitl)
