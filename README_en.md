# 🧠 AITL - All-in-Theory Logic

## Overview

AITL (All-in-Theory Logic) is an AI architecture concept designed to structurally and theoretically model intelligent systems.  
This project is based on a hierarchical model integrating inference, control, and physical dynamics, with the following goals:

- To support a deeper understanding of AI system structures  
- To provide design guidelines based on formal theory  
- To assist in education and research use cases  

AITL is not just a theoretical proposal. It also envisions practical implementation at the PoC (Proof of Concept) level, including applications such as drones and robots.  
It emphasizes meaningful AI construction through structured design, physical consistency, and self-repair concepts.

---

## 📦 Versions & Components

| Version | Description                                      | Corresponding Directory / File |
|---------|--------------------------------------------------|--------------------------------|
| v1.0    | Abstract theory model (3 layers: inference/control/physics) | [theory/](https://github.com/Samizo-AITL/theory) |
| v2.0    | PoC structure and implementation concept         | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)<br>[PoC/](../aitl-lab/PoC/) |

✅ In v2.0, the scope extends from theory to practical implementation plans.

---

## 🧱 AITL Structure and Relationships

| Component       | Description                            | Corresponding Directory / File |
|-----------------|----------------------------------------|--------------------------------|
| Abstract Theory | 3-layer model: Inference, Control, Physics | [theory/](https://github.com/Samizo-AITL/theory) |
| PoC System      | Design documentation for implementation | [SoC PoC Manual](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md) |
| Applied Systems | Drone & Robot system design examples    | [implementation/](./implementation/) |

---

## 📘 Terminology

- **PoC (Proof of Concept)**  
  Directory for actual verification and control design.  
  Includes source files and system architecture.  
  ➜ Main documents consolidated in [SoC_PoC_Manual_v5.0.md](https://github.com/Samizo-AITL/aitl-lab/blob/main/docs/SoC_PoC_Manual_v5.0.md)

- **SoC_PoC_Manual_v5.0.md**  
  Comprehensive manual for SoC-based control design inspired by AITL architecture.  
  Covers philosophy, logic, implementation, and evaluation.

---

## 🧠 Three-Layer Model Summary

| Layer (JP) | Layer (EN)       | Description                                      |
|------------|------------------|--------------------------------------------------|
| 推論層      | Logic Layer       | State recognition, hypothesis generation, decision-making, constraint reasoning |
| 制御層      | Control Layer     | Signal generation and stabilization (MPC, PID, etc.) |
| 物理層      | Physical Layer    | Physical interactions (dynamics, sensors, noise handling) |

---

## 🛠️ Implementation & Design Guides

Transitioning from AITL theory to PoC implementation is documented in the following files:

- 🧩 **[AITL System Implementation Guide](./docs/AITL_SystemGuide.md)**  
  Block diagrams, SoC module configurations, and PoC rollout patterns.

- 🧠 **[AITL Theory-to-Implementation Mapping](./docs/AITL_TheoryMapping.md)**  
  Correspondence table showing how theoretical layers map to practical implementations.

---

## 🚀 PoC Examples and Applications

AITL has been applied to the following conceptual and practical systems:

| Name             | Application Domain        | Model Configuration                 | Documentation |
|------------------|---------------------------|--------------------------------------|----------------|
| **AITL-R**        | Autonomous Robot          | Self-repairing, inference-driven control | [Robotics](./docs/robotics/) |
| **SkyEdge**       | Next-Gen Drone            | AI control + 4K Camera + Edge Computing | [SkyEdge](./docs/EcoPowerPlatform/SkyEdge/) |
| **EcoSmartEdge**  | Industrial DX & Smart IoT | Standard / Professional Models       | [Standard](./docs/EcoPowerPlatform/Standard/), [Professional](./docs/EcoPowerPlatform/Professional/) |
| **EcoAgriSky**    | Agricultural Drone + Sensor | AgriEdge + Eco Agri Power           | [AgriEdge](./docs/EcoPowerPlatform/AgriEdge/), [EcoAgriPower](./docs/EcoPowerPlatform/EcoAgriPower/) |
| **SkyShield**     | Disaster & Defense Systems | Based on Military model             | [Military](./docs/EcoPowerPlatform/Military/) |

📄 Detailed descriptions and use cases are provided in [docs/Projects.md](./docs/Projects.md).

---

## 🔗 Internal Documents

- [docs/AITL_Intro_For_Beginners.md](./docs/AITL_Intro_For_Beginners.md): Introduction to AITL  
- [docs/AITL_Theory_Framework.md](./docs/AITL_Theory_Framework.md): Full framework of AITL logic  
- [docs/AITL_Adopted_Theories.md](./docs/AITL_Adopted_Theories.md): Adopted theories and their rationale  

---

## 📫 Feedback & Collaboration

This is a living project. Questions, suggestions, or contributions regarding theory, implementation, or education are welcome via  
[GitHub Issues](https://github.com/Samizo-AITL/aitl-lab/issues) or Discussions.

---

## 🧾 About This Project

This repository aims to reimagine AI structure from the perspective of semiconductor system engineering.  
It provides a theory-driven, physically consistent, and self-repair-capable AI model in a format suitable for education and concept design.

🔎 This is not a completed implementation.  
Its main goal is theory development, learning support, and concept sharing.

---

## 🤝 Collaboration Opportunities

We welcome the following forms of collaboration:

- Technical contributions in implementation, control design, and robotics  
- Joint research and development using the AITL concept  
- Educational use and adaptation under the MIT License

🔧 Please note: implementation environments are still under development.  
Guidelines will be provided in a future version of `CONTRIBUTING.md`.

---

## ©️ Authorship & License

- Author / Proposer: **Shinichi Samizo**  
  M.Eng. in Electrical and Electronic Engineering, Shinshu University  
  Former engineer at Seiko Epson  
  Expertise: Semiconductor device technology

- License: **MIT License (Open Source)**  
  All content is free to use, modify, and redistribute under MIT terms.  
  Please retain copyright and license.

GitHub: [@Samizo-AITL](https://github.com/Samizo-AITL)  
Email: shin3t72@gmail.com

👉 [日本語版はこちら](#-aitl---all-in-theory-logic)
