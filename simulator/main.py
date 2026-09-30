import argparse
import csv
import os

try:
    from simulator.normal_activity import generate_logs
    from simulator.attacks import brute_force_attack, rotating_attack, distributed_attack
except ImportError:
    from normal_activity import generate_logs
    from attacks import brute_force_attack, rotating_attack, distributed_attack


def save_logs(logs, filename="./data/login_logs.csv"):
    dirname = os.path.dirname(filename)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    fieldnames = (
        list(logs[0].keys())
        if logs
        else ["timestamp", "username", "ip", "location", "user_agent", "status"]
    )

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        if logs:
            writer.writerows(logs)


def build_dataset(
    normal_count=120,
    attacks=("brute_force", "rotating", "distributed"),
    target_user="admin",
):
    logs = []

    # Normal traffic
    if normal_count > 0:
        logs += generate_logs(normal_count)

    # Attacks
    attack_set = set(attacks)
    if "all" in attack_set:
        attack_set = {"brute_force", "rotating", "distributed"}

    if "brute_force" in attack_set:
        logs += brute_force_attack(username=target_user)
    if "rotating" in attack_set:
        logs += rotating_attack(username=target_user)
    if "distributed" in attack_set:
        logs += distributed_attack(username=target_user)

    return logs


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sentinel Login Activity & Attack Simulator"
    )
    parser.add_argument(
        "-n",
        "--normal-count",
        type=int,
        default=120,
        help="Number of normal log events to generate (default: 120)",
    )
    parser.add_argument(
        "-a",
        "--attacks",
        nargs="+",
        default=["brute_force", "rotating", "distributed"],
        choices=["brute_force", "rotating", "distributed", "all", "none"],
        help="Attack types to inject into the dataset (default: all three)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="./data/login_logs.csv",
        help="Destination path for the generated CSV dataset (default: ./data/login_logs.csv)",
    )
    parser.add_argument(
        "-u",
        "--user",
        type=str,
        default="admin",
        help="Target username for simulated attacks (default: admin)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    selected_attacks = [] if "none" in args.attacks else args.attacks
    logs = build_dataset(
        normal_count=args.normal_count,
        attacks=selected_attacks,
        target_user=args.user,
    )
    save_logs(logs, filename=args.output)
    print(f"Generated {len(logs)} logs -> {args.output}")