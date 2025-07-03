# 🧠 AITL - All-in-Theory Logic (English Overview)

**AITL (All-in-Theory Logic)** is an AI architecture framework that defines intelligent systems in a structural, theory-driven manner. It is based on a 3-layer model integrating logic, control, and physical interaction, with the following core goals:

- Structurally understanding AI architecture  
- Providing theory-based design guidance  
- Enabling use in education, research, and system implementation  

AITL is not just theoretical. It includes PoC implementations, robotic control systems, and real-world applications such as space robotics, disaster response, and elder care.

---

## 🧩 System Architecture: Samizo Model

AITL is built on the **Samizo Architecture**, which separates intelligence into three distinct, interconnected layers:

| Japanese Layer | English Layer    | Description                                           |
|----------------|------------------|-------------------------------------------------------|
| 推論層         | Logic Layer       | Situation recognition, hypothesis generation, decision-making |
| 制御層         | Control Layer     | Formal and deterministic state control (FSM, MPC, PID) |
| 物理層         | Physical Layer    | Dynamics, actuation, sensing, and robust response    |

Each layer can be independently developed, verified, and integrated, allowing for modular and interpretable intelligent system design.

---

## 📦 Versions and Structure

| Version | Description                              | Location                                  |
|---------|------------------------------------------|-------------------------------------------|
| v1.0    | Abstract 3-layer theoretical model        | `theory/`                                 |
| v2.0    | PoC structure and system implementation   | `PoC/`, `AITL_SoC_Design_Manual_v1.0.md`  |

✅ Version 2.0 includes actual robotic control PoCs, implementation guides, and applied examples.

---

## 🛠 PoC & Implementations

### 🔹 AITL-HX: Hybrid PoC for Space Robotics

- A core PoC implementing Samizo Architecture with FSM × LLM × H∞ control
- Designed for high-reliability environments (e.g., radiation-tolerant control systems)
- Includes:
  - `fsm_engine.py`: deterministic finite-state control
  - `llm_interface.py`: language-based reasoning and exception handling
  - `h_infinity_control_spec.md`: robust multivariable control theory
- Applied to multi-joint arms, cooling fans, and assistive robots
- Location:  
  `Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/`

📄 See: [AITL-HX README](./Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/README.md)

---

## 🚀 Application Projects

| Project Name | Domain             | Features                             | Reference                            |
|--------------|--------------------|--------------------------------------|---------------------------------------|
| **AITL-R**    | Autonomous Robots   | Self-repairing logic, robust control | `implementation/`                    |
| **Yorisoi**   | Elder Care Support | Empathetic dialogue + state control  | `Application_Expansions/elder_care/` |
| **SkyEdge**   | AI Drone Platform  | 4K camera + MPC flight control       | `Application_Expansions/sky_drone/`  |
| **SkyShield** | Disaster/Defense   | FSM-based risk response              | `Application_Expansions/defense_and_rescue/` |

📘 Full list: [`docs/Projects.md`](./docs/Projects.md)

---

## 📚 Educational Resources

- **Fundamental of AITL Architecture**  
  → Structured educational material for theory and practice
- Includes control theory, FSM design, LLM integration, and hardware deployment
- Connected to the **Edusemi** initiative for next-generation engineering education

---

## 📘 Key Documents

- `docs/AITL_Intro_For_Beginners.md` – Beginner-friendly introduction  
- `docs/AITL_Theory_Framework.md` – Core theory and architecture breakdown  
- `docs/AITL_Adopted_Theories.md` – Control and AI theories adopted in AITL  
- `PoC/SoC_PoC_Manual_v5.0.md` – Comprehensive implementation guide for PoC

---

## 🤝 Contribution Guidelines

We welcome community contributions and collaborations:

- Join development of control implementations or PoC systems  
- Propose use cases in elder care, robotics, disaster response, or space applications  
- Use AITL for research, teaching, or educational projects  

📬 Contribution guide coming soon in `CONTRIBUTING.md`

---

## ©️ License and Attribution

- **Author**: Shinichi Samizo  
  M.Eng, Shinshu University | Former Seiko Epson engineer  
  Expertise: Semiconductor design, robotics, AI control theory

- **License**: MIT License  
  → Free to use, modify, and redistribute with attribution

- GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
- Contact: shin3t72@gmail.com

---

## 🌐 日本語版はこちら / Japanese version available

👉 [README（日本語）はこちら](./README.md)
