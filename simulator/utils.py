import random
from datetime import datetime

# --- IP Generator ---
def generate_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

# --- Timestamp Generator ---
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- User Agents Pool ---
USER_AGENTS = [
    "Chrome/Windows",
    "Firefox/Linux",
    "Safari/iPhone",
    "Edge/Windows",
    "Chrome/Android"
]

# --- IP -> Location Mapping ---
IP_LOCATION = {
    "192.168.1.10": "Johannesburg",
    "192.168.1.43": "Cape Town",
    "192.168.1.15": "Durban",
    "192.168.1.88": "Pretoria",
    "192.168.1.102": "Port Elizabeth",
}

# --- Known External Threat Locations ---
THREAT_LOCATIONS = [
    "Moscow",
    "Beijing",
    "Bucharest",
    "St. Petersburg",
    "Sao Paulo",
    "Frankfurt",
    "Unknown"
]

def get_ip_location(ip):
    """Resolve location for an IP address, falling back to realistic threat origins."""
    if ip in IP_LOCATION:
        return IP_LOCATION[ip]
    # Simple deterministic hash to consistently assign location to same IP
    idx = sum(int(octet) for octet in ip.split(".") if octet.isdigit()) % len(THREAT_LOCATIONS)
    return THREAT_LOCATIONS[idx]