from abc import ABC
from flask.testing import FlaskClient

import pytest

from interfaces.http.app_flask.flask_app import MainApplication

class BaseE2ETest(ABC):
    pytestmark = pytest.mark.e2e

    def get_client(self)->FlaskClient:
        initialized_app = MainApplication().app
        initialized_app.testing = True
        return initialized_app.test_client()