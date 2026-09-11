def assign_serverity(alert_type, count):
    if alert_type == "BRUTE_FORCE":
        return "HIGH" if count > 15 else "MEDIUM"

    if alert_type == "ROTATING_ATTACK":
        return "MEDIUM" if count > 10 else "LOW"

    if alert_type == "DISTRIBUTED_ATTACK":
        return "HIGH" if count > 20 else "MEDIUM"

    return "LOW"

def format_alerts(df, alert_type):
    alerts = []

    for _, row in df.iterrows():
        count = row.get("status", 0)

        alerts.append({
            "type": alert_type,
            "severity": assign_serverity(alert_type, count),
            "timestamp": row["timestamp"],
            "ip": row.get("ip", None),
            "username": row.get("username", None),
          #  "details": row.to_dict()
        })

    return alerts