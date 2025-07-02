# 音声出力設定仕様（voice_output_config.yaml）

---

## 📄 ファイル名

`voice_output_config.yaml`

---

## 🔊 目的

このファイルは、TTS（Text-to-Speech）による音声出力のスタイルや感情表現、声質などを調整する設定を定義します。  
高齢者に対して優しく、安心感を与える対話体験を提供することを目的としています。

---

## 🧾 構造例

```yaml
default:
  language: ja-JP
  voice: "haruka"
  pitch: 1.0
  speed: 1.0
  emotion: "neutral"

emotion_mapping:
  happy:
    voice: "haruka"
    pitch: 1.1
    speed: 1.05
    emotion: "joyful"
  sad:
    voice: "haruka"
    pitch: 0.9
    speed: 0.9
    emotion: "empathetic"
  fear:
    voice: "haruka"
    pitch: 0.95
    speed: 0.95
    emotion: "calm"
```

## 📝 各フィールド説明

| フィールド名               | 型      | 説明                                                                 |
|----------------------------|---------|----------------------------------------------------------------------|
| `default.language`         | string  | 出力音声の言語設定。`ja-JP`（日本語）、`en-US`（英語）など           |
| `default.voice`            | string  | 使用するTTSエンジンの音声モデル名（例：`haruka`, `takumi`）         |
| `default.pitch`            | float   | 音声の高さ調整。1.0が標準、>1.0で高く、<1.0で低くなる               |
| `default.speed`            | float   | 音声の再生速度。1.0が標準、>1.0で速く、<1.0で遅くなる               |
| `default.emotion`          | string  | デフォルトの感情トーン（例：`neutral`, `calm`, `joyful`）           |
| `emotion_mapping`          | object  | 感情推定結果に応じてTTSパラメータを変更する設定                     |
| ├ `<emotion>`              | object  | 感情ラベルごとに指定される出力設定（例：`happy`, `sad`）            |
| ├ `voice`                  | string  | 対応するTTS音声モデル                                               |
| ├ `pitch`                  | float   | 感情ラベルに応じたピッチ（高さ）設定                               |
| ├ `speed`                  | float   | 感情ラベルに応じた話速設定                                          |
| ├ `emotion`                | string  | TTSエンジンに渡す感情パラメータ名（エンジン仕様に依存）             |

---

## 💡 例：感情 `sad` に対応する設定

```yaml
sad:
  voice: "haruka"
  pitch: 0.9
  speed: 0.9
  emotion: "empathetic"
```

→ ゆっくり・低め・共感的な声で出力される。

---

## 📎 備考

- 本設定ファイルは `tts_driver.py` によって読み込まれます  
- ユーザーの感情状態に応じた「声の寄り添い」を実現可能にします  
- 感情変化に合わせて TTS 出力が柔軟に適応し、安心感・信頼感のある応答が可能となります  
- 感情分類と TTS の出力品質のマッピングを精緻にすることで、  
  認知症ケアや心理的支援にも応用が可能です  
- 複数話者モデルに対応させることで、性別や状況に合わせた「パーソナライズ」も可能です

