# 🧠 AITL - All-in-Theory Logic

## Overview

AITL (All-in-Theory Logic) is an AI architecture concept that structurally and theoretically models intelligent systems.  
This project is based on a **three-layer hierarchy** that integrates inference, control, and physical dynamics, aiming to:

- Support a deeper understanding of AI system structures  
- Provide design guidelines grounded in formal theory  
- Promote application in education and research  

AITL is not merely a theoretical proposal. It also envisions **practical validation at the PoC (Proof of Concept)** level, including real-world applications such as drones and robots.  
The framework emphasizes **structured design, physical consistency, and self-repair capabilities** as key principles in building meaningful AI.

---

## 📦 Versions & Components

| Version | Description                                      | Directory / File |
|---------|--------------------------------------------------|------------------|
| v1.0    | Abstract theory model (3-layer: inference, control, physical) | [theory/](https://github.com/Samizo-AITL/theory) |
| v2.0    | PoC structure and implementation strategy         | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)<br>[PoC/](https://github.com/Samizo-AITL/aitl-lab) |

✅ In v2.0, the scope extends beyond theory to structured PoC and implementation planning.  
👉 For detailed SoC design implementation based on AITL, refer to:  
[AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md)

---

## 🧱 AITL Structure & Relationships

| Component       | Description                            | Directory / File |
|-----------------|----------------------------------------|------------------|
| Abstract Theory | Theoretical 3-layer model              | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC System      | System design and verification docs    | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) |
| Applied Systems | Application examples (drones, robots)  | [implementation/](./implementation/) |

---

## 📘 Terminology

- **PoC (Proof of Concept)**  
  Practical design and verification assets.  
  Includes source code, architecture diagrams, and control modules.  
  ➜ Primary reference: [SoC_PoC_Manual_v5.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)

- **SoC_PoC_Manual_v5.0.md**  
  A comprehensive guide for PoC-level control design based on AITL.  
  Covers conceptual theory, structure, control implementation, and evaluation.

- **AITL_SoC_Design_Manual_v1.0.md**  
  A detailed implementation manual for SoC design under the AITL architecture.  
  → [AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md)

---

## 🧠 Three-Layer Model

| Layer (JP) | Layer (EN)       | Description                                      |
|------------|------------------|--------------------------------------------------|
| 推論層      | Logic Layer       | State recognition, hypothesis generation, decision-making, constraint reasoning |
| 制御層      | Control Layer     | Signal generation and feedback control (e.g., MPC, PID) |
| 物理層      | Physical Layer    | Physical interaction (dynamics, sensors, disturbance processing) |

---

## 🛠️ Design & Implementation Guides

The transition from theory to PoC-level implementation is documented in the following materials:

- 🧩 **[AITL System Implementation Guide](./docs/AITL_SystemGuide.md)**  
  Block diagrams for feedback control systems, SoC module structures, and deployment patterns.

- 🧠 **[AITL Theory-to-Implementation Mapping](./docs/AITL_TheoryMapping.md)**  
  A mapping table that links theory layers to corresponding PoC modules.

- 📘 **[AITL_SoC_Design_Manual_v1.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/soc-manual/AITL_SoC_Design_Manual_v1.0.md)**  
  A full implementation manual for SoC design aligned with AITL’s three-layer architecture.

---

## 🚀 Applications & PoC Examples

| Name             | Application Domain        | Configuration                      | Documentation |
|------------------|---------------------------|-------------------------------------|----------------|
| **AITL-R**        | Autonomous Robot          | Self-repairing control with inference logic | [Robotics](./docs/robotics/) |
| **SkyEdge**       | Next-Gen Drone            | AI control + 4K camera + edge computing | [SkyEdge](./docs/EcoPowerPlatform/SkyEdge/) |
| **EcoSmartEdge**  | Industrial DX / Smart IoT | Standard and Professional models    | [Standard](./docs/EcoPowerPlatform/Standard/), [Professional](./docs/EcoPowerPlatform/Professional/) |
| **EcoAgriSky**    | Agricultural Drone System | AgriEdge platform with farm sensors | [AgriEdge](./docs/EcoPowerPlatform/AgriEdge/), [EcoAgriPower](./docs/EcoPowerPlatform/EcoAgriPower/) |
| **SkyShield**     | Disaster / Defense Systems| Military model-oriented application | [Military](./docs/EcoPowerPlatform/Military/) |

📄 For more details, see [docs/Projects.md](./docs/Projects.md).

---

## 📚 Educational Resources and Next-Gen Textbook

This repository includes official educational materials to learn the AITL architecture, its principles, and practical design methods:

- [AITL Textbook (Fundamental of AITL Architecture)](./Education/Fundamental_of_AITL_Architecture/README.md)  
  A beginner-friendly textbook covering the three-layer architecture, LLM-based inference, control theory, physical modeling, and FPGA implementation.

Further development is planned in collaboration with Edusemi and AITL-Lab to support next-generation engineering education.

---

## 🔗 Internal References

- [docs/AITL_Intro_For_Beginners.md](./docs/AITL_Intro_For_Beginners.md): Beginner’s guide to AITL  
- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md): Complete theory structure and design principles  
- [docs/AITL_Adopted_Theories.md](./docs/AITL_Adopted_Theories.md): List of adopted theories and rationale  

---

## 📫 Feedback & Collaboration

This project is still evolving.  
We welcome improvements, questions, and participation in discussions and implementation.  
→ Contact us via [GitHub Issues](https://github.com/Samizo-AITL/aitl-lab/issues) or Discussions.

---

## 🧾 About the Project

This repository is an initiative to rethink AI structure from the perspective of semiconductor engineering.  
It offers a theory-driven, physically consistent, and self-repair-capable AI architecture in a structured documentation format.

🔎 Note: This is **not** a completed implementation or product.  
Its primary purpose is to support theory building, education, and conceptual design.

---

## 🤝 Opportunities for Collaboration

We’re open to collaboration in the following areas:

- Technical contributions in control systems, robotics, and PoC prototyping  
- Research and development based on the AITL concept  
- Educational use under the MIT license

🔧 Development environments are still in progress.  
Contribution guidelines will be provided in a future update of `CONTRIBUTING.md`.

---

## ©️ Authorship & License

- Author / Proposer: **Shinichi Samizo**  
  M.Eng. in Electrical and Electronic Engineering, Shinshu University  
  Former engineer at Seiko Epson  
  Specialty: Semiconductor device technology

- License: **MIT License**  
  All materials are free to use, modify, and redistribute under open source terms.  
  Please include appropriate credit and license reference.

GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

---

📄 [日本語版はこちら / Japanese version available here](./README.md)
