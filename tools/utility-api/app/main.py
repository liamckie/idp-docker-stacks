from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Utility API",
    description="Internal diagnostics and platform utility API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "utility-api",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/version")
def version():
    return {
        "name": "utility-api",
        "version": "0.1.0"
    }


@app.get("/homepage/summary")
def homepage_summary():
    return {
        "containers_running": 0,
        "containers_unhealthy": 0,
        "alerts_firing": 0
    }