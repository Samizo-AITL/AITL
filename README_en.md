# 🧠 AITL - All-in-Theory Logic (English Overview)

## Overview

AITL (All-in-Theory Logic) is a theoretical framework that structurally organizes intelligent systems using a layered architecture.  
Based on three foundational layers—**Logic**, **Control**, and **Physical**—AITL aims to provide:

- Structural understanding of AI  
- Theory-driven design methodology  
- Educational and research applications  

Unlike data-centric black-box AI, AITL emphasizes interpretable, deterministic, and modular AI construction.  
It extends beyond theoretical models to include Proof-of-Concept (PoC) implementation guides and applications such as drones and robots.  
AITL is a comprehensive system model pursuing structure, physical consistency, and self-repairing intelligence.

---

## 📦 Versions and Structure

| Version | Description                                | Target Directories / Files |
|---------|--------------------------------------------|-----------------------------|
| v1.0    | Core theoretical models (Logic, Control, Physical) | [theory/](https://github.com/Samizo-AITL/theory) |
| v2.0    | Added PoC manual and implementation roadmap        | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)<br>[PoC/](../aitl-lab/PoC/) |

✅ v2.0 includes practical design guidelines and implementation strategies derived from the AITL theory.

---

## 🧱 Project Structure and Relationships

| Component         | Description                                         | Location |
|------------------|-----------------------------------------------------|----------|
| Theoretical Core | Three-layer architecture (Logic, Control, Physical) | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC Design        | PoC architecture and control design documentation   | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) |
| Application Layer | Drone, robot, and AI system implementations         | [implementation/](./implementation/) |

---

## 📘 Terminology

- **PoC**  
  Proof-of-Concept implementation and verification layer.  
  Contains source files and design data. The primary design document is:  
  [SoC_PoC_Manual_v5.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)

- **SoC_PoC_Manual_v5.0.md**  
  Central documentation for AITL-based control SoC design.  
  Covers system structure, theoretical grounding, and implementation strategy.

---

## 🧠 AITL Layered Model Overview

| Layer        | Description                                                              |
|--------------|---------------------------------------------------------------------------|
| Logic Layer  | State recognition, hypothesis generation, decision-making, constraint logic |
| Control Layer| Signal generation via PID, MPC, robust or adaptive control                 |
| Physical Layer| Real-world interface including dynamics, sensors, and noise/disturbance |

---

## 🛠️ Design Guides and Implementation Documents

Detailed pathways from theory to implementation, including modular breakdowns and PoC system deployment strategies:

- 🧩 **[AITL System Implementation Guide](./docs/AITL_SystemGuide.md)**  
  Visual guide covering control structure, SoC module mapping, and deployment patterns.

- 🧠 **[AITL Theory-to-Implementation Mapping](./docs/AITL_TheoryMapping.md)**  
  Correlates core theoretical components (logic, control, physical) with their presence in the PoC design.

---

## 🚀 Use Cases and Applications

| Name     | Description                                                       |
|----------|-------------------------------------------------------------------|
| AITL-R   | Robot system architecture with autonomy, redundancy, fault handling |
| SkyEdge  | Aerial drone design for flight control and spatial reasoning       |
| PoC Manual | Main documentation for SoC and system design strategies           |

---

## 🔗 Related Documents (Internal Links)

- [docs/AITL_Intro_For_Beginners.md](./docs/AITL_Intro_For_Beginners.md): Beginner's guide to AITL  
- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md): Structural foundations of AITL theory  
- [docs/AITL_Adopted_Theories.md](./docs/AITL_Adopted_Theories.md): Summary of adopted theories and rationale  

---

## 📫 Feedback and Contributions

This project is actively evolving. We welcome:

- Suggestions to improve the documents  
- Questions about the theory  
- Contributions to implementation or design  
- Collaboration on research or education initiatives  

Feel free to open GitHub Issues or participate in Discussions.

---

## 🧾 About This Project

This repository re-examines AI system design from the perspective of semiconductor device engineering.  
We aim to establish a theory-driven, physically consistent, and self-repairable AI structure.  
Rather than completing implementations or training models, AITL focuses on theoretical insight and educational value.

🔎 **Note**: The project is not intended to deliver production-ready code.  
Its main objective is theory exploration, educational modeling, and open collaboration.

---

## 🤝 Contribution Opportunities

We welcome collaboration and concept sharing through:

- Technical contributions in implementation, control engineering, and robotics  
- Joint research based on the AITL framework  
- Use in academic teaching or technical education (MIT License)  

🔧 Full implementation and hardware testing environments are under development.  
More details will be published in `CONTRIBUTING.md`.

---

## ©️ Author & License

- **Author / Proposal**: Shinichi Samizo  
  M.Sc., Shinshu University / Formerly at Seiko Epson  
  Specialty: Semiconductor Device Engineering

- **License**: MIT License  
  All materials and ideas in this repository are open source under the MIT License.  
  You are free to use, modify, and redistribute with proper credit.

GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

👉 [日本語版はこちら](#-aitl---all-in-theory-logic)
