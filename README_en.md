# 🧠 AITL - All-in-Theory Logic (English Overview)

## Overview

AITL (All-in-Theory Logic) is a theoretical framework designed to structure next-generation intelligent systems.  
Based on a three-layer architecture—Logic, Control, and Physical—AITL aims to support structural understanding, system design, and educational use of AI.  
Unlike data-driven approaches, AITL emphasizes deterministic, interpretable, and modular reasoning.  
It also includes PoC-level system design and implementation planning (e.g., drones, robotics), offering a comprehensive foundation for AI engineering.

## Versions and Structure

| Version | Description                                           | Target Directories / Files                               |
|---------|-----------------------------------------------------|---------------------------------------------------------|
| v1.0    | Core theoretical models (Logic, Control, Physical)  | theory/                                                 |
| v2.0    | Added PoC manuals and implementation structure proposals | `aitl-lab/docs/SoC_PoC_Manual_v5.0.md`、AITL/implementation/ |

✅ v2.0 includes practical design structures for control and implementation, derived from the core theory.

## Project Structure

AITL consists of three key directories in a conceptual pipeline:  
`theory/` ──▶ `aitl-lab/docs/SoC_PoC_Manual_v5.0.md` ──▶ `AITL/implementation/`  
(Theoretical Core) → (Control Design and PoC Manual) → (Application-level Architecture)

| Directory / File               | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| theory/                       | Theoretical models for the three-layer architecture (logic, control, physical). |
| aitl-lab/docs/SoC_PoC_Manual_v5.0.md | PoC manual document covering concept verification and design.  |
| AITL/implementation/          | Application structures for drones (SkyEdge), robots (AITL-R), etc. |

## Model Overview (Three Layers)

| Layer        | Description                                                    |
|--------------|----------------------------------------------------------------|
| Logic Layer  | State recognition, hypothesis generation, decision-making, constraint reasoning. |
| Control Layer| Signal generation using MPC, PID, and robust control techniques. |
| Physical Layer| Connection with the real world (dynamics, sensors, actuators, noise/disturbance handling). |

## Applications and Use Cases

| Name       | Description                                      |
|------------|-------------------------------------------------|
| AITL-R     | Robot-oriented logic (autonomy, redundancy control, fault prediction). |
| SkyEdge    | Flight control and decision-making for drones.  |
| PoC Manual | Documentation for control design and practical system structures. |

## About This Project

This repository was launched as a re-examination of AI architecture from the perspective of semiconductor device engineering.  
It focuses on concepts such as structural AI design, physical consistency, and fault tolerance,  
offered in the form of theoretical proposals and educational materials.

🔎 **This project is not intended to deliver complete implementations or algorithms.**  
Its focus is on conceptual modeling, learning support, and open proposal sharing.

## Contribution

This project aims to promote concept sharing and educational/research collaboration.  
In the future, we are open to contributions such as:  
- Technical collaboration in implementation, control system design, and robotics  
- Collaborative research based on the AITL architecture  
- Free use of AITL materials for education and instruction (MIT License)

🔧 **Note:** As of now, full implementation and testing environments (e.g., development hardware) are not yet available,  
so technical contributions and research collaborations remain future goals.

👉 CONTRIBUTING.md will be prepared soon to guide collaboration.

## Author & License

- Author/Proposal: Shinichi Samizo  
  M.Sc., Shinshu University / Formerly at Seiko Epson  
  Field of Expertise: Semiconductor Device Engineering

- License: MIT License  
  All concepts and materials in the AITL project are freely available for use, modification, and redistribution under the MIT License.  
  Please retain copyright notices.

GitHub: @samizo-aitl  
Email: shin3t72@gmail.com

---

## 日本語版はこちら → README.md
