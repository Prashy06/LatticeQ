import numpy as np
import time
import random


THRESHOLD = 0.55

event_log = []
start_time = time.time()

def ts():
    return time.strftime("%H:%M:%S")

def simulate_features(mode):
    if mode == "threat":
        byte_rate = random.uniform(6.5, 8.5)
        spike = random.uniform(1.2, 1.8)
    else:
        byte_rate = random.uniform(5.8, 6.6)
        spike = random.uniform(0.2, 0.5)

    z_score = (byte_rate - 6.3) / 0.4

    return np.array([byte_rate, z_score, spike])

def autoencoder_loss(x):
    # simple reconstruction approximation
    return abs(x[2])

def compute_risk(loss):
    return min(int((loss / THRESHOLD) * 50), 100)

def get_state(loss):
    if loss > THRESHOLD * 1.4:
        return "CRITICAL"
    elif loss > THRESHOLD:
        return "SUSPICIOUS"
    else:
        return "NORMAL"

def log_event(level, msg):
    event_log.append({
        "time": ts(),
        "level": level,
        "msg": msg
    })

def get_dashboard_metrics(mode):

    features = simulate_features(mode)
    loss = autoencoder_loss(features)
    risk = compute_risk(loss)
    state = get_state(loss)
    deviation = int((loss / THRESHOLD) * 100)

    if state == "CRITICAL":
        log_event("crit", "Neural anomaly detected")
        log_event("warn", "SOAR edge block executed")
        log_event("info", "Kyber-768 PQC channel secured")

    elif state == "SUSPICIOUS":
        log_event("warn", "Behavioral deviation detected")

    else:
        log_event("ok", "Traffic within baseline")

    return {
        "loss": float(loss),
        "risk": risk,
        "deviation": deviation,
        "state": state,
        "threshold": THRESHOLD,
        "events": event_log[-50:]  # limit log size
    }