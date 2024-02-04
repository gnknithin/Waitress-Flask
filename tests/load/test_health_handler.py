# https://progressstory.com/tech/python/stress-test-with-locust-python-application/
from locust import HttpUser, task
class TestHealthHandler(HttpUser):

    @task
    def test_should_check_health_handler_properly(self):
        # Arrange
        # Act
        self.client.get("/health")
        # Assert