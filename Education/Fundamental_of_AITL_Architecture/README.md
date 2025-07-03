# 📘 Fundamental of AITL Architecture

This is **Chapter 1** of the AITL Education Series.  
It provides a structured learning pathway to understand and apply the **Samizo 3-layer architecture** through both theory and working PoC examples.

---

## 🎯 Chapter Objectives

By completing this module, learners will be able to:

- Understand the structure and rationale behind the 3-layer AITL model  
- Design and verify FSM-based control logic  
- Integrate LLM-based reasoning into deterministic control systems  
- Implement robust physical control (e.g. H∞) in simulated or physical hardware

---

## 🧱 Directory Structure

```
Fundamental_of_AITL_Architecture/
├── Robotics_Control_Examples/
│   └── AITL-HX/                 ← Hybrid PoC implementation
│       ├── fsm_engine.py
│       ├── llm_interface.py
│       ├── docs/
│       └── data/
├── chapter1_overview.md         ← (coming soon)
└── README.md                    ← 📘 This file
```

---

## 🧩 Core Example: AITL-HX

**AITL-HX** is the official proof-of-concept example demonstrating:

- Finite-state machine (FSM) control logic  
- Integration with LLM (e.g. GPT-4) for intent override  
- Robust physical control using H∞ formulation

🔍 Features:

| Component         | File / Module              |
|-------------------|----------------------------|
| FSM Logic Engine  | `fsm_engine.py`            |
| LLM Interface     | `llm_interface.py`         |
| FSM Definition    | `fsm_state_def.yaml`       |
| Control Spec      | `h_infinity_control_spec.md` |
| Docs              | `docs/`                    |

---

## 📚 Recommended Learning Path

| Step | Topic                        | Location |
|------|------------------------------|----------|
| 1    | Review 3-layer theory        | [`docs/AITL_Theory_Framework.md`](../../../docs/AITL_Theory_Framework.md) |
| 2    | Understand FSM control       | `fsm_engine.py`, `fsm_state_def.yaml` |
| 3    | Integrate with LLM           | `llm_interface.py` |
| 4    | Add robust control (H∞)      | `h_infinity_control_spec.md` |
| 5    | Run and test the PoC         | Follow `AITL-HX/README.md` |

---

## 🔬 Application Domains

The concepts in this chapter are directly applicable to:

- 🛰 Space robotics (radiation-tolerant control)  
- 🧓 Elder care robotics (empathetic state control)  
- 🛡 Autonomous defense systems (risk-sensitive logic)  
- ⚙️ Smart industrial actuators (AI with formal logic)

---

## 💡 Tips for Educators

This module can be used as:

- A lecture unit in embedded systems or robotics  
- A lab exercise for FSM and control theory  
- A discussion starter on AI interpretability and hybrid design

---

## 📬 Feedback and Contribution

If you are using this chapter in teaching or research, we would love to hear from you.

- Contact: `shin3t72@gmail.com`  
- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)

---

MIT License | 2025 | AITL Education Team
