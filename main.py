from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="MOTRYVA",
    description="AI Vehicle Health & Diagnostic Platform",
    version="0.1.0"
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
    return {
        "vehicle_health": 100,
        "engine": 100,
        "battery": 100,
        "brakes": 100,
        "tires": 100,
        "timestamp": datetime.now().isoformat()
    }
