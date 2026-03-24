![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Traefik](https://img.shields.io/badge/Traefik-Reverse%20Proxy-green)
![Status](https://img.shields.io/badge/Project-Active-success)

# 🚀 Internal Developer Platform (IDP)

> A self-hosted Internal Developer Platform built in a homelab environment, evolving from manual container management into a self-service platform.


- Deploy and expose services using Docker + Portainer + Traefik + GitHub
- Monitor everything with Prometheus & Grafana
- Designed to evolve into a self-service platform (APIs + UI)

&nbsp;

## 🧠 Why this project exists

This project help:

- Build real infrastructure instead of just studying theory
- Understand how platforms abstract complexity for developers
- Demonstrate real-world DevOps workflows

&nbsp;

## 🏗️ Architecture

![IDP Architecture](./docs/architecture-diagram.png)

&nbsp;

## ✨ Features

- 🌐 Reverse proxy routing via Traefik
- 📦 Containerised services using Docker
- 📊 Monitoring with Prometheus + Grafana
- 🧭 Central dashboard via Homepage
- 🔧 Domain-based service access

&nbsp;

## 🧰 Tech Stack

| Category         | Tools               |
|------------------|---------------------|
| Containers       | Docker              |
| Stack Management | Portainer           |
| Reverse Proxy    | Traefik             |
| Monitoring       | Prometheus, Grafana |
| Dashboard        | Homepage            |

&nbsp;

## 📊 Observability

- **Prometheus** collects system and service metrics  
- **Grafana** provides dashboards for visualisation  
- *(Planned)* Loki, promtail for log aggregation and collection

&nbsp;

## 🧩 Platform Vision

This project is evolving into a **self-service Internal Developer Platform**:

### 🔜 Upcoming Features

- Environment Provisioner API  
  → Create services via API instead of manual deployment  

- DevOps Utility API  
  → Logs, restart, status, health checks  

- Web UI  
  → Self-service platform interface  

&nbsp;

## 🛣️ Roadmap

| Version | Focus |
|--------|------|
| V1     | Docker, Traefik, Monitoring, Docs |
| V1.5   | Loki (log aggregation) |
| V2     | Self-service APIs + UI |
| V2.5   | Auth, CI/CD, production improvements |
| V3     | Kubernetes (k3s) |

&nbsp;

## 📁 Documentation

Detailed breakdowns available in [`docs/`](./docs):

- Architecture
- Networking
- Traefik configuration
- Monitoring stack
- Deployment process
- Roadmap

&nbsp;

## 🎯 What this demonstrates

- Platform Engineering fundamentals  
- Infrastructure abstraction  
- Observability (metrics + dashboards)  
- Real-world DevOps workflows  

&nbsp;

## ⚠️ Disclaimer

This is a **homelab project** built for learning and demonstration purposes.

&nbsp;

## 🚀 Future Goal

> Build a platform where services are created, deployed, and managed via API/UI — not manually.