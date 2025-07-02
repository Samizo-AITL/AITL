# YorisoiHybridRobot: LLMインタフェース → FSM連携

import json
from fsm_engine import FSMEngine, FSMState

class LLMInterface:
    def __init__(self, fsm: FSMEngine):
        self.fsm = fsm

    def load_llm_response(self, filepath):
        """ LLM出力JSONファイルを読み込む """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def apply_to_fsm(self, llm_response):
        """ LLMの出力をFSMに反映 """
        try:
            suggested = llm_response.get("suggested_state")
            self.fsm.set_state(FSMState[suggested])
            print(f"[LLM] 状態を {suggested} に変更しました。")
        except Exception as e:
            print("LLM→FSM 状態変更エラー:", e)

# --- 使用例 ---
if __name__ == "__main__":
    fsm = FSMEngine()
    llm_if = LLMInterface(fsm)

    response = llm_if.load_llm_response("YorisoiHybridRobot/spec/llm_response.json")
    llm_if.apply_to_fsm(response)
