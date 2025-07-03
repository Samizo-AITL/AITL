# 📘 AITL Adopted Theories

This document outlines the key **theories, principles, and design models** adopted in the AITL (All-in-Theory Logic) project. Each theory contributes to one or more layers of the **Samizo Architecture** (Logic / Control / Physical).

---

## 🧠 Logic Layer: LLM-Based Reasoning & Intent Modeling

### 🔹 Transformer Architecture

- Foundation for LLMs such as GPT, Claude, and LLaMA
- Self-attention enables dynamic semantic representation  
- Adapted for use in AITL via `llm_interface.py`

**Why adopted?**
> Provides language-driven inference, exception handling, and emotional reasoning in human-facing robotics.

---

### 🔹 Frame Semantics / Intention Modeling

- Contextual interpretation of utterances and environment
- Maps user input to FSM-intended states or goals
- Used for prompting and feedback injection

**AITL Use**: Dialogue → Intent → FSM flag → Safe action

---

## 🔁 Control Layer: Formal Deterministic Control

### 🔹 Finite State Machines (FSM)

- Deterministic, explicitly defined state-transition systems
- Human-readable and verifiable  
- Defined in `fsm_state_def.yaml`

**Why adopted?**
> Ensures traceability, safety, and predictability of control logic.

---

### 🔹 Supervisory Control Theory

- Coordination of multiple FSMs (hierarchical or parallel)
- Used for fault tolerance, task arbitration

**AITL Potential Use**: Multi-modal control (speech + motion + sensor)

---

## ⚙️ Physical Layer: Robust and Adaptive Dynamics

### 🔹 H∞ Control Theory (Robust Control)

- Minimizes worst-case response under uncertainty
- Suitable for dynamic environments (space, disaster)
- Implemented in `h_infinity_control_spec.md`

**Why adopted?**
> Guarantees system stability and performance even under sensor noise or external disturbance.

---

### 🔹 State Space Control (MPC, LQR)

- Model Predictive Control (MPC) for future-state optimization  
- Linear Quadratic Regulator (LQR) for trade-off tuning

**AITL Status**: Reserved for advanced implementation (e.g., drone dynamics)

---

## 📚 Additional Design Principles

| Principle           | Description |
|---------------------|-------------|
| 🧩 Modularity        | Clear separation of logic, control, physical domains |
| 🔍 Explainability    | FSM and transitions are human-readable, loggable |
| 🛡 Robustness        | H∞ ensures bounded performance in unknown conditions |
| 🧠 Adaptivity        | LLMs allow context-based override or recovery |
| 🧮 Formal Verification | FSMs and controllers can be checked against specs |

---

## 🧠 Mapping Table: Theories → Layers

| Theory / Model               | Logic | Control | Physical |
|-----------------------------|:-----:|:-------:|:--------:|
| Transformer (LLM)           | ✅    |         |          |
| Intention Modeling          | ✅    | ✅       |          |
| FSM                         |       | ✅       |          |
| Supervisory Control         |       | ✅       |          |
| H∞ Robust Control           |       |         | ✅       |
| MPC / LQR                   |       | ✅       | ✅       |

---

## 🔗 Related Documents

- [Theory Framework](./AITL_Theory_Framework.md)  
- [PoC Control Manual](../PoC/SoC_PoC_Manual_v5.0.md)  
- [FSM+LLM Spec](../Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/docs/specification/fsm_llm_structure.md)

---

## 📬 Feedback

We welcome discussion on extending or replacing theories depending on domain needs.

→ Use GitHub Issues or contact the project lead at `shin3t72@gmail.com`

---

MIT License | AITL Project Team | 2025
