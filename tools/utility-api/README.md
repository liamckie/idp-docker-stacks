# Utility API

## Purpose

The Utility API is an internal diagnostics and operations service for the IDP project.

It provides a central interface for platform visibility, troubleshooting, and operational checks.

Current capabilities include:

- API health information
- Platform summary information
- Homepage widget integration
- Docker container visibility
- Container health/status reporting

Future capabilities may include:

- Prometheus metrics summaries
- Alert summaries
- HTTP, DNS, and connectivity diagnostics

The Utility API is a supporting service and is not responsible for deployments, environment management, or platform provisioning.

&nbsp;

## Goals

### Current Goals
- API health endpoint
- Service information endpoint
- Homepage summary endpoint
- Docker container visibility
- Platform diagnostics

### Future Goals
- Prometheus integration
- Alert summary integration
- DNS and HTTP diagnostics
- Safe operational actions
- Platform troubleshooting workflows

&nbsp;

## Target Architecture

<pre>
Homepage
    |
    v
Utility API
    |
    +--> Docker
    +--> Prometheus
    +--> Alertmanager
    +--> Loki
</pre>

The Utility API is intended to act as an aggregation layer between platform tools and platform users.

In V0.2.0, Docker is the active integration. Prometheus, alerting, and Loki are planned future integrations.

&nbsp;

## Endpoints

### Health
`GET /health`

Returns API health information.

### Version
`GET /version`

Returns service version information.

### Homepage Summary
`GET /homepage/summary`

Returns summary information for Homepage widgets.

Example:
<pre>
{
  "containers_total": 14,
  "containers_running": 12,
  "containers_unhealthy": 0,
  "alerts_firing": 0
}
</pre>

### Containers
`GET /containers`

Returns a list of Docker containers with name, status, image, and health information.

### Container Health
`GET /containers/{name}/health`

Returns health information for a specific Docker container.

&nbsp;

## Running Locally

Install dependencies:

<pre>pip install -r requirements.txt</pre>

Run the API:

<pre>uvicorn app.main:app --reload</pre>

Swagger documentation:

`http://localhost:8000/docs`

&nbsp;

## Container Deployment

Build image:

<pre>docker build -t utility-api:v0.2.0 .</pre>

Run container using docker run command:

<pre>docker run -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock:ro utility-api:v0.2.0</pre>

Run container with compose:

<pre>docker compose up -d</pre>

Example access name:

`utility-api.idp.labops.uk`

&nbsp;

# Roadmap

### V0.1.0 — API foundation
Status: Complete

- FastAPI app
- Dockerised service
- Traefik routing
- Health, Version, Homepage summary endpoints
- Basic README

&nbsp;

### V0.2.0 — Docker visibility
Status: Complete

- Docker SDK integration
- Container list endpoint
- Container health/status reporting
- Running/unhealthy container counts
- Homepage summary uses real Docker data

&nbsp;

### V0.3.0 — Observability summary
Status: Planned

- Prometheus, Alert summary integration
- Metrics summary endpoint
- Platform health overview
- Homepage summary includes alerts/targets

&nbsp;

### V0.4.0 — Diagnostics toolkit
Status: Planned

- HTTP, DNS check, Troubleshooting summary endpoints
- Optional TCP port check

&nbsp;

### V0.5.0 — Safe operations
Status: Planned

- Optional container restart endpoint
- Allowed-service list only
- Auth required
- No arbitrary commands
