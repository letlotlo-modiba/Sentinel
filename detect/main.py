import argparse
import json
from detect.loader import load_logs, get_failed_logins
from detect.rules import (
    detect_brute_force,
    detect_rotating_attack,
    detect_distributed_attack
)
from detect.alerts import format_alerts

def run_detection(df=None, file_path="./data/login_logs.csv", bf_threshold=10, rotating_threshold=12, dist_threshold=20):
    if df is None:
        df = load_logs(file_path=file_path)
    failed = get_failed_logins(df)

    alerts = []

    brute_force = detect_brute_force(failed, threshold=bf_threshold)
    alerts += format_alerts(brute_force, "BRUTE_FORCE")

    rotating = detect_rotating_attack(failed, threshold=rotating_threshold)
    alerts += format_alerts(rotating, "ROTATING_ATTACK")

    distributed = detect_distributed_attack(failed, threshold=dist_threshold)
    alerts += format_alerts(distributed, "DISTRIBUTED_ATTACK")

    return alerts

def parse_args():
    parser = argparse.ArgumentParser(
        description="Sentinel Threat Detection Engine"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="./data/login_logs.csv",
        help="Path to login logs CSV file (default: ./data/login_logs.csv)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Output alerts as raw JSON",
    )
    parser.add_argument(
        "--threshold-bf",
        type=int,
        default=10,
        help="Brute force threshold (failed attempts per IP, default: 10)",
    )
    parser.add_argument(
        "--threshold-rotating",
        type=int,
        default=12,
        help="Rotating IP attack threshold (failed attempts per user, default: 12)",
    )
    parser.add_argument(
        "--threshold-distributed",
        type=int,
        default=20,
        help="Distributed attack threshold (failed attempts per user, default: 20)",
    )
    return parser.parse_args()

def print_alerts_summary(alerts):
    if not alerts:
        print("\n [✓] Sentinel Engine: No threats or suspicious login activity detected.\n")
        return

    high_count = sum(1 for a in alerts if a.get("severity") == "HIGH")
    med_count = sum(1 for a in alerts if a.get("severity") == "MEDIUM")
    low_count = sum(1 for a in alerts if a.get("severity") == "LOW")

    print("\n" + "=" * 65)
    print("           SENTINEL THREAT DETECTION REPORT")
    print("=" * 65)
    print(f"Total Alerts: {len(alerts)} | HIGH: {high_count} | MEDIUM: {med_count} | LOW: {low_count}")
    print("-" * 65)

    for alert in alerts:
        sev = alert.get("severity", "LOW")
        atype = alert.get("type", "UNKNOWN")
        user = alert.get("username") or "N/A"
        ip = alert.get("ip") or "Multiple / N/A"
        ts = str(alert.get("timestamp"))
        print(f"[{sev:<6}] {atype:<20} | User: {user:<10} | IP: {ip:<15} | {ts}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    args = parse_args()
    alerts = run_detection(
        file_path=args.input,
        bf_threshold=args.threshold_bf,
        rotating_threshold=args.threshold_rotating,
        dist_threshold=args.threshold_distributed,
    )

    if args.as_json:
        # Convert Timestamps to strings for JSON serialization
        serializable_alerts = [
            {**a, "timestamp": str(a["timestamp"])} for a in alerts
        ]
        print(json.dumps(serializable_alerts, indent=2))
    else:
        print_alerts_summary(alerts)