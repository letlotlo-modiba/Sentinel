def format_alerts(df, alert_type):
    alerts = []

    for _, row in df.iterrows():
        alerts.append({
            "type": alert_type,
            "timestamp": row["timestamp"],
            "details": row.to_dict()
        })

    return alerts