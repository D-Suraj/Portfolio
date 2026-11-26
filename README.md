# Suraj Desai — Portfolio

A research-backed personal portfolio built with Python, Flask, HTML, CSS, and vanilla JavaScript.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Configuration

Copy `.env.example` to `.env` or set the variables in your hosting platform. `SITE_URL` should be the public HTTPS origin so canonical, Open Graph, and sitemap URLs are correct.

## Deployment

The app exposes `app:app` as its WSGI entry point. On Linux hosts such as Render, Railway, Fly.io, or an AWS container service, use:

```text
gunicorn app:app
```

Set `SITE_URL`, `SECRET_KEY`, and `PORT` through the platform environment. The included `Procfile` works on platforms that recognize it. For AWS, package the directory in a small Python container, run Gunicorn behind an HTTPS load balancer or reverse proxy, and configure the health check to `/api/health`.

## Evidence policy

Portfolio claims were limited to the supplied resume, the supplied LinkedIn profile, and the public `D-Suraj` GitHub profile and repositories. Employer project descriptions intentionally stay at a non-confidential, technical level.
