import random
import datetime

# List of example sensors / locations
SENSORS = ["River A", "Lake B", "Well C", "Reservoir D"]

def generate_water_data(sensor=None):
    """
    Simulate water sensor reading.
    If sensor is provided, include it in the data.
    """
    data = {
        "timestamp": datetime.datetime.now(),
        "sensor": sensor if sensor else random.choice(SENSORS),
        "pH": round(random.uniform(6.0, 9.0), 2),
        "turbidity": round(random.uniform(0, 10), 2),
        "temperature": round(random.uniform(10, 35), 1),
        "contaminants_ppm": round(random.uniform(0, 10), 2)
    }
    return data
