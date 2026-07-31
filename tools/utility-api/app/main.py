import docker
from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone

app = FastAPI(
    title="Utility API",
    description="Internal diagnostics and platform utility API",
    version="0.2.0",
)
client = docker.from_env()


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
        "version": "0.2.0"
    }


@app.get("/homepage/summary")
def homepage_summary():
    containers = client.containers.list(all=True)

    containers_total = len(containers)
    containers_running = 0
    containers_unhealthy = 0

    for container in containers:
        if container.status == "running":
            containers_running += 1

        health = (
            container.attrs
            .get("State", {})
            .get("Health", {})
            .get("Status")
        )

        if health == "unhealthy":
            containers_unhealthy += 1
            
    return {
        "containers_total": containers_total,
        "containers_running": containers_running,
        "containers_unhealthy": containers_unhealthy,
        "alerts_firing": 0
    }
    
    
@app.get("/containers")
def list_containers():
    containers = client.containers.list(all=True)

    return [
        {
            "name": container.name,
            "status": container.status,
            "image": container.image.tags[0] if container.image.tags else "unknown",
            "health": container.attrs.get("State", {}).get("Health", {}).get("Status", "not_configured"),
        }
        for container in containers
    ]


@app.get("/containers/{name}/health")
def container_health(name: str):
    containers = client.containers.list(all=True, filters={"name": name})

    if not containers:
        raise HTTPException(status_code=404, detail="Container not found")

    container = containers[0]
    state = container.attrs.get("State", {})
    health = state.get("Health", {}).get("Status", "not_configured")

    return {
        "name": container.name,
        "status": container.status,
        "health": health,
    }    