import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dynamic Plotly Timeline")

# Prepare tabular timeline records
df = pd.DataFrame([
    dict(Task="Phase 1", Start='2026-01-01', End='2026-02-28'),
    dict(Task="Phase 2", Start='2026-03-01', End='2026-05-15'),
    dict(Task="Review", Start='2026-05-16', End='2026-06-20')
])

# Generate a horizontal timeline chart
fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Task")
fig.update_yaxes(autorange="reversed") 

# Output chart to interface
st.plotly_chart(fig, use_container_width=True)
