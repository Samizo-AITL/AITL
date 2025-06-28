# Robotics Platform Documentation (AITL準拠 PoC & SystemDK 設計資料)

このディレクトリは、AITL（All-in-Theory Logic）理論に基づくロボット制御系のPoC設計およびSystemDK展開に関する設計ドキュメント群をまとめたものです。

---

## 📂 構成概要

| ディレクトリ            | 内容概要 |
|-------------------------|----------|
| `robot-spec/`           | ロボット全体の要求仕様・構成モジュール定義・ブロック図など |
| `PoC-reference/`        | SoC PoC設計マニュアル（v5.0）の参照リンクと簡易解説 |
| `SystemDK-design/`      | PoCからSystemDKへの発展設計、IP再構成戦略、出口設計事例 |
| `assets/`               | ブロック図・制御フロー図・チェックリスト等の補助ファイル |

---

## 📌 背景と目的

この文書群は、ロボティクス応用において以下を実現するために構成されています：

- AITLに基づいた制御SoCのPoC開発
- アナログ／デジタル／高電圧の協調設計と検証
- SystemDKへのスムーズな設計資産移行
- IP再利用とPoCDK→SystemDK変換の知見集約

---

## 🔗 主な関連ファイル・リンク

- [SoC PoC Manual v5.0（aitl-lab/docs配下）](../SoC_PoC_Manual_v5.0.md)：本プロジェクトのPoC設計方針のベース
- `robot-spec/module_spec_list.md`：ロボットを構成する各ICモジュールのプロセス・機能まとめ
- `SystemDK-design/conversion_cases.md`：PoCDK→SystemDKの変換事例集

---

## 🧩 利用対象者

- ロボット用制御SoCを開発するアーキテクト・設計者
- AITL理論を応用したSoC設計手法に関心のある研究者
- PoC成果を次フェーズに移行させたいプロジェクトマネージャ

---

## 🛠 今後の展開予定

- 要求仕様の精緻化とSystemDK移行パスの実装例
- テスト容易化設計（DFT）とAITL評価の適用事例
- ロボット用PoCテンプレートの公開とチュートリアル化

---

