import csv

try:
    from simulator.normal_activity import generate_logs
    from simulator.attacks import brute_force_attack, rotating_attack, distributed_attack
except ImportError:
    from normal_activity import generate_logs
    from attacks import brute_force_attack, rotating_attack, distributed_attack


def save_logs(logs, filename="./data/login_logs.csv"):
    keys = logs[0].keys()

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(logs)

def build_dataset():
    logs = []

    # normal traffic
    logs += generate_logs(120)

    # attacks
    logs += brute_force_attack()
    logs += rotating_attack()
    logs += distributed_attack()

    return logs

if __name__ == "__main__":
    logs = build_dataset()
    save_logs(logs)
    print(f"Generated {len(logs)} logs.")