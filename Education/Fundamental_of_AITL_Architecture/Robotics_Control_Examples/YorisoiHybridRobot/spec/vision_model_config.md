# 画像認識モデル設定仕様（vision_model_config.yaml）

---

## 📄 ファイル名

`vision_model_config.yaml`

---

## 📷 目的

本ファイルは、ロボットのカメラ映像を用いた  
- 顔認識  
- 表情分類  
- 感情推定  

などの画像認識処理を行うモデルおよびパラメータの構成を定義します。  
推定結果は `emotion_input.json` を通じて LLM/FSM に連携されます。

---

## 🧾 構造例

```yaml
model:
  type: cnn
  backend: tensorflow
  model_path: models/emotion_cnn_v3.h5
  input_size: [224, 224]
  classes: ["happy", "sad", "neutral", "angry", "fear"]

preprocessing:
  grayscale: true
  normalize: true
  histogram_equalization: false

inference:
  threshold: 0.6
  smoothing_window: 5
  frame_rate: 10
```

## 📝 各フィールド説明

| フィールド名                           | 型      | 説明                                                                 |
|----------------------------------------|---------|----------------------------------------------------------------------|
| `model.type`                           | string  | 使用する画像認識モデルの種類（例：`cnn`, `resnet`, `mobilenet`）     |
| `model.backend`                        | string  | 実行するMLフレームワーク（例：`tensorflow`, `onnx`, `torch`）       |
| `model_path`                           | string  | 学習済みモデルファイルのパス（`.h5`, `.pt`, `.onnx`など）            |
| `input_size`                           | list    | 入力画像サイズ `[幅, 高さ]`（例：`[224, 224]`）                     |
| `classes`                              | list    | 出力カテゴリ（感情ラベルの配列。順序はモデルに依存）               |
| `preprocessing.grayscale`              | bool    | 入力画像をグレースケールに変換するか（true/false）                 |
| `preprocessing.normalize`              | bool    | 画素値を0〜1に正規化するか                                          |
| `preprocessing.histogram_equalization` | bool    | ヒストグラム平坦化によるコントラスト調整を行うか                    |
| `inference.threshold`                  | float   | 信頼度のしきい値（この値未満の感情判定は「未定」とする）           |
| `inference.smoothing_window`           | int     | フレーム単位での感情推定を滑らかにするための移動平均ウィンドウ数    |
| `inference.frame_rate`                 | int     | 推論を行う画像処理レート（例：10fps）                               |

---

## 💡 補足

- `smoothing_window` によって、瞬間的な表情変化の誤認識を抑制できます  
- `classes` のラベルは `emotion_input.json` の `emotion` に直接渡されます  
- `threshold` によって「感情なし」や「曖昧な判断」のフィルタリングも可能です  
- 実装側では `cv2.VideoCapture` などと連携してリアルタイム処理が行われます
