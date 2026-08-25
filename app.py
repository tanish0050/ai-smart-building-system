from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

def building_data():
    energy = round(random.uniform(42, 95), 1)
    temperature = round(random.uniform(19, 32), 1)
    occupancy = random.randint(5, 100)
    humidity = round(random.uniform(30, 75), 1)

    alerts = []
    recommendations = []

    if energy > 80:
        alerts.append("High energy consumption detected")
        recommendations.append("Reduce HVAC load and switch off unused equipment.")
    else:
        recommendations.append("Energy usage is within the expected range.")

    if temperature > 27:
        alerts.append("Temperature is above the comfort range")
        recommendations.append("Optimize cooling based on occupancy.")
    elif temperature < 21:
        alerts.append("Temperature is below the comfort range")
        recommendations.append("Reduce unnecessary cooling or adjust HVAC settings.")

    if occupancy < 15 and energy > 65:
        alerts.append("Possible energy wastage in low-occupancy areas")
        recommendations.append("Use occupancy-based automation for lights and HVAC.")

    if not alerts:
        alerts.append("No critical anomalies detected")

    return {
        "energy": energy,
        "temperature": temperature,
        "occupancy": occupancy,
        "humidity": humidity,
        "alerts": alerts,
        "recommendations": list(dict.fromkeys(recommendations)),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    return jsonify(building_data())

if __name__ == "__main__":
    app.run(debug=True)
