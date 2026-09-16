import streamlit as st

def render_metrics(alerts_df):
    st.subheader("Overview Metrics")

    col1, col2, col3, col4 = st.columns(4)

    if alerts_df.empty:
        col1.metric("Total Alerts", 0)
        col2.metric("HIGH", 0)
        col3.metric("MEDIUM", 0)
        col4.metric("LOW", 0)
        return

    total = len(alerts_df)
    high = len(alerts_df[alerts_df["severity"] == "HIGH"])
    medium = len(alerts_df[alerts_df["severity"] == "MEDIUM"])
    low = len(alerts_df[alerts_df["severity"] == "LOW"])

    col1.metric("Total Alerts", total)
    col2.metric("HIGH",high)
    col3.metric("MEDIUM", medium)
    col4.metric("LOW", low)