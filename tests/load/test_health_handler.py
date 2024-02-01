from locust import HttpUser, task
class TestHealthHandler(HttpUser):

    @task
    def test_should_check_health_handler_properly(self):
        # Arrange
        # Act
        # Assert