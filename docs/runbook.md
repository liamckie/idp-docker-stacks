# Platform Runbook

This document provides operational procedures for diagnosing and resolving common platform issues.

&nbsp;

# Service Not Accessible

## Symptoms
- Service URL does not load
- Browser returns "404" or "Bad Gateway"

## Checks

### 1. Verify container is running

<pre>
docker ps
</pre>

### 2. Check Docker Compose Config
- Container is connected to the `pfsense-vlan` network

### 3. Check Traefik config 
- Make sure the port is correct
- Confirm the service has the right `Host(...)` rule
- Confirm Traefik can see the container

### 4. Ensure targets are UP
- Check status is "UP"
- Investigate failing targets

### 5. Verify DNS or private access
- Confirm the `*.idp.labops.uk` hostname resolves from your device
- If using Tailscale, confirm it is connected outside this repo

&nbsp;

# Logs Not Appearing (Loki)

## Symptoms
- No logs visible in Grafana

## Checks

### 1. Verify Alloy is running

<pre>
docker ps
</pre>

### 2. Check Alloy configuration
- Confirm Alloy can read the Docker socket

### 3. Verify Loki datasource in Grafana
- Check the datasource and click **Save & Test**

### 4. Check the Traefik Static Config
- Confirm Traefik access logs are enabled
- Generate traffic before querying Traefik logs

&nbsp;

# Container Resource Issues

## Symptoms
- High CPU usage
- High memory usage
- Slow or unresponsive services

## Checks

### 1. Use Grafana dashboards
- Container CPU usage
- Container memory usage

### 2. Additional tools
- cAdvisor for container metrics
- Node Exporter for host metrics

### 3. Container Logs

<pre>
docker logs container_name
</pre>

or check the container logs through your Docker management UI if one is in use.

### 4. Grafana Alerts
- Check for any alerts and drill down into the data

&nbsp;

# Alert Firing

## Symptoms
- Grafana shows an active alert
- A core target is down
- Host or container resource usage is high

## Checks
- Identify the alert name and affected service
- Check the related Grafana dashboard
- Confirm the container is running with `docker ps`
- Check logs with `docker logs <container_name>`

&nbsp;

# Restarting Platform Services

## Restart all services

<pre>
docker compose -f infra/traefik/docker-compose.yml restart
docker compose -f apps/homepage/docker-compose.yml restart
docker compose -f monitoring/docker-compose.yml restart
docker compose -f logging/docker-compose.yml restart
</pre>

&nbsp;

## Restart individual container

<pre>
docker restart {container_name}
</pre>

&nbsp;

# Platform Health Checks

The following services should always be running:

- Traefik
- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Homepage
- Loki
- Alloy
- Utility API 

&nbsp;

## Verify with:

<pre>
docker ps
</pre>

&nbsp;

# Access Issues

### Symptoms
- Cannot reach platform services

### Checks
- Confirm the service hostname uses `idp.labops.uk`
- Verify DNS/private access from your device
- If using Tailscale, confirm the device is connected and authenticated

&nbsp;

## Notes

- Always check logs first when diagnosing issues
- Use Grafana dashboards for quick visibility
- Validate routing before assuming service failure

&nbsp;

# Utility API — Diagnostics

Purpose: quick operational checks and container visibility for platform services.

### Endpoints:
- `GET /health` — API health
- `GET /version` — service version
- `GET /homepage/summary` — platform summary used by the Homepage card
- `GET /containers` — list Docker containers with `name`, `status`, `image`, and `health`
- `GET /containers/{name}/health` — detailed health for a specific container

&nbsp;

### Examples:

Check API health:
<pre>
curl -sS https://utility-api.idp.labops.uk/health
</pre>

List containers:
<pre>
curl -sS https://utility-api.idp.labops.uk/containers | jq '.'
</pre>

Check a container's health:
<pre>
curl -sS https://utility-api.idp.labops.uk/containers/utility-api/health | jq '.'
</pre>
