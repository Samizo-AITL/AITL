# センサ設定仕様（sensor_config.yaml）

---

## 📄 ファイル名

`sensor_config.yaml`

---

## ⚙ センサ構成とパラメータ定義

このファイルは、ロボットに搭載される各種センサの設定値や更新周期、校正情報などを定義します。  
センサ情報はリアルタイム処理とログ収集の両方に利用されます。

---

## 🧾 構造例

```yaml
temperature_sensor:
  type: digital
  model: TMP117
  update_rate_ms: 100
  accuracy_degC: ±0.3

encoder:
  type: rotary
  resolution_deg: 0.01
  update_rate_ms: 1

load_sensor:
  type: torque
  range_Nm: 0-10
  update_rate_ms: 1

camera:
  type: cmos
  resolution: 640x480
  frame_rate_fps: 30
  emotion_recognition: true
```

## 📝 各フィールド説明

| センサカテゴリ       | フィールド名           | 型     | 必須 | 説明                                                    |
|----------------------|------------------------|--------|------|---------------------------------------------------------|
| `temperature_sensor` | `type`                 | string | 必須 | センサの種類（例：`digital`, `analog`）                |
|                      | `model`                | string | 任意 | 使用されるセンサの型番（例：`TMP117`）                 |
|                      | `update_rate_ms`       | int    | 必須 | センサのデータ更新周期（単位：ミリ秒）                |
|                      | `accuracy_degC`        | string | 任意 | 温度センサの精度（例：`±0.3`）                         |
| `encoder`            | `resolution_deg`       | float  | 必須 | エンコーダの角度分解能（例：0.01度）                   |
|                      | `update_rate_ms`       | int    | 必須 | 更新周期（例：1ms）                                    |
| `load_sensor`        | `range_Nm`             | string | 必須 | トルクセンサの測定範囲（例：`0-10`Nm）                 |
|                      | `update_rate_ms`       | int    | 必須 | 更新周期（例：1ms）                                    |
| `camera`             | `resolution`           | string | 任意 | 解像度（例：`640x480`）                                |
|                      | `frame_rate_fps`       | int    | 任意 | フレームレート（例：30fps）                            |
|                      | `emotion_recognition`  | bool   | 任意 | 感情認識用途かどうか（true/false）                     |

---

## 💡 メモ

- 全センサは `sensor_driver` によって初期化時に読み込まれます  
- `update_rate_ms` により制御周期が決まるため、リアルタイム制御の制約に直結します  
- `emotion_recognition: true` の設定は LLM入力への画像解析を有効にします  
- センサ追加時はこのYAMLに追記し、対応するドライバ実装が必要です
