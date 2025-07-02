# action_executor.py
# 音声出力・動作指示などのアクションを実行するモジュール
# action_output.json や FSM遷移に基づく出力制御を担う

import json
from typing import Dict, Any

class ActionExecutor:
    def __init__(self):
        pass  # 必要に応じてTTSやモーター制御など初期化

    def execute_action(self, action: Dict[str, Any]) -> None:
        action_type = action.get("type")
        content = action.get("content")

        if action_type == "voice":
            self.say(content)
        elif action_type == "motion":
            self.perform_motion(content)
        elif action_type == "sound":
            self.play_sound(content)
        elif action_type == "stop_motion":
            self.stop_all_motion()
        else:
            print(f"[ActionExecutor] Unknown action type: {action_type}")

    def say(self, text: str) -> None:
        print(f"[TTS] {text}")
        # 実際のTTSエンジン呼び出しに置き換える

    def perform_motion(self, motion_id: str) -> None:
        print(f"[Motion] Executing motion: {motion_id}")
        # モーター制御やサーボコマンドに変換して送信

    def play_sound(self, sound_id: str) -> None:
        print(f"[Sound] Playing sound: {sound_id}")
        # 音声ファイル再生やシステム通知に接続

    def stop_all_motion(self) -> None:
        print("[Motion] Stopping all motions.")
        # 緊急停止やモーターオフ指示
