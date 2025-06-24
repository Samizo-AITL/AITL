# Communication Specification - AITL Drone (Professional Model)

## 1. Overview

This document specifies the communication architecture and protocols used in the Professional model of the AITL drone, ensuring robust connectivity in urban operational environments.

## 2. Communication Interfaces

| Interface       | Description                                   | Usage                          |
|-----------------|-----------------------------------------------|--------------------------------|
| Wi-Fi (802.11ac)| Primary high-speed communication link         | Telemetry, video streaming     |
| LTE (4G/5G)     | Secondary cellular fallback and remote control| Backup telemetry and command   |
| USB            | External modem or dongle connection             | LTE/5G modem interface         |
| UART / SPI     | Internal sensor and peripheral data lines       | LiDAR, GPS modules             |

## 3. Network Architecture

- Primary connection is via Wi-Fi to ground station or mesh network.
- LTE fallback activates automatically if Wi-Fi signal degrades below threshold.
- Secure VPN tunnels established for telemetry and command channels.
- Future plans include integration of satellite communication for extended range.

## 4. Protocols and Data Formats

- MAVLink protocol for flight control commands.
- ROS2 DDS for internal communication between onboard nodes.
- Video streaming using RTSP over UDP.
- Telemetry data encoded in JSON and sent via MQTT.

## 5. Failover and Redundancy

- Continuous link quality monitoring to trigger automatic switchover.
- Buffering and retransmission for telemetry packets to prevent data loss.
- Watchdog timers to detect communication blackouts and initiate safe mode.

## 6. Security Considerations

- WPA3 encryption for Wi-Fi communication.
- TLS for all remote telemetry and control data.
- Regular key rotation and certificate validation procedures.

## 7. Testing and Validation

- Simulation of network degradation scenarios.
- Field tests in urban canyons and high-interference environments.
- Performance benchmarks for latency and throughput.

---

*Refer to `hardware.md` for modem and antenna specifications and `software.md` for protocol stack implementation.*
