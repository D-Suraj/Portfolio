import unittest

from app import create_app


class PortfolioRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True, "SITE_URL": "https://example.com"})
        self.client = self.app.test_client()

    def test_core_routes(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        resume_response = self.client.get("/resume")
        self.assertEqual(resume_response.status_code, 200)
        self.assertEqual(resume_response.mimetype, "application/pdf")
        resume_response.close()
        favicon_response = self.client.get("/favicon.ico")
        self.assertEqual(favicon_response.status_code, 200)
        favicon_response.close()
        self.assertEqual(self.client.get("/api/health").get_json(), {"status": "ok"})
        self.assertEqual(len(self.client.get("/api/projects").get_json()["projects"]), 6)
        self.assertEqual(self.client.get("/robots.txt").status_code, 200)
        self.assertEqual(self.client.get("/sitemap.xml").status_code, 200)
        self.assertEqual(self.client.get("/missing").status_code, 404)

    def test_static_assets_and_metadata(self):
        for path in (
            "/static/css/style.css",
            "/static/js/main.js",
            "/static/assets/og.png",
        ):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200, path)
            response.close()

        html = self.client.get("/").get_data(as_text=True)
        self.assertIn('<link rel="canonical" href="https://example.com/">', html)
        self.assertIn('property="og:image"', html)
        self.assertIn("Suraj Desai | AI Application Engineer | Backend Developer", html)

    def test_security_headers(self):
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["X-Frame-Options"], "DENY")
        self.assertIn("default-src 'self'", response.headers["Content-Security-Policy"])


if __name__ == "__main__":
    unittest.main()
