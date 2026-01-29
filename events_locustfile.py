from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(0.2, 0.5)  # keep connections warm

    def on_start(self):
        # Pre-define params once
        self.params = {"user": "locust_user"}

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            params=self.params,
            name="/events",          # group stats
            timeout=2,               # cap slow responses
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed: {response.status_code}")
