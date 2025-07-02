# YorisoiHybridRobot: FSMエンジン実装（簡易版）

from enum import Enum

class FSMState(Enum):
    IDLE = "IDLE"
    CHECK = "CHECK"
    SAFE = "SAFE"
    ALERT = "ALERT"
    EMERGENCY = "EMERGENCY"

class FSMEngine:
    def __init__(self):
        self.state = FSMState.IDLE

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if isinstance(new_state, FSMState):
            print(f"状態遷移: {self.state.name} → {new_state.name}")
            self.state = new_state
        else:
            raise ValueError("不正な状態名")

    def transition_by_input(self, llm_output):
        """ LLM出力（dict形式）を受け取り、FSM遷移を判断する """
        try:
            state_str = llm_output.get("suggested_state")
            new_state = FSMState[state_str]
            self.set_state(new_state)
        except Exception as e:
            print("状態遷移失敗:", e)

# --- 使用例 ---
if __name__ == "__main__":
    fsm = FSMEngine()
    print("現在状態:", fsm.get_state().name)

    sample_input = {
        "suggested_state": "SAFE",
        "reason": "ユーザーが悲しそうな発話を繰り返しています。",
        "confidence": 0.91
    }

    fsm.transition_by_input(sample_input)
    print("新状態:", fsm.get_state().name)
