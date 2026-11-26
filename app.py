import os
from pathlib import Path

from flask import Flask, Response, jsonify, render_template, send_from_directory

from portfolio_data import EXPERIENCE, PROJECTS, SKILL_GROUPS


BASE_DIR = Path(__file__).resolve().parent


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "development-only"),
        SITE_URL=os.getenv("SITE_URL", "http://localhost:5000").rstrip("/"),
    )

    if test_config:
        app.config.update(test_config)

    @app.context_processor
    def inject_site_data():
        return {
            "site_url": app.config["SITE_URL"],
            "projects": PROJECTS,
            "experience": EXPERIENCE,
            "skill_groups": SKILL_GROUPS,
        }

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/resume")
    def resume():
        return send_from_directory(
            BASE_DIR / "static" / "files",
            "Suraj Desai Resume.pdf",
            mimetype="application/pdf",
        )

    @app.get("/favicon.ico")
    def favicon():
        return send_from_directory(
            BASE_DIR / "static" / "assets",
            "favicon.png",
            mimetype="image/png",
        )

    @app.get("/api/projects")
    def projects_api():
        public_projects = [
            {
                "name": item["name"],
                "type": item["type"],
                "summary": item["summary"],
                "technologies": item["technologies"],
                "repository": item.get("repository"),
            }
            for item in PROJECTS
        ]
        return jsonify({"projects": public_projects})

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/robots.txt")
    def robots():
        body = f"User-agent: *\nAllow: /\nSitemap: {app.config['SITE_URL']}/sitemap.xml\n"
        return Response(body, mimetype="text/plain")

    @app.get("/sitemap.xml")
    def sitemap():
        body = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"  <url><loc>{app.config['SITE_URL']}/</loc></url>\n"
            "</urlset>\n"
        )
        return Response(body, mimetype="application/xml")

    @app.errorhandler(404)
    def page_not_found(_error):
        return render_template("404.html"), 404

    @app.after_request
    def apply_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; img-src 'self' data:; style-src 'self'; "
            "script-src 'self'; connect-src 'self'; font-src 'self'; "
            "base-uri 'self'; form-action 'self'; frame-ancestors 'none'"
        )
        return response

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )
