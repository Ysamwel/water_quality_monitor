def check_alerts(data):
    alerts = []
    if data["pH"] < 6.5 or data["pH"] > 8.5:
        alerts.append("pH out of safe range!")
    if data["turbidity"] > 5:
        alerts.append("Turbidity too high!")
    if data["contaminants_ppm"] > 5:
        alerts.append("Contaminants level high!")
    return alerts
