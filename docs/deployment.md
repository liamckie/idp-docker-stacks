# Deployment

## Overview

Services are deployed manually using Docker Compose.

&nbsp;

## Process

1. Create or update a Docker Compose file
2. Define the service, network, and Traefik labels
3. Deploy from the relevant directory:

<pre>
docker compose up -d
</pre>

4. Traefik automatically routes traffic

Current compose locations:

- `infra/` for Traefik
- `apps/` for user-facing apps
- `monitoring/` for Prometheus, Grafana, cAdvisor, and Node Exporter
- `logging/` for Loki and Alloy
- `stacks/` for Portainer-style wrapper compose files

&nbsp;

## Future Improvements

- API-driven deployments
- Service templates
- Automated provisioning
