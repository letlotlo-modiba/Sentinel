import os
from simulator.main import save_logs, build_dataset


def test_save_logs_creates_missing_directory(tmp_path):
    subfolder = tmp_path / "nested" / "logs"
    test_file = subfolder / "test_login_logs.csv"

    sample_logs = [
        {
            "timestamp": "2026-01-01 10:00:00",
            "username": "tester",
            "ip": "192.168.1.10",
            "location": "Johannesburg",
            "user_agent": "Chrome/Linux",
            "status": "SUCCESS"
        }
    ]

    assert not subfolder.exists()
    save_logs(sample_logs, filename=str(test_file))
    assert test_file.exists()
    assert test_file.stat().st_size > 0


def test_build_dataset_custom_normal_count():
    logs = build_dataset(normal_count=30, attacks=[])
    assert len(logs) == 30
    assert all("ip" in log for log in logs)


def test_build_dataset_single_attack():
    logs = build_dataset(normal_count=0, attacks=["brute_force"], target_user="victim")
    assert len(logs) == 12
    assert all(log["username"] == "victim" for log in logs)
    assert all(log["status"] == "FAIL" for log in logs)
