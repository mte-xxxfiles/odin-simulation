# 📱 Odin Flashing & Device Simulation Suite (v1.0-Beta)

An advanced, interactive Python-based desktop simulator that emulates **Samsung Odin3 Professional** firmware installer and modern **Galaxy S-Series (up to S26 Ultra)** download interfaces. 

> ⚠️ **RELEASE NOTE:** This project is currently in **Beta**. Minor visual bugs and log delays may occur. Stable production builds are planned for future updates.

---

## 🚀 Beta Features

- **Dynamic Device Selector:** Switch between multiple flagship models including `Galaxy S24 FE`, `S25+`, `S26 Ultra`, and `Z Fold7`.
- **Realistic Telemetry Engine:** Live simulation of CPU Temperatures, Fan Speeds (RPM), and data block transmission (MB).
- **Intelligent Time-Weights:** Large partitions like `SYSTEM` (6.4 GB) and `USERDATA` (12.8 GB) take significantly longer to stage and write compared to smaller blocks.
- **Android Optimization Loop:** Replicates the Knox-secured reboot sequence followed by the classic "*Optimizing apps...*" Android boot animation.
- **Ultra-Compact Syntax Mapped:** Highly optimized layout pattern avoiding horizontal overflows on GitHub code viewers.

---

## 🛠️ How to Run

### Prerequisites
Make sure you have Python 3.10 or higher installed on your operating system.

### Steps
1. Clone this repository or copy the content of `odin.py`.
2. Fire up your terminal or PowerShell and execute:
   ```bash
   python odin.py
   ```
3. Choose a **Target Device** from the dropdown list.
4. Click on **BL, AP, CP, or CSC** buttons to queue files.
5. Hit **START FLASH** to run the simulator!

---

## 📝 Roadmap & Known Issues (Beta 1)
- [ ] Fixed alignment issue on certain lower display scales.
- [ ] Add real local file-copy operations (Simulated to Real bridge).
- [ ] Custom `.ico` integration fallback stability.

---

## 📜 License
This software is intended strictly for simulation and educational entertainment. It does not communicate with or modify real smartphone hardware partition blocks.
