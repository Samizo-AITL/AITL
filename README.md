# 🧠 AITL - All-in-Theory Logic

---

## 概要（Overview）

**AITL（All-in-Theory Logic）** は、AIシステムを「推論層」「制御層」「物理層」の三層に分離し、それぞれを構造的・理論的に統合する**Samizoアーキテクチャ**に基づくAI設計構想です。

- 🧠 **推論層**：LLMによる意味理解・仮説生成・意図推定  
- 🔁 **制御層**：FSM（有限状態機械）による決定論的制御  
- ⚙️ **物理層**：H∞制御理論等による堅牢な物理系制御  

AITLは**理論提案**にとどまらず、**PoC実装**や**教育教材**、さらには**宇宙・防衛・介護等の応用展開**までを視野に構成されています。

---

## 🧱 プロジェクト構成

| 構成名          | 説明                           | 対応ディレクトリ |
|------------------|----------------------------------|-------------------|
| 抽象理論モデル   | Samizoアーキテクチャ（三層構造） | [`theory/`](./theory/) |
| PoC構成          | FSM+LLM+物理制御の検証実装       | [`PoC/`](./PoC/), [`Education/`](./Education/) |
| 教育教材         | 理論と実装を学ぶための教材群     | [`Education/`](./Education/) |
| 応用展開         | 宇宙ロボット・介護・防衛等の応用 | [`Application_Expansions/`](./Application_Expansions/) |

---

## 🔬 Samizoアーキテクチャ（3層構造）

| 層（日本語） | 英語        | 概要                                       |
|---------------|-------------|--------------------------------------------|
| 推論層        | Logic Layer | 意図理解、対話生成、例外処理（LLM）         |
| 制御層        | Control Layer | 状態遷移・決定論的制御（FSM）               |
| 物理層        | Physical Layer | 実環境でのロバスト制御・センサ信号処理（H∞等） |

<img src="./docs/images/samizo_architecture_v4.png" alt="Samizo Architecture" width="300"/>

---

## 🚀 PoC実装と教育展開

| 名称              | 概要                           | 対応README |
|-------------------|----------------------------------|-------------|
| AITL-HX            | 宇宙ロボット向け PoC             | [AITL-HX/README.md](./Education/Robotics_Control_Examples/AITL-HX/README.md) |
| 教育教材（第1章） | Samizo構造＋PoC導入教材          | [Fundamental README](./Education/Fundamental_of_AITL_Architecture/README.md) |
| SoC設計ガイド     | FSM/LLM/物理をSoC統合            | [SoC設計ガイド](./docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md) |

---

## 🌍 応用展開プロジェクト

| 名称         | 用途         | 説明                              |
|--------------|--------------|-----------------------------------|
| AITL-HX       | 宇宙ロボット | 放射耐性制御＋LLM＋H∞制御           |
| Yorisoi       | 介護ロボット | 感情理解LLM＋安全FSM               |
| SkyShield     | 防災・防衛   | リスク予測FSM＋センサ融合制御       |
| EcoSmartEdge  | 産業IoT      | FSM＋LLMによる最適化制御            |

👉 各READMEは [`Application_Expansions/`](./Application_Expansions/) 以下に配置

---

## 📚 教育資料と教材構成

| 教材名                            | 説明                             |
|----------------------------------|----------------------------------|
| [`Fundamental_of_AITL_Architecture/`](./Education/Fundamental_of_AITL_Architecture/) | Samizo構造とPoC例を学ぶ導入教材    |
| Edusemi-AITL（予定）             | 半導体から構造AIを理解する教材      |
| AITL-Lab（予定）                 | FSMやLLM制御を段階的に体験可能な演習群 |

👉 教育セクション：[Education/README.md](./Education/README.md)

---

## 📄 参考資料・ドキュメント

- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md)：理論全体像とレイヤー定義  
- [PoC/SoC_PoC_Manual_v5.0.md](./PoC/SoC_PoC_Manual_v5.0.md)：初期実装マニュアル  
- [README_for_Publication.md](./README_for_Publication.md)：技術メディア・OpenAI向け英語紹介資料

---

## 🧾 本プロジェクトについて

- 著作・提案：三溝 真一（Shinichi Samizo）  
　信州大学大学院 電気電子工学専攻 修士課程修了  
　専門：半導体デバイス／制御／ロボット構造AI  
- ライセンス：MIT License（利用・改変・教育自由）  
- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
- お問い合わせ：`shin3t72@gmail.com`

---

## 🤝 ご協力のお願い

- 技術貢献（FSM制御／PoC実装／ハードウェア統合）  
- 教育連携（大学・高専での授業使用）  
- 応用研究（宇宙・介護・防衛AI分野）

👉 `CONTRIBUTING.md` にて詳細を掲載予定

---
