# Service Onboarding

## Overview

IDP V1.3.0 introduces a repeatable process for onboarding application workloads onto the platform.

The Utility API V0.2.0 is used as the reference workload. It demonstrates that an application can be deployed and operated consistently using the platform's existing capabilities:

* Docker Compose Deployment
* Traefik Routing and TLS
* Application Health Checks
* Centralised Logging Through Loki
* Monitoring Through Prometheus and Grafana
* Service Visibility Through Homepage
* Documented Deployment, Verification and Recovery Procedures

The Utility API is a consumer of the platform. It is separate from the planned Environment API, which will provide privileged platform management and automation capabilities in V1.4.0.

&nbsp;

## Objectives

The objectives of this release are to:

1. Establish a minimum onboarding standard for application workloads.
2. Validate that standard using a real application.
3. Reduce inconsistency between service deployments.
4. Document the manual onboarding process before automating it.
5. Create a foundation for templates and Environment API validation in V1.4.0.

&nbsp;

## Reference Workload

The reference workload is:

```text
Utility API V0.2.0
```

The Utility API and IDP maintain independent release versions:

```text
IDP:         V1.3.0
Utility API: V0.2.0
```

The Utility API provides application and Docker visibility endpoints, including:

```text
GET /health
GET /version
GET /homepage/summary
GET /containers
```

It provides a realistic workload against which routing, health checks, logging, metrics, dashboard integration and operational procedures can be validated.

&nbsp;

## Service Onboarding Standard

Every application onboarded onto the platform should define:

* A clear name and purpose
* An explicitly versioned container image
* A Docker Compose deployment definition
* A suitable restart policy
* An application-aware health check
* Traefik routing and TLS configuration
* Only the Docker networks required by the application
* Logs written to standard output and standard error
* Monitoring or metrics appropriate to the service
* A Homepage entry where user access is appropriate
* Deployment and rollback instructions
* Basic troubleshooting guidance.

These requirements form the initial service contract for the IDP.

They are applied manually in V1.3.0. Future releases may generate or validate them automatically.

&nbsp;

## Repository Layout

Platform deployment configuration should be separated from application source code.

Example:

```text
apps/
└── utility-api/
    ├── compose.yaml
    ├── .env.example
    └── README.md
```

The application source may remain in its own repository. The IDP repository contains the configuration required to deploy and operate it on the platform.

Environment-specific values and secrets must not be committed to Git.

&nbsp;

## Image Versioning

Workloads should use an explicit image version:

```yaml
image: utility-api:v0.2.0
```

Avoid using:

```yaml
image: utility-api:latest
```

Explicit versions provide:

* Reproducible deployments
* Clearer change history
* Predictable rollback
* Easier incident investigation.

When a new Utility API release is adopted by the platform, the pinned image version in the IDP deployment configuration should be updated through a normal Git change.

&nbsp;

## Deployment Configuration

A workload should define its runtime behaviour in Docker Compose.

Example:

```yaml
services:
  utility-api:
    image: utility-api:v0.2.0
    container_name: utility-api
    restart: unless-stopped
    networks:
      traefik:
        ipv4_address: 0.0.0.0
```

> **Note:** Manual IP assignment is currently used as part of the homelab design. This may be revisited as the platform becomes more automated.

Additional configuration should include:

* Environment variables
* Traefik labels
* A health check
* Logging behaviour
* Resource limits where justified.

An `.env.example` file should document required configuration without containing credentials or sensitive values.

For the full platform deployment process, see [Deployment](deployment.md).

&nbsp;

## Network and Access Model

The Utility API connects to the external Docker network used by Traefik:

```yaml
networks:
  traefik:
    external: true
```

A workload should only be attached to networks it requires.

The Utility API is a normal application workload and should not receive access to privileged platform-management networks or administration interfaces.

This separation becomes more important when the Environment API is introduced. The Environment API may require controlled access to platform metadata or management integrations, while the Utility API should remain low privilege.

For the full network design and trust boundaries, see [Networking](networking.md).

&nbsp;

## Routing and TLS

The Utility API is exposed through Traefik using a dedicated HTTPS router.

Example:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.utility-api.rule=Host(`utility-api.dev.example.com`)"
  - "traefik.http.routers.utility-api.entrypoints=https"
  - "traefik.http.routers.utility-api.tls=true"
  - "traefik.http.services.utility-api.loadbalancer.server.port=8000"
```

The router, service and hostname should follow a consistent naming convention.

Successful onboarding requires confirmation that:

* DNS Resolves to the intended Traefik instance
* HTTPS and certificate handling work
* Traefik forwards traffic to the correct container port
* The application responds through its platform hostname.

Example verification:

```bash
curl -i https://utility-api.dev.example.com/health
```

For the full routing standard, TLS configuration and Traefik troubleshooting guidance, see [Traefik](traefik.md).

&nbsp;

## Application Health Check

The service health check should test application behaviour rather than only confirming that the container process exists.

Example:

```yaml
healthcheck:
  test:
    [
      "CMD",
      "python",
      "-c",
      "import urllib.request; urllib.request.urlopen('http://localhost:8000/health');"
    ]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 10s
