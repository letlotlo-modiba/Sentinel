# --- Brute Force Detection ---
def detect_brute_force(df, threshold=10, window="2min"):
    df = df.set_index("timestamp")

    grouped = df.groupby("ip")["status"].rolling(window).count().reset_index()

    alerts = grouped[grouped["status"] > threshold]

    return alerts


# --- Rotating IP Attack ---
def detect_rotating_attack(df, threshold=12, window="3min"):
    """Detects patterns across small pools targeting same user"""

    df = df.set_index("timestamp")

    grouped = df.groupby("username")["status"].rolling(window).count().reset_index()

    alerts = grouped[grouped["status"] > threshold]

    return alerts


# --- Distributed Attack (botnet) ---
def detect_distributed_attack(df, threshold=20, window="5min"):
    df = df.set_index("timestamp")

    grouped = df.groupby("username")["status"].rolling(window).count().reset_index()

    alerts = grouped[grouped["status"] > threshold]

    return alerts