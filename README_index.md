# AITL - All-in-Theory Logic  
## 📘 Top Index for Theory, Implementation, Spec, and PoC

🌐 **English Overview**

AITL (All-in-Theory Logic) is a multi-layered AI framework integrating logic-based reasoning, control theory, and physical modeling.  
This repository provides a complete architecture from theory (v1.0) to implementation (v2.0), with specifications and proof-of-concept designs.

---

## 📂 Repository Structure

| Directory | Content | Description |
|----------|---------|-------------|
| [`theory/`](./theory/) | 📘 **AITL Core Theory** | Logic, Control, and Physical layer models (v1.0) |
| [`implementation/`](./implementation/) | 💻 **AITL Implementations** | AITL-R (robotics), SkyEdge (drone), etc. (v2.0) |
| [`spec/`](./spec/) | 📑 **Specifications** | Interface, protocol, and integration specs |
| [`poc/`](./poc/) | 🧪 **Proof of Concept** | Application-level testing and demonstrations |

---

## 🧠 Theory Highlights

Theoretical architecture is organized into three core layers:

| Layer | Subfolder | Topics |
|-------|-----------|--------|
| Logic Layer | [`theory/logic_layer/`](./theory/logic_layer/) | Belief updating, constraint logic, causal inference |
| Control Layer | [`theory/control/`](./theory/control/) | MPC, PID, robust control, digital control |
| Physical Layer | [`theory/physical_layer/`](./theory/physical_layer/) | Kinematics, sensors, actuators, disturbances |

📘 Entry Point → [`theory/README.md`](./theory/README.md)

---

## 🛠 Implementation Projects (v2.0)

| Project | Path | Description |
|---------|------|-------------|
| AITL-R | [`implementation/robotics/`](./implementation/robotics/) | Logic + Control + Physical integration in robotics |
| SkyEdge | [`implementation/drone/`](./implementation/drone/) | Drone control and decision architecture |
| Communication & Diagnostics | [`implementation/communication.md`](./implementation/communication.md) | Core messaging and status interface |

---

## 📑 Spec and Interface

| Document | Purpose |
|----------|---------|
| [`spec/control_interface.md`](./spec/control_interface.md) | Actuator & sensor interface definitions |
| [`spec/fault_handling.md`](./spec/fault_handling.md) | Error propagation and self-repair protocol |
| [`spec/logic_runtime.md`](./spec/logic_runtime.md) | Execution model for inference modules |

---

## 🧪 PoC Examples

| Case | Path | Description |
|------|------|-------------|
| Simulation: Multi-agent recovery | [`poc/multiagent_recovery.md`](./poc/multiagent_recovery.md) | Logical recovery from multi-agent faults |
| Drone route replanning | [`poc/drone_path.md`](./poc/drone_path.md) | Environmental adaptation using physical + control logic |
| Robot diagnostic mode | [`poc/diagnostics.md`](./poc/diagnostics.md) | Sensor degradation and fallback mode activation |

---

## 📚 Contribution and Development

- Author: **Shinichi Samizo** (三溝 真一)  
- License: [MIT License](./LICENSE)  
- Contributions welcome: Please fork, improve, or open issues

---

## 🔗 Related Platforms

- Zenn (theory summaries): _coming soon_  
- OpenSim-AITL: *experimental physics + AITL interface simulator*  
- Education Project: [`edusemi`](https://github.com/your-org/edusemi)

---

## 🏁 Entry Point for Readers

To begin exploring the AITL architecture:

👉 Start with the [theory overview](./theory/README.md)  
👉 Then navigate to [implementation/](./implementation/) for real-world designs  
👉 Use [spec/](./spec/) to align system integration  
👉 Try [poc/](./poc/) for applied use-cases and simulation

---
