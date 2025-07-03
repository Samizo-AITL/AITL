# 🧠 AITL - All-in-Theory Logic  
**A Theory-Driven Architecture for Structured AI Systems**

---

## 🧭 What is AITL?

**AITL (All-in-Theory Logic)** is a layered, explainable, and physically grounded architecture for intelligent systems.  
It introduces a structural foundation to integrate:

- 🧠 **LLM-based reasoning**
- 🔁 **FSM-based control**
- ⚙️ **Robust physical actuation**

This architecture is formalized as the **Samizo Model**, a 3-layer structure for AI:

```
 Logic Layer    ← Reasoning (LLMs)
 Control Layer  ← Deterministic state transitions (FSM)
 Physical Layer ← Real-world dynamics (H∞, sensors, actuators)
```

---

## 🚀 Why AITL?

| Challenge in Modern AI   | AITL Response                   |
|--------------------------|----------------------------------|
| Black-box decision logic | Explicit FSM + traceable LLM logic |
| Fragile control systems  | H∞ robust control under noise & drift |
| Limited context awareness| LLM-based adaptive override |
| Lack of formal structure | 3-layer Samizo architecture |

---

## 🧩 AITL-HX: Proof of Concept

**AITL-HX** is a working PoC that demonstrates this structure:

- FSMs defined in YAML
- LLM override via `llm_interface.py`
- H∞ robust controller for actuation
- Designed for space robotics and radiation-tolerant logic

📁 Directory:  
`Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/`

---

## 📘 Key Components

| Component       | Description |
|------------------|-------------|
| `fsm_engine.py`  | Finite state machine engine |
| `llm_interface.py` | GPT-based intent reasoning |
| `h_infinity_control_spec.md` | Control structure using robust H∞ theory |
| `fsm_state_def.yaml` | Human-readable logic graph |

---

## 🌐 Application Domains

| Project       | Domain             | Tech Stack |
|---------------|--------------------|------------|
| **AITL-HX**   | Space robotics      | FDSOI, FSM, H∞ |
| **Yorisoi**   | Elder care robot    | LLM empathy + sensor override |
| **SkyShield** | Disaster / defense  | FSM + LLM for risk handling |
| **EcoSmartEdge** | Industrial DX / IoT | LLM + FSM optimization loop |

See: [`Application_Expansions/`](./Application_Expansions/README.md)

---

## 🎓 For Education and Research

The project includes structured educational materials under `Education/`:

- Introduction to Samizo theory  
- LLM and FSM integration hands-on  
- PoC implementations for lab use  
- Open license for teaching and extension

---

## 📬 Contact and Collaboration

We welcome:

- 🛠 Developers building interpretable control logic  
- 🧑‍🏫 Educators using AITL in robotics curricula  
- 🚀 Researchers extending hybrid architectures

Contact: `shin3t72@gmail.com`  
GitHub: [https://github.com/Samizo-AITL](https://github.com/Samizo-AITL)

---

MIT License | AITL Project Team | 2025
