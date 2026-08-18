from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(
    title="MOTRYVA",
    description="AI Vehicle Health & Diagnostic Platform",
    version="0.2.0"
)


@app.get("/")
def home():
    return {
        "system": "MOTRYVA",
        "status": "online",
        "message": "MOTRYVA core is running"
    }


@app.get("/vehicle/status")
def vehicle_status():
    # Virtual Vehicle - simulation for prototype testing
    engine = random.randint(94, 100)
    battery = random.randint(92, 100)
    brakes = random.randint(90, 100)
    tires = random.randint(88, 100)

    vehicle_health = round(
        (engine + battery + brakes + tires) / 4
    )

    return {
        "vehicle_health": vehicle_health,
        "engine": engine,
        "battery": battery,
        "brakes": brakes,
        "tires": tires,
        "vehicle_speed_kmh": random.randint(0, 120),
        "coolant_temperature_c": random.randint(82, 96),
        "tire_pressure_psi": {
            "front_left": random.randint(31, 35),
            "front_right": random.randint(31, 35),
            "rear_left": random.randint(31, 35),
            "rear_right": random.randint(31, 35)
        },
        "alerts": [],
        "simulation": True,
        "timestamp": datetime.now().isoformat()
    }
