# IDP = Docker + Portainer + Git V1

This IDP currently runs on an existing Docker dev node.
Platform provisioning is handled separately via Ansible and is only required when creating or rebuilding nodes.

## Architecture Overview

This Internal Developer Platform (IDP) provides a GitOps-based workflow for deploying
containerised applications onto an existing Docker environment.

### Current Runtime
- The IDP currently runs on an existing Docker development node (Docker LXC).
- Portainer is used as the deployment engine, with stacks managed via Git repositories.
- Application deployments are triggered by Git commits.

### Infrastructure Provisioning
- Infrastructure provisioning (LXC creation, Docker installation, base networking)
  is handled separately using Ansible.
- Ansible is only required when creating, rebuilding, or expanding platform nodes.
- Day-to-day application deployments do not require Ansible interaction.

This separation mirrors real-world platform engineering practices, where infrastructure
code changes infrequently while application delivery happens continuously.

## IDP Scope (v1)
This IDP intentionally focuses on:

- Git-driven application deployments
- Consistent stack definitions
- Platform-managed networking
- Clear separation between infrastructure and application concerns


Out of scope for v1:
- Kubernetes
- Service mesh
- Secrets automation
- Self-service portals

These may be explored in future iterations but are not required for a functional,
CV-ready IDP foundation.