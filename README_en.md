# 🧠 AITL - All-in-Theory Logic

---

## Overview

**AITL (All-in-Theory Logic)** is a design concept for AI systems based on the **Samizo Architecture**, which structurally and theoretically integrates AI into three layers:

- 🧠 **Logic Layer**: Hypothesis generation and intent estimation using LLM  
- 🔁 **Control Layer**: Deterministic control using FSM (Finite State Machine)  
- ⚙️ **Physical Layer**: Robust control based on H∞ theory and sensor processing  

AITL is not just a theoretical proposal — it includes PoC implementations, educational materials, and applications across domains such as space, defense, and elderly care.

---

## 🧱 Project Structure

| Component         | Description                             | Directory / Link |
|-------------------|------------------------------------------|------------------|
| Abstract Model    | Samizo Architecture (3-layer model)      | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC Implementation| FSM + LLM + Physical control validation  | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md), [`Education/`](./Education/) |
| Educational Materials | Materials to learn theory and implementation | [`Education/`](./Education/) |
| Application Domains | Robotics, elderly care, defense, etc.  | [`Application_Expansions/`](./Application_Expansions/) |

---

## 🔬 Samizo Architecture (Three-Layer Model)

| Layer (JP)    | Layer (EN)      | Description                                     |
|---------------|------------------|-------------------------------------------------|
| 推論層        | Logic Layer      | Intent understanding, dialogue generation (LLM) |
| 制御層        | Control Layer    | Deterministic control using FSM                |
| 物理層        | Physical Layer   | Robust control in real-world systems (H∞, sensors) |

<img src="./docs/images/samizo_architecture_v4.png" alt="Samizo Architecture" width="300"/>

---

## 🚀 PoC and Education

| Name              | Description                        | README |
|-------------------|------------------------------------|--------|
| AITL-HX           | PoC for space robotics              | [AITL-HX/README.md](./Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/README.md) |
| Education (Ch.1)  | Samizo Architecture and PoC intro  | [Fundamental README](./Education/Fundamental_of_AITL_Architecture/README.md) |
| SoC Design Guide  | SoC integrating FSM/LLM/Physical    | [AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md) |

---

## 🌍 Application Projects

| Name           | Domain         | Description                                 |
|----------------|----------------|---------------------------------------------|
| AITL-HX        | Space robotics | Radiation-tolerant control + LLM + H∞       |
| Yorisoi        | Elderly care   | Emotion-aware LLM + Safe FSM                |
| SkyShield      | Disaster/Defense| Risk-aware FSM + sensor fusion              |
| EcoSmartEdge   | Industrial IoT | Optimization with FSM + LLM                 |

👉 See each README in [`Application_Expansions/`](./Application_Expansions/)

---

## 📚 Education and Materials

| Material                              | Description                                 |
|--------------------------------------|---------------------------------------------|
| [`Fundamental_of_AITL_Architecture/`](./Education/Fundamental_of_AITL_Architecture/) | Intro materials for Samizo Architecture and PoC |
| Edusemi-AITL (planned)               | Semiconductor-to-AI educational path         |
| AITL-Lab (planned)                   | FSM/LLM control exercises and experimentation |

👉 Top of education: [Education/README.md](./Education/README.md)

---

## 📄 Reference Documents

- [AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md): Theoretical overview  
- [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md): Initial implementation guide  
- [README_for_Publication.md](./README_for_Publication.md): Technical media & OpenAI introduction

---

## 🧾 About this Project

- Author & Architect: **Shinichi Samizo**  
  M.Eng. in Electrical & Electronic Engineering, Shinshu University  
  Formerly: Seiko Epson (Semiconductor/Control/Robot Architectures)  
- License: MIT License (free to use/modify/redistribute)  
- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
- Contact: `shin3t72@gmail.com`

---

## 🤝 Call for Contribution

- Technical collaboration (FSM/PoC/hardware integration)  
- Educational use (for universities, technical colleges)  
- Research & development (AI in space, care, defense)

👉 Guidelines will be published in `CONTRIBUTING.md`

---
