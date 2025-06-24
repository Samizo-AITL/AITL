# Hardware Specification - AITL Robot (AITL-R Model)

## 1. Overview

This document outlines the hardware components and architecture of the AITL-R robot model, focusing on mixed-signal AMS/LDMOS SoCs integration for robust autonomous control.

## 2. Major Components

| Module            | Process         | Main Function                              |
|-------------------|-----------------|--------------------------------------------|
| 65nm AI SoC       | 65nm CMOS       | Cortex-M7 MPU, CNN Core, eFPGA, I/F control |
| AMS Control IC    | 0.18µm AMS      | ADC/DAC, Bandgap, LDO, power management     |
| CMOS I/O IC       | 0.18µm CMOS     | SPI/I²C control, external sensor I/F, GPIO  |
| HV Control IC     | 0.18µm SOI      | High-voltage switch control, isolated drive |
| Driver IC         | 0.35µm LDMOS    | High-voltage actuator drive (48V/500mA)     |

## 3. Interfaces

- SPI, I²C buses for sensor and peripheral communication
- GPIO pins for actuator and status signals
- High-voltage isolated drivers for actuators
- Power rails stabilized and monitored by AMS ICs

## 4. Physical Integration Notes

- Modular board stacking for scalable sensor and actuator expansion
- Shielding and isolation for noise-sensitive analog circuits
- Thermal management considerations for power ICs

## 5. Power Supply

- Battery-powered with regulated DC-DC converters
- Power sequencing controlled by AMS IC

---

*Refer to `software.md` and `systemdk_integration.md` for related software and system integration details.*
