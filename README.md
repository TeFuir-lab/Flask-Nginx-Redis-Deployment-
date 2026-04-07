# Flask-Nginx-Redis-Deployment-
Flask + Nginx + Redis 🚀

Overview

This project demonstrates a production-style deployment of a Flask application.
Using the Mac version of CentOS Stream 10, Docker and Redis cannot be used. Redis can only be started with Podman, and Redis is automatically started within the Podman container.

Architecture

Client → Nginx → Gunicorn → Flask → Redis

Features
	•	Reverse proxy with Nginx
	•	Redis cache using Podman
	•	Auto-start with systemd

How to Run
	1.	Start Redis (Podman)
	2.	Start Flask (Gunicorn
