import pandas as pd
from detect.alerts import assign_severity, assign_serverity
from detect.main import run_detection


def test_assign_severity_alias():
    # Both names should return identical outputs
    assert assign_severity("BRUTE_FORCE", 20) == assign_serverity("BRUTE_FORCE", 20) == "HIGH"
    assert assign_severity("ROTATING_ATTACK", 5) == assign_serverity("ROTATING_ATTACK", 5) == "LOW"


def test_custom_detection_thresholds():
    # Create 8 failed attempts (below default threshold of 10)
    data = [
        {
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "admin",
            "ip": "10.0.0.1",
            "location": "Unknown",
            "user_agent": "TestAgent",
            "status": "FAIL",
        }
        for i in range(8)
    ]
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Default threshold (10) -> no alert
    alerts_default = run_detection(df, bf_threshold=10)
    assert len([a for a in alerts_default if a["type"] == "BRUTE_FORCE"]) == 0

    # Lower threshold (5) -> alert triggered
    alerts_low = run_detection(df, bf_threshold=5)
    bf_alerts = [a for a in alerts_low if a["type"] == "BRUTE_FORCE"]
    assert len(bf_alerts) > 0
