# Power Specification - AITL Drone (Professional & SkyEdge Models)

## 1. Overview

This document details the power system architecture for AITL drones, focusing on efficient, reliable energy supply to support extended missions and self-repair functions.

## 2. Power Sources

- Primary: 4S LiPo battery pack (14.8V, 6400mAh) with integrated Battery Management System (BMS)
- Secondary (SkyEdge): Hybrid power including solar panels with MPPT (Maximum Power Point Tracking)

## 3. Power Distribution

- DC-DC converters providing stable 5V and 12V rails for compute, sensors, and communication modules
- Redundant power lines to critical components for failover capability
- Power gating controlled via AMS ICs for energy saving

## 4. Monitoring and Protection

- Real-time voltage, current, and temperature monitoring via ADC channels and BMS telemetry
- Over-current, over-voltage, and thermal shutdown protections
- Battery state-of-charge (SoC) estimation algorithms for flight planning

## 5. Charging and Maintenance

- External charging port supporting fast charge protocols
- Safe charging firmware with cell balancing
- Field-replaceable battery modules

## 6. Future Enhancements

- Integration with SystemDK for power diagnostics and management
- Support for alternative energy sources (e.g., hydrogen fuel cells)

---

*See `hardware.md` for physical battery specifications.*
