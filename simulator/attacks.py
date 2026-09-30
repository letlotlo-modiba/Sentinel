import random
try:
    from simulator.utils import generate_ip, now, get_ip_location
except ImportError:
    from utils import generate_ip, now, get_ip_location


# --- Brute Force Attack ---
def brute_force_attack(count=12, username="admin", ip=None, location=None):
    attacker_ip = ip or generate_ip()
    loc = location if location is not None else get_ip_location(attacker_ip)
    return [{
        "timestamp": now(),
        "username": username,
        "ip": attacker_ip,
        "location": loc,
        "user_agent": "Firefox/Linux",
        "status": "FAIL"
    }
    for _ in range(count)
    ]


# --- Rotating IP Attack ---
def rotating_attack(count=18, ip_pool_size=3, username="admin", location=None):
    attacker_ips = [generate_ip() for _ in range(ip_pool_size)]

    logs = []

    for _ in range(count):
        ip = random.choice(attacker_ips)
        loc = location if location is not None else get_ip_location(ip)
        logs.append({
            "timestamp": now(),
            "username": username,
            "ip": ip,
            "location": loc,
            "user_agent": "Firefox/Linux",
            "status": "FAIL"
        })

    return logs


# --- Distributed Attack (botnet) ---
def distributed_attack(count=25, username="admin", location=None):
    logs = []

    for _ in range(count):
        ip = generate_ip()
        loc = location if location is not None else get_ip_location(ip)
        logs.append({
            "timestamp": now(),
            "username": username,
            "ip": ip,
            "location": loc,
            "user_agent": "Firefox/Linux",
            "status": "FAIL"  
        })

    return logs