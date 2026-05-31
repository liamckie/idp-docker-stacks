# Traefik

## Overview

Traefik is used as the reverse proxy to route traffic to services.

&nbsp;

## How it Works

- Traefik listens on ports 80 and 443
- Traefik exposes Prometheus metrics on port 8081 internally
- Services register themselves using Docker labels

&nbsp;

## Example Labels

- traefik.enable=true
- traefik.http.routers.app.rule=Host(`app.idp.labops.uk`)
- traefik.http.services.app.loadbalancer.server.port=3000

&nbsp;

## Benefits

- Automatic service discovery
- Dynamic configuration
- Easy scaling of services
