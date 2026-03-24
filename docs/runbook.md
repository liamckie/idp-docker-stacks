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
- Container is connected to the correct network

### 3. Check Traefik config 
- Make sure the port is correct
- Create a dynamic route if needed
- Ensure the correct middleware is connected if needed
- Ensure treafik can see the correct host name

### 4. Ensure targets are UP
- Check status is "UP"
- Investigate failing targets

### 5. Verify Grafana datasource
- Confirm Prometheus is configured correctly
- Test datasource connection

&nbsp;

# Logs Not Appearing (Loki) ⚠️ (Planned for V1.5)

## Symptoms
- No logs visible in Grafana

## Checks

### 1. Verify Promtail is running

<pre>
docker ps
</pre>

### 2. Check Promtail configuration
- Ensure correct log paths are configured

### 3. Verify Loki datasource in Grafana

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

or 

- Go to Portainer to the container and check the logs

&nbsp;

# Restarting Platform Services

## Restart all services

<pre>
docker compose restart
</pre>

&nbsp;

## Restart individual container

<pre>
docker restart <container_name>
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

## Verify with:

<pre>
docker ps
</pre>

&nbsp;

# Access Issues (Tailscale)

## Symptoms
- Cannot reach platform services

## Checks
- Verify Tailscale is connected
- Confirm device is authenticated
- Ensure correct network access is configured

&nbsp;

# Notes

- Always check logs first when diagnosing issues
- Use Grafana dashboards for quick visibility
- Validate routing before assuming service failure