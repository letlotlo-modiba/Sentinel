from detect.alerts import assign_serverity

def test_brute_force_high_severity():
    result = assign_serverity("BRUTE_FORCE", 20)
    assert result == "HIGH"

def test_brute_force_medium_severity():
    result = assign_serverity("BRUTE_FORCE", 12)
    assert result == "MEDIUM"


def test_rotating_attack_medium_severity():
    result = assign_serverity("ROTATING_ATTACK", 11)
    assert result == "MEDIUM"

def test_rotating_attack_low_severity():
    result = assign_serverity("ROTATING_ATTACK", 5)
    assert result == "LOW"


def test_distributed_attack_high_severity():
    result = assign_serverity("DISTRIBUTED_ATTACK", 25)
    assert result == "HIGH"

def test_distributed_attack_medium_severity():
    result = assign_serverity("DISTRIBUTED_ATTACK", 15)
    assert result == "MEDIUM"

# --- Edge Case ---
def test_unknown_alert_type():
    result = assign_serverity("UNKNOWN_ATTACK", 100)
    assert result == "LOW"