# sensor_manager.py
# センサ入力（emotion_input.json, system_status.json など）を統合的に取得・提供するモジュール

import json
from typing import Dict, Any
import os

class SensorManager:
    def __init__(self, data_dir: str = "../data"):
        self.data_dir = data_dir

    def load_json(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.data_dir, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[SensorManager] Failed to load {filename}: {e}")
            return {}

    def get_emotion_input(self) -> Dict[str, Any]:
        return self.load_json("emotion_input.json")

    def get_system_status(self) -> Dict[str, Any]:
        return self.load_json("system_status.json")

    def get_combined_inputs(self) -> Dict[str, Any]:
        # FSMやLLMへの入力として統合する
        emotion = self.get_emotion_input()
        status = self.get_system_status()
        combined = {**emotion, **status}
        return combined
