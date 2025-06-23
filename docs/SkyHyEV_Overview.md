# SkyHyEV Overview

## 概要

SkyHyEVモデルは、AITL-RのPoC（Proof of Concept）として設計された災害対応ドローンおよび遠隔制御モビリティ向けの自己修復型システムです。  
省電力かつ異常発生時にも継続動作が可能な高度な自己修復機構を備えています。

## 対象

- 災害対応ドローン
- 遠隔制御モビリティ（ロボティクス）

## 特徴

- 自己修復機能による故障検知・動的再構成
- 低消費電力設計
- 異常時の継続動作保証

## SoC構成

SkyHyEVは以下の4チップSoC構成を採用しています。

| チップ | プロセス        | 主な役割                        |
|--------|-----------------|--------------------------------|
| Chip 1 | 3nm FinFET/GAA  | AI推論・再構成判断（DNN/RL）   |
| Chip 2 | 0.18µm SOI      | 高耐圧制御系・Meta-Control      |
| Chip 3 | 0.35µm CMOS     | センサ処理・自己診断・通信制御  |
| Chip 4 | 0.18µm AMS      | アナログ異常抽出（温度・電流）  |

## PoCシナリオ

- アクチュエータ故障やセンサ欠損発生時に自動的に再構成を行い、継続稼働を維持
- 強化学習による動的な制御モデルの適応更新

## 関連ドキュメント

- `aitl-r/robotics_soc_config.md` — SoC構成詳細  
- `aitl-r/self_repair_control.md` — 自己修復ロジック詳細  
- `AITL_Model_v1.0.md` — AITL理論モデル全体

---

✍ 作成：Shinichi Samizo  
GitHub: @samizo-aitl  
Email: shin3t72@gmail.com
