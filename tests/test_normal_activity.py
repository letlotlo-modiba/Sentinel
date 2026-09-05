from simulator.normal_activity import generate_normal_log, generate_logs

def test_single_log_structure():
    log = generate_normal_log()

    required_keys = {"timestamp", "username", "ip", "location", "user_agent", "status"}

    assert set(log.keys()) == required_keys
    assert log["status"] in ["SUCCESS", "FAIL"]

def test_batch_logs():
    logs = generate_logs(10)

    assert len(logs) == 10
    assert all("ip" in log for log in logs)