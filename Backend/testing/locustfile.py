import os
import uuid
from datetime import date, timedelta

from locust import HttpUser, between, task


def _env_bool(name, default="true"):
    return os.getenv(name, default).lower() in {"1", "true", "yes", "y"}


class ArchiveKKNUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.auth_ok = False
        self.headers = {}
        self.enable_writes = _env_bool("LOCUST_ENABLE_WRITES", "true")
        self.icon_id = self._resolve_icon_id()

        self._login()

    def _login(self):
        username = os.getenv("API_USERNAME")
        password = os.getenv("API_PASSWORD")
        if not username or not password:
            return

        with self.client.post(
            "/api/auth/login",
            json={"username": username, "password": password},
            name="/api/auth/login",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                token = response.json().get("data", {}).get("access_token")
                if token:
                    self.headers = {"Authorization": f"Bearer {token}"}
                    self.auth_ok = True
                return
            response.failure(f"Login failed: {response.text}")

    def _resolve_icon_id(self):
        env_icon_id = os.getenv("LOCUST_ICON_ID")
        if env_icon_id and env_icon_id.isdigit():
            return int(env_icon_id)
        return None

    def _ensure_icon_id(self):
        if self.icon_id:
            return self.icon_id

        response = self.client.get("/api/icons/", name="/api/icons/ (list)")
        if response.status_code != 200:
            return None

        icons = response.json().get("data", [])
        if not icons:
            return None

        self.icon_id = icons[0].get("id")
        return self.icon_id

    def _get_first_project_id(self):
        response = self.client.get("/api/projects/", name="/api/projects/ (list)")
        if response.status_code != 200:
            return None

        items = response.json().get("data", {}).get("items", [])
        if not items:
            return None

        return items[0].get("id")

    def _validate_project_tools_svg_path(self, response):
        try:
            data = response.json().get("data", {})
        except Exception:
            response.failure(f"Invalid JSON: {response.text}")
            return

        tools = data.get("tools") or []
        if not tools:
            return

        missing = [t for t in tools if t.get("icon_id") and not t.get("svg_path")]
        if missing:
            response.failure("Missing tools.svg_path for one or more tools")

    @task(1)
    def login(self):
        if not self.auth_ok:
            self._login()

    @task(3)
    def list_projects(self):
        self.client.get("/api/projects/", name="/api/projects/ (list)")

    @task(2)
    def list_icons(self):
        self.client.get("/api/icons/", name="/api/icons/ (list)")

    @task(2)
    def get_project_detail(self):
        project_id = self._get_first_project_id()
        if not project_id:
            return
        with self.client.get(
            f"/api/projects/{project_id}",
            name="/api/projects/<id> (detail)",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Detail failed: {response.text}")
                return
            self._validate_project_tools_svg_path(response)

    @task(2)
    def get_icon_detail(self):
        icon_id = self._ensure_icon_id()
        if not icon_id:
            return
        self.client.get(
            f"/api/icons/{icon_id}",
            name="/api/icons/<id> (detail)",
        )

    @task(2)
    def create_update_delete_project(self):
        if not self.enable_writes or not self.auth_ok:
            return

        icon_id = self._ensure_icon_id()
        tools = (
            [{"icon_id": icon_id, "name": "Crimper", "category": "Networking"}]
            if icon_id
            else []
        )

        today = date.today()
        payload = {
            "title": f"Load Test {uuid.uuid4().hex[:8]}",
            "description": "Locust generated project",
            "status": "IN PROGRESS",
            "start_date": today.isoformat(),
            "end_date": (today + timedelta(days=7)).isoformat(),
            "location": "Jakarta",
            "volunteer_count": 5,
            "photo_url": "https://example.com/photo.jpg",
            "materials": [
                {
                    "item_name": "Router",
                    "quantity": 1,
                    "unit": "PCS",
                    "estimated_price": 100000,
                    "total_cost": 100000,
                }
            ],
            "tools": tools,
            "sourcing_locations": [
                {
                    "store_name": "Tech Store",
                    "address": "Jl. Contoh 1",
                    "distance_km": 1.2,
                    "provides": "Routers",
                    "google_maps_url": "https://maps.google.com",
                }
            ],
        }

        with self.client.post(
            "/api/projects/",
            json=payload,
            headers=self.headers,
            name="/api/projects/ (create)",
            catch_response=True,
        ) as create_response:
            if create_response.status_code != 201:
                create_response.failure(f"Create failed: {create_response.text}")
                return

            project_id = create_response.json().get("data", {}).get("id")
            if not project_id:
                create_response.failure("Create failed: missing project id")
                return

        self.client.get("/api/projects/", name="/api/projects/ (list)")
        with self.client.get(
            f"/api/projects/{project_id}",
            name="/api/projects/<id> (detail)",
            catch_response=True,
        ) as detail_response:
            if detail_response.status_code != 200:
                detail_response.failure(f"Detail failed: {detail_response.text}")
                return
            self._validate_project_tools_svg_path(detail_response)

        update_payload = {
            "status": "DONE",
            "volunteer_count": 10,
        }
        with self.client.put(
            f"/api/projects/{project_id}",
            json=update_payload,
            headers=self.headers,
            name="/api/projects/<id> (update)",
            catch_response=True,
        ) as update_response:
            if update_response.status_code not in {200, 201}:
                update_response.failure(f"Update failed: {update_response.text}")

        with self.client.delete(
            f"/api/projects/{project_id}",
            headers=self.headers,
            name="/api/projects/<id> (delete)",
            catch_response=True,
        ) as delete_response:
            if delete_response.status_code not in {200, 204}:
                delete_response.failure(f"Delete failed: {delete_response.text}")
