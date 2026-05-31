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
  - homepage.idp.labops.uk
  - grafana.idp.labops.uk

### Reverse Proxy
- Traefik routes traffic based on host rules

### Internal Networking
- Services currently use the external `pfsense-vlan` Docker network
- Some core services have static IPs for predictable routing and scraping

&nbsp;

## Goals

- Consistent service access
- Clear separation of services
- Scalable routing model
