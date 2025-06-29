# 🧠 AITL - All-in-Theory Logic

## 概要（Overview）

AITL（All-in-Theory Logic）は、知能システムを構造的・理論的に捉えるためのAIアーキテクチャ構想です。  
本プロジェクトは、推論・制御・物理を統合する階層モデルに基づき、次のような目的を持ちます：

- AI構造の理解支援  
- 理論に基づく設計指針の提示  
- 教育・研究への応用支援  

AITLは単なる理論提案にとどまらず、PoC（Proof of Concept）レベルの検証や応用設計（例：ドローン・ロボット）まで視野に入れています。  
構造化・物理整合・自己修復といった視点から、AIの意味ある構成を追求します。

---

## 📦 バージョンと構成

| バージョン | 内容                                  | 対応ディレクトリ・ファイル |
|------------|---------------------------------------|------------------------------|
| v1.0       | 抽象理論モデル（推論・制御・物理の3層） | [theory/](https://github.com/Samizo-AITL/theory) |
| v2.0       | PoC構成と実装構想                     | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)<br>[PoC/](../aitl-lab/PoC/) |

✅ v2.0 では、理論に加えて PoC や実装構想の整理まで踏み込んでいます。

---

## 🧱 AITL全体の構成と関係性

| 構成名        | 説明                             | 対応ディレクトリ・ファイル |
|---------------|----------------------------------|------------------------------|
| 抽象理論モデル | 推論・制御・物理の3層理論モデル    | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC構成       | 概念検証・設計ドキュメント        | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) |
| 応用構成       | ドローン・ロボット応用構成         | [implementation/](./implementation/) |

---

## 📘 用語説明

- **PoC**  
  実際の設計検証や制御実装のためのディレクトリ。ソースコードや設計ファイルを格納。  
  ※現在は [SoC_PoC_Manual_v5.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) に設計ドキュメントを集約。

- **SoC_PoC_Manual_v5.0.md**  
  AITL構想に基づくSoC制御PoC設計の全体マニュアル。設計方針・理論・実装・評価を包括的に記述。

---

## 🧠 モデル概要（3層構造）

| 層（日本語） | 層（英語）        | 概要                                     |
|--------------|------------------|------------------------------------------|
| 推論層        | Logic Layer      | 状態認識、仮説生成、意思決定、制約推論など |
| 制御層        | Control Layer    | MPC・PIDなどによる信号生成、安定制御     |
| 物理層        | Physical Layer   | 現実世界との接続（動力学、センサ、外乱処理など） |

---

## 🛠️ 実装ドキュメント・設計ガイド

AITLの理論 → 実装への流れ、およびモジュール分解・PoC展開手順は以下に整理されています：

- 🧩 **[AITL System Implementation Guide](./docs/AITL_SystemGuide.md)**  
  フィードバック制御構成図、SoCモジュール構成、PoC展開パターンを視覚化したガイド。

- 🧠 **[AITL Theory-to-Implementation Mapping](./docs/AITL_TheoryMapping.md)**  
  各種理論（物理・制御・推論）がPoC実装のどこに反映されているかをマッピングした対応表。

---

## 🚀 応用と展開例

AITL構想は以下のようなPoC実装・応用システムに展開されています：

| 名称              | 用途・対象               | モデル構成                         | 関連ドキュメントの案内 |
|-------------------|--------------------------|-------------------------------------|--------------------------|
| **AITL-R**        | 自律ロボット             | 自己修復・推論制御                 | `docs/Robotics/` を参照 |
| **SkyEdge**       | 次世代ドローン           | AI制御＋4Kカメラ＋高度エッジ       | `docs/EcoPowerPlatform/SkyEdge/` を参照 |
| **EcoSmartEdge**  | 産業DX・スマートIoT      | Standard / Professional モデル     | `docs/EcoPowerPlatform/Standard/`, `.../Professional/` を参照 |
| **EcoAgriSky**    | 農業ドローン＋畑センサ   | AgriEdge + Eco Agri Power           | `docs/EcoPowerPlatform/AgriEdge/`, `.../EcoAgriPower/` を参照 |
| **SkyShield**     | 防災・防衛・公共安全     | Militaryモデル中心                 | `docs/EcoPowerPlatform/Military/` を参照 |

| 名称              | 用途・対象               | モデル構成                         | 関連ドキュメントの案内 |
|-------------------|--------------------------|-------------------------------------|--------------------------|
| **AITL-R**        | 自律ロボット             | 自己修復・推論制御                 | [Robotics](../Robotics/) |
| **SkyEdge**       | 次世代ドローン           | AI制御＋4Kカメラ＋高度エッジ       | [SkyEdge](EcoPowerPlatform/SkyEdge/) |
| **EcoSmartEdge**  | 産業DX・スマートIoT      | Standard / Professional モデル     | [Standard](EcoPowerPlatform/Standard/), [Professional](EcoPowerPlatform/Professional/) |
| **EcoAgriSky**    | 農業ドローン＋畑センサ   | AgriEdge + Eco Agri Power           | [AgriEdge](EcoPowerPlatform/AgriEdge/), [EcoAgriPower](EcoPowerPlatform/EcoAgriPower/) |
| **SkyShield**     | 防災・防衛・公共安全     | Militaryモデル中心                 | [Military](EcoPowerPlatform/Military/) |


📄 各プロジェクトの概要・構成・背景は [docs/Projects.md](./docs/Projects.md) に詳述しています。

---

## 🔗 関連ドキュメント（内部リンク）

- [docs/AITL_Intro_For_Beginners.md](./docs/AITL_Intro_For_Beginners.md)：AITL入門ガイド  
- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md)：AITL理論の全体像と構成原理  
- [docs/AITL_Adopted_Theories.md](./docs/AITL_Adopted_Theories.md)：採用理論一覧と選定根拠  

---

## 📫 フィードバック歓迎

このプロジェクトは現在も進行中です。ドキュメントへの改善提案、理論への質問、PoC実装への参画など、  
[GitHub Issues](https://github.com/Samizo-AITL/aitl-lab/issues) または Discussions にてお気軽にご参加ください。

---

## 🧾 本プロジェクトについて

本リポジトリは、半導体デバイス技術の視点からAI構造を再考する試みとして立ち上げられました。  
AIの構造化・物理整合・自己修復といった視点を、理論提案と教育資料の形で体系化しています。

🔎 本プロジェクトは、実装やアルゴリズムの完成を目的としたものではありません。  
理論モデルの検討・学習支援・構想の共有が主な目的です。

---

## 🤝 協力について

このプロジェクトは以下のような協力を視野に入れています：

- 実装、制御設計、ロボティクス分野での技術的貢献  
- AITL構想をもとにした共同研究・展開  
- 教育・指導用資料としての自由な活用（MITライセンス）

🔧 ※現時点では実装・検証環境が十分に整っておらず、技術的な貢献・共同研究は今後の検討課題です。  
👉 `CONTRIBUTING.md` にて方針を順次整備予定です。

---

## ©️ 著作・ライセンス

- 著作・提案：三溝 真一（Shinichi Samizo）  
  信州大学大学院電気電子工学専攻修士課程修了／元セイコーエプソン  
  専門：半導体デバイス技術

- ライセンス：MIT License（オープンソース）  
  本構想および関連資料は、自由に利用・改変・再配布が可能です。  
  ご利用の際は著作権表示とライセンス文の保持をお願いします。

GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com
