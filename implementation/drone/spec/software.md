# Software Specification - AITL Drone (Professional Model)

## 1. Overview

This document describes the software stack and key modules for the Professional model of the AITL drone, focusing on autonomous flight, AI inference, and sensor integration.

## 2. Operating System

- Ubuntu 22.04 LTS (Jetson JetPack 5.x base)
- Real-time kernel patches applied for deterministic control
- Containerized environments using Docker for modular AI deployment

## 3. Middleware

- ROS 2 Humble Hawksbill
- AITL middleware core modules for inference and control abstraction
- DDS (Data Distribution Service) for inter-node communication

## 4. AI Inference Modules

- YOLOv8-based object detection and damage classification models
- TensorRT optimized models for real-time onboard inference
- CNN-based terrain analysis for autonomous navigation support

## 5. Flight Control Software

- ROS2-native flight controller nodes integrated with PX4 firmware
- PID and waypoint navigation control algorithms
- Manual override and safety interlocks implemented at software level

## 6. Sensor Data Processing

- Sensor fusion nodes aggregating IMU, GPS, LiDAR, and camera data
- Kalman filter and Bayesian estimators for state estimation
- Real-time environmental mapping for obstacle avoidance

## 7. Diagnostics and Logging

- Event-driven logging framework capturing sensor and actuator states
- Health monitoring services triggering alerts on anomaly detection
- Remote telemetry uplink over Wi-Fi / LTE

## 8. Development and Deployment

- CI/CD pipelines using GitHub Actions for continuous integration
- Automated testing with hardware-in-the-loop (HIL) simulators
- OTA updates supported via secure channels

## 9. Future Enhancements

- Integration with SystemDK for educational PoC evaluation
- Expansion of AI models to include semantic segmentation
- Advanced self-repair software logic incorporating meta-control loops

---

*Refer to `hardware.md` for physical interfaces and `communication.md` for network specifications.*
