# Hardware Specification - AITL Drone (Professional Model)

## 1. Overview

This document details the hardware components used in the Professional model drone for AITL-based PoC deployment. The platform emphasizes modularity, real-time inference capability, and robust sensing for urban mission scenarios.

## 2. Major Components

| Component        | Specification                                      |
|------------------|----------------------------------------------------|
| **Frame**        | 4-rotor quadcopter (carbon composite, 1–5kg)       |
| **Compute Unit** | NVIDIA Jetson Orin Nano (8GB, 20TOPS)              |
| **Camera**       | 4K HDR RGB camera (USB 3.0, rolling shutter)       |
| **LiDAR**        | Livox Mid-70 (Mid-range, 70m, 100k pts/s)          |
| **Thermal Camera** | FLIR Lepton 3.5 (IR spectrum, I²C/SPI interface) |
| **GPS**          | RTK module (u-blox ZED-F9P or similar)             |
| **IMU**          | 9-axis IMU with magnetometer (Bosch BMI088 or similar) |
| **Barometer**    | Integrated in flight controller                     |
| **Battery**      | 4S LiPo (14.8V, 6400mAh), BMS-monitored            |
| **Power Unit**   | DC-DC converter (5V / 12V rails)                   |
| **Flight Controller** | PX4 or Ardupilot compatible unit              |
| **Wireless Comm**| Dual-band Wi-Fi + LTE (USB dongle or embedded)    |

## 3. Interfaces

| Module              | Interface      |
|---------------------|----------------|
| Camera              | USB 3.0        |
| LiDAR               | UART / CAN     |
| Thermal camera      | I²C / SPI      |
| GPS                 | UART (NMEA)    |
| IMU                 | SPI / I²C      |
| Battery monitoring  | ADC (via BMS)  |

## 4. Physical Integration Notes

- Camera and thermal units are mounted forward-facing with vibration damping.
- LiDAR is top-mounted for better vertical visibility in urban environments.
- Antennas (GPS, LTE) are mounted on vibration-isolated pylons.
- Weight budget allows for additional payload (~500g margin).

## 5. Optional Expansions

- **Secondary compute**: Coral TPU via USB (for redundancy)
- **Edge storage**: NVMe SSD via M.2 slot on Jetson carrier board
- **Secondary sensors**: Air quality, audio, magnetic field probes (experimental)

---

*See `software.md` and `communication.md` for integration and protocols.*
