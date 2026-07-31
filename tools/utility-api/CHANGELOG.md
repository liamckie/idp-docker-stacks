# Utility API Changelog

&nbsp;

## V0.2.0 — Docker visibility

### Overview
This release adds Docker-based visibility to the Utility API, allowing the platform and Homepage to surface live container status and health information.

&nbsp;

### Added
- Docker SDK integration for local container visibility
- `GET /containers` endpoint returning container list with `name`, `status`, `image`, and `health`
- `GET /containers/{name}/health` endpoint returning container health details
- Homepage summary (`GET /homepage/summary`) now uses real Docker data

&nbsp;

## Notes
- Read-only observability: no operational endpoints (restart/exec) are provided in v0.2.0.

&nbsp;

# V0.1.0 — API foundation

### Overview

Initial API foundation providing basic health/version endpoints and Homepage integration for the Internal Developer Platform.

&nbsp;

### Added
- FastAPI application skeleton and routing
- Basic README and documentation
- `GET /health` endpoint
- `GET /version` endpoint
- `GET /homepage/summary` endpoint (stubbed/sample data)
- Dockerised service and Traefik routing example

&nbsp;

## Notes
- Foundation release: focuses on API surface and documentation. Docker visibility and metrics are planned for later releases.
