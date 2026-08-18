from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(
    title="MOTRYVA",
    description="AI Vehicle Health & Diagnostic Platform",
    version="0.4.0"
)


@app.get("/")
def home():
    return {
        "system": "MOTRYVA",
        "status": "online",
        "message": "MOTRYVA core is running"
    }


def health_status(value):
    if value >= 90:
        return "healthy"
    elif value >= 75:
        return "attention"
    return "critical"


def estimate_life(health, max_km):
    remaining_km = round(max_km * health / 100)

    if health >= 90:
        condition = "good"
    elif health >= 75:
        condition = "monitor"
    else:
        condition = "service_soon"

    return {
        "estimated_remaining_km": remaining_km,
        "condition": condition
    }


@app.get("/vehicle/status")
def vehicle_status():

    engine = random.randint(80, 100)
    battery = random.randint(80, 100)
    brakes = random.randint(75, 100)
    tires = random.randint(70, 100)

    vehicle_health = round(
        (engine + battery + brakes + tires) / 4
    )

    speed = random.randint(0, 120)
    coolant_temperature = random.randint(82, 105)

    tire_pressure = {
        "front_left": random.randint(28, 36),
        "front_right": random.randint(28, 36),
        "rear_left": random.randint(28, 36),
        "rear_right": random.randint(28, 36)
    }

    alerts = []

    if engine < 90:
        alerts.append({
            "component": "engine",
            "severity": "warning",
            "message": "Engine health requires attention"
        })

    if battery < 90:
        alerts.append({
            "component": "battery",
            "severity": "warning",
            "message": "Battery health is below optimal level"
        })

    if brakes < 85:
        alerts.append({
            "component": "brakes",
            "severity": "critical",
            "message": "Brake system requires inspection"
        })

    if tires < 85:
        alerts.append({
            "component": "tires",
            "severity": "warning",
            "message": "Tire condition requires attention"
        })

    if coolant_temperature > 100:
        alerts.append({
            "component": "cooling_system",
            "severity": "critical",
            "message": "Coolant temperature is too high"
        })

    for tire, pressure in tire_pressure.items():
        if pressure < 30:
            alerts.append({
                "component": tire,
                "severity": "warning",
                "message": "Tire pressure is low"
            })

    predictions = {
        "engine": estimate_life(engine, 100000),
        "battery": estimate_life(battery, 80000),
        "brakes": estimate_life(brakes, 50000),
        "tires": estimate_life(tires, 60000)
    }

    return {
        "vehicle_health": vehicle_health,
        "vehicle_status": health_status(vehicle_health),

        "engine": engine,
        "engine_status": health_status(engine),

        "battery": battery,
        "battery_status": health_status(battery),

        "brakes": brakes,
        "brakes_status": health_status(brakes),

        "tires": tires,
        "tires_status": health_status(tires),

        "vehicle_speed_kmh": speed,
        "coolant_temperature_c": coolant_temperature,

        "tire_pressure_psi": tire_pressure,

        "alerts": alerts,

        "predictive_maintenance": predictions,

        "simulation": True,
        "timestamp": datetime.now().isoformat()
    }
