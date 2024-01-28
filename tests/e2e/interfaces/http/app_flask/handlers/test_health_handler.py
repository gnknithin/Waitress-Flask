import json
from typing import Any
from tests.utils.base_tests import BaseE2ETest
from infra.constants._url import HandlerConstants
from infra.constants._string import GenericConstants

class TestHealthHandler(BaseE2ETest):

    def test_should_check_health_handler_properly(self):
        # Arrange
        _test_client = self.get_client()
        # Act
        _response = _test_client.get(
            path=HandlerConstants.HEALTH_URI,
        )
        # Assert
        assert _response is not None
        assert _response.status_code == 200
        assert _response.content_type == 'application/json;charset=utf-8'
        _decoded_body:Any = json.loads(_response.data)
        assert _decoded_body is not None
        assert isinstance(_decoded_body, dict)
        assert len(_decoded_body) == 1
        assert GenericConstants.SUCCESS in _decoded_body
        assert isinstance(_decoded_body[GenericConstants.SUCCESS], bool)
        assert _decoded_body[GenericConstants.SUCCESS] is True