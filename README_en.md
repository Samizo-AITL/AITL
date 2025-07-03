# 🧠 AITL - All-in-Theory Logic (English Overview)

**AITL (All-in-Theory Logic)** is an AI architecture framework that defines intelligence systems with a structural, theory-driven approach. It is built on a layered model that integrates reasoning, control, and physical interaction, with the following core goals:

- Supporting structural understanding of intelligent systems  
- Providing a theory-based design guide for engineering  
- Enabling educational use and research application  

AITL is not only a conceptual model but also includes practical validation via PoCs (Proof of Concept), and expansion toward applications in robotics, drones, elder care, and more.

---

## 🧩 System Architecture: Samizo Model

AITL is based on the **Samizo Architecture**, which separates intelligence into three explicit layers:

| Layer (JP)    | Layer (EN)       | Description                            |
|---------------|------------------|----------------------------------------|
| 推論層        | Logic Layer       | Situation recognition, hypothesis generation, decision making |
| 制御層        | Control Layer     | Formal control (FSM, MPC, PID)         |
| 物理層        | Physical Layer    | Real-world sensing, actuation, dynamics |

Each layer is physically and functionally separated and integrated via clear interfaces (IF), enabling robust, interpretable, and adaptive behavior in AI agents.

---

## 📦 Versions and Structure

| Version | Content                           | Folder/Document                     |
|---------|-----------------------------------|--------------------------------------|
| v1.0    | Abstract 3-layer theory            | `theory/`                            |
| v2.0    | Implementation concept and PoC     | `PoC/`, `AITL_SoC_Design_Manual.md`  |

✅ In **v2.0**, we have extended beyond theory to include actual PoC implementations and SoC-level design guidance.

---

## 🛠 PoC & Implementations

- **FSM + LLM + H∞ Control** as a robust and adaptive control structure
- Tested in robotic environments (multi-joint arms, cooling fans)
- `fsm_engine.py`, `fsm_state_def.yaml`, `llm_interface.py` in `AITL-HX/`
- PoC details: `Education/Fundamental_of_AITL_Architecture/Robotics_Control_Examples/AITL-HX/README.md`

---

## 🚀 Application Projects

| Project Name   | Domain           | Features                          | Docs                     |
|----------------|------------------|-----------------------------------|--------------------------|
| AITL-R          | Autonomous robots | Self-repair, FSM×LLM structure     | `implementation/`        |
| Yorisoi         | Elder care        | Empathetic support via dialogue    | `Application_Expansions/elder_care/` |
| SkyEdge         | Drone + AI Edge   | 4K Camera, spatial control         | `Application_Expansions/space_robotics/` |
| SkyShield       | Defense/Rescue    | FSM-driven emergency behavior      | `defense_and_rescue/`    |

📄 See: [`docs/Projects.md`](./docs/Projects.md)

---

## 📚 Educational Resources

- **Fundamental of AITL Architecture**  
  → Learn the theory and implementation in a structured course

- Integration with **Edusemi** and future AITL-Lab for next-gen engineering education

---

## 📘 Key Documents

- `docs/AITL_Intro_For_Beginners.md`: Beginner-friendly overview  
- `docs/AITL_Theory_Framework.md`: Full theory and layered model  
- `docs/AITL_Adopted_Theories.md`: Core theories and their rationale  
- `PoC/SoC_PoC_Manual_v5.0.md`: Control structure implementation manual

---

## 🤝 Contribution

We welcome all contributions and collaborations:

- Join PoC development or control implementation
- Use and adapt AITL theory for your own research or education
- Propose new applications under `Application_Expansions/`

📝 Contribution guidelines coming soon in `CONTRIBUTING.md`.

---

## ©️ License and Attribution

- **Author**: Shinichi Samizo  
  (M.Eng, Shinshu University; Former Seiko Epson engineer; Semiconductor expert)  
- **License**: MIT License — Free to use, modify, and redistribute with attribution  
- GitHub: `@Samizo-AITL`  
- Contact: `shin3t72@gmail.com`

---

## 🔗 日本語版はこちら / Japanese version available

👉 [日本語READMEはこちら](./README.md)
