# Logging

## Overview
Version 1.1.0 introduces centralised logging to the IDP using:

- Grafana Loki for log storage
- Grafana Alloy for log collection
- Grafana Explore for log querying

&nbsp;

## Logging flow
Docker containers write logs to stdout/stderr.

Alloy reads container logs from the Docker socket and forwards them to Loki.

Grafana queries Loki as a datasource.

Flow:

Container logs -> Alloy -> Loki -> Grafana

&nbsp;

## Components added
- Loki
- Alloy

&nbsp;

## Key configuration notes
- Grafana Explore must use the **Loki** datasource when querying logs
- Traefik access logs must be written to **stdout**, not to a file, for Docker log collection to work
- Loki was configured to allow ingestion of older samples during initial setup

&nbsp;

## Example queries
Show all Docker logs:

```logql
{job="docker"}
```

&nbsp;

## Show Grafana logs:

```logql
{compose_service="grafana"}
```

&nbsp;

## Show Traefik logs:

```logql
{compose_service="traefik"}
```

&nbsp;

## Show logs by container name:

```logql
{container="traefik"}
```

&nbsp;

## Validation steps

### Logging is considered working when:

- Loki is healthy
- Alloy is running
- Grafana can connect to the Loki datasource
- Logs are visible in Grafana Explore
- Traefik access logs appear after generating traffic

&nbsp;

## Troubleshooting

### No logs in Grafana

- Make sure Explore is using the Loki datasource, not Prometheus
- Check Alloy container logs
- Check Loki container health
- Make sure the correct labels are being queried

&nbsp;

### Traefik logs not appearing
- Ensure Traefik access logs are enabled
- Ensure access logs are written to stdout
- Do not use filePath if Alloy is collecting via Docker logs