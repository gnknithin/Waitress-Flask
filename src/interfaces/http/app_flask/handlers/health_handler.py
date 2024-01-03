from typing import Any, Dict

from flask import make_response
from flask.views import MethodView
from infra.constants._string import GenericConstants
from interfaces.http.app_flask.schemas.base_schema import BaseSuccessSchema


class HealthHandler(MethodView):
    init_every_request = False

    async def get(self):
        _info: Dict[Any, Any] = dict()
        _info[GenericConstants.SUCCESS] = True
        _loaded: Any = BaseSuccessSchema().load(data=_info)
        return make_response(
            _loaded,
            200,
            {
                "Content-Type":"application/json;charset=utf-8"
            }
        )
