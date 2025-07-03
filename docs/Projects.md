# 📄 AITL 応用プロジェクト一覧（Projects Overview）

本ドキュメントは、AITL構想に基づいて展開される応用プロジェクト群を体系的に整理したものです。各プロジェクトの概要、対象分野、モデル構成、関連ドキュメントを一覧化し、開発・連携・発信のためのナビゲーションとして機能します。

---

## 🧠 AITLベース構成モデル

| 構成名      | 概要                              | 主な技術要素         |
|-------------|-----------------------------------|----------------------|
| AITL-R       | 自律ロボット制御                 | FSM＋LLM＋H∞         |
| AITL-HX      | 宇宙対応型PoC制御                | FDSOI, LDMOS, ロバスト制御 |
| Yorisoi構想  | 介護支援・共感AIロボット         | 寄り添い対話、センサ融合 |
| SkyEdge      | ドローン＋エッジAI               | 高精度カメラ、空間制御 |
| SkyShield    | 防衛・災害対応型ロボット         | 危機対応FSM、自己判断 |
| EcoSmartEdge | 産業IoT・自律システム            | エッジ制御、自己診断   |

---

## 🚀 応用プロジェクト一覧

### 🔹 AITL-HX：Hybrid Space Robot Control PoC

- **概要**：FSM×LLM×H∞によるロボット制御構造のPoC実装（宇宙適応設計）
- **特長**：放射線耐性構造（25nm FDSOI／0.35um LDMOS）、センサ応答設計
- **主ファイル**：`Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/`
- **詳細**：[AITL-HX README](../Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/README.md)

---

### 🔹 Yorisoi構想：寄り添い型介護支援ロボット

- **概要**：高齢者に寄り添う共感型AIロボット。発話／行動／感情理解で支援。
- **特長**：対話＋予測補助、感情推論、FSM制御による行動の安定化
- **文書**：`Application_Expansions/elder_care/yorisoi_robot_outline.md`
- **PoC**：`AITL-HX`の制御構造をベースに展開

---

### 🔹 SkyEdge：次世代エッジドローン構想

- **概要**：AITL構造を用いた高精度ドローン制御と空間AI処理（SkyEdge構成）
- **特長**：4Kカメラ処理／空中MPC制御／低遅延FSM制御
- **予定文書**：`Application_Expansions/sky_drone/SkyEdge_Design.md`

---

### 🔹 SkyShield：防災・防衛対応型ロボット

- **概要**：災害／戦術環境下での自律判断・危機回避が可能な知能ロボット
- **特長**：危機予測FSM・LLM対話・センサ融合判断
- **予定文書**：`Application_Expansions/defense_and_rescue/fsm_in_hazard_response.md`

---

### 🔹 EcoSmartEdge：産業DX／スマートIoT構成

- **概要**：AITL構造を産業設備・スマートファクトリに適用
- **特長**：自己診断／遠隔制御／モジュール分散処理
- **予定文書**：`Application_Expansions/eco_smart/SmartEdge_Overview.md`

---

## 📚 補足資料・展開中リンク

- [`Application_Expansions/README.md`](../Application_Expansions/README.md)：応用展開の全体構成
- [`Education/.../AITL-HX/`](../Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/)：PoC制御構造例
- [`docs/AITL_Theory_Framework.md`](AITL_Theory_Framework.md)：三層モデルの基礎理論
- [`docs/AITL_Intro_For_Beginners.md`](AITL_Intro_For_Beginners.md)：入門者向け概要

---

## 🤝 貢献・連携案内

本プロジェクトは理論から実装・社会応用までを志向するオープン構想です：

- ご自身の応用シナリオを追加したい方は `Application_Expansions/` 以下に提案ください
- 教育応用・研究連携・実装支援などの協力も歓迎します
- Issues / Discussions / Pull Request にてご連絡ください

---

MIT License © 2025 AITL Project / Shinichi Samizo
