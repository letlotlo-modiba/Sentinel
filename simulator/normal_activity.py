import random
try:
    from simulator.utils import generate_ip, now, USER_AGENTS, IP_LOCATION
except ImportError:
    from utils import generate_ip, now, USER_AGENTS, IP_LOCATION


USERS = ["letlotlo", "lesedi", "nathan", "admin", "guest"]

def generate_normal_log():
    ip = random.choice(list(IP_LOCATION.keys()))
    return {
        "timestamp": now(),
        "username": random.choice(USERS),
        "ip": ip,
        "location": IP_LOCATION[ip],
        "user_agent": random.choice(USER_AGENTS),
        "status": random.choices(["SUCCESS", "FAIL"], weights=[0.85, 0.15])[0]
    }

def generate_logs(n=100):
    return [generate_normal_log() for _ in range(n)]