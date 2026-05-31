# Architecture

## Overview

The platform is built around Docker as the execution layer, with Traefik acting as the entry point for services and Homepage as the central hub for navigation.

<pre>
User
│
▼
Network access
│
▼
Traefik (Reverse Proxy)
│
├── Homepage
├── Grafana
├── Hello / Whoami demo services
└── Prometheus metrics
│
▼
Loki logs → Grafana
</pre>

&nbsp;

## Components

### Traefik
- Handles routing based on domain names
- Automatically detects services via Docker labels

### Docker
- Runs all services as containers
- Provides isolation and portability

### Prometheus
- Collects metrics from services

### Grafana
- Visualises metrics and dashboards

### Loki and Alloy
- Collect and store Docker container logs

### Demo services
- Hello and Whoami are lightweight services used to validate routing

### External access
- Tailscale may be used for private access, but it is managed outside this repository

&nbsp;

## Design Principles

- Simplicity over complexity
- Incremental evolution
- Platform abstraction
