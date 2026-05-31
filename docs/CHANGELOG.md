# V1.2.0 — Alerting and Reliability

This release completes the first alerting pass for the Docker-based IDP.

## Added

- Grafana alerting coverage for core platform health
- Alert documentation in the monitoring guide
- Runbook checks for alerts, routing, logs, and service access

&nbsp;

## Notes

- Alerting remains intentionally simple for v1.x
- v1.3.0 will focus on service onboarding

&nbsp;

# V1.1.0 — Logging

This release introduces centralised logging to the IDP.
Added

- Grafana Loki for log aggregation
- Grafana Alloy for log collection
- Logging integration with Grafana

&nbsp;

## Improvements

- Updated documentation
- Standardised versioning across roadmap

&nbsp;

## Notes

- Docker logs are collected by Alloy and forwarded to Loki

&nbsp;


# V1.0.0 — Foundation Internal Developer Platform

### Overview

This PR introduces v1.0 of the Internal Developer Platform.
Features

- Docker-based service deployment
- Traefik reverse proxy
- Tailscale-secured access
- Prometheus + Grafana monitoring
- Homepage dashboard
- Documentation (README, roadmap, runbook, etc.)

&nbsp;

## Notes

- Establishes platform foundation
- Logging was added later in v1.1.0
