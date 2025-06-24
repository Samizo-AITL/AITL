# AITL Drone - Professional Model (PoC Specification)

## 1. Objective

The Professional model of AITL Drone aims to validate core inference-control-physical integration with limited autonomy for urban missions. This PoC targets semi-autonomous deployment with real-time AI inference and sensor-based control for structural inspection and disaster assessment.

## 2. Use Case Scenarios

- Bridge and high-rise building inspection
- Urban disaster evaluation (post-earthquake, fire, flood)
- Road/utility pole monitoring
- Edge inference for on-site analysis

## 3. Core Components

### Hardware

- **Frame**: Custom 4-rotor drone (1–5kg class)
- **Compute**: NVIDIA Jetson Orin Nano
- **Sensors**:
  - 4K RGB camera (HDR support)
  - LiDAR (Livox Mid-70)
  - Thermal camera (IR)
  - GPS + RTK module
  - IMU (9-axis with magnetometer)

### AITL Mapping

| AITL Layer           | Implementation                                 |
|----------------------|------------------------------------------------|
| Inference Layer      | YOLOv8-based defect detection, RT terrain analysis |
| Control Layer        | ROS2-based flight controller (PID/waypoint system) |
| Physical Integration | Sensor fusion with IMU/LiDAR for stable flight |
| Self-Repair Layer    | Fault detection, mode switching, emergency stop logic |

## 4. Software Stack

- **OS**: Ubuntu 22.04 + JetPack
- **Middleware**: ROS2 Humble + AITL middleware core
- **AI Models**: Object detection / damage classification (custom-trained)
- **Flight Logic**: Waypoint planner + manual override support
- **Diagnostics**: Onboard event logging + telemetry uplink

## 5. Key Features

- Real-time damage inference (onboard)
- Failover: switch to manual or return-to-home
- Hover stability in light wind (<±5cm drift)
- Communication fallback (Wi-Fi → LTE)

## 6. Evaluation Metrics

| Metric                             | Target Value       |
|------------------------------------|--------------------|
| Inference latency                  | <150 ms (YOLOv8)   |
| Hovering position error (GPS)      | <0.5 m             |
| Fault recovery time (motor/sensor) | <300 ms            |
| Flight time                        | ~25 minutes        |
| Power consumption per mission      | <80Wh              |

## 7. Roadmap

| Phase | Milestone                                | Timeline |
|-------|------------------------------------------|----------|
| P1    | Hardware assembly + flight stability test | 2025 Q3  |
| P2    | AITL integration + sensor fusion test     | 2025 Q4  |
| P3    | Field testing in urban environment        | 2026 Q1  |

---

*For module-level specifications, refer to `spec/` folder.*
