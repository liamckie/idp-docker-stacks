# Monitoring

## Overview

Monitoring is implemented using Prometheus and Grafana. v1.2.0 adds basic Grafana alerting for platform reliability.

&nbsp;

## Components

### Prometheus
- Collects metrics from services
- Stores time-series data
- Scrapes Prometheus, Node Exporter, cAdvisor, and Traefik metrics

### Grafana
- Visualises metrics
- Provides dashboards
- Alerts

### Node Exporter
- Exposes host metrics

### cAdvisor
- Exposes container metrics

&nbsp;


### Grafana Alerts

Alerting is handled in Grafana and focuses on simple platform signals.

| Alert                       | Purpose                                                    | Severity |
| --------------------------- | ---------------------------------------------------------- | -------- |
| `CoreTargetDown`            | Detects failed Prometheus scrape targets for core services | Critical |
| `DiskSpaceLow`              | Detects low available disk space on the host               | Warning  |
| `HostMemoryLow`             | Detects low available system memory                        | Warning  |
| `HostCPUHigh`               | Detects sustained high CPU usage                           | Warning  |
| `ContainerRestartedRecently` | Detects recently restarted containers                      | Warning  |




&nbsp;

## Architecture

<pre>
                    Developer
                        │
                        ▼
                  Homepage Portal
                        │
                        ▼
                  Traefik Proxy
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
  Application        Grafana          Prometheus
   Services             │                 │
      │                 │                 │
      ▼                 │                 ▼
   cAdvisor ────────────┼─────────► Metrics Storage
                        │
                        ▼
                   Node Exporter
</pre>

&nbsp;

## Goals

- Visibility into system performance
- Early detection of issues
- Centralised monitoring
