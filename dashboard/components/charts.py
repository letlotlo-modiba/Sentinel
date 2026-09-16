import streamlit as st

def render_charts(alerts_df):
    st.subheader("Attacks Insights")

    if alerts_df.empty:
        st.info("No data to display")
        return

    col1, col2 = st.columns(2)

    # --- Attack type distribution ---
    with col1:
        st.markdown("**Attack Types**")
        st.bar_chart(alerts_df["type"].value_counts())

    # --- Severity distribution ---
    with col2:
        st.markdown("**Severity Distribution**")
        st.bar_chart(alerts_df["severity"].value_counts())