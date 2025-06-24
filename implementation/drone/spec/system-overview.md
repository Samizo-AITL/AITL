# System Overview - AITL Drone (Professional Model)

## Purpose

This document outlines the system-level architecture of the Professional drone model implementing the AITL framework, mapping the theory’s four-layer design onto a practical, urban-use drone.

## AITL 4-Layer Mapping

| AITL Layer         | Description |
|--------------------|-------------|
| Inference Layer    | Onboard image recognition and structural damage classification using lightweight AI models (YOLOv8). |
| Control Layer      | Navigation and flight stability logic implemented via ROS2 and PID-based waypoint control. |
| Physical Integration | Sensor fusion from GPS, IMU, and LiDAR to ensure stable autonomous flight. |
| Self-Repair Layer  | Monitoring subsystems to detect sensor/motor failures and switch to safe modes or return-home fallback. |

## Mission Profile

- **Flight Time**: ~25 minutes
- **Max Altitude**: 120 meters (regulatory limit)
- **Payload**: 1–2 kg
- **Autonomy**: Assisted (autonomous + manual override)
- **Communication**: Wi-Fi (primary), LTE (backup)

## Component Layers

- **Sensing**: RGB + IR Camera, LiDAR, GPS, IMU
- **Compute**: Jetson Orin Nano (Edge AI)
- **Control**: ROS2 flight stack, AITL middleware
- **Energy**: 4S LiPo battery (6400mAh), BMS monitored

## Operation Modes

- Manual / Assisted / Autonomous
- Emergency landing / return-to-home
- Diagnostic + telemetry mode

---

*See `hardware.md` for component-level details.*
