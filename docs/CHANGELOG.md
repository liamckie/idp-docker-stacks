# V1.3.0 — Service Onboarding

## Added

- Introduced a repeatable service onboarding process using Utility API V0.2.0 as the reference workload.
- Added service onboarding documentation and onboarding standards.
- Added application-aware Docker health checking for the Utility API.
- Added Utility API integration with Traefik routing and TLS.
- Added Utility API log visibility through Loki and Grafana.
- Added Utility API monitoring visibility through existing Traefik and container metrics.
- Added Utility API Homepage integration with a custom platform summary widget.
- Added Utility API operational guidance to the platform runbook.

## Changed

- Updated documentation to reflect the Utility API as a normal platform workload rather than a platform control service.
- Updated the roadmap to mark V1.3.0 as complete and V1.4.0 as the next phase of platform automation.
- Updated README upcoming features to reflect the Environment API, templates, validation and standardisation planned for V1.4.0.

## Notes

- Utility API and IDP versioning remain independent.
- V1.3.0 validates the current manual onboarding process before automation is introduced in V1.4.0.

&nbsp;

# V1.2.0 — Alerting and Reliability

This release completes the first alerting pass for the Docker-based IDP.

## Added

- Grafana alerting coverage for core platform health
- Alert documentation in the monitoring guide
- Runbook checks for alerts, routing, logs, and service access

&nbsp;

## Notes

- Alerting remains intentionally simple for V1.x
- V1.3.0 will focus on service onboarding

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

This PR introduces V1.0 of the Internal Developer Platform.
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
- Logging was added later in V1.1.0
