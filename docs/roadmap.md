# Roadmap


&nbsp;

# V1.0 - Foundation ![Status](https://img.shields.io/badge/Status-✅%20Complete-green)

 <b>Goal</b>: Create a working Docker-based internal platform.

## Core features:

- Docker Compose deployment
- Traefik reverse proxy
- TLS certificates
- Homepage dashboard
- Basic service routing
- Initial documentation

&nbsp;

# V1.1 - Logging ![Status](https://img.shields.io/badge/Status-✅%20Complete-green)

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

# V1.2 - Alerting ![Status](https://img.shields.io/badge/Status-✅%20Complete-green)

<b>Goal</b>: Introduce basic platform alerting.

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

# V1.3 - Service Onboarding / Platform UX using Utility API ![Status](https://img.shields.io/badge/Status-✅%20Complete-green)

<b>Goal</b>: Make it easier to add and observe new services by using the Utility API as the example workload.

### Core features:
- Utility API as a demo/internal service
- Service onboarding documentation
- Standard Traefik label example
- Standard healthcheck pattern
- Homepage card
- Grafana/Loki log visibility
- Prometheus metrics
- Basic runbook entries for the Utility API

### Utility API endpoints:
- `GET /health`
- `GET /version`
- `GET /info`
- `GET /metrics`

### Purpose:
- Prove the platform works end to end
- Demonstrate routing, logging, monitoring, dashboards and docs
- Create a realistic service to onboard onto the IDP

&nbsp;

# V1.4 - Platform Automation / Environment API ![Status](https://img.shields.io/badge/Status-🚧%20In%20Progress-black)

<b>Goal</b>: Start turning the IDP into something that can standardise and automate platform-managed workloads.

### Core features:
- Environment API
- Service/environment metadata model
- Service registration workflow
- Templates
- Naming conventions
- Standard config generation
- Basic automation scripts

### Possible endpoints:
- `GET /health`
- `GET /services`
- `GET /services/{name}`
- `POST /services`
- `GET /environments`
- `POST /environments`

### Purpose:
- Improve the platform itself
- Reduce manual copy-paste setup
- Standardise service definitions
- Move towards self-service/internal platform workflows

&nbsp;

# V1.5 - Polish Before V2 ![Status](https://img.shields.io/badge/Status-⏳%20Planned-blue)

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

# V2 - Automation and Delivery ![Status](https://img.shields.io/badge/Status-🔮%20Future-darkred)

<b>Goal</b>: Add more realistic DevOps workflows.

## Possible additions:

- CI checks
- Automated testing
- Image build workflow
- Registry or registry proxy
- Better deployment process
- Secrets management basics

&nbsp;

# V3 - Advanced Platform Capabilities ![Status](https://img.shields.io/badge/Status-🔮%20Future-darkred)

<b>Goal</b>: Explore more advanced platform engineering concepts.

## Possible additions:

- k3s or Kubernetes
- GitOps
- Backstage or a stronger portal
- Policy checks
- Tracing
- DevSecOps tooling
- Self-service workflows

&nbsp;

## Current Focus

Current Version: V1.4.0


&nbsp;

### Next Version:
- V1.5.0 Final Polish before V2

&nbsp;

### Roadmap Rule:
Complete current objectives before proposing future capabilities.
