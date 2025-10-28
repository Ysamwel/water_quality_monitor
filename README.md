# 🌊 Real-Time Water Quality Monitoring Platform

A Python-based web application that simulates and visualizes real-time water quality data from multiple sensors.  
This project aligns with **SDG 6: Clean Water and Sanitation**, aiming to provide instant monitoring and alerting for water quality.

---

## Features

- Simulates real-time water readings including:
  - pH levels
  - Turbidity
  - Temperature
  - Contaminants (ppm)
- Select sensor/location to view specific data.
- Interactive line charts using Plotly for live visualization.
- Real-time alerts when water quality parameters exceed safe thresholds.
- Easily extendable to save historical readings or integrate real sensor data.

---

## Project Structure

water_quality_monitor/
├── app.py # Main Streamlit app
├── utils/
│ ├── data_simulation.py # Functions to generate simulated sensor data
│ └── alerts.py # Functions to generate alerts based on readings
├── data/ # Optional: Store historical readings here
├── venv/ # Python virtual environment
└── README.md


---

## Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd water_quality_monitor
```

## Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies:
pip install -r requirements.txt

## Running the App
streamlit run app.py

Open your browser at http://localhost:8501.

Select a sensor from the dropdown to start monitoring.

Watch the real-time graph and check for alerts.

## Optional Enhancements

Save simulated readings to CSV in the data/ folder for historical tracking.

Add a map to visualize sensor locations.

Integrate real sensor data for live water quality monitoring.

Use AI models to predict contamination or water shortages.

# License

This project is licensed under the MIT License.

## Author

Yvonne  – Software Engineer & SDG Enthusiast