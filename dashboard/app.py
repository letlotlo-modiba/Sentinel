import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from detect.main import run_detection
from detect.loader import load_logs

from dashboard.components.metrics import render_metrics
from dashboard.components.charts import render_charts
from dashboard.components.table import render_table
from dashboard.components.filters import apply_filters

# --- Page Configuration ---
st.set_page_config(
    page_title="Sentinel SOC Dashboard",
    layout="wide"
)

st.title("Sentinel SOC Dashboard")
st.markdown("Real-time login attack monitoring system")


# --- Load Data ---
df = load_logs()
alerts = run_detection(df)
alerts_df = pd.DataFrame(alerts) if alerts else pd.DataFrame()


# Render components
render_metrics(alerts_df)

filtered_df = apply_filters(alerts_df)

render_charts(filtered_df)
render_table(filtered_df)