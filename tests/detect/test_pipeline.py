"""
Controlled dataset - deterministic logs
"""
import pandas as pd
from detect.main import run_detection

def create_test_logs():
    data = []

    # Brute force
    for i in range(12):
        data.append({
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "admin",
            "ip": "1.1.1.1",
            "location": "Unknown",
            "user_agent": "Firefox/Linux",
            "status": "FAIL"
        })

    # Distributed attack
    for i in range(25):
        data.append({
            "timestamp": f"2026-01-01 10:10:{i:02d}",
            "username": "admin",
            "ip": "1.1.1.1",
            "location": "Unknown",
            "user_agent": "Firefox/Linux",
            "status": "FAIL"
        })

    return pd.DataFrame(data)


# --- INTEGRATION TESTING ---
def test_full_pipeline_detection():
    df = create_test_logs()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = run_detection(df)

    assert len(alerts) > 0


def test_alert_types_present():
    df = create_test_logs()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = run_detection(df)

    types = {alert["type"] for alert in alerts}

    assert "BRUTE_FORCE" in types
    assert "DISTRIBUTED_ATTACK" in types


def test_alerts_have_severity():
    df = create_test_logs()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = run_detection(df)

    for alert in alerts:
        assert "severity" in alert
        assert alert["severity"] in ["LOW", "MEDIUM", "HIGH"]


def test_no_false_alerts_on_clean_data():
    data = []

    for i in range(5):
        data.append({
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "lesedi",
            "ip": "1.1.1.1",
            "location": "Unknown",
            "user_agent": "Chrome",
            "status": "FAIL"
        })

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = run_detection(df)

    assert len(alerts) == 0