import random
try:
    from simulator.utils import generate_ip, now
except ImportError:
    from utils import generate_ip, now


# --- Brute Force Attack ---
def brute_force_attack():
    attacker_ip = generate_ip()
    return [{
        "timestamp": now(),
        "username": "admin",
        "ip": attacker_ip,
        "location": "Unknown",
        "user_agent": "Firefox/Linux",
        "status": "FAIL"
    }
    for _ in range(12)
    ]


# --- Rotating IP Attack ---
def rotating_attack():
    attacker_ips = [generate_ip() for _ in range(3)]

    logs = []

    for _ in range(18):
        logs.append({
            "timestamp": now(),
            "username": "admin",
            "ip": random.choice(attacker_ips),
            "location": "Unknown",
            "user_agent": "Firefox/Linux",
            "status": "FAIL"
        })

    return logs


# --- Distributed Attack (botnet) ---
def distributed_attack():
    logs = []

    for _ in range(25):
        logs.append({
            "timestamp": now(),
            "username": "admin",
            "ip": generate_ip(),
            "location": "Unknown",
            "user_agent": "Firefox/Linux",
            "status": "FAIL"  
        })

    return logs