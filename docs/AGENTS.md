# Project Overview

- This project is a homelab Internal Developer Platform used to learn DevOps, Platform Engineering, observability, automation, and service onboarding.

- The platform currently runs on a Docker-based Dev LXC inside Proxmox.

&nbsp;

# Current Stack
- Docker / Docker Compose
- Traefik
- Homepage
- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Loki
- Alloy
- Alerting via Grafana

Portainer and Tailscale may be used outside this repository, but they are not currently defined as active Docker Compose services here.

&nbsp;

# Main Goals
- Keep the project realistic for a junior DevOps / Platform Engineering portfolio.
- Prefer simple, understandable solutions over enterprise complexity.
- Build features gradually and document the reasoning.
- Make the project easy to explain in interviews.

&nbsp;

# Rules for AI Assistance
- Do not rewrite the whole project unless explicitly asked.
- Explain changes before making major edits.
- Prefer small, reviewable changes.
- Keep documentation concise and interview-friendly.
- Do not introduce Kubernetes, cloud, service mesh, or complex CI/CD unless requested.
- Do not add secrets, API tokens, passwords, or private keys to the repo.
- Update documentation when behaviour changes.
- Prefer Docker Compose solutions for v1.x.
- Ask before changing architecture-level decisions.
- Coding Preferences
- Keep scripts simple and readable.
- Prefer Bash or Python where appropriate.
- Use clear folder names.
- Add comments only where they explain why something exists.
- Avoid overengineering.

&nbsp;

# Documentation Style

### Documentation should explain:

- What the component does?
- Why it exists?
- How to run it?
- How to troubleshoot it?
- What an interviewer might ask about it?

Avoid long walls of text.
