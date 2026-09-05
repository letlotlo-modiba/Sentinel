from simulator.attacks import brute_force_attack, rotating_attack, distributed_attack

def test_brute_force_same_ip():
    logs = brute_force_attack()

    ips = {log["ip"] for log in logs}

    # logs must use same IP
    assert len(ips) == 1
    assert len(logs) == 12


def test_rotating_attack_variation():
    logs = rotating_attack()

    ips = {log["ip"] for log in logs}

    # should have more than 1 IP
    assert len(ips) >= 1
    assert len(logs) == 18

def test_distributed_attack_many_ips():
    logs = distributed_attack()

    ips = {log["ip"] for log in logs}

    # high variability expected
    assert len(ips) > 10
    assert len(logs) == 25