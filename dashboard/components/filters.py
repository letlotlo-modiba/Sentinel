import streamlit as st

def apply_filters(alerts_df):
    st.subheader("Filters")

    if alerts_df.empty:
        return alerts_df

    col1, col2, col3 = st.columns(3)

    # Severity filter
    with col1:
        severity = st.selectbox("Severity", ["ALL", "HIGH", "MEDIUM", "LOW"])

    # Username filter
    with col2:
        usernames = ["ALL"] + sorted(alerts_df["username"].dropna().astype(str).unique().tolist())
        user = st.selectbox("Username", usernames)

    # IP filter
    with col3:
        ips = ["ALL"] + sorted(alerts_df["ip"].dropna().astype(str).unique().tolist())
        ip = st.selectbox("IP Address", ips)

    # Apply filters
    filtered = alerts_df.copy()

    if severity != "ALL":
        filtered = filtered[filtered["severity"] == severity]

    if user != "ALL":
        filtered = filtered[filtered["username"] == user]

    if ip != "ALL":
        filtered = filtered[filtered["ip"] == ip]

    return filtered