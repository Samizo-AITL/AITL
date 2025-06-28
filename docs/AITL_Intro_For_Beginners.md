# 👋 AITL入門ガイド（Intro to AITL）

## AITLとは？

**AITL（All-in-Theory Logic）**は、AIシステムを「理論構造に基づいて設計する」ためのアーキテクチャ構想です。  
以下の3つの理論層に基づいて、AIを分解・理解・設計するための枠組みを提供します：

- **推論層**：意味理解、仮説生成、意思決定（Logic Layer）
- **制御層**：信号生成、安定制御（Control Layer）
- **物理層**：現実環境との接続（Physical Layer）

---

## なぜAITLなのか？

今日のAI（例：ChatGPTなどのLLM）は、非常に強力ですが、**「意味ある構造を持つAI」ではありません。**

| 項目 | LLM（統計型AI） | AITL（構造型AI） |
|------|------------------|------------------|
| 基本手法 | 統計・確率・大規模言語データ | 因果・物理・制御理論 |
| 意味理解 | パターン的類似で予測 | 仮説・制約・因果関係による判断 |
| 世界モデル | 内在せず | 明示的に設計可能（物理制約あり） |
| 応用設計 | 難しい（ブラックボックス） | 実装しやすい（PoC・モジュール化） |

AITLは、LLMのような「言語的・確率的な予測」だけではなく、  
**構造・制御・現実との整合性を重視する設計思想**です。

---

## こんな人におすすめ

- 意味あるAIアーキテクチャを設計したい  
- LLM以外のアプローチを模索している  
- ロボットや制御系PoCと連動するAI設計に興味がある  
- AI教育や初学者向け教材に理論的な軸を加えたい

---

## AITLの構成（ざっくり）

AITLは、以下の構成から成り立っています：

```
AITL/
├── theory/         ← 推論・制御・物理の基礎理論
├── aitl-lab/       ← PoC設計と実装マニュアル（v2.0）
├── implementation/ ← 応用展開例（SkyEdge、AITL-Rなど）
└── docs/           ← 解説資料・入門・理論整理
```

---

## はじめの一歩：おすすめ閲覧順

1. [AITL_Intro_For_Beginners.md](./AITL_Intro_For_Beginners.md)（← 今読んでいるページ）  
2. [AITL_Theory_Framework.md](./AITL_Theory_Framework.md)：AITL構造そのものの定義と3層理論  
3. [AITL_Adopted_Theories.md](./AITL_Adopted_Theories.md)：採用している制御理論・物理モデルの選定基準  
4. [aitl-lab/docs/SoC_PoC_Manual_v5.0.md](../aitl-lab/docs/SoC_PoC_Manual_v5.0.md)：実際の設計PoCガイド

---

## 注意点・FAQ

> ❓ AITLは実装ライブラリではないの？

いいえ。**理論と構成設計を重視するフレームワーク**です。実装は可能ですが、それ自体が目的ではありません。

> ❓ LLMやニューラルネットは使わないの？

補助的には使えますが、主役ではありません。主軸は「物理・制御・因果構造」にあります。

> ❓ 実際の応用例はあるの？

はい。PoCとしてドローン（SkyEdge）やロボット（AITL-R）向け設計が構想されています。

---

## 👣 次に読むべきドキュメント

- [AITL_Theory_Framework.md](./AITL_Theory_Framework.md)：AITLを理論的に理解したい方向け  
- [AITL_Adopted_Theories.md](./AITL_Adopted_Theories.md)：理論の選定プロセスを知りたい方向け  
- [SoC_PoC_Manual_v5.0.md](../aitl-lab/docs/SoC_PoC_Manual_v5.0.md)：PoCレベルの実践設計を見たい方向け

---

## 📫 ご意見・参加

GitHub Issues や Discussions にて、質問・改善提案・協力の申し出を歓迎します。  
初学者の立場からのフィードバックは特にありがたいです。

---
