# Monitoring

## Overview

Monitoring is implemented using Prometheus and Grafana.

&nbsp;

## Components

### Prometheus
- Collects metrics from services
- Stores time-series data

### Grafana
- Visualises metrics
- Provides dashboards

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