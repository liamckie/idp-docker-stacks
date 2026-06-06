# Utility API

## Purpose

The Utility API is an internal diagnostics and operations service for the IDP project.

It provides a central interface for platform visibility, troubleshooting, and operational checks.

Current capabilities include:

- API health information
- Platform summary information
- Homepage widget integration

Future capabilities may include:

- Docker container health
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

## Architecture

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

The Utility API acts as an aggregation layer between platform tools and platform users.

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
  "containers_running": 12,
  "containers_unhealthy": 0,
  "alerts_firing": 0
}
</pre>

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

Build image (with latest tag):

<pre>docker build -t utility-api .</pre>

Run container using docker run command:

<pre>docker run -p 8000:8000 utility-api</pre>

Run container with compose:

<pre>docker compose up -d</pre>

&nbsp;

# Roadmap
### V0.1.0 — API foundation
- FastAPI app
- Dockerised service
- Traefik routing
- Health, Version, Homepage summary endpoints
- Basic README

### V0.2.0 — Docker visibility
- Docker SDK integration
- Container list endpoint
- Container health/status reporting
- Running/unhealthy container counts
- Homepage summary uses real Docker data

### V0.3.0 — Observability summary
- Prometheus, Alert summary integration
- Metrics summary endpoint
- Platform health overview
- Homepage summary includes alerts/targets

### V0.4.0 — Diagnostics toolkit
- HTTP, DNS check, Troubleshooting summary endpoints
- Optional TCP port check

### V0.5.0 — Safe operations
- Optional container restart endpoint
- Allowed-service list only
- Auth required
- No arbitrary commands