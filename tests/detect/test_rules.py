import pandas as pd
from detect.rules import detect_brute_force, detect_rotating_attack, detect_distributed_attack

def test_detect_brute_force():
    data = []

    for i in range(12):
        data.append({
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "admin",
            "ip": "1.1.1.1",
            "status": "FAIL"
        })

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = detect_brute_force(df, threshold=10, window="2min")

    assert not alerts.empty


def test_detect_rotating_attack():
    data = []
    ips = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]

    for i in range(18):
        data.append({
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "admin",
            "ip": ips[i % 3],
            "status": "FAIL"
        })

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = detect_rotating_attack(df, threshold=12, window="3min")

    assert not alerts.empty


def test_detect_distributed_attack():
    data = []

    for i in range(25):
        data.append({
            "timestamp": f"2026-01-01 10:00:{i:02d}",
            "username": "admin",
            "ip": f"192.168.1.{i}",
            "status": "FAIL"
        })

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    alerts = detect_distributed_attack(df, threshold=20, window="5min")

    assert not alerts.empty
