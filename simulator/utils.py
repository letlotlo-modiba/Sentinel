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
}