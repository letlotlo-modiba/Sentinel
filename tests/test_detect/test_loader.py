import pandas as pd
from detect.loader import get_failed_logins

def test_get_failed_logins():
    data = [
        {"timestamp": "2026-01-01 10:00:00", "status": "SUCCESS"},
        {"timestamp": "2026-01-01 10:01:00", "status": "FAIL"},
        {"timestamp": "2026-01-01 10:02:00", "status": "FAIL"},
    ]

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    failed = get_failed_logins(df)

    assert len(failed) == 2
    assert all(failed["status"] == "FAIL")