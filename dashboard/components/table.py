import streamlit as st

def render_table(alerts_df):
    st.subheader("Alerts Table")

    if alerts_df.empty:
        st.success("No threats detected")
        return

    st.dataframe(alerts_df, use_container_width=True)