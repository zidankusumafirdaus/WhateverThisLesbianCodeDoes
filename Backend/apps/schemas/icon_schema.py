from marshmallow import Schema, fields


class IconResponseSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    svg_path = fields.String(required=True)
    category = fields.String(required=True)
    created_at = fields.String(required=True)
