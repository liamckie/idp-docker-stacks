# Networking

## Overview

The platform uses domain-based routing to expose services.

&nbsp;

## Routing Flow

User → Domain → Traefik → Container

&nbsp;

## Key Concepts

### Domains
- Each service is assigned a subdomain
- Example:
  - app.idp.local
  - grafana.idp.local

### Reverse Proxy
- Traefik routes traffic based on host rules

### Internal Networking
- Docker containers are all on one network for now (plan on creating a seperate one just for containers, so there's no need to statically assign IP addresses to each container)

&nbsp;

## Goals

- Consistent service access
- Clear separation of services
- Scalable routing model