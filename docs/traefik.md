# Traefik

## Overview

Traefik is used as the reverse proxy to route traffic to services.

&nbsp;

## How it Works

- Traefik listens on ports 80 and 443
- Services register themselves using Docker labels

&nbsp;

## Example Labels

- traefik.enable=true
- traefik.http.routers.app.rule=Host(app.local)
- traefik.http.services.app.loadbalancer.server.port=3000

&nbsp;

## Benefits

- Automatic service discovery
- Dynamic configuration
- Easy scaling of services