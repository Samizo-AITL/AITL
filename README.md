# 🧠 AITL - All-in-Theory Logic

## 概要（Overview）

AITL（All-in-Theory Logic）は、知能システムを**構造的・理論的に捉える**ためのAIアーキテクチャ構想です。  
本プロジェクトは、**推論・制御・物理を統合**する階層モデルに基づき、次の目的を持ちます：

- AI構造の理解支援  
- 理論に基づく設計指針の提示  
- 教育・研究への応用支援  

AITLは単なる理論提案にとどまらず、PoC（Proof of Concept）による検証や、ドローン・ロボット等の応用設計まで視野に入れています。  
**構造化・物理整合・自己修復**といった視点から、AIの意味ある構成を追求します。

---

## 📦 バージョンと構成

| バージョン | 内容                                  | 対応ディレクトリ・ファイル |
|------------|---------------------------------------|------------------------------|
| v1.0       | 抽象理論モデル（推論・制御・物理の3層） | [theory/](https://github.com/Samizo-AITL/theory) |
| v2.0       | PoC構成と実装構想                     | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)<br>[PoC/](https://github.com/Samizo-AITL/aitl-lab) |

✅ v2.0 では、理論に加えて PoC や実装構想の整理まで踏み込んでいます。  
👉 特に SoC 設計の詳細は [AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md) にて解説しています。

---

## 🧱 AITL全体の構成と関係性

| 構成名        | 説明                             | 対応ディレクトリ・ファイル |
|---------------|----------------------------------|------------------------------|
| 抽象理論モデル | 推論・制御・物理の3層理論モデル    | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC構成       | 概念検証・設計ドキュメント        | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) |
| 応用構成      | ドローン・ロボット応用構成         | [implementation/](./implementation/) |

---

## 📘 用語説明

- **PoC**  
  実際の設計検証や制御実装のためのディレクトリ。ソースコードや設計ファイルを格納。  
  ※現在は [SoC_PoC_Manual_v5.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) に設計ドキュメントを集約。

- **SoC_PoC_Manual_v5.0.md**  
  制御PoC設計の中核マニュアル。設計方針・理論・実装・評価を包括的に記述。

- **AITL_SoC_Design_Manual_v1.0.md**  
  AITL構想に基づく**SoC設計・実装フロー**の詳細マニュアル。  
  → [AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md)

---

## 🧠 モデル概要（3層構造）

| 層（日本語） | 層（英語）      | 概要                                       |
|--------------|----------------|--------------------------------------------|
| 推論層        | Logic Layer    | 状態認識、仮説生成、意思決定、制約推論など |
| 制御層        | Control Layer  | MPC・PIDなどによる信号生成、安定制御       |
| 物理層        | Physical Layer | 動力学・センサ信号・外乱処理などの物理系   |

---

## 🛠️ 実装ドキュメント・設計ガイド

以下の文書で、理論からPoC実装への展開を図解・構造化しています：

- 🧩 **[AITL System Implementation Guide](./docs/AITL_SystemGuide.md)**  
  フィードバック制御構成・SoCモジュール構成・展開パターンを図解した実装ガイド。

- 🧠 **[AITL Theory-to-Implementation Mapping](./docs/AITL_TheoryMapping.md)**  
  3層理論がPoCにどう反映されるかを整理した対応表。

- 📘 **[AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md)**  
  制御PoCからSoC設計に至るまでの詳細フローを体系化したマニュアル。

---

## 🚀 応用と展開例

| 名称             | 用途・対象            | モデル構成                     | 関連ドキュメント |
|------------------|-----------------------|--------------------------------|------------------|
| **AITL-R**       | 自律ロボット          | 自己修復・推論制御             | [Robotics](./docs/robotics/) |
| **SkyEdge**      | 次世代ドローン        | AI制御＋4Kカメラ＋高度エッジ   | [SkyEdge](./docs/EcoPowerPlatform/SkyEdge/) |
| **EcoSmartEdge** | 産業DX・スマートIoT   | Standard / Professional モデル | [Standard](./docs/EcoPowerPlatform/Standard/), [Professional](./docs/EcoPowerPlatform/Professional/) |
| **EcoAgriSky**   | 農業ドローン＋畑センサ | AgriEdge + Eco Agri Power      | [AgriEdge](./docs/EcoPowerPlatform/AgriEdge/), [EcoAgriPower](./docs/EcoPowerPlatform/EcoAgriPower/) |
| **SkyShield**    | 防災・防衛・公共安全  | Militaryモデル中心             | [Military](./docs/EcoPowerPlatform/Military/) |

📄 詳細は [docs/Projects.md](./docs/Projects.md) を参照。

---

## 📚 教育リソースと次世代教科書

AITLの設計原理・実装手法を学べる公式教材です：

- [AITL 教科書（Fundamental of AITL Architecture）](./Education/Fundamental_of_AITL_Architecture/README.md)  
  三層構造の原理、LLM・制御理論・物理モデル統合、FPGA実装までを体系的に学べる入門書。

今後、EdusemiやAITL-Labと連携し、次世代工学教育の教材として拡充予定です。

---

## 🔗 関連ドキュメント（内部リンク）

- [docs/AITL_Intro_For_Beginners.md](./docs/AITL_Intro_For_Beginners.md)：AITL入門ガイド  
- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md)：理論の全体像と構成原理  
- [docs/AITL_Adopted_Theories.md](./docs/AITL_Adopted_Theories.md)：採用理論と選定根拠  

---

## 📫 フィードバック歓迎

このプロジェクトは現在も進行中です。  
ドキュメント改善、理論への質問、PoC実装への参画など歓迎します。  
→ [GitHub Issues](https://github.com/Samizo-AITL/aitl-lab/issues) または Discussions にてご参加ください。

---

## 🧾 本プロジェクトについて

AITLは、半導体技術の視点から**AI構造の理論化**を目指した構想です。  
理論提案・実装構想・教育資料を統合し、**学習・研究・議論の場**として活用されることを意図しています。

🔎 完成済みの製品設計やアルゴリズム開発ではなく、**理論モデルとその展開可能性の共有**が主目的です。

---

## 🤝 協力について

以下のような貢献・連携を歓迎します：

- 制御実装・PoC構築・ロボティクスへの技術協力  
- AITL構想に基づいた共同研究・応用開発  
- 教育用途での資料利用（MITライセンス）

👉 `CONTRIBUTING.md` にてガイドラインを順次公開予定です。

---

## ©️ 著作・ライセンス

- 著作・提案：三溝 真一（Shinichi Samizo）  
  信州大学大学院 電気電子工学専攻 修士課程修了／元セイコーエプソン  
  専門：半導体デバイス技術

- ライセンス：MIT License（オープンソース）  
  → 利用・改変・再配布可。著作権表示・ライセンス明記をお願いします。

GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---

📄 [English version available here](./README_en.md)
