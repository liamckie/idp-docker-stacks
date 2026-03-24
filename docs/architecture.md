# Architecture

## Overview

The platform is built around Docker as the execution layer, with Traefik acting as the entry point for all services and Homepage as the central hub for navigation and easy access to services

<pre>
User
│
▼
Tailscale
│
▼
Traefik (Reverse Proxy)
│
├── Homepage
├── Portainer
└── Hello (first test app)
│
▼
Prometheus → Grafana
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

&nbsp;

## Design Principles

- Simplicity over complexity
- Incremental evolution
- Platform abstraction