```

This confirms that the application can accept and respond to requests from inside its container.

Health status can be verified with:

```bash
docker inspect utility-api \
  --format='{{json .State.Health}}'
```

A container that is running but unable to serve requests should not be considered healthy.

&nbsp;

## Centralised Logging

The Utility API writes application and HTTP access logs to standard output.

Uvicorn access logging is enabled in the container command:

```dockerfile
CMD [
  "uvicorn",
  "main:app",
  "--host",
  "0.0.0.0",
  "--port",
  "8000",
  "--access-log"
]
```

Logs should be validated first at the container level:

```bash
docker logs -f utility-api
```

They should then be visible through Loki in Grafana Explore.

A successful request should produce an entry similar to:

```text
"GET /health HTTP/1.1" 200 OK
```

For the full logging architecture, query workflow and troubleshooting process, see [Logging](logging.md).

&nbsp;

## Monitoring and Metrics

The Utility API is observable through the platform's existing monitoring stack.

Current visibility includes:

* Container CPU and memory usage
* Container state
* Network activity
* Traefik request counts
* Request methods
* Request duration
* Protocol and service-level request information.

This confirms that the workload can be monitored through the platform.

Application-specific FastAPI instrumentation may be added later if deeper application metrics are required. For V1.3.0, platform and proxy-level visibility is sufficient for the onboarding standard.

For the complete monitoring architecture and dashboard design, see [Monitoring](monitoring.md).

&nbsp;

## Homepage Integration

The Utility API appears in the user-facing applications section of Homepage.

It provides a custom summary showing:

* Running containers
* Unhealthy containers
* Firing alerts.

The Utility API is user-facing because it represents a normal workload consuming the platform.

Privileged services such as the future Environment API should not appear on the same unrestricted dashboard. Platform administration services should be placed behind separate access controls.

Hiding a service from Homepage is not an access-control mechanism.

&nbsp;

## Deploy, Validate and Roll Back

A workload should not be considered successfully onboarded simply because its container is running.

Deployment:

```bash
docker compose up -d
```

For a locally built image:

```bash
docker compose up -d --build
```

Basic validation:

```bash
docker compose ps
docker compose logs --tail=100 utility-api
curl -i https://utility-api.dev.example.com/health
```

Successful onboarding requires confirmation that:

* The container is running
* The health check passes
* The HTTPS route works
* Logs appear in Loki
* Expected metrics are visible
* The Homepage integration works.

Rollback should restore the previous known-good image version and then repeat the same validation checks.

For the full deployment, update and rollback process, see [Deployment](deployment.md).

&nbsp;

## Troubleshooting

Common onboarding failures include:

* Traefik Returning HTTP 502
* Container Health Checks Failing
* Logs Missing from Grafana
* Expected Metrics Missing
* DNS or Hostname Resolution Failures.

Detailed recovery procedures are maintained in the platform runbook.

See [Runbook](runbook.md) for:

* Utility API Unhealthy
* Routing Failures
* Logging Failures
* Metrics Issues
* Container Availability Checks
* Current Utility API Endpoints.

&nbsp;

## Definition of Done

A service is considered successfully onboarded when:

```text
[ ] The Service Has a Documented Purpose and Owner
[ ] The Deployment Uses a Pinned Image Version
[ ] Compose Configuration Is Stored in Git
[ ] Secrets and Environment-Specific Values Are Excluded from Git
[ ] An Appropriate Restart Policy Is Configured
[ ] An Application-Aware Health Check Passes
[ ] Traefik Routing and TLS Work
[ ] Logs Are Visible Through Loki and Grafana
[ ] Required Monitoring Information Is Visible
[ ] The Appropriate Homepage Entry Is Present
[ ] Deployment and Update Procedures Are Documented
[ ] Rollback Is Documented
[ ] Common Failure Scenarios Have Troubleshooting Guidance
```

&nbsp;

## Future Automation

The V1.3.0 onboarding process is intentionally manual.

Documenting and validating the manual standard first provides a clear set of requirements for V1.4.0.

The Environment API and future templates may later support:

* Service Registration
* Metadata Validation
* Naming Convention Enforcement
* Generation of Standard Compose Configuration
* Traefik Label Generation
* Health-Check Validation
* Homepage Configuration Generation
* Environment-Specific Configuration
* Management of Development and Production Service Definitions.

The Utility API demonstrates that the platform can host and operate a workload.

The Environment API will improve and automate how the platform manages workloads.
