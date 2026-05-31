# Roadmap


&nbsp;

# V1.0 - Foundation

 <b>Goal</b>: Create a working Docker-based internal platform.

## Core features:

- Docker Compose deployment
- Traefik reverse proxy
- TLS certificates
- Homepage dashboard
- Basic service routing
- Initial documentation

&nbsp;

# V1.1 - Logging

<b>Goal</b>: Introduce centralised logging and improve platform observability.

## Core features:

- Grafana Loki for log aggregation
- Grafana Alloy for log collection
- Logging integration with Grafana

## Improvements:

Updated documentation
Standardised versioning across roadmap

### Notes:

Docker logs collected by Alloy and forwarded to Loki

&nbsp;

# V1.2 - Alerting

<b>Goal</b>: Introduce basic platform alerting.

Status: Complete

## Core features:

### Basic alert rules

Example alerts:

- CoreTargetDown
- HostMemoryLow
- HostCPUHigh
- ContainerRestartedRecently

### Improvements:

- Updated documentation
- Runbook aligned with current stack

&nbsp;

# V1.3 - Service Onboarding

<b>Goal</b>: Make it easier to add new services.

## Core features:

- Service onboarding documentation
- Example service template
- Standard labels
- Standard healthcheck pattern
- Basic runbook entries

&nbsp;

# V1.4 - Utility / Environment API

<b>Goal</b>: Build a small API that exposes useful platform information.

## Possible endpoints:

- GET /health
- GET /services
- GET /containers
- GET /containers/{name}/health
- GET /platform/status

## Purpose:

- Learn Python / FastAPI
- Learn operational automation
- Provide useful platform visibility
- Create a coding component for the IDP

&nbsp;

# V1.x - Polish Before V2

<b>Goal</b>: Make the Docker-based platform feel complete.

## Possible additions:

- Simple deployment scripts
- Better documentation
- Healthcheck improvements
- Alert tuning
- Screenshots for portfolio
- Interview notes
- Lightweight tests for the API

&nbsp;

# V2 - Automation and Delivery

<b>Goal</b>: Add more realistic DevOps workflows.

## Possible additions:

- CI checks
- Automated testing
- Image build workflow
- Registry or registry proxy
- Better deployment process
- Secrets management basics

&nbsp;

# V3 - Advanced Platform Capabilities

<b>Goal</b>: Explore more advanced platform engineering concepts.

## Possible additions:

- k3s or Kubernetes
- GitOps
- Backstage or a stronger portal
- Policy checks
- Tracing
- DevSecOps tooling
- Self-service workflows



## Current Focus

Current Version: v1.3.0

Working On:
- Service onboarding documentation
- Example service template
- Standard labels and healthcheck pattern

Next Version:
- v1.4.0 Utility / Environment API

Roadmap Rule:
Complete current objectives before proposing future capabilities.
