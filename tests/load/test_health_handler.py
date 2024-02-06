# https://progressstory.com/tech/python/stress-test-with-locust-python-application/
# make run-dev-server
# locust -f tests/load/test_health_handler.py
from locust import HttpUser, task
class TestHealthHandler(HttpUser):

    @task
    def test_should_check_health_handler_properly(self):
        # Arrange
        # Act
        self.client.get("/health")
        # Assert