# LatticeQ
LatticeQ - Edge AI Behavioural Network Detection and Automated Response with Post-Quantum Cryptographic Protection on AMD Zynq UltraScale+ ZCU102
## Edge-Based AI-Powered Network Detection & Autonomous Response System

Campus AI-NDR is an edge-deployed autonomous Network Detection and Response (NDR) system that uses neural anomaly detection and post-quantum secure signaling to detect and contain network threats in real time.

The system operates fully at the edge using a lightweight AI inference engine and provides a live dashboard for monitoring behavioral deviations, threat escalation, and automated containment actions.

# 1. Overview

Traditional NDR systems rely heavily on rule-based detection and cloud-dependent analytics. These approaches suffer from signature dependence, delayed response cycles, and limited resilience against zero-day attacks.

Campus AI-NDR replaces static detection logic with behavioral manifold learning using an Autoencoder model trained exclusively on baseline traffic. The system detects anomalies based on reconstruction error rather than predefined signatures.

The result is an edge-native, autonomous, adaptive defense node.

---

# 2. Core Objectives

- Detect behavioral anomalies using neural reconstruction error
- Quantify threat levels using an adaptive risk index
- Trigger autonomous containment using a SOAR-style engine
- Secure response signaling with simulated post-quantum cryptography
- Provide real-time visualization via a hardened dashboard
- Operate without cloud dependency

---

# 3. System Architecture

## High-Level Flow


Network Traffic
↓
Feature Extraction Engine
↓
Autoencoder Inference
↓
Reconstruction Error
↓
Risk Scoring Engine
↓
State Decision Logic
↓
PQC Secure Signaling
↓
SOAR Containment Engine
↓
Live Dashboard


The entire pipeline runs locally on the edge node.

---

# 4. AI Detection Model

## 4.1 Feature Representation

Each traffic sample is encoded into behavioral features such as:

- Byte rate deviation
- Statistical Z-score
- Burst intensity pattern

These features describe behavioral patterns rather than packet signatures.

---

## 4.2 Autoencoder-Based Anomaly Detection

The Autoencoder is trained on normal traffic only.

During inference:

- Normal behavior → low reconstruction loss
- Abnormal behavior → high reconstruction loss

The reconstruction error is treated as anomaly magnitude.

---

## 4.3 Risk Index Calculation

The Threat Risk Index is derived from reconstruction loss:


Risk Index = (Loss / Threshold) × 50


The value is clipped between 0 and 100.

System states are determined as:

- NORMAL → loss below threshold
- SUSPICIOUS → loss slightly above threshold
- CRITICAL → loss significantly above threshold

---

# 5. Autonomous Escalation Engine

The system operates in three operational states:

### NORMAL
- Passive monitoring
- PQC channel ready
- No containment action

### SUSPICIOUS
- Elevated behavioral deviation
- Increased monitoring
- No immediate block

### CRITICAL
- Confirmed anomaly
- Post-quantum secure channel activated
- Automated edge block triggered
- Attacker IP quarantined
- Incident logged

Containment is automatic and requires no manual SOC intervention.

---

# 6. Post-Quantum Secure Channel

The system simulates Kyber-768 post-quantum encryption to secure containment commands.

Purpose:

- Protect SOAR signaling
- Prevent spoofed response injection
- Future-proof response integrity against quantum-capable adversaries

This ensures secure orchestration of defensive actions.

---

# 7. SOAR Integration

When CRITICAL state is triggered:

1. Secure signaling channel activates
2. SOAR policy validation occurs
3. Edge firewall rule applied
4. Attacker IP quarantined
5. Incident counter updated
6. Event logged in dashboard

The containment cycle is fully automated.

---

# 8. Dashboard Layer

The frontend provides a real-time operational view of the edge node.

### Displayed Metrics

- Threat Risk Index (0–100)
- Behavioral Deviation Percentage
- Reconstruction Error vs Threshold (Live Chart)
- Network State
- PQC Channel Status
- SOAR Action Status
- Incident Counter
- Append-only Event Log

The dashboard polls the backend every 2 seconds using a REST endpoint.

---

# 9. Technical Stack

Backend:
- Python 3.11
- Flask
- NumPy

Frontend:
- HTML5
- CSS (Dark-mode hardened UI)
- Chart.js

Architecture:
- REST-based polling
- State-driven logic engine
- Append-only logging model
- Watchdog mechanism for backend failure detection

---

# 10. File Structure


campus_aindr/
│
├── app.py
├── ndr_engine.py
├── ae_weights.npy
├── requirements.txt
│
├── templates/
│ └── index.html
│
└── README.md


---

# 11. Installation

### Step 1 — Install dependencies


pip install -r requirements.txt


### Step 2 — Run the application


python app.py


### Step 3 — Access dashboard


http://localhost:5000


or


http://<your-device-ip>:5000


---

# 12. Edge Deployment Model

Designed for Zynq UltraScale+ or similar edge platforms.


Campus LAN
↓
Edge AI Defense Node
├── AI Inference Engine
├── PQC Module
├── SOAR Engine
└── Dashboard Server


Advantages:

- Zero cloud dependency
- Low latency detection
- Hardware acceleration ready
- Autonomous containment

---

# 13. Security Characteristics

- Behavioral anomaly detection
- Adaptive thresholding
- Autonomous containment
- Post-quantum secure signaling simulation
- Real-time visualization
- Session-based incident tracking
- Backend watchdog protection

---

# 14. Future Enhancements

- Real packet capture integration
- FPGA-based inference acceleration
- True Kyber cryptographic implementation
- Distributed edge mesh network
- Federated anomaly learning
- Persistent incident database

---

# 15. Research Positioning

Campus AI-NDR demonstrates how:

Neural behavioral modeling + edge-native inference + post-quantum secure response + autonomous SOAR orchestration

can form a next-generation decentralized security architecture.

It bridges:

- AI-based IDS
- Edge computing
- Post-quantum security
- Autonomous cyber defense systems

---

# License

Academic / Research Prototype
