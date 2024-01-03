from infra.constants._string import MessagesConstants
from marshmallow import Schema, fields


class BaseSchema(Schema):
    ...


class BaseSuccessSchema(BaseSchema):
    success = fields.Boolean(
        required=True,
        description=MessagesConstants.MSG_VALIDITY_IN_CASE_OF_FAILURE,
        example=True,
    )