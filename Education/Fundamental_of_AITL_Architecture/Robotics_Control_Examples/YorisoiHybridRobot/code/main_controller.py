# main_controller.py
# ロボット全体の周期的制御を担うメインコントローラ
# センサ取得 → FSM更新 → LLM推論 → アクション実行 までを統括

import time

from fsm_engine import FSMEngine
from llm_interface import LLMInterface
from sensor_manager import SensorManager
from action_executor import ActionExecutor

FSM_DEF_PATH = "../spec/fsm_state_def.yaml"
RECOVERY_PATH = "../spec/recovery_strategy.yaml"
LOOP_INTERVAL_SEC = 1.0  # 制御周期（秒）

def main():
    fsm = FSMEngine(FSM_DEF_PATH, RECOVERY_PATH)
    llm = LLMInterface()
    sensors = SensorManager()
    actions = ActionExecutor()

    print("[MainController] 起動しました")

    while True:
        # 1. 入力の統合
        inputs = sensors.get_combined_inputs()

        # 2. FSM状態更新
        current_state = fsm.update(inputs)

        # 3. 状態に応じたLLM提案
        suggested_state, action = llm.get_suggestion(current_state, inputs)

        # 4. FSMが遷移しないならLLM提案を検討（オプション）
        if suggested_state and suggested_state != current_state:
            print(f"[Main] LLM提案による状態候補: {suggested_state}")

        # 5. アクションの実行
        if action:
            actions.execute_action(action)

        time.sleep(LOOP_INTERVAL_SEC)

if __name__ == "__main__":
    main()
