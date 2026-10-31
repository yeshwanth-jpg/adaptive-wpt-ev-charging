# Adaptive Wireless Power Transfer (WPT) EV Charging System

## 📌 Project Overview
A high-efficiency wireless power transfer system designed for Electric Vehicles (EVs), featuring closed-loop adaptive impedance matching and dynamic frequency tuning to maintain optimal energy transfer efficiency despite varying air gaps and lateral misalignments.

## ⚙️ Key Technical Features
* **Closed-Loop Frequency Tuning:** Implements dynamic control algorithms to counteract detuning effects caused by spatial misalignments between primary and secondary coils.
* **Coupling & Efficiency Estimation:** Real-time calculation of magnetic coupling coefficients ($k$) and mutual inductance to optimize power converter operation.
* **Inverter Control Logic:** Regulates primary-side DC/AC inverter switching parameters (phase-shift / duty cycle) to match target power profiles under shifting load conditions.

## 🛠️ Tech Stack
* **Control Core:** Python (Closed-loop state estimation and optimization)
* **Power Electronics Theory:** Magnetic resonance, inductive coupling, LCC-S compensation topologies
* **Standards Reference:** SAE J2954 (Wireless Power Transfer for Light-Duty Plug-in Electric Vehicles)

## 📊 Performance Metrics
* **Operating Frequency:** Tuned around the 85 kHz ISM band standard.
* **Efficiency Optimization:** Maintains $>88\%$ end-to-end DC-to-DC efficiency across standard parking misalignments ($\pm 75\,\text{mm}$).
