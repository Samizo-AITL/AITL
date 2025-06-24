# Common PoC Evaluation Specifications - AITL Drone Models

## 1. Purpose

This document defines the common evaluation metrics and templates used across multiple AITL drone PoC models (Professional, SkyEdge) to ensure standardized testing and comparability.

## 2. Evaluation Metrics

| Metric                     | Description                                    | Target / Threshold            |
|----------------------------|------------------------------------------------|------------------------------|
| Inference Latency          | Time from sensor input to AI output             | < 150 ms                     |
| Flight Stability           | GPS/IMU-based position drift during hover       | < ±0.5 m                     |
| Fault Recovery Time        | Time to detect and recover from actuator/sensor faults | < 300 ms                     |
| Communication Uptime       | Percentage of time communication is active      | > 99.9%                      |
| Flight Duration            | Total operational flight time                    | > 25 min (Professional), > 2 hours (SkyEdge) |
| Power Consumption          | Energy used per mission                           | < 80 Wh                      |

## 3. Test Environments

- Urban test sites for Professional model
- Open fields and harsh environments for SkyEdge model
- Simulation scenarios with fault injection

## 4. Reporting Templates

- Flight logs summary
- AI inference accuracy report
- Fault injection and recovery logs
- Communication quality report

## 5. Tools and Platforms

- SystemDK integration for data collection and analysis
- HIL simulators for automated testing
- Remote telemetry dashboards

---

*Refer to individual PoC specification files for model-specific details.*
