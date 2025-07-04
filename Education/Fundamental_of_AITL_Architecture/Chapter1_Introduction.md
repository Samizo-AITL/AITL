# Chapter 1: Introduction  
## Why AITL? 〜なぜAITLアーキテクチャが必要か〜

---

## 1.1 現代設計の課題

近年のエンジニアリング分野では、以下のような分断が深刻です：

- AI（特にLLM）はソフトウェア領域に限定され、ハードウェア設計とは乖離している  
- 制御理論は物理的環境に対して有効だが、AIとは統合されていない  
- センサ信号処理や遅延・ノイズ対策は、制御とは別領域で扱われる  

このような分離された設計では、次世代の自律システム（例：災害対応ドローン、知能ロボット、スマート農業）に対応できません。

---

## 1.2 AITLの目的

AITL（All-in-Theory Logic）は、AI・制御・物理を**統合的に設計・実装する教育/研究フレームワーク**です。  
その目的は以下の通りです：

- **LLM（大規模言語モデル）による高レベル仕様生成・推論**
- **制御理論（PID、MPC、Stateflow）に基づく動作設計**
- **センサ・物理環境との整合性ある信号処理**
- **FPGAやSoC上でのPoC実装を可能にするモデルベース設計**

---

## 1.3 AITLの適用分野

| 分野 | 応用例 |
|------|--------|
| 自律移動体 | 災害ドローン、探査ロボットの経路最適化と環境適応 |
| エネルギー | スマート農業、再生可能電力制御（EcoAgriPower） |
| 教育 | AI/制御/半導体を統合的に学ぶ教材として |
| 防災・軍事 | 状況理解と判断に基づいた緊急行動切替（SkyEdge） |

---

## 1.4 教材の位置づけ

この教材「**Fundamental of AITL Architecture**」は、以下のような人を対象に設計されています：

- LLMやAIを単なるツールとしてでなく「**設計の一部**」として使いたい人  
- モデルベース制御を実システムに応用したい人  
- FPGAやSoCでの実装まで見据えた教育を受けたい学生・研究者

---

## 1.5 今後の章構成について

次章では、AITLのコアである「**三層アーキテクチャ（論理・制御・物理）**」を詳しく解説します。  
それぞれの層がどのように設計され、どのように連携するのかを段階的に学びます。

---
