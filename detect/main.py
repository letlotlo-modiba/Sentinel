from loader import load_logs, get_failed_logins
from rules import (
    detect_brute_force,
    detect_rotating_attack,
    detect_distributed_attack
)
from alerts import format_alerts

def run_detection():
    df = load_logs()
    failed = get_failed_logins(df)

    alerts = []

    brute_force = detect_brute_force(failed)
    alerts += format_alerts(brute_force, "BRUTE_FORCE")

    rotating = detect_rotating_attack(failed)
    alerts += format_alerts(rotating, "ROTATING_ATTACK")

    distributed = detect_distributed_attack(failed)
    alerts += format_alerts(distributed, "DISTRIBUTED_ATTACK")

    return alerts

if __name__ == "__main__":
    alerts = run_detection()

    print("ALERTS DETECTED:")
    for alert in alerts:
        print(alert)