from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(0.2, 0.5)  # keeps connections warm

    def on_start(self):
        # Define once, reuse every request
        self.params = {"user": "locust_user"}

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            params=self.params,
            name="/my-events",        # clean stats grouping
            timeout=2,                # cap slow requests
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed: {response.status_code}")
