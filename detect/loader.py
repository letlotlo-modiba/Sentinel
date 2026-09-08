import pandas as pd

def load_logs(file_path="./data/login_logs.csv"):
    df = pd.read_csv(file_path)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df

def get_failed_logins(df):
    return df[df["status"] == "FAIL"]