import streamlit as st
import pandas as pd
import plotly.express as px
from time import sleep

from utils.data_simulation import generate_water_data, SENSORS
from utils.alerts import check_alerts

# Initialize dataframe with columns
df = pd.DataFrame(columns=["timestamp", "sensor", "pH", "turbidity", "temperature", "contaminants_ppm"])

st.title("🌊 Real-Time Water Quality Monitoring")

# Sensor selection
selected_sensor = st.selectbox("Select Sensor/Location", SENSORS)

# Placeholder for chart
chart_placeholder = st.empty()

# Run simulation
for _ in range(50):
    # Generate new data
    new_data = generate_water_data(sensor=selected_sensor)

    # Ensure all columns exist and handle missing values
    cols = ["timestamp", "sensor", "pH", "turbidity", "temperature", "contaminants_ppm"]
    new_row = {col: new_data.get(col, None) for col in cols}
    new_row_df = pd.DataFrame([new_row])

    # Concatenate safely only if new_row_df is not empty
    if not new_row_df.empty:
        df = pd.concat([df, new_row_df], ignore_index=True)

    # Filter data for selected sensor
    sensor_df = df[df["sensor"] == selected_sensor]

    # Make sure numeric columns are floats
    for col in ["pH", "turbidity", "temperature", "contaminants_ppm"]:
        sensor_df[col] = pd.to_numeric(sensor_df[col], errors='coerce')

    # Plot line chart
    fig = px.line(
        sensor_df,
        x="timestamp",
        y=["pH", "turbidity", "temperature", "contaminants_ppm"],
        title=f"Water Quality Readings - {selected_sensor}"
    )
    chart_placeholder.plotly_chart(fig)

    # Check alerts
    alerts = check_alerts(new_data)
    for alert in alerts:
        st.warning(alert)

    # Pause for 2 seconds before next iteration
    sleep(2)
